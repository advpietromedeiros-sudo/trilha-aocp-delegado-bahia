#!/usr/bin/env python3
"""Gera discursiva/artigos.js: o texto OFICIAL de cada artigo e súmula citados na condução e no estudo das peças.

Pedido do titular (03/11/2026, D-015): na condução de cada peça, ler os artigos "já atualizados".
Fonte: assets/lei_seca_oficial.json (Planalto, baixado por ferramentas/atualizar_lei_seca.py) e assets/sumulas.json.
Se o separador do atualizador perdeu um artigo, extrai direto da página do Planalto (reserva).

Uso:  python ferramentas/gerar_artigos_discursiva.py
Referência nos dados: 'CPP:312' (artigo), 'CPP:312:§2' (parágrafo), 'CF:5:LXI' (inciso), 'CPP:13-B:pu' (parágrafo único);
súmulas: 'SUM-STJ-676', 'SUM-STF-145', 'SV-11'.
"""
from __future__ import annotations
import importlib.util, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DISC = ROOT / 'discursiva'
FONTES = [DISC / 'conducao.js', DISC / 'estudo.js']
LEI = ROOT / 'assets' / 'lei_seca_oficial.json'
SUM = ROOT / 'assets' / 'sumulas.json'
CAT = ROOT / 'assets' / 'catalogo_leis.json'
OUT = DISC / 'artigos.js'

PECAS_JS = [DISC / 'conteudo.js', DISC / 'pecas_complementares.js']
CHIP = re.compile(r'^(CF|CPP|CP|ECA|LEP|CTN|LC\s*(\d+)(?:/\d+)?|Lei\s*([\d.]+)/\d+)\s*,\s*arts?\.\s*(\d+)\s*(?:º|°|o)?\s*(-[A-Z])?')
SIGLA = {'CF': 'CF', 'CP': 'CP', 'CPP': 'CPP', 'ECA': 'L8069', 'LEP': 'L7210', 'CTN': 'L5172'}
REF = re.compile(r"'((?:CF|CP|CPP|LC\d+|L\d{4,5}):\d+(?:-[A-Z])?(?::[^'\s]+)?)'")
JUR = re.compile(r"'((?:SUM-ST[FJ]|SV)-\d+)'")
ROT = {'CF': 'CF', 'CP': 'CP', 'CPP': 'CPP', 'L5172': 'CTN', 'L8069': 'ECA', 'L7210': 'LEP'}
NOTA = r'\((?:Reda[çc][ãa]o dada|Inclu[íi]d[oa]|Revogad[oa]|Vide|Vig[êe]ncia|Acrescid[oa]|Renumerad[oa])[^)]*\)'


def rotulo_lei(sig: str) -> str:
    if sig in ROT: return ROT[sig]
    m = re.match(r'(LC|L)(\d+)$', sig)
    n = f'{int(m.group(2)):,}'.replace(',', '.')
    return ('LC ' if m.group(1) == 'LC' else 'Lei ') + n


def normaliza(txt: str) -> str:
    """Junta as linhas quebradas do Planalto e devolve uma linha por caput, parágrafo, inciso e alínea."""
    t = re.sub(r'\s+', ' ', txt).strip()
    t = re.sub(r'\s(?:TÍTULO|CAPÍTULO|LIVRO|PARTE|SEÇÃO|Seção|Subseção)\s+[IVXLC]+\b.*$', '', t)  # título do capítulo seguinte
    # só quebra depois de fim de frase ou de nota: "nos termos do § 2º-A do art. 121-A" fica na mesma linha
    fim = r'(?<=[.;:)])\s'
    t = re.sub(fim + r'(?=§\s*\d)', '\n', t)
    t = re.sub(fim + r'(?=Parágrafo único)', '\n', t)
    t = re.sub(fim + r'(?=(?:[IVXL]{1,8})\s*[-–]\s)', '\n', t)
    t = re.sub(fim + r'(?=[a-z]\)\s)', '\n', t)
    t = re.sub(fim + r'(?=Pena\s*[-–:])', '\n', t)
    return t


def fragmento(txt: str, frag: str) -> str | None:
    linhas = txt.split('\n')
    if frag == 'pu': alvo = re.compile(r'^Parágrafo único')
    elif frag.startswith('§'): alvo = re.compile(r'^§\s*' + re.escape(frag[1:]) + r'(?:º|°|o)?[\s.-]')
    else: alvo = re.compile(r'^' + re.escape(frag) + r'\s*[-–]\s')
    for i, ln in enumerate(linhas):
        if alvo.match(ln):
            fim = i + 1
            nivel_par = frag == 'pu' or frag.startswith('§')
            while fim < len(linhas):
                prox = linhas[fim]
                if re.match(r'^(§|Parágrafo único)', prox): break
                if not nivel_par and re.match(r'^[IVXL]{1,8}\s*[-–]\s', prox): break
                fim += 1
            corpo = '\n'.join(linhas[i:fim])
            return linhas[0] + '\n(…)\n' + corpo if i > 0 else corpo
    return None


