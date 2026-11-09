#!/usr/bin/env python3
"""Constrói a base local da Trilha AOCP a partir dos PDFs dos Drives.

Uso (requer o utilitário pdftotext / poppler):
    python ferramentas/construir_base.py PASTA_COM_PDFS assets/

Gera:
    assets/lei_seca_material.json   artigos por diploma (texto + anotações do material)
    assets/sumulas.json             súmulas STF/STJ/SV (texto do material DD Súmulas)
    assets/teses_rg.json            teses de repercussão geral (STF)
    assets/juris_aocp.json          precedentes do LD JURIS com incidência em provas AOCP
    assets/fontes_paginas.json      páginas de doutrina/atualização para recuperação (RAG)
"""
from __future__ import annotations
import json, pathlib, re, subprocess, sys, unicodedata

# ---------------------------------------------------------------- catálogo
LEIS = {
    'LEI_CP.pdf':     ('CP',   'Código Penal — Decreto-Lei 2.848/1940', 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm'),
    'LEI_CPP.pdf':    ('CPP',  'Código de Processo Penal — Decreto-Lei 3.689/1941', 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm'),
    'LEI_CF.pdf':     ('CF',   'Constituição Federal de 1988', 'https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm'),
    'LEI_12830.pdf':  ('L12830', 'Lei 12.830/2013 — Investigação criminal conduzida por Delegado', 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12830.htm'),
    'LEI_LINDB.pdf':  ('LINDB', 'LINDB — Decreto-Lei 4.657/1942', 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del4657compilado.htm'),
    'LEI_CADH.pdf':   ('CADH', 'Convenção Americana de Direitos Humanos — Decreto 678/1992', 'https://www.planalto.gov.br/ccivil_03/decreto/d0678.htm'),
    'LEI_6938.pdf':   ('L6938', 'Lei 6.938/1981 — Política Nacional do Meio Ambiente', 'https://www.planalto.gov.br/ccivil_03/leis/l6938.htm'),
    'LEI_DEC6514.pdf':('D6514', 'Decreto 6.514/2008 — Infrações e sanções administrativas ambientais', 'https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/decreto/d6514.htm'),
    'LEI_9868.pdf':   ('L9868', 'Lei 9.868/1999 — ADI e ADC', 'https://www.planalto.gov.br/ccivil_03/leis/l9868.htm'),
    'LEI_9882.pdf':   ('L9882', 'Lei 9.882/1999 — ADPF', 'https://www.planalto.gov.br/ccivil_03/leis/l9882.htm'),
    'LEI_12063.pdf':  ('L12063', 'Lei 12.063/2009 — ADO', 'https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/lei/l12063.htm'),
}
# arquivo -> (rótulo exibido, disciplinas, posterior ao edital?)
DOUTRINA = {
    'LD_DELEGADO_AOCP.pdf': ('LD DELEGADO AOCP.pdf', '*', False),
    'LD_DELEGADO_AOCP_JURIS.pdf': ('LD DELEGADO AOCP JURIS.pdf', '*', False),
    'ATUALIZACOES_2026_1.pdf': ('Atualizações Legislativas e Jurisprudenciais - 2026.1-1.pdf', '*', False),
    'POSTERIOR_LPE_Lei_15487_06ago2026.pdf': ('Atualização - LPE - Lei 15.487 - 06 Ago 2026-1.pdf', 'LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE', True),
    'ESC_JURIS_TRAFICO_DROGAS.pdf': ('ESCLARECIMENTO - JURIS - TRÁFICO DE DROGAS.pdf', 'LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE', False),
    'ESC_DIREITOS_FUNDAMENTAIS_EC.pdf': ('ESCLARECIMENTO DIREITOS FUNDAMENTAIS INSERIDOS POR EC.pdf', 'DIREITO CONSTITUCIONAL', False),
    'ESC_CRIMES_PERIGO.pdf': ('Crimes de Perigosidade Real & Crimes de Potencial Perigo.pdf', 'DIREITO PENAL', False),
    'ESC_PROVAS_WHATSAPP.pdf': ('esclarecimento Provas Obtidas Do Whatsapp.pdf', 'DIREITO PROCESSUAL PENAL', False),
    'ESC_MARIA_PENHA_ART16.pdf': ('designaçao audiência especial prevista no art. 16 da Lei Maria da Penha.pdf', 'LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE', False),
    'ESC_PROC_PENAL_PRINCIPIOS.pdf': ('ESCLARECIMENTO - PROCESSO PENAL NOÇÕES INICIAIS E PRINCÍPIOS.pdf', 'DIREITO PROCESSUAL PENAL', False),
    'ESC_JURIS_MEDIDA_PROTETIVA.pdf': ('ESCLARECIMENTO - JURIS - CONSENTIMENTO DE APROXIMAÇÃO E DESCUMPRIMENTO DE MED PROTETIVA.pdf', 'LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE', False),
    'AULA_PE_DIR_PENAL_CRIMINOLOGIA.pdf': ('Aula Delta PE 01 - Direito Penal e Criminologia.pdf', 'DIREITO PENAL|CRIMINOLOGIA', False),
    'AULA_PE_PROC_PENAL_PRINCIPIOS.pdf': ('Aula Delta PE 02 - Proc. Penal: noções iniciais e princípios.pdf', 'DIREITO PROCESSUAL PENAL', False),
    'AULA_PE_DIR_HUMANOS.pdf': ('Aula Delta PE 03 - Direitos Humanos.pdf', 'DIREITO CONSTITUCIONAL|PROMOÇÃO DA IGUALDADE RACIAL E DE GÊNERO', False),
    'AULA_PE_CONST_TRATADOS.pdf': ('Aula Delta PE 04 - Const.: tratados e convenções.pdf', 'DIREITO CONSTITUCIONAL', False),
    'AULA_PE_DIR_ADM_PRINCIPIOS.pdf': ('Aula Delta PE 05 - Dir. Adm.: noções iniciais e princípios.pdf', 'DIREITO ADMINISTRATIVO', False),
    'AULA_PE_DIR_AMBIENTAL_CF.pdf': ('Aula Delta PE 06 - Dir. Ambiental: CF e meio ambiente.pdf', 'DIREITO AMBIENTAL', False),
}
SUMULAS = ['SUM_01_ADMINISTRATIVO.pdf', 'SUM_02_CONSTITUCIONAL.pdf', 'SUM_03_PENAL.pdf', 'SUM_04_PROCESSO_PENAL.pdf',
           'SUM_05_CIVIL.pdf', 'SUM_06_AMBIENTAL.pdf', 'SUM_07_TRIBUTARIO.pdf']
SUM_DISC = {'01': 'DIREITO ADMINISTRATIVO', '02': 'DIREITO CONSTITUCIONAL', '03': 'DIREITO PENAL', '04': 'DIREITO PROCESSUAL PENAL',
            '05': 'DIREITO CIVIL E EMPRESARIAL', '06': 'DIREITO AMBIENTAL', '07': 'DIREITO TRIBUTÁRIO'}

# ---------------------------------------------------------------- utilidades
WATERMARK = re.compile(r'^.*\b\d{11}\b.*$|^.*\d{3}\.\d{3}\.\d{3}-\d{2}.*$')
def pages_of(pdf: pathlib.Path) -> list[str]:
    out = subprocess.run(['pdftotext', '-enc', 'UTF-8', str(pdf), '-'], capture_output=True, check=True).stdout.decode('utf8', 'replace')
    return out.split('\f')

def clean_lines(page: str, drop: set[str]) -> list[str]:
    res = []
    for ln in page.splitlines():
        s = ln.strip()
        if not s: res.append(''); continue
        if WATERMARK.match(s): continue                 # marca d'água com CPF do licenciado
        if s in drop or re.fullmatch(r'\d{1,3}', s): continue
        res.append(s)
    return res

def norm(s: str) -> str:
    return unicodedata.normalize('NFKD', s.casefold()).encode('ascii', 'ignore').decode()

# ---------------------------------------------------------------- lei seca
ART_RE = re.compile(r'^Art\.\s*(\d{1,4}(?:\.\d{3})?)\s*(?:º|°|o\b)?\s*(?:-\s*([A-Z]{1,2})\b)?\s*(?:[\.\-–:]\s*|\s+)(.*)$')
LAW_START = re.compile(r'^(§\s*\d+|Parágrafo\s+único|[IVXLC]{1,7}\s*[-–]|[a-z]\)\s|Pena\s*[-–:]|Pena\b)')
NOTE_START = re.compile(r'^(•|↳|⚠|\*|➢|→|⇾|►|✓|Obs|OBS|Ex\.|EX\.|Exemplo|STJ\b|STF\b|Súmula|Sumula|Info\b|Enunciado|Tema\b|Jurisprud|Atenção|ATENÇÃO|Cuidado|CUIDADO|Não confundir|Doutrina|Lembre|Dica|Vide|\()')
REF_INSIDE = re.compile(r'^Art\.\s*\d+[^.]{0,25},\s*(?:§|CP|CF|CPP|da\b|do\b|inc|I\b)')

def tidy_law(s: str) -> tuple[str, bool]:
    """remove notas inline do material: [comentário] e '; – comentário'"""
    s2 = re.sub(r'\s*\[[^\]]{1,220}\]', '', s)
    s3 = re.sub(r'([;:.,])\s+[–—]\s+.*$', r'\1', s2)
    s3 = re.sub(r'\s+(?:↳|•|⚠|➢|⇾|→).*$', '', s3)
    s3 = re.sub(r'([.;:])\s*\((?!Revogad|Vetad|VETAD|REVOGAD|Inclu|Reda|Vide|Vig)[^)]{1,90}\)(?:\s+\S.*)?$', r'\1', s3)
    return s3.strip(), (s3 != s2)

def art_key(num: str, suf: str | None) -> tuple[int, str]:
    return (int(num.replace('.', '')), suf or '')

ROMAN = {'I':1,'V':5,'X':10,'L':50,'C':100}
def roman(s: str) -> int:
    t = 0; prev = 0
    for ch in reversed(s):
        v = ROMAN.get(ch, 0)
        t = t - v if v < prev else t + v; prev = max(prev, v)
    return t

def lis_indices(keys: list) -> list:
    """maior subsequência não decrescente (com salto máximo) — elimina remissões a artigos dentro das anotações"""
    import bisect
    n = len(keys)
    if not n: return []
    best = [1] * n; prv = [-1] * n
    for i in range(n):
        for j in range(max(0, i - 400), i):
            if keys[j] <= keys[i] and keys[i][0] - keys[j][0] <= 30 and best[j] + 1 > best[i] and keys[j] != keys[i]:
                best[i] = best[j] + 1; prv[i] = j
    i = max(range(n), key=lambda x: best[x]); out = []
    while i != -1: out.append(i); i = prv[i]
    return out[::-1]

def roman_seq_ahead(lines, a, b, want):
    for k in range(a, b):
        mi = re.match(r'^([IVXLC]{1,7})\s*[-–]', lines[k][1])
        if mi and roman(mi.group(1)) == want: return True
    return False

DISPLAY = {'LEI_CP.pdf': 'Código Penal (CP).pdf', 'LEI_CPP.pdf': 'Código de Processo Penal (CPP).pdf', 'LEI_CF.pdf': 'Constituição Federal.pdf',
           'LEI_12830.pdf': 'Lei nº 12.830 de 2013.pdf', 'LEI_LINDB.pdf': 'LINDB.pdf', 'LEI_CADH.pdf': 'Dec. nº 678 de 1992 - CADH.pdf',
           'LEI_6938.pdf': 'Lei nº 6.938 de 1981.pdf', 'LEI_DEC6514.pdf': 'Dec. nº 6.514 de 2008.pdf', 'LEI_9868.pdf': 'Lei nº 9.868 de 1999 - ADI e ADC.pdf',
           'LEI_9882.pdf': 'Lei nº 9.882 de 1999 - ADPF.pdf', 'LEI_12063.pdf': 'Lei nº 12.063 de 2009 - ADO.pdf'}

def parse_lei(pdf: pathlib.Path, sigla: str, diploma: str, url: str) -> dict:
    pages = pages_of(pdf)
    drop = {'DD LEGIS – CARREIRAS POLICIAIS', 'DD LEGIS', 'CARREIRAS POLICIAIS'}
    from collections import Counter
    tops = Counter()
    for pg in pages:
        tops.update(set([l.strip() for l in pg.splitlines() if l.strip()][:4]))
    drop |= {l for l, c in tops.items() if c > len(pages) * 0.4 and not ART_RE.match(l)}
    lines = []  # (página, texto)
    for pno, pg in enumerate(pages, 1):
        for s in clean_lines(pg, drop):
            if s: lines.append((pno, s))
    cands = []
    for idx, (pno, s) in enumerate(lines):
        m = ART_RE.match(s)
        if not m or REF_INSIDE.match(s) or 'c/c' in s[:30]: continue
        rest = m.group(3).strip()
        if len(rest) < 3: continue                      # célula de tabela ("Art. 5º.")
        if not re.match(r'^Art\.\s*\d+[\.\d]*\s*(?:º|°|o\b)?\s*(?:-\s*[A-Z]{1,2}\b)?\s*[\.\-–:]', s): continue
        cands.append((idx, art_key(m.group(1), m.group(2))))
    keep = [cands[i] for i in lis_indices([k for _, k in cands])]
    arts: dict[str, dict] = {}
    bounds = [i for i, _ in keep] + [len(lines)]
    for n, (idx, k) in enumerate(keep):
        art = str(k[0]) + (('-' + k[1]) if k[1] else '')
        # rubrica: linha curta imediatamente anterior
        rub = ''
        if idx > 0:
            ps = lines[idx - 1][1]
            if (len(ps) < 70 and not ps.endswith(('.', ';', ':', ',', ')')) and not NOTE_START.match(ps) and ps[:1].isupper()
                    and len(re.findall(r'\d', ps)) <= 2 and not re.search(r'DIVULG|PUBLIC|julgad|Rel\.|Min\.|Info', ps)): rub = ps
        law = []; notes = []; mode = 'law'; seen_par = set(); pena = False; last_inc = 0; last_par = 0; last_ali = 96; stripped_prev = False
        first, _ = tidy_law(lines[idx][1]); law.append(first)
        mode = 'law_end' if first.endswith(('.', ';', ':')) else 'law'
        for j in range(idx + 1, bounds[n + 1]):
            s = lines[j][1]
            ls = LAW_START.match(s) and not NOTE_START.match(s)
            if ls:
                ok = True
                if last_inc and re.match(r'^(§|Parágrafo|Pena|[a-z]\))', s):
                    # o rol de incisos continua adiante? então isto é citação dentro de anotação
                    nxt = roman_seq_ahead(lines, j + 1, min(bounds[n + 1], j + 120), last_inc + 1)
                    if nxt: ok = False
                    if not ok:
                        mode = 'note'; notes.append(s); continue
                mi = re.match(r'^([IVXLC]{1,7})\s*[-–]', s)
                mp = re.match(r'^§\s*(\d+)\s*(?:º|°|o)?\s*(-\s*[A-Z])?', s)
                ma = re.match(r'^([a-z])\)', s)
                if mi:
                    v = roman(mi.group(1))
                    ok = (v == 1 and law[-1].rstrip().endswith(':')) or v == last_inc + 1
                    if ok: last_inc = v
                elif mp:
                    v = int(mp.group(1)); lab = mp.group(1) + (mp.group(2) or '').replace(' ', '')
                    ok = v >= last_par and v <= last_par + 3 and lab not in seen_par
                    if ok: last_par = v; last_inc = 0; last_ali = 96; seen_par.add(lab); pena = False
                elif ma:
                    v = ord(ma.group(1)); ok = (v == 97 and law[-1].rstrip().endswith(':')) or v == last_ali + 1
                    if ok: last_ali = v
                elif s.startswith('Parágrafo'):
                    ok = 'PU' not in seen_par; seen_par.add('PU'); last_inc = 0; pena = False
                elif s.startswith('Pena'):
                    ok = not pena and law[-1].rstrip().endswith(':'); pena = pena or ok
                if ok:
                    t, stripped_prev = tidy_law(s); law.append(t)
                    mode = 'law_end' if t.endswith(('.', ';', ':')) else 'law'; continue
            if mode == 'law' and not NOTE_START.match(s):
                if stripped_prev and s.startswith('('): continue
                t, stripped_prev = tidy_law(s); law[-1] += ' ' + t
                mode = 'law_end' if t.endswith(('.', ';', ':')) else 'law'; continue
            mode = 'note'; stripped_prev = False; notes.append(s)
        txt = '\n'.join(law).strip()
        key = f'{sigla}:{art}'
        if key in arts and len(arts[key]['texto']) >= len(txt): continue
        arts[key] = {'id': key, 'sigla': sigla, 'art': art, 'diploma': diploma, 'rubrica': rub, 'pagina': lines[idx][0],
                     'arquivo': 'DD LEGIS — ' + DISPLAY.get(pdf.name, pdf.name), 'url': url, 'texto': txt, 'anotacoes': '\n'.join(notes)[:6000]}
    return arts

# ---------------------------------------------------------------- súmulas
SUM_RE = re.compile(r'^Súmula\s+(vinculante\s+)?(?:n[ºo°]\s*)?(\d{1,4})\s*(?:[-–]\s*)?(?:\(?\s*(STF|STJ|TSE|TST)\s*\)?)?\s*[-–:]+\s*(.*)$', re.I)
def parse_sumulas(raw: pathlib.Path) -> dict:
    out = {}
    for fn in SUMULAS:
        disc = SUM_DISC[fn[4:6]]
        pages = pages_of(raw / fn)
        cur = None; tema = ''
        def close():
            if cur:
                txt = ' '.join(cur.pop('_t')).strip()
                txt = re.sub(r'\s+', ' ', txt)
                cur['texto'] = txt
                cur['id'] = cur['tipo'] + '-' + cur['numero']
                out.setdefault(cur['id'], cur)
        for pno, pg in enumerate(pages, 1):
            lines = [l.strip() for l in pg.splitlines()]
            for i, s in enumerate(lines):
                if not s or WATERMARK.match(s) or s.startswith('Esse é o primeiro bloco'):
                    if cur and cur['_t'] and not s: cur['_closed_para'] = True
                    continue
                m = SUM_RE.match(s)
                if m:
                    close()
                    trib = (m.group(3) or 'STF').upper()
                    tipo = 'SV' if m.group(1) else ('SUM-' + trib)
                    cur = {'tipo': tipo, 'tribunal': 'STF' if tipo == 'SV' else trib, 'numero': m.group(2), 'tema': tema,
                           'disciplina': disc, 'arquivo': fn, 'pagina': pno, '_t': [m.group(4)]}
                    continue
                if cur is None:
                    if len(s) < 80: tema = s
                    continue
                if s.startswith(('•', '↳', '⚠', '*', 'Obs', 'OBS', '➢')):
                    close(); cur = None; continue
                if cur.get('_closed_para') or (len(s) < 70 and not s.endswith(('.', ';', ',', ')', ':')) and cur['_t'][-1].rstrip().endswith(('.', ')'))):
                    close(); cur = None; tema = s if len(s) < 80 else tema; continue
                cur['_t'].append(s)
        close()
    return out

# ---------------------------------------------------------------- teses RG
def parse_teses(pdf: pathlib.Path) -> dict:
    text = '\n'.join(l for l in pages_of(pdf) for l in [l] )
    full = []
    area = ''; ano = ''
    for pno, pg in enumerate(pages_of(pdf), 1):
        for s in pg.splitlines():
            s = s.strip()
            if not s or s == 'TESES DE REPERCUSSÃO GERAL' or re.fullmatch(r'\d{1,3}', s) or '.....' in s: continue
            full.append((pno, s))
    out = {}; cur = None
    for pno, s in full:
        m = re.match(r'^TESES DE REPERCUSSÃO GERAL DO ANO DE (\d{4})', s)
        if m: ano = m.group(1); continue
        m = re.match(r'^Tese fixada no tema (\d+)\s*:\s*(.*)$', s, re.I)
        if m:
            if cur: out.setdefault(cur['id'], cur)
            cur = {'id': 'RG-' + m.group(1), 'tema': m.group(1), 'area': area, 'ano': ano, 'pagina': pno, 'arquivo': pdf.name, 'texto': m.group(2)}
            continue
        if len(s) < 70 and re.match(r'^Direito|^DIREITO', s) and not s.endswith(('.', ',', ';')):
            if cur: out.setdefault(cur['id'], cur); cur = None
            area = s; continue
        if cur: cur['texto'] += ' ' + s
    if cur: out.setdefault(cur['id'], cur)
    for v in out.values():
        v['texto'] = re.sub(r'\s+', ' ', v['texto']).strip()
        m = re.search(r'\((?:Leading Case:\s*)?((?:RE|ARE|ADI|ADPF)\s*[\d\.]+(?:/[A-Z]{2})?)\)\s*”?\s*$', v['texto'])
        v['leading_case'] = m.group(1) if m else ''
    return out

# ---------------------------------------------------------------- LD JURIS (incidência AOCP)
PREC_RE = re.compile(r'^((?:AgRg no |AgInt no |EDcl no |EDcl nos )?(?:RE|REsp|HC|RHC|ARE|AREsp|EREsp|ADI|ADPF|ADC|ADO|Rcl|MS|RMS|Inq|AP|CC|Pet|RvCr|ExtrA?|MI)\s*[\d\.]+(?:\s*/\s*[A-Z]{2})?(?:\s*-\s*[A-Z]{2})?)\s*$')
def parse_juris_aocp(pdf: pathlib.Path) -> list:
    out = []; cur = None; secao = []
    for pno, pg in enumerate(pages_of(pdf), 1):
        for s in pg.splitlines():
            s = s.strip()
            if not s or WATERMARK.match(s) or re.fullmatch(r'\d{1,3}', s): continue
            m = PREC_RE.match(s)
            if m:
                if cur: out.append(cur)
                cur = {'identificador': m.group(1), 'secao': ' > '.join(secao[-3:]), 'pagina': pno, 'arquivo': 'LD DELEGADO AOCP JURIS.pdf',
                       'texto': '', 'incidencias': 0, 'provas': []}
                continue
            if s.isupper() and len(s) < 80 and not cur:
                secao.append(s); continue
            if cur is None: continue
            m = re.match(r'^Total de Incid[êe]ncias:\s*(\d+)', s)
            if m: cur['incidencias'] = int(m.group(1)); continue
            m = re.match(r'^\((\d+)x\)\s*Institui[çc][ãa]o:\s*(.*?)\s*Banca:\s*(.*?)\s*Ano:\s*(\d{4})', s)
            if m: cur['provas'].append({'vezes': int(m.group(1)), 'instituicao': m.group(2), 'banca': m.group(3), 'ano': m.group(4)}); continue
            if s in ('DELEGADO DE POLÍCIA',): continue
            if s.isupper() and len(s) < 80 and (cur['incidencias'] or cur['provas']):
                out.append(cur); cur = None; secao.append(s); continue
            cur['texto'] += ('\n' if re.match(r'^\d+\.\s', s) else ' ') + s
    if cur: out.append(cur)
    for c in out:
        c['texto'] = c['texto'].strip()
        t = c['texto']
        c['tribunal'] = 'STF' if re.search(r'\bSTF\b|Tribunal Pleno|Primeira Turma, julgado|Segunda Turma, julgado', t[-400:]) and not re.search(r'\bSTJ\b', t[-400:]) else ('STJ' if 'STJ' in t[-400:] or c['identificador'].startswith(('REsp', 'AREsp', 'EREsp', 'RHC', 'AgRg', 'AgInt')) else '')
    return out

# ---------------------------------------------------------------- páginas de doutrina
def build_pages(raw: pathlib.Path, old: list) -> list:
    rows = []
    for fn, (label, disc, posterior) in DOUTRINA.items():
        for pno, pg in enumerate(pages_of(raw / fn), 1):
            ls = [l.strip() for l in pg.splitlines() if l.strip() and not WATERMARK.match(l.strip()) and not re.fullmatch(r'\d{1,3}', l.strip())]
            txt = re.sub(r'[ \t]+', ' ', '\n'.join(ls)).strip()
            if len(txt) < 120: continue
            rows.append({'file': label, 'page': pno, 'text': txt, 'posterior': posterior, 'disciplinas': disc})
    have = {r['file'] for r in rows}
    for r in old:  # preserva fontes que não estão nos Drives (AOCP INFO, RAC LOG...)
        if r['file'] not in have:
            r = dict(r); r.setdefault('disciplinas', '*')
            if r['file'].startswith('AOCP INFO'): r['disciplinas'] = 'INFORMÁTICA'
            if 'RAC LOG' in r['file']: r['disciplinas'] = 'RACIOCÍNIO LÓGICO'
            r['text'] = '\n'.join(l for l in r['text'].splitlines() if not WATERMARK.match(l.strip()))
            rows.append(r)
    return rows

def main():
    raw = pathlib.Path(sys.argv[1]); dst = pathlib.Path(sys.argv[2])
    lei = {}
    stats = {}
    for fn, (sig, dip, url) in LEIS.items():
        a = parse_lei(raw / fn, sig, dip, url); lei.update(a); stats[sig] = len(a)
    print('artigos:', stats, 'total', len(lei))
    (dst / 'lei_seca_material.json').write_text(json.dumps(lei, ensure_ascii=False), 'utf8')
    s = parse_sumulas(raw); print('súmulas:', len(s))
    (dst / 'sumulas.json').write_text(json.dumps(s, ensure_ascii=False, indent=0), 'utf8')
    # a extração diverge do oficial em casos conferidos: reaplica as correções registradas (07/11/2026)
    if (dst / 'sumulas.json').resolve() == (pathlib.Path(__file__).resolve().parent.parent / 'assets' / 'sumulas.json'):
        import subprocess
        subprocess.run([sys.executable, str(pathlib.Path(__file__).with_name('corrigir_sumulas.py'))], check=False)
    else:
        print('súmulas: gravadas fora de assets/ — rode ferramentas/corrigir_sumulas.py sobre a base oficial')
    t = parse_teses(raw / 'TESES_RG_STF.pdf'); print('teses RG:', len(t))
    (dst / 'teses_rg.json').write_text(json.dumps(t, ensure_ascii=False, indent=0), 'utf8')
    j = parse_juris_aocp(raw / 'LD_DELEGADO_AOCP_JURIS.pdf'); print('precedentes LD JURIS:', len(j))
    (dst / 'juris_aocp.json').write_text(json.dumps(j, ensure_ascii=False, indent=0), 'utf8')
    oldf = dst / 'fontes_paginas.json'
    old = json.loads(oldf.read_text('utf8')) if oldf.exists() else []
    p = build_pages(raw, old); print('páginas de doutrina:', len(p))
    oldf.write_text(json.dumps(p, ensure_ascii=False), 'utf8')

if __name__ == '__main__':
    main()
