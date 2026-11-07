#!/usr/bin/env python3
"""Baixa a redação OFICIAL dos diplomas do edital e grava assets/lei_seca_oficial.json.

Fontes oficiais (campo "fonte" do catálogo assets/catalogo_leis.json):
  * planalto      — leis e decretos federais (www.planalto.gov.br);
  * legislabahia  — leis e a Constituição do Estado da Bahia (Portal de Legislação do Estado da Bahia, Casa Civil,
                    www.legislabahia.ba.gov.br).

Rode no seu computador (precisa de internet):  atualizar_lei_seca.bat   ou   py -3 ferramentas/atualizar_lei_seca.py
Só alguns diplomas:  py -3 ferramentas/atualizar_lei_seca.py CP L11340 BA11370
Somente biblioteca padrão do Python 3.10+.

O que o script faz com cada página:
  * descarta o texto riscado (<strike>/<s>/<del>) — é redação revogada (Planalto);
  * descarta os quadros de alteração da Bahia (class="Alteracao"), que trazem a "Redação original" revogada, e
    guarda o texto deles em `notas`;
  * separa o texto por artigo (Art. 1º, Art. 2º-A …); convenção promulgada por decreto ("Artigo 1", "Artigo I")
    vai para a sigla do campo `anexo` do catálogo;
  * marca o artigo com `alteracao_2026` quando uma nota de alteração cita 2026, para conferir o marco de 29/07/2026.

Defeitos corrigidos em 07/11/2026 (REGRA ZERO: provados com a página real, em .scratch/revisao/diag/):
  1. "Art. 3º - A lei excepcional…" virava a chave CP:3-A (o "A" da frase lido como sufixo): 39 chaves no CP
     e 24 na L7210. Agora o sufixo exige o hífen colado ("2º-A") ou pontuação depois da letra ("2º - A.").
  2. A página da L11340 vem em UTF-16 (marca FF FE); lida como latin-1, não achava artigo nenhum.
  3. A quebra de linha do código-fonte do HTML partia "Art." e "1º" em linhas diferentes (L6091, L14133…).
  4. Convenções em anexo (D65810, D4377, CADH) usam "Artigo N": só os artigos do decreto entravam.
  5. Uma vírgula nos 20 primeiros caracteres ("Art. 22 - O início, a suspensão…") fazia o artigo ser lido como
     remissão e descartado. Agora remissão é só a vírgula logo depois do número ("Art. 5º, II").
  6. Sufixo separado por espaço, como a Bahia escreve ("Art. 111 B - …"), não era lido.
  7. Hífen colado na palavra seguinte ("Art. 88 -O subsídio…", CE-BA) também virava sufixo: o sufixo colado agora
     exige o hífen colado no NÚMERO ("88-O"), sem espaço antes.
  8. O título do capítulo seguinte ("CAPÍTULO XXIV -" + "DO ÍNDIO") ficava grudado no fim do último artigo.
  9. Página iso-8859-1 com aspas do Windows (0x93/0x94) virava caractere de controle (D65810): lida como cp1252.
"""
from __future__ import annotations
import datetime, html.parser, json, pathlib, re, ssl, sys, time, urllib.error, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CAT = ROOT / 'assets' / 'catalogo_leis.json'
OUT = ROOT / 'assets' / 'lei_seca_oficial.json'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) TrilhaAOCP/7 (estudo pessoal)'
BLOCK = {'p', 'br', 'div', 'tr', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'blockquote'}
SKIP = {'strike', 's', 'del', 'script', 'style', 'head', 'title'}
NOTA = '⟦NOTA⟧ '  # marca de linha de nota (quadro de alteração da Bahia): sai do texto, vai para `notas`
VAZIOS = {'br', 'img', 'hr', 'meta', 'link', 'input', 'col', 'area', 'base', 'wbr'}


