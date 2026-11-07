"""Conferidor do Pente Fino: lê discursiva/pente_fino_<disc>.js (--disc CPC, padrão, ou CIV) e PARA (saída 1) se algo não bater.
  1. esquema (docs/PENTE_FINO_ESQUEMA.md): campos, ids únicos, gabarito C/E, pontos do edital na ordem;
  2. todo lei[].texto CONTIDO, letra por letra, em assets/lei_seca_oficial.json[<lei>:<art>];
  3. toda juris com tribunal, fonte e data dd/mm/aaaa;
  4. volume (R1 8–12, R2 6–10 por ponto; a disciplina pode fixar outro em disciplinas.py — MLE: 6–10 e 5–8) e
     equilíbrio (40%–60% de E por rodada).
Disciplina com doutrina_sem_fonte (MLE) admite assertiva sem lei nem juris (só doutrina), e o total delas é informado.
Avisos (não param): artigo citado com redação dupla na base (texto antigo + novo) ou marcado alteracao_2026.
Uso: python conferir.py [--disc CPC|CIV|MLE]   → imprime contagens; saída 0 = tudo certo."""
import argparse, collections, json, pathlib, re, sys

sys.stdout.reconfigure(encoding='utf-8')
RAIZ = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import disciplinas
ap = argparse.ArgumentParser()
ap.add_argument('--disc', default='CPC', choices=sorted(disciplinas.DISC))
DISC = ap.parse_args().disc
CFG = disciplinas.DISC[DISC]
src = (RAIZ / 'discursiva' / f'pente_fino_{DISC.lower()}.js').read_text(encoding='utf-8')
m = re.search(r'window\.PENTE_FINO\.' + DISC + r'\s*=\s*(\{.*\});\s*$', src, re.S)
if not m:
    print(f'ERRO: não achei "window.PENTE_FINO.{DISC} = {{...}};"'); sys.exit(1)
D = json.loads(m.group(1))
OF = json.load(open(RAIZ / 'assets' / 'lei_seca_oficial.json', encoding='utf-8'))
IT = json.load(open(RAIZ / 'assets' / 'items.json', encoding='utf-8'))
IT = IT if isinstance(IT, list) else IT.get('items', [])
edital = sorted([x['id'] for x in IT if str(x.get('id', '')).startswith(CFG['prefixo'])], key=disciplinas.ordem_ponto)

erros, avisos = [], []
DATA = re.compile(r'^\d{2}/\d{2}/\d{4}$')
if not DATA.match(D.get('conferido_em', '')): erros.append('conferido_em fora de dd/mm/aaaa')
if [p['id'] for p in D['pontos']] != edital: erros.append('pontos ≠ edital (ou fora de ordem)')
for k in ['disciplina', 'fontes', 'pontos', 'rodadas']:
    if k not in D: erros.append(f'falta campo {k}')

