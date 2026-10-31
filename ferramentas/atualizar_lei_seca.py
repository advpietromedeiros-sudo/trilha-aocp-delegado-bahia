#!/usr/bin/env python3
"""Baixa do Planalto a redação OFICIAL dos diplomas do edital e grava assets/lei_seca_oficial.json.

Rode no seu computador (precisa de internet):  atualizar_lei_seca.bat   ou   py -3 ferramentas/atualizar_lei_seca.py
Somente biblioteca padrão do Python 3.10+.

O que o script faz com cada página do Planalto:
  * descarta o texto riscado (<strike>/<s>/<del>) — é redação revogada;
  * separa o texto por artigo (Art. 1º, Art. 2º-A …);
  * guarda as notas "(Redação dada pela Lei nº …, de 2026)" e marca o artigo com
    `alteracao_2026` quando houver alteração em 2026, para você conferir o marco de 29/07/2026.
"""
from __future__ import annotations
import datetime, html.parser, json, pathlib, re, sys, time, urllib.error, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CAT = ROOT / 'assets' / 'catalogo_leis.json'
OUT = ROOT / 'assets' / 'lei_seca_oficial.json'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) TrilhaAOCP/7 (estudo pessoal)'
BLOCK = {'p', 'br', 'div', 'tr', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'blockquote'}
SKIP = {'strike', 's', 'del', 'script', 'style', 'head', 'title'}


class Txt(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []; self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP: self.skip += 1
        elif tag in BLOCK: self.out.append('\n')

    def handle_endtag(self, tag):
        if tag in SKIP: self.skip = max(0, self.skip - 1)
        elif tag in BLOCK: self.out.append('\n')

    def handle_data(self, data):
        if not self.skip: self.out.append(data)


def decode(raw: bytes) -> str:
    head = raw[:3000].decode('ascii', 'ignore').lower()
    m = re.search(r'charset=["\']?([\w-]+)', head)
    for enc in ([m.group(1)] if m else []) + ['utf-8', 'cp1252', 'latin-1']:
        try: return raw.decode(enc)
        except (LookupError, UnicodeDecodeError): continue
    return raw.decode('latin-1', 'replace')


def html_to_lines(page: str) -> list[str]:
    p = Txt(); p.feed(page)
    text = ''.join(p.out).replace('\xa0', ' ')
    lines = []
    for ln in text.split('\n'):
        s = re.sub(r'[ \t\r]+', ' ', ln).strip()
        if s: lines.append(s)
    return lines


ART = re.compile(r'^Art\.\s*(\d{1,4}(?:\.\d{3})?)\s*(?:º|°|o\b)?\s*(?:-\s*([A-Z]{1,2})\b)?\s*[\.\-–:]?\s*(.*)$')


def split_articles(lines: list[str], sigla: str, nome: str, url: str) -> dict:
    cands = []
    for i, s in enumerate(lines):
        m = ART.match(s)
        if m and not re.match(r'^Art\.\s*\d+[^.]{0,20},', s):
            cands.append((i, (int(m.group(1).replace('.', '')), m.group(2) or '')))
    # sequência crescente mais longa (protege contra remissões no meio do texto)
    best = [1] * len(cands); prv = [-1] * len(cands)
    for i in range(len(cands)):
        for j in range(max(0, i - 300), i):
            if cands[j][1] < cands[i][1] and cands[i][1][0] - cands[j][1][0] <= 400 and best[j] + 1 > best[i]:
                best[i] = best[j] + 1; prv[i] = j
    keep = []
    if cands:
        i = max(range(len(cands)), key=lambda x: best[x])
        while i != -1: keep.append(cands[i]); i = prv[i]
        keep.reverse()
    arts = {}; today = datetime.date.today().strftime('%d/%m/%Y')
    cur_sig = sigla
    bounds = [i for i, _ in keep] + [len(lines)]
    for n, (i, k) in enumerate(keep):
        body = lines[i:bounds[n + 1]]
        # corta títulos/capítulos que antecedem o próximo artigo
        while body and re.match(r'^(TÍTULO|CAPÍTULO|Seção|SEÇÃO|LIVRO|PARTE|Subseção)\b', body[-1]): body.pop()
        if len(body) > 1 and len(body[-1]) < 60 and not re.search(r'[.;:)]$', body[-1]): body.pop()
        art = str(k[0]) + ('-' + k[1] if k[1] else '')
        txt = '\n'.join(body).strip()
        notas = re.findall(r'\((?:Reda[çc][ãa]o dada|Inclu[íi]d[oa]|Revogad[oa]|Vide|Vig[êe]ncia|Acrescid[oa])[^)]*\)', txt)
        alt26 = any(re.search(r'de\s+2026|/2026', x) for x in notas)
        key = f'{cur_sig}:{art}'
        if key in arts: continue
        arts[key] = {'id': key, 'sigla': cur_sig, 'art': art, 'diploma': nome, 'texto': txt, 'url': url,
                     'fonte': 'planalto', 'baixado_em': today, 'alteracao_2026': alt26}
    return arts


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'pt-BR'})
    with urllib.request.urlopen(req, timeout=90) as r:
        return decode(r.read())


def variants(url: str) -> list[str]:
    out = [url]
    if 'compilad' in url: out.append(re.sub(r'compilad[oa]', '', url))
    else: out += [url.replace('.htm', 'compilado.htm'), url.replace('.htm', 'compilada.htm')]
    out += [re.sub(r'/l(\d)', r'/L\1', u) for u in list(out)]
    return list(dict.fromkeys(out))


def main():
    cat = json.loads(CAT.read_text('utf8'))['diplomas']
    only = set(a.upper() for a in sys.argv[1:])
    base = json.loads(OUT.read_text('utf8')) if OUT.exists() else {}
    ok, fail = [], []
    for d in cat:
        if only and d['sigla'].upper() not in only: continue
        if not d.get('url'):
            print(f"-- {d['sigla']}: sem URL no catálogo (lei estadual?) — pulando"); continue
        got = None
        for u in variants(d['url']):
            try:
                page = fetch(u)
                arts = split_articles(html_to_lines(page), d['sigla'], d['nome'], u)
                if len(arts) >= 2: got = arts; break
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                last = exc
            time.sleep(0.8)
        if got:
            for k in [k for k in base if k.startswith(d['sigla'] + ':')]: base.pop(k)
            base.update(got); ok.append(f"{d['sigla']}({len(got)})")
            print(f"OK  {d['sigla']:8} {len(got):5} artigos")
        else:
            fail.append(d['sigla']); print(f"ERRO {d['sigla']}: não foi possível ler {d['url']}")
        time.sleep(1.0)
    OUT.write_text(json.dumps(base, ensure_ascii=False), 'utf8')
    print('\nConcluído. Diplomas atualizados:', ', '.join(ok) or 'nenhum')
    if fail: print('Falharam (corrija a URL em assets/catalogo_leis.json):', ', '.join(fail))
    print('Arquivo gravado:', OUT)
    print('Reinicie o servidor (iniciar_windows.bat) para usar o texto oficial.')


if __name__ == '__main__':
    main()