class Txt(html.parser.HTMLParser):
    """HTML → linhas. `classes_nota`: elementos com essas classes viram UMA linha de nota (fora do texto)."""

    def __init__(self, classes_nota: set[str] | None = None):
        super().__init__(convert_charrefs=True)
        self.out = []; self.skip = 0
        self.classes_nota = classes_nota or set()
        self.nota = None  # (tag, profundidade, [partes]) enquanto dentro de um quadro de nota

    def handle_starttag(self, tag, attrs):
        if self.nota is not None:
            if tag == self.nota[0] and tag not in VAZIOS: self.nota[1] += 1
            if tag in BLOCK: self.nota[2].append(' ')
            return
        cls = set((dict(attrs).get('class') or '').split())
        if cls & self.classes_nota and tag not in VAZIOS:
            self.nota = [tag, 0, []]; return
        if tag in SKIP: self.skip += 1
        elif tag in BLOCK: self.out.append('\n')

    def handle_endtag(self, tag):
        if self.nota is not None:
            if tag == self.nota[0]:
                if self.nota[1] == 0:
                    txt = re.sub(r'\s+', ' ', ''.join(self.nota[2])).strip()
                    if txt: self.out.append('\n' + NOTA + txt + '\n')
                    self.nota = None
                else: self.nota[1] -= 1
            return
        if tag in SKIP: self.skip = max(0, self.skip - 1)
        elif tag in BLOCK: self.out.append('\n')

    def handle_data(self, data):
        # quebra de linha do CÓDIGO-FONTE é espaço em HTML; só as tags de bloco quebram linha (defeito 3)
        data = re.sub(r'[\r\n]+', ' ', data)
        if self.nota is not None: self.nota[2].append(data)
        elif not self.skip: self.out.append(data)


def decode(raw: bytes) -> str:
    # marca de ordem de bytes primeiro (defeito 2: L11340 em UTF-16)
    for bom, enc in ((b'\xef\xbb\xbf', 'utf-8-sig'), (b'\xff\xfe', 'utf-16'), (b'\xfe\xff', 'utf-16')):
        if raw.startswith(bom):
            return raw.decode(enc, 'replace')
    if raw[:400].count(b'\x00') > 50:  # UTF-16 sem marca
        return raw.decode('utf-16-le' if raw[1:2] == b'\x00' else 'utf-16-be', 'replace')
    head = raw[:3000].decode('ascii', 'ignore').lower()
    m = re.search(r'charset=["\']?([\w-]+)', head)
    declarado = [m.group(1)] if m else []
    # página que se diz iso-8859-1 usa as aspas do Windows (0x93/0x94): lida como latin-1, viravam caracteres de
    # controle (D65810). O cp1252 é o mesmo latin-1 com essas posições preenchidas (defeito 9).
    declarado = ['cp1252' if e.lower() in ('iso-8859-1', 'latin-1', 'latin1', 'iso8859-1') else e for e in declarado]
    for enc in declarado + ['utf-8', 'cp1252', 'latin-1']:
        try: return raw.decode(enc)
        except (LookupError, UnicodeDecodeError): continue
    return raw.decode('latin-1', 'replace')


def html_to_lines(page: str, classes_nota: set[str] | None = None) -> list[str]:
    p = Txt(classes_nota); p.feed(page)
    text = ''.join(p.out).replace('\xa0', ' ')
    lines = []
    for ln in text.split('\n'):
        s = re.sub(r'[ \t\r]+', ' ', ln).strip()
        if s: lines.append(s)
    return lines


# Sufixo (2º-A, 121-A): hífen COLADO na letra ("2º-A") ou letra seguida de pontuação/fim ("2º - A."). O "- A" solto
# é o artigo da frase ("Art. 3º - A lei excepcional…"), não sufixo (defeito 1).
ART = re.compile(r'^Art\.\s*(\d{1,4}(?:\.\d{3})?)(?:\s*(?:º|°|o\b))?'
                 r'(?:-([A-Z]{1,2})\b|\s*-?\s*([A-Z]{1,2})(?=\s*[\.\-–:]|\s*$))?\s*[\.\-–:]?\s*(.*)$')
