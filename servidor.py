#!/usr/bin/env python3
"""Servidor local da Trilha AOCP — V7 (base dos Drives).

Usa apenas a biblioteca padrão do Python 3.10+.

Novidade central da V7: a IA NÃO escreve a redação da lei nem o enunciado de súmula.
Ela cita o dispositivo (ou o identificador do precedente) e o servidor preenche o texto
a partir da base local:
  1. assets/lei_seca_oficial.json   — redação oficial do Planalto (gerada por atualizar_lei_seca.bat)
  2. assets/lei_seca_material.json  — lei seca anotada dos PDFs do curso (DD LEGIS)
  3. assets/sumulas.json, teses_rg.json, juris_aocp.json — súmulas, teses de RG e ementas do LD JURIS
"""
from __future__ import annotations
import concurrent.futures, http.server, json, math, os, pathlib, re, sys, threading, time, unicodedata, urllib.error, urllib.parse, urllib.request, webbrowser
from collections import Counter

RELEASE = '2026.11.01-v10-revisao-ce'
ROOT = pathlib.Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
CACHE = ROOT / 'cache'; CACHE.mkdir(exist_ok=True)
HIST = ROOT / 'historico'      # D-006: o arquivo acumulado (fora do Git: tem respostas e comentários)
BLOCO_MAX = 30                 # D-005: tamanho do bloco
HIST_MAX = 40_000_000          # bytes aceitos no POST do histórico
CUTOFF = '29/07/2026'


def load_env():
    f = ROOT / '.env'
    if not f.exists(): return
    for line in f.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line: continue
        a, b = line.split('=', 1)
        os.environ.setdefault(a.strip(), b.strip().strip('"').strip("'"))


load_env()


def load(name, default):
    f = ASSETS / name
    if not f.exists(): return default
    try: return json.loads(f.read_text(encoding='utf-8'))
    except Exception as exc:
        print('[trilha] aviso: não foi possível ler', name, exc); return default


ITEMS = load('items.json', [])
BY_ID = {t['id']: t for t in ITEMS}
BANK = load('banco_inicial.json', {})
PAGES = load('fontes_paginas.json', [])
OFFICIAL = load('acervo_oficial_curado.json', {})
LEI_MAT = load('lei_seca_material.json', {})
LEI_OF = load('lei_seca_oficial.json', {})
SUMULAS = load('sumulas.json', {})
TESES = load('teses_rg.json', {})
JURIS = load('juris_aocp.json', [])
CATALOGO = load('catalogo_leis.json', {'diplomas': []}).get('diplomas', [])
WORKERS = concurrent.futures.ThreadPoolExecutor(max_workers=2, thread_name_prefix='geracao')
TASKS = {}; TASK_LOCK = threading.Lock()
PORT = int(os.environ.get('PORT', '8765'))

# ======================================================================= texto
STOP = {'de', 'da', 'do', 'dos', 'das', 'e', 'a', 'o', 'ao', 'os', 'as', 'em', 'na', 'no', 'para', 'por', 'um', 'uma', 'se', 'que', 'com',
        'art', 'lei', 'direito', 'federal', 'estadual', 'geral', 'tema', 'sob', 'sobre', 'nocoes', 'codigo',
        'pela', 'pelo', 'quando', 'como', 'mais', 'ser', 'sera', 'nos', 'nas', 'seu', 'sua', 'seus', 'suas', 'ou', 'nao', 'esta', 'este',
        'pena', 'artigo', 'inciso', 'paragrafo', 'caso', 'casos', 'forma', 'termos', 'qualquer', 'outro', 'outra', 'ainda', 'desde'}


def fold(s: str) -> str:
    return unicodedata.normalize('NFKD', str(s).casefold()).encode('ascii', 'ignore').decode('ascii')


def terms(s):
    """radicais de 6 letras (stemming leve): administração ~ administrativo, princípio ~ princípios"""
    return set(w[:6] for w in re.findall(r'\b[a-z]{4,}\b', fold(s)) if w not in STOP)


def idf_table(sets):
    df = Counter()
    for st in sets: df.update(st)
    n = max(1, len(sets))
    return {t: math.log(1 + n / (1 + c)) for t, c in df.items()}


def wscore(q, doc, idf):
    return sum(idf.get(t, 1.0) for t in q & doc)


def squash(s: str) -> str:
    """normaliza para comparação literal: sem acento, sem pontuação, sem caixa"""
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', fold(s))).strip()


# ======================================================================= base de lei seca
FONTES_OFICIAIS = {'planalto': 'Planalto', 'legislabahia': 'Legisla Bahia'}


def oficial(v):
    """Texto oficial (Planalto ou, para as leis estaduais, o Legisla Bahia) — e não o material do curso."""
    return v.get('fonte') in FONTES_OFICIAIS


def merged_lei():
    out = {}
    for k, v in LEI_MAT.items():
        out[k] = dict(v, fonte='material')
    for k, v in LEI_OF.items():
        base = out.get(k, {})
        # A fonte vem da própria base oficial: as leis da Bahia são do Legisla Bahia, não do Planalto (07/11/2026).
        fonte = v.get('fonte') if v.get('fonte') in FONTES_OFICIAIS else 'planalto'
        out[k] = dict(v, fonte=fonte, anotacoes=base.get('anotacoes', ''), rubrica=base.get('rubrica', ''),
                      material_pagina=base.get('pagina'), material_arquivo=base.get('arquivo'))
    return out


LEI = merged_lei()
LEI_TERMS = {k: (terms(v.get('rubrica', '')), terms(v.get('texto', '')[:3000]), terms(v.get('anotacoes', '')[:2500])) for k, v in LEI.items()}
LEI_IDF = idf_table([r | t for r, t, _ in LEI_TERMS.values()])
DIPLOMA_NOME = {d['sigla']: d['nome'] for d in CATALOGO}
for v in LEI.values(): DIPLOMA_NOME.setdefault(v['sigla'], v.get('diploma', v['sigla']))
DIPLOMA_URL = {d['sigla']: d.get('url', '') for d in CATALOGO}

NUM_SPECIAL = {'DL2848': 'CP', 'DL3689': 'CPP', 'DL4657': 'LINDB', 'D678': 'CADH', 'L10406': 'L10406'}
NAME_ALIASES = [  # ordem importa: mais específicos primeiro
    (r'\bcpp\b|codigo de processo penal', 'CPP'), (r'\bcpc\b|codigo de processo civil', 'L13105'),
    (r'\bcpm\b|codigo penal militar', 'CPM'), (r'\bcp\b|codigo penal', 'CP'), (r'\badct\b', 'ADCT'),
    (r'\bcf\b|cf/88|constituicao federal|constituicao da republica|\bcrfb\b', 'CF'),
    (r'\blindb\b|lei de introducao', 'LINDB'), (r'\bctn\b|codigo tributario', 'L5172'), (r'\bctb\b|codigo de transito', 'L9503'),
    (r'\beca\b|estatuto da crianca', 'L8069'), (r'\blep\b|execucao penal', 'L7210'), (r'\bcdc\b|defesa do consumidor', 'L8078'),
    (r'\bcc\b|codigo civil', 'L10406'), (r'\blcp\b|contravencoes penais', 'DL3688'), (r'maria da penha', 'L11340'),
    (r'lei de drogas|antidrogas', 'L11343'), (r'desarmamento', 'L10826'), (r'crimes hediondos|lei dos hediondos', 'L8072'),
    (r'abuso de autoridade', 'L13869'), (r'organizac\w* criminos', 'L12850'), (r'interceptacao', 'L9296'),
    (r'lavagem', 'L9613'), (r'improbidade', 'L8429'), (r'licitac', 'L14133'), (r'tortura', 'L9455'),
    (r'pacto de sao jose|convencao americana|\bcadh\b', 'CADH'), (r'pessoa idosa|estatuto do idoso', 'L10741'),
    (r'igualdade racial', 'L12288'), (r'crimes ambientais', 'L9605'), (r'henry borel', 'L14344'),
]
for d in CATALOGO:
    for ap in d.get('apelidos', []):
        if len(ap) > 4: NAME_ALIASES.append((re.escape(fold(ap)), d['sigla']))


def resolve_sigla(text: str) -> str | None:
    t = fold(text)
    m = re.search(r'lei complementar\s*(?:n[o.\s]*)?(\d+)', t)
    if m: return 'LC' + m.group(1)
    m = re.search(r'decreto[- ]lei\s*(?:federal\s*)?(?:n[o.\s]*)?([\d\.]+\d)', t)
    if m: s = 'DL' + m.group(1).replace('.', ''); return NUM_SPECIAL.get(s, s)
    m = re.search(r'\bdecreto\s*(?:federal\s*)?(?:n[o.\s]*)?([\d\.]+\d)', t)
    if m: s = 'D' + m.group(1).replace('.', ''); return NUM_SPECIAL.get(s, s)
    m = re.search(r'\blei\s*(?:federal\s*|estadual\s*)?(?:n[o.\s]*)?(\d{1,2}\.?\d{3})\b', t)
    if m:
        s = 'L' + m.group(1).replace('.', '')
        if 'estadual' in t or 'bahia' in t: s = 'BA' + s[1:]
        return NUM_SPECIAL.get(s, s)
    for pat, sig in NAME_ALIASES:
        if re.search(pat, t): return sig
    return None


ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}


def roman(s):
    t = 0; prev = 0
    for ch in reversed(s):
        v = ROMAN.get(ch, 0); t = t - v if v < prev else t + v; prev = max(prev, v)
    return t


def parse_dispositivo(s: str) -> list[dict]:
    """'Art. 5º, XLV a XLVII' / 'arts. 1º e 2º' / 'art. 121, § 2º, IV' -> lista de alvos"""
    s = str(s or '')
    m = re.search(r'\barts?\.?\s*((?:\d[\d\.]*\s*(?:º|°|o)?(?:\s*-\s*[A-Z])?)(?:\s*(?:,|e|a|ao|até)\s*\d[\d\.]*\s*(?:º|°|o)?(?:\s*-\s*[A-Z])?)*)', s, re.I)
    if not m: return []
    nums = re.findall(r'(\d[\d\.]*)\s*(?:º|°|o)?(?:\s*-\s*([A-Z]))?', m.group(1))
    arts = [n.replace('.', '') + ('-' + suf if suf else '') for n, suf in nums]
    if re.search(r'\d\s*(?:º|°|o)?\s+(?:a|ao|até)\s+\d', m.group(1)) and len(arts) == 2 and arts[0].isdigit() and arts[1].isdigit():
        a, b = int(arts[0]), int(arts[1])
        if 0 < b - a <= 6: arts = [str(x) for x in range(a, b + 1)]
        else: arts = arts[:1]
    rest = s[:m.start()] + ' ' + s[m.end():]
    rest = re.split(r'\s[—–]\s|:', rest)[0]
    par = None
    mp = re.search(r'§\s*(\d+)\s*(?:º|°|o)?(?:\s*-\s*([A-Z]))?', rest)
    if mp: par = mp.group(1) + ('-' + mp.group(2) if mp.group(2) else '')
    elif re.search(r'par[aá]grafo [uú]nico', rest, re.I): par = 'unico'
    incs = re.findall(r'(?<![A-Za-zÀ-ú])([IVXLC]{1,7})(?![A-Za-zÀ-ú])', rest)
    inc_range = None
    if incs:
        vals = [roman(x) for x in incs]
        if len(vals) == 2 and re.search(r'[IVXLC]\s+(?:a|ao|até)\s+[IVXLC]', rest) and 0 < vals[1] - vals[0] <= 12:
            inc_range = set(range(vals[0], vals[1] + 1))
        else:
            inc_range = set(vals[:8])
    ali = None
    ma = re.search(r'al[ií]nea\s*["“]?([a-z])\b|\b([a-z])\)', rest)
    if ma: ali = ma.group(1) or ma.group(2)
    return [{'art': a, 'par': par if i == 0 else None, 'inc': inc_range if i == 0 else None, 'ali': ali if i == 0 else None} for i, a in enumerate(arts[:4])]


