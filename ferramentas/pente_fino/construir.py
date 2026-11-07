"""Monta discursiva/pente_fino_cpc.js a partir dos arquivos c*.py (Pente Fino de Processo Civil).
Cada lei é (chave, início, fim|None, rótulo): o texto é RECORTADO do oficial (assets/lei_seca_oficial.json),
do início até o fim do trecho final — nada é digitado à mão. Uso: python construir.py"""
import importlib, json, pathlib, re, sys, collections

AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(AQUI))
sys.stdout.reconfigure(encoding='utf-8')
import base

for m in ['c01_04', 'c05_08', 'c09_12']:
    if (AQUI / (m + '.py')).exists():
        importlib.import_module(m)

OF = json.load(open(RAIZ / 'assets' / 'lei_seca_oficial.json', encoding='utf-8'))
ITEMS = json.load(open(RAIZ / 'assets' / 'items.json', encoding='utf-8'))
L = ITEMS if isinstance(ITEMS, list) else ITEMS.get('items', [])
PONTOS = [dict(id=x['id'], titulo=x['label']) for x in L if str(x.get('id', '')).startswith('DBA26-CPC-')]
PONTOS.sort(key=lambda p: int(p['id'].rsplit('-', 1)[1]))

erros = []


def recorta(chave, ini, fim):
    t = OF.get(chave, {}).get('texto')
    if t is None:
        erros.append(f'{chave}: artigo ausente'); return None
    i = t.find(ini)
    if i < 0:
        erros.append(f'{chave}: início não achado: {ini!r}'); return None
    if fim is None:
        return ini
    j = t.find(fim, i)
    if j < 0:
        erros.append(f'{chave}: fim não achado após início: {fim!r}'); return None
    return t[i:j + len(fim)]


SIGLA_LEI = {'L13105': 'CPC', 'L7347': 'Lei 7.347/1985', 'L4717': 'Lei 4.717/1965', 'L12016': 'Lei 12.016/2009',
             'L9099': 'Lei 9.099/1995', 'L12153': 'Lei 12.153/2009', 'CF': 'CF'}
cont = collections.Counter()
rodadas = {1: [], 2: []}
for it in base.ITENS:
    n = it['ponto'].rsplit('-', 1)[1]
    cont[(it['ponto'], it['rodada'])] += 1
    iid = f"CPC-{n}-R{it['rodada']}-{cont[(it['ponto'], it['rodada'])]:02d}"
    lei = []
    for chave, ini, fim, rot in it['lei']:
        txt = recorta(chave, ini, fim)
        if txt is None:
            erros.append(f'  ↳ no item {iid}'); continue
        sig, art = chave.split(':', 1)
        lei.append(dict(lei=sig, art=art, par='', inc='', rotulo=rot, texto=txt))
    resumo = it['resumo']
    if '**' not in resumo:  # sem negrito escrito à mão: destaca a 1ª palavra-chave presente, senão o 1º dispositivo citado
        for kw in it['palavras_chave']:
            i = resumo.lower().find(kw.lower())
            if i >= 0:
                resumo = resumo[:i] + '**' + resumo[i:i + len(kw)] + '**' + resumo[i + len(kw):]; break
        else:
            m = re.search(r'(Súmulas? [\d/ e]+(?:STJ|STF)|Arts?\. [\d.º]+(?:, [§ºI-V\d, ]+)?|Tema [\d.]+(?:/STJ)?)', resumo)
            if m:
                resumo = resumo[:m.start()] + '**' + m.group(0).rstrip(', ') + '**' + resumo[m.start() + len(m.group(0).rstrip(', ')):]
    com = dict(resumo=resumo)
    if it['regra']: com['regra'] = it['regra']
    if it['excecoes']: com['excecoes'] = it['excecoes']
    if lei: com['lei'] = lei
    if it['juris']: com['juris'] = [{k: v for k, v in j.items() if not k.startswith('_')} for j in it['juris']]
    if it['pegadinha']: com['pegadinha'] = it['pegadinha']
    com['palavras_chave'] = it['palavras_chave']
    rodadas[it['rodada']].append(dict(id=iid, ponto=it['ponto'], tema=it['tema'], assertiva=it['assertiva'],
                                      gabarito=it['gabarito'], comentario=com))

if erros:
    print('\n'.join(erros)); print(f'\n{len([e for e in erros if not e.startswith("  ")])} ERRO(S) — arquivo NÃO gravado.')
    sys.exit(1)

ordem = {p['id']: i for i, p in enumerate(PONTOS)}
for r in rodadas.values():
    r.sort(key=lambda x: (ordem[x['ponto']], x['id']))

dados = dict(
    disciplina='Direito Processual Civil',
    conferido_em='07/11/2026',
    fontes=['Lei 13.105/2015 (CPC) — Planalto', 'Lei 7.347/1985 (Ação Civil Pública) — Planalto',
            'Lei 4.717/1965 (Ação Popular) — Planalto', 'Lei 12.016/2009 (Mandado de Segurança) — Planalto',
            'Lei 9.099/1995 (Juizados Especiais) — Planalto', 'Lei 12.153/2009 (Juizados da Fazenda Pública) — Planalto',
            'Súmulas do STJ — processo.stj.jus.br/SCON/sumstj', 'Temas repetitivos do STJ — processo.stj.jus.br/repetitivos',
            'Súmulas do STF — PDF oficial "Enunciados das Súmulas do STF 1 a 736" (stf.jus.br)',
            'STF — Tema 1.075/RG (portal.stf.jus.br) e ADI 4.296 (Informativo STF 1.021)'],
    pontos=PONTOS,
    rodadas=[dict(n=1, titulo='Rodada 1 · O essencial', itens=rodadas[1]),
             dict(n=2, titulo='Rodada 2 · Aprofundamento', itens=rodadas[2])])
js = ('// Pente Fino — Direito Processual Civil (DBA26-CPC-1 a 12). Gerado por ferramentas/pente_fino/construir.py em 07/11/2026.\n'
      '// Esquema: docs/PENTE_FINO_ESQUEMA.md. Lei recortada de assets/lei_seca_oficial.json; jurisprudência conferida em fonte oficial.\n'
      'window.PENTE_FINO = window.PENTE_FINO || {};\nwindow.PENTE_FINO.CPC = '
      + json.dumps(dados, ensure_ascii=False, indent=1) + ';\n')
(RAIZ / 'discursiva' / 'pente_fino_cpc.js').write_text(js, encoding='utf-8', newline='\n')
print('gravado: discursiva/pente_fino_cpc.js', len(js), 'bytes')