so_doutrina = 0
ids = set(); leis = collections.Counter(); juris = {}; cont = collections.Counter(); e_cont = collections.Counter()
for r in D['rodadas']:
    for it in r['itens']:
        iid = it.get('id')
        if iid in ids: erros.append(f'id repetido {iid}')
        ids.add(iid)
        for k in ['id', 'ponto', 'tema', 'assertiva', 'gabarito', 'comentario']:
            if not it.get(k): erros.append(f'{iid}: falta {k}')
        if it['gabarito'] not in ('C', 'E'): erros.append(f'{iid}: gabarito {it["gabarito"]!r}')
        if it['ponto'] not in edital: erros.append(f'{iid}: ponto {it["ponto"]} fora do edital')
        c = it['comentario']
        if not c.get('resumo') or '**' not in c['resumo']: erros.append(f'{iid}: resumo sem negrito')
        if not c.get('palavras_chave'): erros.append(f'{iid}: sem palavras_chave')
        if not c.get('lei') and not c.get('juris'):
            if CFG.get('doutrina_sem_fonte'): so_doutrina += 1
            else: erros.append(f'{iid}: sem lei nem juris')
        if 'excecoes' in c and not (isinstance(c['excecoes'], list) and c['excecoes']): erros.append(f'{iid}: excecoes não é lista')
        for l in c.get('lei', []):
            chave = f"{l['lei']}:{l['art']}"
            of = OF.get(chave)
            if of is None: erros.append(f'{iid}: {chave} não existe na lei seca oficial'); continue
            if l['texto'] not in of['texto']: erros.append(f'{iid}: texto NÃO contido em {chave}: {l["texto"][:70]!r}')
            if not l.get('rotulo'): erros.append(f'{iid}: lei sem rótulo')
            leis[chave] += 1
            # Redação superada: a base às vezes guarda o texto antigo seguido do novo com o MESMO marcador
            # (ex.: "§ 6º ..." e logo depois "§ 6º ... (Redação dada pela Lei ...)"). Se o trecho citado está na
            # linha antiga, ERRO; se o artigo foi mexido em 2026, AVISO.
            linhas = of['texto'].split('\n')
            marca = lambda s: (re.match(r'^(§\s*\d+[ºo°.]*(?:-[A-Z])?|[IVXL]+\s*[-–]|Art\.\s*[\d.]+[ºo]?|Parágrafo único)', s) or [None])[0]
            norm = lambda s: re.sub(r'[\s–-]+', '', s or '')
            for i, ln in enumerate(linhas):
                if l['texto'].split('\n')[0] in ln:
                    mk = marca(ln)
                    if mk and any(norm(marca(x)) == norm(mk) and ('Redação dada' in x or 'Incluído' in x)
                                  for x in linhas[i + 1:i + 3]) and 'Redação dada' not in ln:
                        erros.append(f'{iid}: {chave} — trecho citado está em REDAÇÃO SUPERADA ({mk}); usar a linha seguinte')
            if of.get('alteracao_2026') or '2026' in of['texto']:
                avisos.append(f'{iid}: {chave} tem alteração de 2026 na base — conferir se o trecho citado é o vigente')
        for j in c.get('juris', []):
            for k in ['tribunal', 'fonte', 'data', 'texto']:
                if not j.get(k): erros.append(f'{iid}: juris sem {k}')
            if not DATA.match(j.get('data', '')): erros.append(f'{iid}: data de juris {j.get("data")!r}')
            juris[j['fonte']] = (j['tribunal'], j['data'])
        cont[(r['n'], it['ponto'])] += 1
        if it['gabarito'] == 'E': e_cont[r['n']] += 1

(V1a, V1b), (V2a, V2b) = CFG.get('volume', ((8, 12), (6, 10)))
print('Assertivas por ponto (R1 / R2):')
for p in edital:
    a, b = cont[(1, p)], cont[(2, p)]
    print(f'  {p:13s} {a:3d} / {b:3d}')
    if not V1a <= a <= V1b: erros.append(f'{p}: R1 com {a} (esperado {V1a}–{V1b})')
    if not V2a <= b <= V2b: erros.append(f'{p}: R2 com {b} (esperado {V2a}–{V2b})')
for r in D['rodadas']:
    n = len(r['itens']); e = e_cont[r['n']]; pct = 100 * e / n
    print(f'Rodada {r["n"]}: {n} assertivas, {e} E ({pct:.1f}%)'.replace('.', ','))
    if not 40 <= pct <= 60: erros.append(f'Rodada {r["n"]}: {pct:.1f}% de E fora de 40–60%')
print(f'Total: {len(ids)} assertivas · {len(leis)} dispositivos de lei distintos ({sum(leis.values())} citações) · {len(juris)} julgados/súmulas distintos')
por_lei = collections.Counter(k.split(':')[0] for k in leis)
print('Dispositivos por diploma:', dict(por_lei))
if CFG.get('doutrina_sem_fonte'):
    print(f'Assertivas só de doutrina (sem lei nem juris): {so_doutrina}')
if avisos:
    print(f'\n{len(avisos)} AVISO(S):'); print('\n'.join('  ' + a for a in avisos))
if erros:
    print(f'\n{len(erros)} ERRO(S):'); print('\n'.join('  ' + e for e in erros)); sys.exit(1)
print('\nOK — conferência sem erros.')