def extract(text: str, par, inc, ali) -> tuple[str, str]:
    lines = text.split('\n')
    is_par = lambda l: re.match(r'^(§|Parágrafo [uú]nico)', l)
    block = lines; label = 'artigo integral'
    if par:
        start = None
        for i, l in enumerate(lines):
            if par == 'unico' and re.match(r'^Parágrafo [uú]nico', l): start = i; break
            mp = re.match(r'^§\s*(\d+)\s*(?:º|°|o)?(?:\s*-\s*([A-Z]))?', l)
            if mp and par == mp.group(1) + ('-' + mp.group(2) if mp.group(2) else ''): start = i; break
        if start is None: return '', ''
        end = next((j for j in range(start + 1, len(lines)) if is_par(lines[j])), len(lines))
        block = lines[start:end]; label = 'parágrafo integral' if par != 'unico' else 'parágrafo único integral'
    elif inc:
        end = next((j for j in range(1, len(lines)) if is_par(lines[j])), len(lines))
        block = lines[:end]
    if inc:
        picked = []; on = False
        for l in block:
            mi = re.match(r'^([IVXLC]{1,7})\s*[-–]', l)
            if mi:
                v = roman(mi.group(1)); on = v in inc
                if on: picked.append(l)
                continue
            if on and re.match(r'^[a-z]\)', l): picked.append(l); continue
            if on and not re.match(r'^(Pena|§|Parágrafo)', l): continue
            on = False
        if not picked: return '', ''
        if ali:
            sub = [l for l in picked if l.startswith(ali + ')')]
            if sub: return '\n'.join(sub), 'alínea integral'
        return '\n'.join(picked), ('incisos integrais' if len(inc) > 1 else 'inciso integral')
    return '\n'.join(block), label


def lei_lookup(sigla: str, alvo: dict):
    k = f"{sigla}:{alvo['art']}"
    v = LEI.get(k)
    if not v: return None
    excerpt, label = extract(v['texto'], alvo.get('par'), alvo.get('inc'), alvo.get('ali'))
    if not excerpt: excerpt, label = v['texto'], 'artigo integral (o trecho específico não foi isolado automaticamente)'
    return v, excerpt, label


def fonte_label(v):
    if oficial(v):
        return f"Texto oficial — {FONTES_OFICIAIS[v['fonte']]} (baixado em {v.get('baixado_em', '?')})"
    return f"Lei seca do material do curso — {v.get('arquivo', '')}, p. {v.get('pagina', '?')} (destaques em CAIXA ALTA são do material)"


def enrich_law(raw) -> list[dict]:
    """recebe referência da IA ou do banco antigo e devolve cartões com texto preenchido pela base"""
    if isinstance(raw, str):
        parts = re.split(r'\s[—–]\s', raw, maxsplit=1)
        ref = {'diploma': parts[0], 'dispositivo': parts[0], 'explicacao': parts[1] if len(parts) > 1 else '', 'texto_literal': '', 'url': ''}
    elif isinstance(raw, dict):
        ref = dict(raw)
    else:
        return []
    if ref.get('status') == 'conferido' or ref.get('origin') == 'aluno':
        return [ref]
    rid = str(ref.get('ref') or '')
    combo = ' '.join(str(ref.get(x, '')) for x in ('diploma', 'dispositivo'))
    sigla = None; alvos = []
    mref = re.match(r'^([A-Z0-9]+):(\d+(?:-[A-Z])?)$', rid)
    if mref: sigla = mref.group(1); alvos = [{'art': mref.group(2), 'par': None, 'inc': None, 'ali': None}]
    disp_alvos = parse_dispositivo(ref.get('dispositivo', '') or combo)
    if disp_alvos:
        if not sigla or (alvos and disp_alvos[0]['art'] == alvos[0]['art']): alvos = disp_alvos
    sigla = sigla or resolve_sigla(combo)
    out = []
    for alvo in alvos:
        hit = lei_lookup(sigla, alvo) if sigla else None
        if not hit: continue
        v, excerpt, label = hit
        card = dict(ref)
        card.update({'diploma': DIPLOMA_NOME.get(v['sigla'], v.get('diploma', '')),
                     'dispositivo': ref.get('dispositivo') if len(alvos) == 1 and ref.get('dispositivo') else f"Art. {alvo['art']}",
                     'texto_literal': excerpt, 'texto_artigo': v['texto'] if excerpt != v['texto'] else '',
                     'anotacoes': (v.get('anotacoes') or '')[:3500], 'rubrica': v.get('rubrica', ''),
                     'extensao': label if oficial(v) else label.replace('integral', '').replace('integrais', '').strip() + ' — conforme o material (pode omitir trechos)',
                     'status': 'oficial' if oficial(v) else 'material',
                     'fonte': fonte_label(v), 'base_id': v['id'], 'alteracao_2026': bool(v.get('alteracao_2026')),
                     'url': v.get('url') or DIPLOMA_URL.get(v['sigla'], '') or ref.get('url', '')})
        out.append(card)
    if out: return out
    ref['texto_literal'] = ''  # nunca exibir redação não localizada na base
    ref['status'] = 'pendente'
    if sigla and not ref.get('url'): ref['url'] = DIPLOMA_URL.get(sigla, '')
    ref['nao_localizado'] = True
    return [ref]


# ======================================================================= jurisprudência
def norm_proc(s: str) -> str:
    s = fold(s)
    m = re.search(r'\b(agrg no |agint no |edcl no )?(resp|re|hc|rhc|are|aresp|eresp|adi|adpf|adc|ado|rcl|ms|rms|inq|ap|cc|pet)\s*([\d\.]+)', s)
    return (m.group(2) + m.group(3).replace('.', '')) if m else ''


JURIS_IDX = {}
for j in JURIS:
    k = norm_proc(j['identificador'])
    if k: JURIS_IDX.setdefault(k, j)
SUM_TERMS = {k: terms(v.get('texto', '') + ' ' + v.get('tema', '')) for k, v in SUMULAS.items()}
TESE_TERMS = {k: terms(v.get('texto', '')) for k, v in TESES.items()}
JURIS_TERMS = [terms(j.get('texto', '')[:2500] + ' ' + j.get('secao', '')) for j in JURIS]
PREC_IDF = idf_table(list(SUM_TERMS.values()) + list(TESE_TERMS.values()) + JURIS_TERMS)


def sum_url(base_id: str) -> str:
    tipo, _, num = base_id.rpartition('-')
    if base_id.startswith('SV-'): return f'https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=26&sumula={num}'
    if tipo == 'SUM-STF': return f'https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=30&sumula={num}'
    if tipo == 'SUM-STJ': return f'https://scon.stj.jus.br/SCON/SearchBRS?b=SUMU&livre=%40NUM%3D{num}'
    return ''


def find_juris(ref: dict):
    rid = str(ref.get('ref') or '').strip()
    s = ' '.join(str(ref.get(x, '')) for x in ('ref', 'tribunal', 'identificador'))
    t = fold(s)
    if rid in SUMULAS: return 'sumula', SUMULAS[rid]
    if rid in TESES: return 'tese', TESES[rid]
    m = re.search(r'sumula\s+vinculante\s*(?:n[o.\s]*)?(\d+)|\bsv\s*-?\s*(\d+)', t)
    if m:
        k = 'SV-' + (m.group(1) or m.group(2))
        if k in SUMULAS: return 'sumula', SUMULAS[k]
    m = re.search(r'sumula\s*(?:n[o.\s]*)?(\d+)', t)
    if m:
        n = m.group(1); trib = 'STJ' if 'stj' in t else ('STF' if 'stf' in t else '')
        cands = [f'SUM-{trib}-{n}'] if trib else [f'SUM-STJ-{n}', f'SUM-STF-{n}']
        found = [SUMULAS[c] for c in cands if c in SUMULAS]
        if len(found) == 1: return 'sumula', found[0]
    m = re.search(r'tema\s*(?:n[o.\s]*)?(\d+)', t)
    if m and ('repercuss' in t or 'stf' in t or rid.startswith('RG')):
        k = 'RG-' + m.group(1)
        if k in TESES: return 'tese', TESES[k]
    k = norm_proc(rid) or norm_proc(s)
    if k and k in JURIS_IDX: return 'juris', JURIS_IDX[k]
    return None, None


def literal_in(text: str, corpus: list[str]) -> bool:
    q = squash(text)
    if len(q) < 40: return False
    probe = q[:220]
    return any(probe in squash(c) for c in corpus)