def carrega_atualizador():
    spec = importlib.util.spec_from_file_location('atualizar', ROOT / 'ferramentas' / 'atualizar_lei_seca.py')
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def extrai_direto(mod, url: str, art: str) -> str | None:
    """Reserva: procura 'Art. N' (ou 'N-A.' depois de uma linha 'Art.') na página e corta no próximo artigo."""
    num, _, suf = art.partition('-')
    ls = mod.html_to_lines(mod.fetch(url))
    pad = re.compile(r'^(?:Art\.\s*)?' + num + r'\s*(?:º|°|o)?\s*' + (r'-\s*' + suf + r'\b' if suf else r'(?![\d-])') + r'\s*[.\-–]?')
    for i, s in enumerate(ls):
        if pad.match(s) and (s.startswith('Art') or (i and ls[i - 1].strip() == 'Art.')):
            fim = i + 1
            while fim < len(ls) and not re.match(r'^Art\.\s*\d', ls[fim]) and not (ls[fim] == 'Art.' ): fim += 1
            return ('Art. ' if not s.startswith('Art') else '') + '\n'.join(ls[i:fim])
    return None


def main():
    lei = json.loads(LEI.read_text('utf8')) if LEI.exists() else {}
    sumulas = json.loads(SUM.read_text('utf8'))
    urls = {d['sigla']: d.get('url') for d in json.loads(CAT.read_text('utf8'))['diplomas']}
    texto = '\n'.join(f.read_text('utf8') for f in FONTES if f.exists())
    refs = set(REF.findall(texto)); jurs = sorted(set(JUR.findall(texto)))
    # os artigos citados nos passos de escrita ('CPP, art. 313, I (…)'): mesmo parser de chaveDe() no motor
    for f in PECAS_JS:
        for s in re.findall(r"'((?:[^'\\]|\\.)*)'", f.read_text('utf8')):
            m = CHIP.match(s)
            if m:
                sig = 'LC' + m.group(2) if m.group(2) else 'L' + m.group(3).replace('.', '') if m.group(3) else SIGLA[m.group(1)]
                refs.add(f'{sig}:{m.group(4)}{m.group(5) or ""}')
    refs = sorted(refs)
    arts, faltas, mod, paginas = {}, [], None, {}
    for ref in refs:
        sig, art, *fr = ref.split(':'); frag = fr[0] if fr else None
        base = lei.get(f'{sig}:{art}'); fonte = 'planalto'
        bruto = base['texto'] if base else None
        if not bruto and urls.get(sig):
            try:
                mod = mod or carrega_atualizador()
                bruto = extrai_direto(mod, urls[sig], art); fonte = 'planalto (extração direta)'
            except Exception as exc:  # rede fora: registra a falta
                print('  rede:', sig, art, exc)
        if not bruto:
            faltas.append(ref); arts[ref] = {'d': rotulo_lei(sig), 'u': urls.get(sig) or '', 'falta': 1}; continue
        txt = normaliza(bruto)
        if frag:
            parte = fragmento(txt, frag)
            if parte is None: faltas.append(ref + ' (trecho não achado; vai o artigo inteiro)')
            else: txt = parte
        notas = re.findall(NOTA, bruto)
        arts[ref] = {'d': rotulo_lei(sig), 't': txt, 'u': (base or {}).get('url') or urls.get(sig) or '',
                     'b': (base or {}).get('baixado_em') or '', 'f': fonte,
                     'n26': int(any(re.search(r'de\s*2026|/2026', n) for n in re.findall(NOTA, txt)))}
    juris = {}
    for j in jurs:
        s = sumulas.get(j)
        if not s: faltas.append(j); continue
        t = re.split(r'\s+-\s+(?=[A-ZÁÉÍÓÚ])', s['texto'], 1)[0].strip()  # o acervo anexa notas depois de " - "
        juris[j] = {'t': t, 'tri': s.get('tribunal') or ('STF' if j.startswith('SV') else ''), 'n': s.get('numero') or j.split('-')[-1]}
    cab = ('/* GERADO por ferramentas/gerar_artigos_discursiva.py — não edite à mão (D-015).\n'
           '   Texto oficial do Planalto (lei seca) e das súmulas do STF e do STJ citados em conducao.js e estudo.js. */\n')
    OUT.write_text(cab + 'const ARTIGOS = ' + json.dumps(arts, ensure_ascii=False, indent=0) + ';\n'
                   + 'const JURIS = ' + json.dumps(juris, ensure_ascii=False, indent=0) + ';\n', 'utf8')
    print(f'{len(arts)} referências de lei, {len(juris)} súmulas -> {OUT.relative_to(ROOT)}')
    if faltas:
        print('Sem texto oficial (aparece só o link do Planalto):'); [print('  -', f) for f in faltas]
    return 0


if __name__ == '__main__':
    sys.exit(main())