TITULO = re.compile(r'^(TÍTULO|CAPÍTULO|Seção|SEÇÃO|LIVRO|PARTE|Subseção|SUBSEÇÃO)\b')
# remissão ("Art. 5º, II, da CF") = vírgula LOGO depois do número. Antes, qualquer vírgula nos 20 primeiros caracteres
# descartava artigo verdadeiro ("Art. 22 - O início, a suspensão…", BA6677; "Art. 7º - É assegurada, em…") (defeito 5)
REMISSAO = re.compile(r'^Art\.\s*\d+(?:\.\d{3})?\s*(?:º|°|o\b)?\s*(?:-?\s*[A-Z]{1,2}\b)?\s*,')
# artigo de convenção em anexo: "Artigo 1o", "ARTIGO 1", "Artigo XV"
ARTIGO = re.compile(r'^(?:Artigo|ARTIGO)\s+(\d{1,3}|[IVXLC]{1,8})\s*(?:º|°|o\b)?\s*[\.\-–:]?\s*(.*)$')


def romano(s: str) -> int | None:
    v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    if not re.fullmatch(r'[IVXLC]+', s): return None
    tot = 0
    for i, ch in enumerate(s):
        n = v[ch]
        tot += -n if i + 1 < len(s) and v[s[i + 1]] > n else n
    return tot


def candidatos(lines: list[str], inicio: int = 0, anexo: bool = False) -> list:
    cands = []
    for i in range(inicio, len(lines)):
        s = lines[i]
        if anexo:
            m = ARTIGO.match(s)
            if m:
                n = int(m.group(1)) if m.group(1).isdigit() else romano(m.group(1))
                if n: cands.append((i, (n, '')))
            continue
        m = ART.match(s)
        if m and not REMISSAO.match(s):
            cands.append((i, (int(m.group(1).replace('.', '')), m.group(2) or m.group(3) or '')))
    return cands


def split_articles(lines: list[str], sigla: str, nome: str, url: str, anexo: str | None = None,
                   sigla_decreto: str | None = None, fonte: str = 'planalto') -> dict:
    """Separa por artigo. Com `anexo` (convenção promulgada por decreto), os "Artigo N" que vêm depois do decreto
    vão para a sigla `anexo`; os "Art. N" do decreto, para `sigla_decreto` (padrão: `sigla`)."""
    if anexo:
        ini = next((i for i, s in enumerate(lines) if ARTIGO.match(s)), len(lines))
        arts = _cortar(lines[:ini], candidatos(lines[:ini]), sigla_decreto or sigla, nome, url, fonte) if ini else {}
        arts.update(_cortar(lines, candidatos(lines, ini, anexo=True), anexo, nome, url, fonte))
        return arts
    return _cortar(lines, candidatos(lines), sigla, nome, url, fonte)


def tirar_titulos(body: list[str]) -> None:
    """Tira do fim do artigo os títulos do bloco seguinte, inclusive o par "CAPÍTULO II" + nome em linha própria."""
    while len(body) > 1:
        if TITULO.match(body[-1]):
            body.pop()
            continue
        if len(body) > 2 and TITULO.match(body[-2]) and not re.search(r'[.;:]$', body[-1]):
            del body[-2:]
            continue
        break


def _cortar(lines: list[str], cands: list, sigla: str, nome: str, url: str, fonte: str) -> dict:
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
    bounds = [i for i, _ in keep] + [len(lines)]
    for n, (i, k) in enumerate(keep):
        bruto = lines[i:bounds[n + 1]]
        notas_ba = [x[len(NOTA):] for x in bruto if x.startswith(NOTA)]
        body = [x for x in bruto if not x.startswith(NOTA)]
        # corta títulos/capítulos que antecedem o próximo artigo: o par "CAPÍTULO II" + "DOS CRIMES…" (o nome vem
        # em linha própria). Antes só o nome saía e o "CAPÍTULO …" ficava grudado no fim do artigo (defeito 8).
        tirar_titulos(body)
        # rubrica do próximo artigo ("Inimputáveis"), linha curta sem pontuação; depois dela, de novo os títulos
        if len(body) > 1 and len(body[-1]) < 60 and not re.search(r'[.;:)]$', body[-1]): body.pop()
        tirar_titulos(body)
        art = str(k[0]) + ('-' + k[1] if k[1] else '')
        txt = '\n'.join(body).strip()
        notas = re.findall(r'\((?:Reda[çc][ãa]o dada|Inclu[íi]d[oa]|Revogad[oa]|Vide|Vig[êe]ncia|Acrescid[oa])[^)]*\)', txt)
        alt26 = any(re.search(r'de\s+2026|/2026', x) for x in notas + notas_ba)
        key = f'{sigla}:{art}'
        if key in arts: continue
        arts[key] = {'id': key, 'sigla': sigla, 'art': art, 'diploma': nome, 'texto': txt, 'url': url,
                     'fonte': fonte, 'baixado_em': today, 'alteracao_2026': alt26}
        if notas_ba: arts[key]['notas'] = notas_ba
    return arts