def enrich_juris(raw, corpus: list[str]) -> dict:
    if isinstance(raw, str):
        ref = {'tribunal': '', 'identificador': raw, 'explicacao': raw, 'texto_literal': '', 'url': ''}
    elif isinstance(raw, dict):
        ref = dict(raw)
    else:
        return {}
    if ref.get('status') == 'conferido' or ref.get('origin') == 'aluno':
        return ref
    kind, hit = find_juris(ref)
    if hit:
        card = dict(ref)
        if kind == 'sumula':
            card.update({'tribunal': hit['tribunal'], 'identificador': ('Súmula Vinculante ' if hit['tipo'] == 'SV' else 'Súmula ') + hit['numero'] + ('' if hit['tipo'] == 'SV' else ' — ' + hit['tribunal']),
                         'texto_literal': hit['texto'], 'extensao': 'enunciado integral', 'url': sum_url(hit['id']) or ref.get('url', ''),
                         'fonte': f"DD Súmulas — {hit['arquivo']}, p. {hit['pagina']}", 'base_id': hit['id']})
        elif kind == 'tese':
            card.update({'tribunal': 'STF', 'identificador': f"Tema {hit['tema']} de Repercussão Geral" + (f" — {hit['leading_case']}" if hit.get('leading_case') else ''),
                         'texto_literal': hit['texto'], 'extensao': 'tese integral', 'url': f"https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num={hit['tema']}",
                         'fonte': f"Teses de Repercussão Geral — p. {hit['pagina']}", 'base_id': hit['id']})
        else:
            card.update({'tribunal': hit.get('tribunal') or ref.get('tribunal', ''), 'identificador': hit['identificador'],
                         'texto_literal': hit['texto'][:4000], 'extensao': 'ementa conforme material', 'fonte': f"LD DELEGADO AOCP JURIS, p. {hit['pagina']}",
                         'incidencias_aocp': [p for p in hit.get('provas', []) if 'AOCP' in p.get('banca', '').upper()], 'incidencias_total': hit.get('incidencias', 0),
                         'base_id': 'JUR-' + norm_proc(hit['identificador'])})
        card['status'] = 'material'
        return card
    lit = str(ref.get('texto_literal') or '')
    if lit and literal_in(lit, corpus):
        ref['status'] = 'material'; ref['extensao'] = ref.get('extensao') or 'trecho localizado nos materiais'
        ref['fonte'] = 'Trecho conferido por comparação literal com os PDFs do curso'
    else:
        if lit: ref['explicacao'] = (ref.get('explicacao') or '') + ' [Trecho literal sugerido pela IA omitido: não foi localizado nas fontes.]'
        ref['texto_literal'] = ''; ref['status'] = 'pendente'
    return ref


def enrich_commentary(c: dict, item: dict) -> dict:
    if not isinstance(c, dict): return c
    c = dict(c)
    laws = []
    seen = set()
    for raw in c.get('laws', []) or []:
        for card in enrich_law(raw):
            k = card.get('base_id') or json.dumps(card, ensure_ascii=False)[:200]
            if k in seen: continue
            seen.add(k); laws.append(card)
    corpus = [x['excerpt'] for x in fetch_sources(item)] + [p['text'] for p in PAGES if p['file'].startswith('LD DELEGADO AOCP JURIS')]
    jur = []; seenj = set()
    for raw in c.get('jurisprudence', []) or []:
        card = enrich_juris(raw, corpus)
        k = card.get('base_id') or json.dumps(card, ensure_ascii=False)[:200]
        if not card or k in seenj: continue
        seenj.add(k); jur.append(card)
    c['laws'] = laws; c['jurisprudence'] = jur
    return c


# ======================================================================= recuperação para o prompt
DISC_DIPLOMAS = {
    'DIREITO PENAL': ['CP', 'CF'], 'DIREITO PROCESSUAL PENAL': ['CPP', 'CF', 'L12830'],
    'DIREITO CONSTITUCIONAL': ['CF', 'L9868', 'L9882', 'L12063', 'CADH'],
    'DIREITO ADMINISTRATIVO': ['CF', 'L14133', 'L8429', 'L11079'], 'DIREITO TRIBUTÁRIO': ['L5172', 'CF', 'L8137'],
    'DIREITO CIVIL E EMPRESARIAL': ['L10406', 'LINDB', 'L8078', 'L11101'], 'DIREITO PROCESSUAL CIVIL': ['L13105', 'CF'],
    'DIREITO AMBIENTAL': ['CF', 'L6938', 'L9605', 'D6514', 'L12651', 'L9985', 'LC140'],
    'PROMOÇÃO DA IGUALDADE RACIAL E DE GÊNERO': ['CF', 'L12288', 'L7716', 'L11340', 'CP'],
    'MEDICINA LEGAL': ['CP', 'CPP'], 'LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE': ['CP', 'CPP'],
}
SUM_DISC_OK = {'DIREITO PENAL': {'DIREITO PENAL', 'DIREITO PROCESSUAL PENAL'}, 'DIREITO PROCESSUAL PENAL': {'DIREITO PROCESSUAL PENAL', 'DIREITO PENAL'},
               'LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE': {'DIREITO PENAL', 'DIREITO PROCESSUAL PENAL'}}


def family(item):
    n = item['number']
    kids = [x for x in ITEMS if x['discipline'] == item['discipline'] and x['number'].startswith(n + '.')]
    parent = n.rsplit('.', 1)[0] if '.' in n else None
    par = [x for x in ITEMS if parent and x['discipline'] == item['discipline'] and x['number'] == parent]
    return [item] + kids[:12] + par


def item_query(item) -> str:
    return ' '.join(x['label'] for x in family(item)[:6]) + ' ' + item['discipline']


REF_RE = re.compile(r'\barts?\.?\s*(\d{1,4})\s*(?:º|°|o)?(?:\s*-\s*([A-Z]))?([^\n]{0,70})', re.I)


def refs_in_text(text: str, default_sigla: str | None = None) -> Counter:
    """remissões a artigos dentro dos PDFs do curso: 'art. 107 do CP', 'art. 5º, XXXIX, da CF'"""
    out = Counter()
    for m in REF_RE.finditer(text):
        tail = m.group(3)
        sig = resolve_sigla(tail[:60]) or default_sigla
        if sig: out[f"{sig}:{m.group(1)}" + (f"-{m.group(2).upper()}" if m.group(2) else '')] += 1
    return out


def rank_articles(item, k=8, frags=None):
    q = item_query(item); qt = terms(q)
    explicit = []
    siglas = []
    for x in family(item)[:6]:
        s = resolve_sigla(x['label'])
        if s: siglas.append(s)
        for alvo in parse_dispositivo(x['label'].replace('Artigos', 'arts.').replace('Artigo', 'art.')):
            if s: explicit.append(f"{s}:{alvo['art']}")
    first = resolve_sigla(item['label'])
    if first and not any(kk.startswith(first + ':') for kk in LEI):
        return []  # diploma do item ainda não está na base: melhor não sugerir artigos de outra lei
    siglas = list(dict.fromkeys(siglas + DISC_DIPLOMAS.get(item['discipline'], [])))
    if not siglas: return []
    main = siglas[0]
    cited = Counter()
    for fr in (frags if frags is not None else fetch_sources(item)):
        cited.update(refs_in_text(fr['excerpt'], main))
    scored = []
    for key, (rub, txt, notes) in LEI_TERMS.items():
        sig = key.split(':', 1)[0]
        if sig not in siglas: continue
        hit = 2.5 * wscore(qt, rub, LEI_IDF) + wscore(qt, txt, LEI_IDF) + 0.3 * wscore(qt, notes, LEI_IDF)
        hit += 6 * min(3, cited.get(key, 0))
        if first == sig: hit *= 1.3
        if hit >= 6: scored.append((hit, key))
    scored.sort(key=lambda x: -x[0])
    keys = [e for e in explicit if e in LEI] + [kk for _, kk in scored if kk not in explicit]
    if first and not any(kk.startswith(first + ':') for kk in keys[:k]):
        keys = [kk for kk in LEI if kk.startswith(first + ':')][:4] + keys
    out = []
    for kk in list(dict.fromkeys(keys))[:k]:
        v = LEI[kk]
        out.append({'ref': kk, 'rotulo': f"{DIPLOMA_NOME.get(v['sigla'], v['sigla'])}, art. {v['art']}" + (f" ({v['rubrica']})" if v.get('rubrica') else ''),
                    'texto': v['texto'][:1800], 'fonte': FONTES_OFICIAIS.get(v.get('fonte'), 'material do curso')})
    return out


def rank_precedents(item, k=10):
    qt = terms(item_query(item)); disc = item['discipline']
    ok_disc = SUM_DISC_OK.get(disc, {disc})
    scored = []
    for key, st in SUM_TERMS.items():
        s = wscore(qt, st, PREC_IDF) * (1.4 if SUMULAS[key].get('disciplina') in ok_disc else 0.5)
        if s >= 7: scored.append((s, 'sumula', key))
    for key, st in TESE_TERMS.items():
        area = fold(TESES[key].get('area', ''))
        s = wscore(qt, st, PREC_IDF) * (1.3 if any(fold(d.split()[-1]) in area for d in ok_disc) else 0.6)
        if s >= 8: scored.append((s, 'tese', key))
    for i, st in enumerate(JURIS_TERMS):
        s = wscore(qt, st, PREC_IDF) * (1 + 0.05 * JURIS[i].get('incidencias', 0))
        if s >= 8: scored.append((s, 'juris', i))
    scored.sort(key=lambda x: -x[0])
    out = []
    for s, kind, key in scored[:k]:
        if kind == 'sumula':
            v = SUMULAS[key]; out.append({'ref': key, 'tipo': 'Súmula Vinculante' if v['tipo'] == 'SV' else 'Súmula ' + v['tribunal'], 'texto': v['texto'][:900]})
        elif kind == 'tese':
            v = TESES[key]; out.append({'ref': key, 'tipo': f"Tema {v['tema']} RG/STF", 'texto': v['texto'][:1200]})
        else:
            v = JURIS[key]; out.append({'ref': 'JUR:' + v['identificador'], 'tipo': f"{v.get('tribunal') or 'Tribunal'} — {v['identificador']} (cobrado {v.get('incidencias', 0)}x em provas de Delegado)", 'texto': v['texto'][:1500]})
    return out


PAGE_TERMS = [terms(r['text'][:5500]) for r in PAGES]
PAGE_IDF = idf_table(PAGE_TERMS)


def fetch_sources(item):
    q = terms(item_query(item)); disc = item['discipline']
    scored = []
    for row, body in zip(PAGES, PAGE_TERMS):
        if row.get('posterior'): continue  # atualizações posteriores ao edital não são fonte do núcleo exigível
        d = row.get('disciplinas', '*')
        if d != '*' and disc not in d.split('|'): continue
        hit = q & body
        if not hit: continue
        ratio = wscore(q, body, PAGE_IDF)
        if d != '*': ratio *= 1.5
        if 'LD DELEGADO AOCP' in row['file']: ratio *= 1.25
        if row['file'].startswith('Atualizações'): ratio *= 0.8   # evita que o PDF de 335 páginas domine
        scored.append((ratio, row))
    scored.sort(key=lambda x: -x[0]); selected = []; used = set(); per_file = Counter()
    for score, row in scored:
        if len(selected) >= 7: break
        kf = (row['file'], row['page'])
        if kf in used or score < 4 or per_file[row['file']] >= 3: continue
        used.add(kf); per_file[row['file']] += 1
        selected.append({'file': row['file'], 'page': row['page'], 'excerpt': row['text'][:2700]})
    return selected


# ======================================================================= prompt
SYS = """Você é a banca elaboradora de uma prova de DELEGADO DE POLÍCIA CIVIL no estilo do Instituto AOCP (concurso PC-BA, Edital SAEB 02/2026). Escreva em português do Brasil, com rigor técnico e linguagem de prova — enxuta, impessoal, sem floreios.
MARCO NORMATIVO: Edital publicado em 29/07/2026 (retificado em 16/09/2026). Não aplique leis posteriores a essa data, salvo exceção expressa do Anexo I. Nunca invente número de processo, tese, citação, estatística ou fonte.
BASE LOCAL: o pedido traz 'dispositivos_da_base' (lei seca com 'ref' SIGLA:ARTIGO) e 'precedentes_da_base' (súmulas, teses de RG e julgados cobrados em provas, com 'ref'). A AOCP cobra literalidade: construa a questão sobre a redação desses dispositivos/precedentes quando pertinentes ao ponto do edital. CAIXA ALTA no material é só grifo didático.
LETRA DA LEI EM TODAS AS DISCIPLINAS (titular, 01/11/2026): a AOCP cobra o DETALHE da legislação aplicada — prazos (número, unidade, termo inicial), quóruns, competências, legitimados, penas (reclusão × detenção, mínimo e máximo), qualificadoras, causas de aumento e de diminuição (frações exatas), requisitos, exceções e vedações expressas, "poderá" × "deverá". Em Civil, Empresarial, Processo Civil, Ambiental e Tributário, a questão gira sobre a literalidade dos dispositivos; nas demais, o caso prático se resolve por um detalhe legal preciso. Distratores trocam UM desses detalhes.

=== A QUESTÃO (estilo AOCP) ===
1. Escolha UM formato em 'formato' e varie entre as rodadas:
   • "situacoes": caso prático da rotina policial com 2 ou 3 situações rotuladas (Situação I:, Situação II:, Situação III:), personagens com nomes simples (Antônio, Bruno, Carlos…), datas e fatos objetivos — cada situação cobra um instituto diferente do mesmo ponto;
   • "assertivas": "Analise as assertivas a seguir." + I, II, III e IV; alternativas no padrão AOCP "Apenas I e II.", "Apenas II, III e IV.", "I, II, III e IV.";
   • "direta": enunciado curto (1 a 3 linhas) seguido de cinco alternativas sobre a literalidade da lei, súmula ou tese.
2. Em 'stem', separe parágrafos com \\n. O comando final é sempre uma linha própria, no padrão AOCP: "Considerando …, assinale a alternativa correta." ou "… assinale a alternativa INCORRETA." (negativa em caixa alta).
3. Alternativas A–E: estrutura PARALELA (no formato situações: "Na primeira situação, …; na segunda, …; na terceira, …."), mesma extensão e mesmo tom, sem "sempre/nunca/jamais" como pista, sem alternativa mais técnica ou mais longa. Cada distrator troca UMA ou DUAS conclusões por erros típicos da banca: regra × exceção, confusão entre institutos vizinhos, prazo/quórum/competência trocados, inversão do entendimento sumulado, literalidade alterada em uma palavra.
4. Exatamente UMA alternativa correta. Distribua a letra do gabarito considerando 'gabaritos_anteriores'.

=== O COMENTÁRIO (estilo professor de cursinho, direto) ===
• commentary.summary: 1 ou 2 frases dizendo o que a questão cobra ("A questão envolve simultaneamente …").
• commentary.alternatives.{A..E}: {"veredito":"Correta" ou "Errada", "titulo": frase curta (máx. 12 palavras) que diz o erro/acerto começando por verbo — ex.: "desconsidera a lei intermediária benéfica", "confunde início da consumação com cessação da permanência", "aplica adequadamente os três institutos"; "explicacao": 2 a 4 frases objetivas, citando artigo/súmula que resolvem a alternativa}.
• commentary.certo_errado ("Certo ou Errado — estudo ativo"; substitui a antiga aula de aprofundamento): 8 a 15 afirmações para o aluno julgar, que juntas cobrem o que a aula ensinaria — DOUTRINA (conceitos, distinções, exceções), LEI SECA (literalidade dos dispositivos que resolvem a questão; troque UMA palavra para fazer a errada, como a AOCP faz) e JURISPRUDÊNCIA (súmulas, teses e precedentes da base). Cada item: {"afirmacao": 1 ou 2 frases no estilo de prova, "gabarito": "C" ou "E", "tipo": "doutrina" | "lei_seca" | "jurisprudencia", "comentario": 2 a 4 frases que explicam POR QUE está certo ou errado — no item errado, diga a versão correta, "fundamento": artigo, súmula ou precedente que resolve (ou vazio)}. Misture certos e errados (ao menos 3 de cada), use ao menos 2 dos 3 tipos e transforme as pegadinhas recorrentes da AOCP em itens errados. Pode avançar em conteúdo correlato do edital. Não repita literalmente as alternativas A–E.
• commentary.laws: cite os dispositivos usados (ref da base + dispositivo preciso: artigo, §, inciso). NÃO transcreva a lei: o sistema preenche a redação a partir da base local. 'explicacao' = 1 frase do que memorizar.
• commentary.jurisprudence: prefira 'precedentes_da_base' (informe 'ref'); o sistema preenche o enunciado. 'texto_literal' fica vazio, salvo trecho copiado exatamente de 'fragmentos_do_material_anexo'. 'explicacao' = 1 frase do que memorizar.
• commentary.auditoria: {"checklist": ["Uma única alternativa correta", "Cinco alternativas juridicamente plausíveis", "Extensão das alternativas equilibrada", "Fundamentação legal e jurisprudencial"] — ajuste ao caso real; "cobertura": o que a questão trabalhou e o que fica para outras questões do mesmo ponto; "fundamento_edital": "Item X — texto do ponto do edital"}.
• commentary.gaps: subtemas do ponto ainda não cobrados (para a rodada 2).
• commentary.itens_correlatos: ids (o campo 'id' de 'pontos_para_correlacao') de OUTROS pontos do edital que a aula e os comentários EXPLICARAM de verdade — com profundidade suficiente para o aluno dar baixa nesses pontos. Pode avançar em conteúdo correlato para isso. Lista vazia se nenhum; no máximo 5; NUNCA invente id.
Somente JSON válido, sem Markdown e sem texto fora do JSON."""

LESSON_TYPES = ['conceito', 'regra', 'distincao', 'fundamento', 'exemplo', 'juris', 'pegadinha', 'atencao', 'tabela', 'linha_do_tempo']


def _obj(props: dict) -> dict:
    return {'type': 'object', 'additionalProperties': False, 'properties': props, 'required': list(props)}


S = {'type': 'string'}
ARR_S = {'type': 'array', 'items': S}
ALT = _obj({'veredito': {'type': 'string', 'enum': ['Correta', 'Errada']}, 'titulo': S, 'explicacao': S})
BLOCK = _obj({'type': {'type': 'string', 'enum': LESSON_TYPES}, 'heading': S, 'body': S,
              'columns': ARR_S, 'rows': {'type': 'array', 'items': ARR_S},
              'timeline': {'type': 'array', 'items': _obj({'marco': S, 'rotulo': S, 'detalhe': S, 'tom': {'type': 'string', 'enum': ['neutro', 'favoravel', 'desfavoravel']}})}})
# 31/10/2026 (titular): a aula, as pegadinhas e o mapa mental viram itens Certo/Errado comentados —
# "a ideia é ficar sempre um estudo ativo". A questão AOCP não muda.
CE_ITEM = _obj({'afirmacao': S, 'gabarito': {'type': 'string', 'enum': ['C', 'E']},
                'tipo': {'type': 'string', 'enum': ['doutrina', 'lei_seca', 'jurisprudencia']},
                'comentario': S, 'fundamento': S})
CE_SCHEMA = _obj({'certo_errado': {'type': 'array', 'items': CE_ITEM}})


def tem_fonte(c) -> bool:
    """O comentário cita lei ou jurisprudência? Sem isso, item de lei seca ou de jurisprudência seria inventado."""
    return bool(isinstance(c, dict) and (c.get('laws') or c.get('jurisprudence')))


def validar_ce(itens, exige_tipos=True, minimo=8, maximo=15, min_cada=3) -> str | None:
    """Os itens Certo/Errado: 8 a 15, com C e E (ao menos 3 de cada) e, se exige_tipos, ao menos 2 dos 3 tipos.

    💥 31/10/2026: o ponto CON-2 (perspectivas sociológica, política e jurídica da Constituição) não tem artigo
    nem precedente — exigir 2 tipos ali obrigava a IA a INVENTAR fonte, e ela, certa, recusou 4 vezes. Entre
    cobrir os três tipos e não inventar, vence não inventar (REGRA ZERO): sem fonte no comentário, só doutrina."""
    if not isinstance(itens, list) or not minimo <= len(itens) <= maximo: return f'Certo/Errado: são de {minimo} a {maximo} itens.'
    for n, it in enumerate(itens, 1):
        if not isinstance(it, dict): return f'Certo/Errado: item {n} malformado.'
        if it.get('gabarito') not in ('C', 'E'): return f'Certo/Errado: item {n} sem gabarito C ou E.'
        if it.get('tipo') not in ('doutrina', 'lei_seca', 'jurisprudencia'): return f'Certo/Errado: item {n} com tipo inválido.'
        if len(str(it.get('afirmacao', ''))) < 40: return f'Certo/Errado: afirmação {n} curta demais.'
        if len(str(it.get('comentario', ''))) < 60: return f'Certo/Errado: comentário {n} curto demais.'
    gab = Counter(it['gabarito'] for it in itens)
    if gab['C'] < min_cada or gab['E'] < min_cada: return f'Certo/Errado: misture certos e errados (ao menos {min_cada} de cada).'
    if exige_tipos and len({it['tipo'] for it in itens}) < 2: return 'Certo/Errado: use ao menos 2 tipos (doutrina, lei seca, jurisprudência).'
    return None


SCHEMA = _obj({
    'formato': {'type': 'string', 'enum': ['situacoes', 'assertivas', 'direta']},
    'stem': S, 'options': _obj({L: S for L in 'ABCDE'}), 'correct': {'type': 'string', 'enum': list('ABCDE')},
    'tag': S, 'difficulty': S, 'source_scope': S,
    'commentary': _obj({
        'summary': S, 'alternatives': _obj({L: ALT for L in 'ABCDE'}),
        'certo_errado': {'type': 'array', 'items': CE_ITEM},
        'laws': {'type': 'array', 'items': _obj({'ref': S, 'diploma': S, 'dispositivo': S, 'explicacao': S, 'extensao': S})},
        'jurisprudence': {'type': 'array', 'items': _obj({'ref': S, 'tribunal': S, 'identificador': S, 'data': S, 'texto_literal': S, 'explicacao': S, 'url': S})},
        'gaps': ARR_S, 'itens_correlatos': ARR_S,
        'auditoria': _obj({'checklist': ARR_S, 'cobertura': S, 'fundamento_edital': S})}),
})


# 01/11/2026 (titular): ao montar o bloco, cada assunto pode vir como OBJETIVA (estudar) ou como REVISÃO
# RÁPIDA Certo/Errado ("tem temas que eu já estudei bastante e quero passar mais rápido"), com os comentários
# no mesmo padrão das objetivas (veredito + título curto + explicação) e foco na letra da lei.
REV_ITEM = _obj({'afirmacao': S, 'gabarito': {'type': 'string', 'enum': ['C', 'E']},
                 'tipo': {'type': 'string', 'enum': ['doutrina', 'lei_seca', 'jurisprudencia']},
                 'titulo': S, 'comentario': S, 'fundamento': S})