def contexto_tls(url: str):
    """O servidor do Legisla Bahia só fecha o aperto de mão TLS com o nível de segurança 1 do OpenSSL 3 (medido em
    07/11/2026: o padrão dá SSL UNEXPECTED_EOF_WHILE_READING; o curl do Windows lê). O certificado continua
    verificado; a exceção vale só para esse host."""
    if 'legislabahia.ba.gov.br' not in url: return None
    ctx = ssl.create_default_context()
    ctx.set_ciphers('DEFAULT:@SECLEVEL=1')
    ctx.options |= getattr(ssl, 'OP_LEGACY_SERVER_CONNECT', 0x4)
    return ctx


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'pt-BR'})
    with urllib.request.urlopen(req, timeout=90, context=contexto_tls(url)) as r:
        return decode(r.read())


def variants(url: str) -> list[str]:
    if 'planalto.gov.br' not in url: return [url]
    out = [url]
    if 'compilad' in url: out.append(re.sub(r'compilad[oa]', '', url))
    else: out += [url.replace('.htm', 'compilado.htm'), url.replace('.htm', 'compilada.htm')]
    out += [re.sub(r'/l(\d)', r'/L\1', u) for u in list(out)]
    return list(dict.fromkeys(out))


def siglas_de(d: dict) -> list[str]:
    return [s for s in dict.fromkeys([d.get('sigla_decreto') or d['sigla'], d.get('anexo')]) if s]


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    cat = json.loads(CAT.read_text('utf8'))['diplomas']
    only = set(a.upper() for a in sys.argv[1:])
    base = json.loads(OUT.read_text('utf8')) if OUT.exists() else {}
    ok, fail = [], []
    for d in cat:
        if only and d['sigla'].upper() not in only: continue
        if not d.get('url'):
            print(f"-- {d['sigla']}: sem URL no catálogo — pulando"); continue
        fonte = d.get('fonte', 'planalto')
        notas = {'Alteracao', 'alteracao'} if fonte == 'legislabahia' else None
        got, motivos = None, []
        for u in variants(d['url']):
            try:
                page = fetch(u)
                arts = split_articles(html_to_lines(page, notas), d['sigla'], d['nome'], u, d.get('anexo'),
                                      d.get('sigla_decreto'), fonte)
                if len(arts) >= 2: got = arts; break
                motivos.append(f'{u}: página lida, {len(arts)} artigo(s) achado(s)')
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                motivos.append(f'{u}: {type(exc).__name__}: {exc}')
            time.sleep(0.8)
        if got:
            for s in siglas_de(d):
                for k in [k for k in base if k.startswith(s + ':')]: base.pop(k)
            base.update(got)
            por = {}
            for v in got.values(): por[v['sigla']] = por.get(v['sigla'], 0) + 1
            ok.append(f"{d['sigla']}({len(got)})")
            print(f"OK  {d['sigla']:8} {len(got):5} artigos" + ('' if len(por) == 1 else '  ' + ', '.join(f'{s}: {n}' for s, n in por.items())))
        else:
            fail.append(d['sigla']); print(f"ERRO {d['sigla']}: não foi possível ler {d['url']}")
            for m in motivos: print(f"     {m}")
        time.sleep(1.0)
    OUT.write_text(json.dumps(base, ensure_ascii=False), 'utf8')
    print('\nConcluído. Diplomas atualizados:', ', '.join(ok) or 'nenhum')
    if fail: print('Falharam (corrija a URL em assets/catalogo_leis.json):', ', '.join(fail))
    print('Arquivo gravado:', OUT)
    print('Reinicie o servidor (iniciar_windows.bat) para usar o texto oficial.')


if __name__ == '__main__':
    main()