_COM = SCHEMA['properties']['commentary']['properties']
REV_SCHEMA = _obj({'difficulty': S, 'commentary': _obj({
    'summary': S, 'certo_errado': {'type': 'array', 'items': REV_ITEM}, 'laws': _COM['laws'], 'jurisprudence': _COM['jurisprudence'],
    'gaps': ARR_S, 'itens_correlatos': ARR_S, 'auditoria': _COM['auditoria']})})
REV_MIN, REV_MAX = 12, 20
REV_SYS = (SYS.split('=== A QUESTÃO')[0] + f"""=== REVISÃO RÁPIDA CERTO/ERRADO (o aluno já estudou este ponto e quer passar rápido) ===
Não escreva questão de múltipla escolha. Escreva de {REV_MIN} a {REV_MAX} itens Certo/Errado que cubram o ponto oficial HORIZONTALMENTE: todos os aspectos cobráveis, não um só.
• Prioridade é a LETRA DA LEI APLICADA: quando o ponto tem lei, ao menos metade dos itens é do tipo "lei_seca", cada um sobre um detalhe que a AOCP cobra (prazo, fração, pena, qualificadora, majorante, quórum, competência, legitimado, exceção, "poderá"/"deverá"). O item errado troca UM detalhe, como a banca faz. Complete com jurisprudência da base e a doutrina essencial.
• Cada item: {{"afirmacao": 1 ou 2 frases de prova, "gabarito": "C" ou "E", "tipo": "doutrina" | "lei_seca" | "jurisprudencia", "titulo": frase curta (máx. 12 palavras) começando por verbo, no padrão do comentário das alternativas — ex.: "troca o prazo de 10 por 15 dias", "reproduz fielmente o art. 121, § 2º, IV", "confunde majorante com qualificadora"; "comentario": 2 a 4 frases — por que está certo ou errado; no errado, a versão correta com o detalhe exato; "fundamento": artigo, súmula ou precedente (ou vazio)}}.
• Ao menos 4 certos e 4 errados; ao menos 2 tipos quando houver lei ou precedente; ordem misturada.
• commentary.summary (1 ou 2 frases: o que a revisão cobriu), commentary.laws, commentary.jurisprudence, commentary.auditoria, commentary.gaps e commentary.itens_correlatos seguem as MESMAS regras da questão objetiva: cite a lei pela 'ref' da base, sem transcrever (o sistema preenche); nunca invente artigo, número de processo, tese ou id.
• 'difficulty': "médio" ou "alto".
Somente JSON válido, sem Markdown e sem texto fora do JSON.""")
AUDIT_REV_SYS = ('Você é auditor crítico de itens Certo/Errado para Delegado no estilo Instituto AOCP. Retorne APENAS JSON {"approved":true/false,"problems":["..."],"reason":"..."}. '
                 'Confira, item por item, se o gabarito C/E está juridicamente certo no marco de 29/07/2026, se o comentário e o título explicam o gabarito sem contradição '
                 'e se o item errado tem UM erro claro (sem ambiguidade). A redação literal da lei NÃO é enviada; não reprove por falta de transcrição. '
                 'Reprove apenas por erro jurídico real ou item ambíguo, apontando o número do item.')


def recent_formats(n=8):
    out = []
    for path in sorted(CACHE.glob('*_R*.json'), key=lambda p: p.stat().st_mtime)[-n:]:
        try: out.append(json.loads(path.read_text('utf8')).get('formato', ''))
        except Exception: pass
    return [x for x in out if x]


EXEMPLO = load('exemplo_aocp.json', None)


def exemplo_compacto():
    """questão-modelo do professor: ancora o estilo (enunciado, alternativas, comentários e aula)"""
    if not EXEMPLO: return None
    e = json.loads(json.dumps(EXEMPLO))
    c = e.get('commentary', {})
    for chave in ('mindmap', 'mindmap_titulo', 'gaps', 'lessons', 'traps'): c.pop(chave, None)
    return e


def user_prompt(item, round_, gaps, prev):
    related = family(item)
    frags = fetch_sources(item)
    arts = rank_articles(item, frags=frags)
    first = resolve_sigla(item['label'])
    aviso_lei = ''
    if first and not arts:
        aviso_lei = (f"O texto de {DIPLOMA_NOME.get(first, first)} ainda não está na base local (rode atualizar_lei_seca.bat). "
                     'Cite os dispositivos com precisão em laws (diploma + artigo); o sistema marcará a conferência como pendente.')
    return json.dumps({
        'disciplina': item['discipline'], 'ponto_oficial': item['number'], 'conteudo_literal': item['label'],
        'itens_relacionados': [{'item': t['number'], 'texto': t['label']} for t in related[1:]],
        'pontos_para_correlacao': [{'id': t['id'], 'ponto': t['number'], 'texto': t['label'][:160]}
                                   for t in ITEMS if t['discipline'] == item['discipline'] and t['id'] != item['id']],
        'rodada': round_, 'prioridade': item['priority'],
        'missao_especifica': ('COBERTURA HORIZONTAL: explorar o maior número possível de aspectos do ponto oficial e mapear lacunas' if round_ == 1 else
                              'APROFUNDAMENTO VERTICAL: concentrar-se em exceções, distinções, controvérsias e erros identificados, sem repetir o núcleo da primeira rodada'),
        'lacunas_previas': gaps[:15], 'gabaritos_anteriores': prev[-12:], 'formatos_anteriores': recent_formats(),
        'corte_legislativo': CUTOFF + ', salvo exceção do Anexo I comprovada',
        'dispositivos_da_base': arts,
        'aviso_lei_seca': aviso_lei,
        'precedentes_da_base': rank_precedents(item),
        'fragmentos_do_material_anexo': frags,
        'transcricoes_primarias_conferidas': next((OFFICIAL[c] for c in [item['id'], item['id'].rsplit('.', 1)[0]] if c in OFFICIAL), {}),
        'QUESTAO_MODELO_DE_ESTILO': {'instrucao': 'Siga o FORMATO e o TOM deste modelo (enunciado, paralelismo das alternativas, comentário com veredito + título curto, auditoria). A aula do modelo foi SUBSTITUÍDA por "certo_errado" — não gere aula, pegadinhas nem mapa mental. NÃO copie o conteúdo nem o tema.', 'modelo': exemplo_compacto()},
        'aviso': 'Fragmentos são excertos dos materiais do curso, não texto oficial integral nem prova de vigência. Indique arquivo e página somente quando sustentados no material.'
    }, ensure_ascii=False)


# ======================================================================= chamadas aos modelos
def post_json(url, payload, headers, timeout=240):
    req = urllib.request.Request(url, data=json.dumps(payload, ensure_ascii=False).encode(), headers={'Content-Type': 'application/json', **headers}, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res: return json.load(res)
    except urllib.error.HTTPError as exc:
        msg = exc.read(1500).decode('utf8', 'replace')
        raise RuntimeError(f'API HTTP {exc.code}: {msg}')


OPENAI_FORMAT = {}  # modelo -> último formato aceito

# 31/10/2026 (D-007, docs/VIABILIDADE_BLOCOS_30.md): mede cada geração — chamadas e tokens somados
# por thread, porque cada geração roda numa thread do WORKERS. Antes, nada era registrado e o custo
# de um bloco de 30 não tinha como ser medido.
_MEDIDA = threading.local()


def _somar_uso(res, provider):
    m = getattr(_MEDIDA, 'atual', None)
    if m is None or not isinstance(res, dict): return
    u = res.get('usage') or {}
    m['chamadas'] += 1
    m['tokens_entrada'] += int(u.get('input_tokens') or 0)
    m['tokens_saida'] += int(u.get('output_tokens') or 0)


def call_model(system, user, provider, schema=None):
    provider = (provider or 'openai').lower()
    if provider == 'openai':
        key = os.environ.get('OPENAI_API_KEY', '')
        if not key: raise RuntimeError('Configure OPENAI_API_KEY no arquivo .env para gerar novas questões.')
        model = os.environ.get('OPENAI_MODEL', 'gpt-6.1-sol')
        msg = [{'role': 'user', 'content': [{'type': 'input_text', 'text': 'FORMATO OBRIGATÓRIO: responda somente com um objeto JSON válido.\n\n' + user}]}]
        formats = []
        if schema and os.getenv('OPENAI_STRUCTURED', '1') != '0':
            formats.append({'type': 'json_schema', 'name': 'questao_aocp', 'schema': schema, 'strict': True})
        formats += [{'type': 'json_object'}, {'type': 'text'}]
        start = OPENAI_FORMAT.get((model, bool(schema)), 0)
        last_exc = None
        for i in range(start, len(formats)):
            data = {'model': model, 'instructions': system, 'input': msg, 'max_output_tokens': int(os.getenv('MAX_OUTPUT_TOKENS', '14000')), 'text': {'format': formats[i]}}
            try:
                res = post_json('https://api.openai.com/v1/responses', data, {'Authorization': 'Bearer ' + key})
                OPENAI_FORMAT[(model, bool(schema))] = i
                break
            except RuntimeError as exc:
                last_exc = exc; d = str(exc).lower()
                if 'http 400' in d and any(w in d for w in ('format', 'schema', 'json', 'text')):
                    print(f"[trilha] formato {formats[i]['type']} recusado pela API; tentando o próximo.")
                    continue
                raise
        else:
            raise last_exc
        raw = ''.join(c.get('text', '') for out in res.get('output', []) for c in out.get('content', []) if c.get('type') == 'output_text') or res.get('output_text', '')
    elif provider == 'claude':
        key = os.environ.get('ANTHROPIC_API_KEY', '')
        if not key: raise RuntimeError('Configure ANTHROPIC_API_KEY no arquivo .env para gerar novas questões.')
        model = os.environ.get('CLAUDE_MODEL', 'claude-sonnet-4-6')
        res = post_json('https://api.anthropic.com/v1/messages', {'model': model, 'max_tokens': int(os.getenv('MAX_OUTPUT_TOKENS', '14000')), 'system': system,
                                                                   'messages': [{'role': 'user', 'content': user}]}, {'x-api-key': key, 'anthropic-version': '2023-06-01'})
        raw = ''.join(c.get('text', '') for c in res.get('content', []) if c.get('type') == 'text')
    else:
        raise RuntimeError('Provedor inválido; use openai ou claude.')
    _somar_uso(res, provider)
    m = re.search(r'\{.*\}', raw, re.S)
    if not m: raise RuntimeError('API não retornou JSON reconhecível.')
    try: return json.loads(m.group(0))
    except json.JSONDecodeError as exc: raise RuntimeError('JSON inválido do modelo: ' + str(exc))


def has_key(provider):
    return bool(os.getenv('OPENAI_API_KEY' if provider == 'openai' else 'ANTHROPIC_API_KEY'))


def audit_provider(gen_provider):
    pref = os.getenv('AUDIT_PROVIDER', 'auto').lower()
    if pref in ('openai', 'claude') and has_key(pref): return pref
    other = 'claude' if gen_provider == 'openai' else 'openai'
    return other if pref == 'auto' and has_key(other) else gen_provider


def alt_parts(c, L):
    """aceita o formato novo {veredito,titulo,explicacao} e o antigo (string)"""
    a = (c.get('alternatives') or {}).get(L)
    if isinstance(a, dict): return a.get('veredito', ''), str(a.get('titulo', '')), str(a.get('explicacao', ''))
    return '', '', str(a or '')


def validate(q):
    if not isinstance(q, dict): return 'A questão não é um objeto JSON.'
    stem = str(q.get('stem', ''))
    if len(stem) < 90: return 'Enunciado curto demais.'
    if not re.search(r'assinale|marque|analise', stem, re.I): return 'Falta o comando AOCP ("assinale a alternativa correta/INCORRETA").'
    op = q.get('options', {})
    if not isinstance(op, dict) or set(op) != set('ABCDE'): return 'Faltam alternativas A-E.'
    min_len = 6 if q.get('formato') == 'assertivas' else 25
    if any(not isinstance(op[k], str) or len(op[k].strip()) < min_len for k in 'ABCDE'): return 'Alternativa curta/vazia.'
    if len({op[k].casefold().strip() for k in 'ABCDE'}) < 5: return 'Alternativas duplicadas.'
    if q.get('correct') not in list('ABCDE'): return 'Gabarito inválido.'
    c = q.get('commentary', {})
    if not isinstance(c, dict) or set(c.get('alternatives', {})) != set('ABCDE'): return 'Comentários A-E incompletos.'
    vered = {L: alt_parts(c, L)[0] for L in 'ABCDE'}
    if all(vered.values()):
        if [L for L in 'ABCDE' if vered[L] == 'Correta'] != [q['correct']]: return 'Vereditos das alternativas incoerentes com o gabarito (deve haver exatamente uma "Correta", igual a correct).'
    for L in 'ABCDE':
        _, tit, exp = alt_parts(c, L)
        if len(exp) < 60: return f'Comentário da alternativa {L} curto demais.'
        if tit and len(tit.split()) > 18: return f'Título do comentário da alternativa {L} longo demais (máx. 12 palavras).'
    err_ce = validar_ce(c.get('certo_errado'), tem_fonte(c))
    if err_ce: return err_ce
    for group in ('laws', 'jurisprudence'):
        if not isinstance(c.get(group, []), list): return 'Referências jurídicas devem ser listas.'
    if q.get('formato') != 'assertivas':
        sizes = [len(op[k]) for k in 'ABCDE']
        if min(sizes) > 0 and max(sizes) > min(sizes) * 1.9: return 'Alternativas desequilibradas em extensão (a AOCP mantém tamanhos próximos).'
    return None


def file_for(itemid, round_):
    return CACHE / (re.sub('[^a-zA-Z0-9_.-]', '_', itemid) + '_R' + str(round_) + '.json')


def stored(key):
    if key in BANK: return BANK[key]
    iid, r = key.rsplit('|', 1); f = file_for(iid, r)
    if f.exists():
        try: return json.loads(f.read_text('utf8'))
        except Exception: return None
    return None


AUDIT_SYS = ('Você é auditor crítico de questões para Delegado no estilo Instituto AOCP. Retorne APENAS JSON {"approved":true/false,"problems":["..."],"reason":"..."}. '
             'Audite SOMENTE a questão e o comentário: uma única alternativa juridicamente correta; alternativas paralelas e de extensão próxima; comando no padrão AOCP; '
             'distratores plausíveis (sem absurdos); coerência com o marco de 29/07/2026; consistência entre gabarito, vereditos, comentários e os itens certo/errado (o gabarito C/E de cada item precisa estar juridicamente certo). '
             'A redação literal da lei seca NÃO é enviada (o sistema a preenche depois a partir da base local); não reprove por falta ou forma de transcrição de lei, '
             'nem pelo checklist interno. Reprove apenas por erro jurídico real, ambiguidade de gabarito ou defeito de construção da questão.')


def audit_view(q):
    """o que o auditor recebe: questão + comentário, sem os textos de lei seca da base (o material anotado pode conter grifos e notas)"""
    c = dict(q.get('commentary', {}))
    c['laws'] = [{k: v for k, v in (l if isinstance(l, dict) else {'dispositivo': str(l)}).items() if k in ('diploma', 'dispositivo', 'explicacao')} for l in c.get('laws', [])]
    c.pop('auditoria', None)
    return json.dumps(dict(q, commentary=c), ensure_ascii=False)[:40000]


def correlatos_validos(ids, itemid, limite=5):
    """D-005: a baixa por correlação é automática — por isso só passa id que EXISTE no edital, que não é
    o próprio ponto e sem repetição. O modelo pode inventar id; a tela nunca recebe um."""
    if not isinstance(ids, list): return []
    out = []
    for i in ids:
        if isinstance(i, str) and i in BY_ID and i != itemid and i not in out: out.append(i)
    return out[:limite]


def _checar_revisao(q) -> str | None:
    c = q.get('commentary') if isinstance(q, dict) else None
    if not isinstance(c, dict): return 'Revisão sem commentary.'
    err = validar_ce(c.get('certo_errado'), exige_tipos=tem_fonte(c), minimo=REV_MIN, maximo=REV_MAX, min_cada=4)
    if err: return err
    if any(len(str(x.get('titulo', ''))) < 8 for x in c['certo_errado']): return 'Certo/Errado: cada item precisa de título curto (padrão das alternativas).'
    return None


def gerar_revisao(item, round_, provider, gaps, t0):
    """revisão rápida C/E de um ponto: mesma base (lei, precedentes, fragmentos), mesma auditoria dupla (D-007)"""
    base = json.loads(user_prompt(item, round_, gaps or [], []))
    for chave in ('QUESTAO_MODELO_DE_ESTILO', 'gabaritos_anteriores', 'formatos_anteriores'): base.pop(chave, None)
    base['formato_pedido'] = f'REVISÃO RÁPIDA CERTO/ERRADO ({REV_MIN} a {REV_MAX} itens), foco na letra da lei aplicada'
    prompt = json.dumps(base, ensure_ascii=False)
    q = call_model(REV_SYS, prompt, provider, REV_SCHEMA); err = _checar_revisao(q)
    if err:
        q = call_model(REV_SYS, 'Reelabore corrigindo especificamente: ' + err + '\nBase do pedido: ' + prompt[:30000] + '\nVersão anterior: ' + json.dumps(q, ensure_ascii=False)[:18000], provider, REV_SCHEMA)
        err = _checar_revisao(q)
    if err: raise RuntimeError('Revisão reprovada na auditoria formal: ' + err)
    alerta = []
    if os.getenv('DEEP_AUDIT', '1').lower() not in ('0', 'false', 'nao'):
        auditor = audit_provider(provider)
        a = call_model(AUDIT_REV_SYS, audit_view(q), auditor)
        if not a.get('approved'):
            problems = [str(x) for x in a.get('problems', [])]
            q2 = call_model(REV_SYS, 'AUDITORIA JURÍDICA REPROVOU. Problemas: ' + '; '.join(problems)[:900] + '\nRefaça integralmente sem esses problemas. Base: ' + prompt, provider, REV_SCHEMA)
            if _checar_revisao(q2) is None:
                q = q2
                a2 = call_model(AUDIT_REV_SYS, audit_view(q), auditor)
                if not a2.get('approved'): alerta = [str(x) for x in a2.get('problems', [])]
            else:
                alerta = problems
            if alerta and os.getenv('AUDIT_STRICT', '0') == '1':
                raise RuntimeError('Auditoria independente ainda detectou problemas: ' + str(alerta)[:500])
    q['formato'] = 'revisao_ce'; q['n_itens'] = len(q['commentary']['certo_errado'])
    return _finalizar(q, item, round_, provider, alerta, t0)


def generate(itemid, round_, provider, gaps=None, modo='obj'):
    key = f'{itemid}|{round_}'
    existing = stored(key)
    if existing: return existing
    item = BY_ID[itemid]
    _MEDIDA.atual = {'chamadas': 0, 'tokens_entrada': 0, 'tokens_saida': 0}; t0 = time.time()
    if modo == 'ce': return gerar_revisao(item, round_, provider, gaps, t0)
    previous = [v['correct'] for v in BANK.values() if 'correct' in v]
    for path in sorted(CACHE.glob('*_R*.json'), key=lambda p: p.stat().st_mtime)[-30:]:
        try: previous.append(json.loads(path.read_text('utf8'))['correct'])
        except Exception: pass
    prompt = user_prompt(item, round_, gaps or [], previous)
    q = call_model(SYS, prompt, provider, SCHEMA)
    err = validate(q)
    if err:
        q = call_model(SYS, 'Reelabore esta questão corrigindo especificamente: ' + err + '\nBase do pedido: ' + prompt[:30000] + '\nQuestão anterior: ' + json.dumps(q, ensure_ascii=False)[:18000], provider, SCHEMA)
        err = validate(q)
    if err: raise RuntimeError('Questão reprovada na auditoria formal: ' + err)
    alerta = []
    if os.getenv('DEEP_AUDIT', '1').lower() not in ('0', 'false', 'nao'):
        auditor = audit_provider(provider)
        assessment = call_model(AUDIT_SYS, audit_view(q), auditor)
        if not assessment.get('approved'):
            problems = [str(x) for x in assessment.get('problems', [])]
            q2 = call_model(SYS, 'AUDITORIA JURÍDICA REPROVOU. Problemas: ' + '; '.join(problems)[:900] + '\nRefaça integralmente a questão sem esses problemas. Base: ' + prompt, provider, SCHEMA)
            if validate(q2) is None:
                q = q2
                assessment2 = call_model(AUDIT_SYS, audit_view(q), auditor)
                if not assessment2.get('approved'): alerta = [str(x) for x in assessment2.get('problems', [])]
            else:
                alerta = problems  # a refação saiu mal formada: mantém a 1ª versão, com o alerta
            if alerta and os.getenv('AUDIT_STRICT', '0') == '1':
                raise RuntimeError('Auditoria independente ainda detectou problemas: ' + str(alerta)[:500])
    return _finalizar(q, item, round_, provider, alerta, t0)


def _finalizar(q, item, round_, provider, alerta, t0):
    """o que toda geração grava (objetiva ou revisão C/E): texto da base, correlatos filtrados, métricas e o arquivo"""
    itemid = item['id']
    q['commentary'] = enrich_commentary(q.get('commentary', {}), item)
    q['commentary']['itens_correlatos'] = correlatos_validos(q['commentary'].get('itens_correlatos'), itemid)
    if alerta: q['commentary']['alerta_auditoria'] = alerta[:6]
    q['id'] = itemid; q['round'] = round_; q['origin'] = f'Gerada via {provider} com base na trilha, na lei seca local e nos excertos anexos'
    q['sources_used'] = [{'file': x['file'], 'page': x['page']} for x in fetch_sources(item)]
    q['release'] = RELEASE
    modelo = os.environ.get('OPENAI_MODEL', 'gpt-6.1-sol') if provider == 'openai' else os.environ.get('CLAUDE_MODEL', 'claude-sonnet-4-6')
    q['metricas'] = dict(_MEDIDA.atual, duracao_s=round(time.time() - t0, 1), provider=provider, modelo=modelo,
                         gerada_em=time.strftime('%d/%m/%Y %H:%M'))
    f = file_for(itemid, round_); tmp = f.with_suffix('.tmp'); tmp.write_text(json.dumps(q, ensure_ascii=False, indent=2), encoding='utf8'); os.replace(tmp, f)
    return q


CE_SYS = ('Você é professor de cursinho para DELEGADO (banca Instituto AOCP, PC-BA 2026). Recebe uma questão JÁ PRONTA e o '
          'comentário dela (aula, lei seca, jurisprudência, pegadinhas). NÃO altere a questão. Transforme o conteúdo do comentário em '
          'itens Certo/Errado para estudo ativo, cobrindo DOUTRINA, LEI SECA (literalidade: troque UMA palavra para fazer o item errado, '
          'como a AOCP faz) e JURISPRUDÊNCIA. Cada item: afirmacao (1 ou 2 frases de prova), gabarito "C" ou "E", tipo '
          '("doutrina", "lei_seca" ou "jurisprudencia"), comentario (2 a 4 frases: por que está certo ou errado; no errado, a versão '
          'correta) e fundamento (artigo, súmula ou precedente; vazio se não houver). De 8 a 15 itens, ao menos 3 certos e 3 errados, '
          'ao menos 2 tipos; as pegadinhas viram itens errados. Use só o que está no comentário e na questão: nunca invente número de '
          'processo, tese ou artigo. Somente JSON válido {"certo_errado": [...]}.')
CONVERSOES = {}  # caminho do arquivo -> 'na_fila' | 'pronta' | 'erro: …'  (D-008, 31/10/2026)


def converter_ce(path: pathlib.Path, provider: str):
    """Converte o comentário de UMA questão já gerada para Certo/Errado. A questão não muda; a aula antiga
    fica em commentary.aula_original (dado não se apaga, HARNESS §F17)."""
    q = json.loads(path.read_text('utf8'))
    c = q.get('commentary') or {}
    exige = tem_fonte(c)
    if validar_ce(c.get('certo_errado'), exige) is None: return 'pronta'
    base = {'questao': {k: q.get(k) for k in ('stem', 'options', 'correct')},
            'comentario': {k: c.get(k) for k in ('summary', 'alternatives', 'lessons', 'traps', 'mindmap', 'laws', 'jurisprudence')}}
    texto = json.dumps(base, ensure_ascii=False)[:60000]
    _MEDIDA.atual = {'chamadas': 0, 'tokens_entrada': 0, 'tokens_saida': 0}; t0 = time.time()
    itens = call_model(CE_SYS, texto, provider, CE_SCHEMA).get('certo_errado')
    err = validar_ce(itens, exige)
    if err:
        itens = call_model(CE_SYS, 'Corrija especificamente: ' + err + '\n' + texto, provider, CE_SCHEMA).get('certo_errado')
        err = validar_ce(itens, exige)
    if err: raise RuntimeError(err)
    q2 = json.loads(path.read_text('utf8'))  # relê: o arquivo pode ter mudado durante a chamada
    c2 = q2.setdefault('commentary', {})
    c2['aula_original'] = {k: c2.pop(k) for k in ('lessons', 'traps', 'mindmap', 'mindmap_titulo') if k in c2}
    c2['certo_errado'] = itens
    q2['metricas_conversao'] = dict(_MEDIDA.atual, duracao_s=round(time.time() - t0, 1), provider=provider,
                                    convertida_em=time.strftime('%d/%m/%Y %H:%M'))
    tmp = path.with_suffix('.tmp'); tmp.write_text(json.dumps(q2, ensure_ascii=False, indent=2), encoding='utf8'); os.replace(tmp, path)
    return 'pronta'


def _job_conversao(path, provider):
    try: CONVERSOES[str(path)] = converter_ce(path, provider)
    except Exception as exc: CONVERSOES[str(path)] = 'erro: ' + str(exc)[:300]


def pedir_conversoes(provider: str) -> dict:
    """Enfileira a conversão de toda questão do cache que ainda não tem Certo/Errado."""
    novas = 0
    for f in sorted(CACHE.glob('*_R*.json')):
        try: c = json.loads(f.read_text('utf8')).get('commentary') or {}
        except Exception: continue
        if validar_ce(c.get('certo_errado'), tem_fonte(c)) is None: CONVERSOES[str(f)] = 'pronta'; continue
        if CONVERSOES.get(str(f)) == 'na_fila': continue
        CONVERSOES[str(f)] = 'na_fila'; novas += 1
        WORKERS.submit(_job_conversao, f, provider)
    return estado_conversoes(novas)


def estado_conversoes(novas: int = 0) -> dict:
    est = Counter('erro' if v.startswith('erro') else v for v in CONVERSOES.values())
    erros = {pathlib.Path(k).name: v for k, v in CONVERSOES.items() if v.startswith('erro')}
    return {'novas_na_fila': novas, 'contagem': dict(est), 'erros': erros}


def jobkey(i, r): return f'{i}|{r}'


def submit(i, r, provider, gaps=None, modo='obj'):
    key = jobkey(i, r)
    if stored(key): return 'ready'
    if i not in BY_ID: return 'invalid'
    if not has_key(provider): return 'no_api'
    with TASK_LOCK:
        f = TASKS.get(key)
        if f and not f.done(): return 'generating'
        if f and f.done() and f.exception(): TASKS.pop(key, None)
        TASKS[key] = WORKERS.submit(generate, i, r, provider, gaps or [], 'ce' if modo == 'ce' else 'obj')
    return 'generating'


def task_status(key):
    if stored(key): return 'ready', None
    with TASK_LOCK: f = TASKS.get(key)
    if not f: return 'missing', None
    if f.done() and f.exception(): return 'error', str(f.exception())[:1500]
    return 'generating', None


def public_q(q):
    return {k: v for k, v in q.items() if k not in ['correct', 'commentary', 'sources_used']}


# ======================================================================= consulta à base (aba Lei seca & Súmulas)
def base_search(q: str, tipo: str = 'todos', limit: int = 30):
    q = q.strip()
    res = []
    if not q: return res
    if tipo in ('todos', 'lei'):
        sig = resolve_sigla(q); alvos = parse_dispositivo(q)
        if sig and alvos:
            for a in alvos:
                hit = lei_lookup(sig, a)
                if hit:
                    v, ex, lab = hit
                    res.append({'tipo': 'lei', 'id': v['id'], 'titulo': f"{DIPLOMA_NOME.get(v['sigla'], v['sigla'])} — Art. {v['art']}", 'texto': v['texto'], 'trecho': ex if ex != v['texto'] else '',
                                'anotacoes': v.get('anotacoes', '')[:3500], 'fonte': fonte_label(v), 'url': v.get('url', ''), 'score': 99})
    kw = terms(q); sq = squash(q)
    def score(text_terms, text):
        s = len(kw & text_terms)
        if len(sq) >= 6 and sq in squash(text[:4000]): s += 5
        return s
    if tipo in ('todos', 'lei'):
        for k, (rub, txt, _) in LEI_TERMS.items():
            v = LEI[k]; s = score(rub | txt, v.get('rubrica', '') + ' ' + v['texto'])
            if s >= max(1, min(3, len(kw))):
                res.append({'tipo': 'lei', 'id': k, 'titulo': f"{DIPLOMA_NOME.get(v['sigla'], v['sigla'])} — Art. {v['art']}" + (f" ({v['rubrica']})" if v.get('rubrica') else ''),
                            'texto': v['texto'], 'anotacoes': v.get('anotacoes', '')[:3500], 'fonte': fonte_label(v), 'url': v.get('url', ''), 'score': s})
    if tipo in ('todos', 'sumula'):
        for k, v in SUMULAS.items():
            s = score(SUM_TERMS[k], v['texto'])
            if re.fullmatch(r'\d{1,4}', q) and v['numero'] == q: s = 50
            if s >= max(1, min(3, len(kw))) or s == 50:
                res.append({'tipo': 'sumula', 'id': k, 'titulo': ('Súmula Vinculante ' if v['tipo'] == 'SV' else f"Súmula {v['tribunal']} ") + v['numero'], 'texto': v['texto'],
                            'fonte': f"DD Súmulas — p. {v['pagina']} • {v.get('tema', '')}", 'url': sum_url(k), 'score': s})
    if tipo in ('todos', 'tese'):
        for k, v in TESES.items():
            s = score(TESE_TERMS[k], v['texto'])
            if re.fullmatch(r'\d{1,4}', q) and v['tema'] == q: s = 50
            if s >= max(1, min(3, len(kw))) or s == 50:
                res.append({'tipo': 'tese', 'id': k, 'titulo': f"Tema {v['tema']} — Repercussão Geral ({v.get('area', '')})", 'texto': v['texto'],
                            'fonte': f"Teses de RG — p. {v['pagina']}", 'url': f"https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num={v['tema']}", 'score': s})
    if tipo in ('todos', 'juris'):
        for i, v in enumerate(JURIS):
            s = score(JURIS_TERMS[i], v['identificador'] + ' ' + v['texto'])
            if s >= max(1, min(3, len(kw))):
                aocp = sum(p['vezes'] for p in v.get('provas', []) if 'AOCP' in p.get('banca', '').upper())
                res.append({'tipo': 'juris', 'id': 'JUR-' + norm_proc(v['identificador']), 'titulo': f"{v.get('tribunal', '')} {v['identificador']} — cobrado {v.get('incidencias', 0)}x ({aocp}x AOCP)",
                            'texto': v['texto'], 'fonte': f"LD DELEGADO AOCP JURIS — p. {v['pagina']}", 'url': '', 'score': s + 0.1 * v.get('incidencias', 0)})
    res.sort(key=lambda x: -x['score'])
    seen = set(); out = []
    for r in res:
        if r['id'] in seen: continue
        seen.add(r['id']); out.append(r)
        if len(out) >= limit: break
    return out


def base_stats():
    fontes = Counter(v.get('fonte') for v in LEI.values())
    return {'artigos': len(LEI), 'artigos_planalto': fontes.get('planalto', 0) + fontes.get('legislabahia', 0),
            'artigos_legislabahia': fontes.get('legislabahia', 0), 'artigos_material': fontes.get('material', 0),
            'diplomas': sorted({v['sigla'] for v in LEI.values()}), 'sumulas': len(SUMULAS), 'teses_rg': len(TESES),
            'precedentes_ld_juris': len(JURIS), 'paginas_doutrina': len(PAGES)}


# ======================================================================= HTTP
ALLOWED_HOSTS = {f'127.0.0.1:{PORT}', f'localhost:{PORT}'}


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=str(ROOT), **k)
    def log_message(self, fmt, *args): print('[trilha]', fmt % args)

    def send_json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(status); self.send_header('Content-Type', 'application/json; charset=utf-8'); self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store'); self.send_header('X-Content-Type-Options', 'nosniff'); self.end_headers(); self.wfile.write(body)

    def local_only(self) -> bool:
        """bloqueia páginas de outros sites (CSRF) e DNS rebinding — protege seus créditos de API"""
        if self.headers.get('Host', '') not in ALLOWED_HOSTS: return False
        origin = self.headers.get('Origin')
        return origin is None or origin in {f'http://{h}' for h in ALLOWED_HOSTS}

    def descartar_corpo(self):
        """Lê (até HIST_MAX) e joga fora o corpo de uma requisição que será recusada."""
        try: size = int(self.headers.get('Content-Length', '0'))
        except ValueError: return
        while 0 < size:
            parte = self.rfile.read(min(size, 65536))
            if not parte: break
            size -= len(parte)
            if size > HIST_MAX: break

    def read_json(self, limite=100000):
        # 31/10/2026: o limite passa a ser por rota (o histórico tem MB) e o tamanho é validado — antes,
        # Content-Length negativo prendia a thread e não numérico derrubava a requisição (revisão, item 8).
        try: size = int(self.headers.get('Content-Length', '0'))
        except ValueError: return {}
        if size < 0 or size > limite: return {}
        try: dado = json.loads(self.rfile.read(size).decode('utf8'))
        except Exception: return {}
        return dado if isinstance(dado, dict) else {}

    def do_GET(self):
        p = urllib.parse.urlparse(self.path); z = urllib.parse.parse_qs(p.query)
        if p.path.startswith('/api/') and not self.local_only(): return self.send_json({'error': 'Origem não permitida'}, 403)
        if p.path == '/api/health':
            return self.send_json({'ok': True, 'version': RELEASE, 'api': {'openai': has_key('openai'), 'claude': has_key('claude')},
                                   'model': {'openai': os.getenv('OPENAI_MODEL', 'gpt-6.1-sol'), 'claude': os.getenv('CLAUDE_MODEL', 'claude-sonnet-4-6')},
                                   'items': len(ITEMS), 'prepared': len(BANK) + len(list(CACHE.glob('*_R*.json'))), 'base': base_stats()})
        if p.path == '/api/question':
            i = (z.get('id') or [''])[0]
            try: r = int((z.get('round') or ['1'])[0] or 1)
            except ValueError: r = 1
            if i not in BY_ID or r not in (1, 2): return self.send_json({'error': 'Item não existe.'}, 404)
            q = stored(jobkey(i, r))
            if q: return self.send_json({'status': 'ready', 'question': public_q(q)})
            st, err = task_status(jobkey(i, r))
            return self.send_json({'status': st, **({'error': err} if err else {})})
        if p.path == '/api/converter_ce':
            return self.send_json(estado_conversoes())
        if p.path == '/api/bloco':
            try: r = int((z.get('round') or ['1'])[0] or 1)
            except ValueError: r = 1
            ids = [i for i in (z.get('ids') or [''])[0].split(',') if i in BY_ID][:BLOCO_MAX]
            est = {i: task_status(jobkey(i, r))[0] for i in ids}
            return self.send_json({'round': r, 'total': len(ids), 'contagem': dict(Counter(est.values())), 'estados': est})
        if p.path == '/api/status':
            i = (z.get('id') or [''])[0]
            try: r = int((z.get('round') or ['1'])[0] or 1)
            except ValueError: r = 1
            st, err = task_status(jobkey(i, r))
            return self.send_json({'status': st, **({'error': err} if err else {})})
        if p.path == '/api/base/busca':
            q = (z.get('q') or [''])[0][:200]; tipo = (z.get('tipo') or ['todos'])[0]
            return self.send_json({'results': base_search(q, tipo if tipo in ('todos', 'lei', 'sumula', 'tese', 'juris') else 'todos')})
        if p.path == '/api/base/stats':
            return self.send_json(base_stats())
        if p.path in ('/', '/index.html'):
            return super().do_GET()
        return self.send_json({'error': 'Recurso não público'}, 403)

    def do_POST(self):
        p = urllib.parse.urlparse(self.path).path
        if p not in ['/api/prefetch', '/api/generate', '/api/reveal', '/api/bloco', '/api/historico', '/api/converter_ce']:
            self.descartar_corpo(); return self.send_json({'error': 'Endpoint inexistente'}, 404)
        if not self.local_only():
            # 31/10/2026: recusar SEM ler o corpo fazia o Windows derrubar a conexão (ConnectionReset) antes
            # de a recusa chegar — intermitente, medido no testar_servidor.py. Lê e descarta antes de responder.
            self.descartar_corpo(); return self.send_json({'error': 'Origem não permitida'}, 403)
        if p == '/api/converter_ce':
            # D-008: converte para Certo/Errado as questões já geradas (1 chamada ao modelo por questão).
            provider = str(self.read_json().get('provider', 'openai'))
            if provider not in ('openai', 'claude'): return self.send_json({'error': 'Provedor inválido'}, 400)
            if not has_key(provider): return self.send_json({'error': 'API não configurada no .env'}, 400)
            return self.send_json(pedir_conversoes(provider))
        if p == '/api/historico':
            # D-006: um único arquivo, regravado a cada bloco SEMPRE com tudo (a tela manda o histórico inteiro).
            html_txt = self.read_json(limite=HIST_MAX).get('html')
            if not isinstance(html_txt, str) or not html_txt.lower().startswith('<!doctype html>'):
                return self.send_json({'error': 'Histórico inválido ou grande demais'}, 400)
            HIST.mkdir(exist_ok=True); alvo = HIST / 'Trilha_historico_acumulado.html'; tmp = alvo.with_suffix('.tmp')
            tmp.write_text(html_txt, encoding='utf8'); os.replace(tmp, alvo)
            return self.send_json({'ok': True, 'bytes': len(html_txt.encode('utf8')), 'arquivo': alvo.relative_to(ROOT).as_posix()})
        if p == '/api/bloco':
            # Blocos de 30 (D-005 a D-007): a tela escolhe os pontos (ela sabe o que foi respondido) e o servidor
            # enfileira a geração de todos; os 2 geradores do WORKERS trabalham a fila.
            req = self.read_json(); ids = req.get('ids'); provider = str(req.get('provider', 'openai'))
            try: r = int(req.get('round', 1))
            except (TypeError, ValueError): r = 1
            gaps = req.get('gaps') if isinstance(req.get('gaps'), dict) else {}
            modos = req.get('modos') if isinstance(req.get('modos'), dict) else {}  # {id: 'obj' | 'ce'} (01/11/2026)
            if not isinstance(ids, list) or not ids or len(ids) > BLOCO_MAX or r not in (1, 2):
                return self.send_json({'error': f'Bloco inválido (1 a {BLOCO_MAX} ids, rodada 1 ou 2)'}, 400)
            if provider not in ('openai', 'claude'): return self.send_json({'error': 'Provedor inválido'}, 400)
            validos = [i for i in dict.fromkeys(ids) if isinstance(i, str) and i in BY_ID]
            estados = {i: submit(i, r, provider, gaps.get(i) if isinstance(gaps.get(i), list) else [], modos.get(i)) for i in validos}
            return self.send_json({'round': r, 'pedidos': len(validos), 'ignorados': len(ids) - len(validos), 'estados': estados})
        req = self.read_json(); i = str(req.get('id', '')); r = req.get('round', 1)
        try: r = int(r)
        except Exception: r = 1
        if i not in BY_ID or r not in (1, 2): return self.send_json({'error': 'ID/rodada inválidos'}, 400)
        key = jobkey(i, r)
        if p == '/api/reveal':
            q = stored(key)
            if not q: return self.send_json({'error': 'Questão ainda não preparada'}, 404)
            if q.get('formato') == 'revisao_ce':  # revisão C/E: o aluno julga item a item na tela; não há letra
                return self.send_json({'correct': '', 'formato': 'revisao_ce', 'commentary': enrich_commentary(q.get('commentary', {}), BY_ID[i]),
                                       'sources_used': q.get('sources_used', [])})
            choice = str(req.get('choice', '')).upper()
            if choice not in list('ABCDE'): return self.send_json({'error': 'Selecione uma alternativa'}, 400)
            # questões antigas do cache também ganham o texto da base local, sem regerar
            return self.send_json({'correct': q['correct'], 'is_correct': choice == q['correct'], 'commentary': enrich_commentary(q.get('commentary', {}), BY_ID[i]),
                                   'sources_used': q.get('sources_used', [])})
        provider = str(req.get('provider', 'openai'))
        if provider not in ('openai', 'claude'): return self.send_json({'error': 'Provedor inválido'}, 400)
        status = submit(i, r, provider, req.get('gaps', []) if isinstance(req.get('gaps'), list) else [], req.get('modo'))
        self.send_json({'status': status, 'id': i, 'round': r})


if __name__ == '__main__':
    print('\nTRILHA AOCP — Delegado Bahia | V7 Base dos Drives')
    print(f'Abra: http://127.0.0.1:{PORT}/')
    print('OpenAI:', 'configurada' if has_key('openai') else 'não configurada', '| Claude:', 'configurada' if has_key('claude') else 'não configurada')
    st = base_stats()
    print(f"Base local: {st['artigos']} artigos ({st['artigos_planalto']} oficiais do Planalto, {st['artigos_material']} do material), "
          f"{st['sumulas']} súmulas, {st['teses_rg']} teses de RG, {st['precedentes_ld_juris']} precedentes do LD JURIS, {st['paginas_doutrina']} páginas de doutrina")
    if not st['artigos_planalto']:
        print('Dica: rode atualizar_lei_seca.bat para baixar a redação oficial do Planalto (sem os grifos do material).')
    print('As chaves são mantidas no servidor local. Ctrl+C para encerrar.')
    print('Versão do servidor:', RELEASE, '\n')
    try:
        server = http.server.ThreadingHTTPServer(('127.0.0.1', PORT), Handler)
    except OSError as exc:
        print('\nERRO: não foi possível iniciar na porta', PORT)
        print('Provavelmente a versão ANTIGA do servidor ainda está aberta. Feche TODAS as janelas pretas da Trilha AOCP e tente novamente.')
        print('Detalhe técnico:', exc)
        sys.exit(2)
    threading.Timer(1.0, lambda: webbrowser.open(f'http://127.0.0.1:{PORT}/')).start()
    server.serve_forever()
