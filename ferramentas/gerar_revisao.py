"""Gera um módulo da Revisão Delegado PC-BA (estilo caderno): HTML interativo autocontido e PDF.

Uso:
  python ferramentas/gerar_revisao.py MODULO            gera revisao/saida/MODULO.html e .pdf
  python ferramentas/gerar_revisao.py MODULO --validar  só valida o JSON (não escreve nada)
  python ferramentas/gerar_revisao.py MODULO --sem-pdf  gera só o HTML
  python ferramentas/gerar_revisao.py --autoteste       REGRA CINCO: planta defeitos num módulo
                                                         válido e só sai 0 se a validação ACUSAR todos
Opções para teste: --itens ARQ --lei ARQ --sumulas ARQ --saida PASTA

MODULO é o nome (lido de revisao/conteudo/MODULO.json) ou o caminho de um .json.
O esquema do módulo está em revisao/ESQUEMA_MODULO.md. O molde (HTML, CSS, JS, avatar) está em
revisao/molde/. O conteúdo (revisao/conteudo/) e a saída (revisao/saida/) ficam fora do Git (D-018).

RECUSA (sai 1) o módulo com: ponto sem id do edital ou com id que não existe em assets/items.json;
lei seca sem chave ou sem artigo, com chave:artigo ausente de assets/lei_seca_oficial.json ou com
texto que não confere com o oficial; jurisprudência sem tribunal, fonte ou data; súmula com texto
diferente do de assets/sumulas.json; ficha sem gabarito C/E ou sem fundamento; questão sem as cinco
alternativas, sem gabarito A–E, sem comentário ou com origem fora do padrão; HTML fora da lista
permitida; referência proibida no texto final (ferramentas/referencias_proibidas.py).
Saídas: 0 gerado/válido · 1 recusado ou falha · 2 uso errado.
"""

import base64
import copy
import datetime as dt
import html
import io
import json
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "ferramentas"))
import referencias_proibidas as RP  # noqa: E402

MOLDE = RAIZ / "revisao" / "molde"
CONTEUDO = RAIZ / "revisao" / "conteudo"
SAIDA = RAIZ / "revisao" / "saida"
ITENS = RAIZ / "assets" / "items.json"
LEI = RAIZ / "assets" / "lei_seca_oficial.json"
SUMULAS = RAIZ / "assets" / "sumulas.json"
AVATAR = MOLDE / "avatar-professor-pietro-medeiros.jpg"
NAVEGADORES = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
]

ESQUEMA = 1
TAGS_OK = {"b", "strong", "i", "em", "mark", "u", "br", "sub", "sup", "small", "code"}
ORIGEM_OK = re.compile(r"^(AOCP .+|Trilha|Simulado( .+)?|Revisão)$")
DATA_OK = re.compile(r"^\d{2}/\d{2}/\d{4}$")
SUMULA_OK = re.compile(r"^(STF|STJ|TSE|TST|STM)-(V-)?\d+$")
# anotações do Planalto que não fazem parte do texto normativo
ANOTACAO = re.compile(
    r"\((?:Reda[cç][aã]o|Inclu[ií]d|Revogad|Vide|Vig[eê]ncia|Renumerad|Acrescid|"
    r"Express[aã]o|Promulga|Regulament|Produ[cç][aã]o de efeito)[^)]*\)",
    re.I,
)


# ------------------------------------------------------------------ utilidades
def esc(t):
    return html.escape(str(t), quote=True)


def norm(t):
    """Normaliza para conferir citação × texto oficial: tira anotações do Planalto e junta espaços."""
    t = ANOTACAO.sub(" ", str(t))
    return re.sub(r"\s+", " ", t).strip()


def data_valida(s):
    if not isinstance(s, str) or not DATA_OK.match(s):
        return None
    try:
        return dt.datetime.strptime(s, "%d/%m/%Y").date()
    except ValueError:
        return None


def lista(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def rico(t):
    """Texto com HTML restrito (já validado). ==x== vira marca-texto."""
    return re.sub(r"==(.+?)==", r"<mark>\1</mark>", str(t)).replace("\n", "<br>")


def num_br(x):
    if isinstance(x, (int, float)) and float(x).is_integer():
        return str(int(x))
    return f"{x:.1f}".replace(".", ",")


def art_rot(a):
    m = re.match(r"^(\d+)(.*)$", str(a))
    if not m:
        return str(a)
    n = int(m.group(1))
    return f"{n}º{m.group(2)}" if n < 10 else f"{n}{m.group(2)}"


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", str(t).lower()).strip("-")


def carregar_json(p, rotulo):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"[FALHA] {rotulo} não encontrado: {p}") from None
    except json.JSONDecodeError as e:
        raise SystemExit(f"[FALHA] {rotulo} não é JSON válido: {p} ({e})") from e


# ------------------------------------------------------------------ validação
def checar_html(v, onde, erros):
    for t in lista(v):
        if not isinstance(t, str):
            erros.append(f"{onde}: esperado texto, veio {type(t).__name__}")
            continue
        for m in re.finditer(r"<\s*(/?)\s*([a-zA-Z0-9]+)([^>]*)>", t):
            tag, attrs = m.group(2).lower(), m.group(3).strip().rstrip("/").strip()
            if tag not in TAGS_OK:
                erros.append(f"{onde}: tag <{tag}> fora da lista permitida {sorted(TAGS_OK)}")
            elif attrs:
                erros.append(f"{onde}: tag <{tag}> com atributo ({attrs[:40]}) não é permitida")


def obrig(d, campo, onde, erros, tipo=str):
    v = d.get(campo) if isinstance(d, dict) else None
    vazio = (
        v is None or (isinstance(v, (str, list, dict)) and not v) or (isinstance(v, str) and not v.strip())
    )
    if vazio:
        erros.append(f"{onde}: falta '{campo}'")
        return None
    if tipo and not isinstance(v, tipo if isinstance(tipo, tuple) else (tipo,)):
        erros.append(f"{onde}: '{campo}' deveria ser {tipo}")
        return None
    return v


def validar(mod, itens, lei, sumulas):
    """Devolve (erros, avisos). Erro reprova a geração; aviso só se relata."""
    erros, avisos = [], []
    if not isinstance(mod, dict):
        return ["o módulo não é um objeto JSON"], []
    if mod.get("esquema") != ESQUEMA:
        erros.append(f"módulo: 'esquema' deve ser {ESQUEMA} (veio {mod.get('esquema')!r})")
    for c in ("modulo", "titulo"):
        obrig(mod, c, "módulo", erros)
    if mod.get("modulo") and not re.match(r"^[a-z0-9_][a-z0-9_-]*$", str(mod["modulo"])):
        erros.append("módulo: 'modulo' só aceita letras minúsculas, números, _ e - (vira nome de arquivo)")
    conf = data_valida(mod.get("conferido_em"))
    if not conf:
        erros.append("módulo: 'conferido_em' ausente ou fora de dd/mm/aaaa")
    elif conf > dt.date.today():
        erros.append(f"módulo: 'conferido_em' ({mod['conferido_em']}) está no futuro")
    for c in ("titulo", "subtitulo", "apresentacao"):
        checar_html(mod.get(c), f"módulo.{c}", erros)
    for i, s in enumerate(lista(mod.get("sensivel_a_mudanca")), 1):
        checar_html(s, f"módulo.sensivel_a_mudanca[{i}]", erros)
    for i, s in enumerate(lista(mod.get("dicas")), 1):
        checar_html(s, f"módulo.dicas[{i}]", erros)

    blocos = mod.get("blocos")
    if not isinstance(blocos, list) or not blocos:
        erros.append("módulo: 'blocos' ausente ou vazio")
        return erros, avisos
    vistos = set()
    baixados = set()
    for bi, b in enumerate(blocos, 1):
        ob = f"bloco {bi}"
        obrig(b, "titulo", ob, erros)
        checar_html(b.get("titulo"), f"{ob}.titulo", erros)
        checar_html(b.get("em_uma_frase"), f"{ob}.em_uma_frase", erros)
        pontos = b.get("pontos") if isinstance(b, dict) else None
        if not isinstance(pontos, list) or not pontos:
            erros.append(f"{ob}: 'pontos' ausente ou vazio")
            continue
        for pi, p in enumerate(pontos, 1):
            op = f"{ob}, ponto {pi}"
            if not isinstance(p, dict):
                erros.append(f"{op}: não é objeto")
                continue
            pid = p.get("id")
            if not pid or not isinstance(pid, str):
                erros.append(f"{op}: ponto sem id do edital")
            else:
                op = f"{op} ({pid})"
                if pid not in itens:
                    erros.append(f"{op}: id não existe em assets/items.json")
                if pid in vistos:
                    erros.append(f"{op}: id repetido no módulo")
                vistos.add(pid)
            pr = p.get("prioridade")
            if (
                not isinstance(pr, dict)
                or not isinstance(pr.get("escore"), (int, float))
                or isinstance(pr.get("escore"), bool)
            ):
                erros.append(f"{op}: falta 'prioridade.escore' numérico")
            if p.get("titulo") is not None:
                checar_html(p["titulo"], f"{op}.titulo", erros)
            if not lista(p.get("o_que_cai")):
                erros.append(f"{op}: falta 'o_que_cai'")
            for campo in ("o_que_cai", "pegadinhas", "dia_a_dia", "detalhe_tecnico", "checklist"):
                for k, t in enumerate(lista(p.get(campo)), 1):
                    checar_html(t, f"{op}.{campo}[{k}]", erros)
            # lei seca
            for k, L in enumerate(lista(p.get("lei_seca")), 1):
                ol = f"{op}, lei seca {k}"
                if not isinstance(L, dict):
                    erros.append(f"{ol}: não é objeto")
                    continue
                chave, art = L.get("lei"), L.get("art")
                if not chave:
                    erros.append(f"{ol}: lei sem chave ('lei', ex. CP)")
                if not art:
                    erros.append(f"{ol}: lei sem artigo ('art')")
                txt = L.get("texto")
                if not isinstance(txt, str) or not txt.strip():
                    erros.append(f"{ol}: falta 'texto' (trecho exato do texto oficial)")
                elif re.search(r"<[a-zA-Z/]", txt):
                    erros.append(f"{ol}: 'texto' da lei é texto puro, sem HTML")
                if chave and art:
                    of = lei.get(f"{chave}:{art}")
                    if of is None:
                        erros.append(f"{ol}: '{chave}:{art}' não existe em assets/lei_seca_oficial.json")
                    elif isinstance(txt, str) and txt.strip() and norm(txt) not in norm(of.get("texto", "")):
                        erros.append(
                            f"{ol}: texto não confere com o oficial de {chave}:{art} "
                            f"(citado: {norm(txt)[:70]!r}…)"
                        )
                    elif of:
                        if of.get("baixado_em"):
                            baixados.add(of["baixado_em"])
                        if of.get("alteracao_2026"):
                            avisos.append(
                                f"{ol}: {chave}:{art} tem alteração de 2026 (vai para 'sensível a mudança')"
                            )
                for c in ("par", "inc", "rotulo"):
                    if L.get(c) is not None and not isinstance(L.get(c), str):
                        erros.append(f"{ol}: '{c}' deve ser texto")
            # jurisprudência
            for k, J in enumerate(lista(p.get("jurisprudencia")), 1):
                oj = f"{op}, juris {k}"
                if not isinstance(J, dict):
                    erros.append(f"{oj}: não é objeto")
                    continue
                if not J.get("tribunal"):
                    erros.append(f"{oj}: juris sem tribunal")
                if not J.get("fonte"):
                    erros.append(f"{oj}: juris sem fonte")
                dj = data_valida(J.get("data"))
                if not J.get("data"):
                    erros.append(f"{oj}: juris sem data")
                elif not dj:
                    erros.append(f"{oj}: data da juris fora de dd/mm/aaaa ({J.get('data')!r})")
                if not J.get("texto"):
                    erros.append(f"{oj}: falta 'texto'")
                elif re.search(r"<[a-zA-Z/]", str(J.get("texto"))):
                    erros.append(f"{oj}: 'texto' da juris é texto puro, sem HTML")
                checar_html(J.get("comentario"), f"{oj}.comentario", erros)
                s = J.get("sumula")
                if s:
                    if not SUMULA_OK.match(str(s)):
                        erros.append(f"{oj}: 'sumula' fora do padrão TRIBUNAL-NÚMERO (ex. STJ-593): {s!r}")
                    else:
                        trib = str(s).split("-")[0]
                        if J.get("tribunal") and J["tribunal"] != trib:
                            erros.append(f"{oj}: tribunal {J['tribunal']} diferente do da súmula {s}")
                        ref = sumulas.get(f"SUM-{s}")
                        if ref is None:
                            avisos.append(
                                f"{oj}: súmula {s} não está em assets/sumulas.json (texto não conferido)"
                            )
                        elif J.get("texto") and norm(J["texto"]) not in norm(ref.get("texto", "")):
                            erros.append(f"{oj}: texto da súmula {s} não confere com assets/sumulas.json")
            # pegadinhas, esquema
            esq = p.get("esquema")
            if esq is not None:
                oe = f"{op}, esquema"
                tipo = esq.get("tipo") if isinstance(esq, dict) else None
                if tipo == "tabela":
                    cols = esq.get("colunas")
                    if not isinstance(cols, list) or not cols:
                        erros.append(f"{oe}: tabela sem 'colunas'")
                    for li, ln in enumerate(lista(esq.get("linhas")), 1):
                        if not isinstance(ln, list) or (isinstance(cols, list) and len(ln) != len(cols)):
                            erros.append(f"{oe}: linha {li} não tem o número de colunas")
                        else:
                            checar_html(ln, f"{oe}.linha {li}", erros)
                    checar_html(cols or [], f"{oe}.colunas", erros)
                elif tipo == "comparativo":
                    cs = esq.get("colunas")
                    if not isinstance(cs, list) or len(cs) < 2:
                        erros.append(f"{oe}: comparativo pede ao menos 2 colunas")
                    for c in lista(cs):
                        if not isinstance(c, dict) or not c.get("titulo") or not lista(c.get("itens")):
                            erros.append(f"{oe}: coluna do comparativo sem 'titulo' ou 'itens'")
                        else:
                            checar_html([c["titulo"]] + lista(c["itens"]), f"{oe}.coluna", erros)
                else:
                    erros.append(f"{oe}: 'tipo' deve ser 'tabela' ou 'comparativo'")
                checar_html(esq.get("titulo") if isinstance(esq, dict) else None, f"{oe}.titulo", erros)
            # fichas
            for k, F in enumerate(lista(p.get("fichas")), 1):
                of_ = f"{op}, ficha {k}"
                if not isinstance(F, dict):
                    erros.append(f"{of_}: não é objeto")
                    continue
                if not F.get("item"):
                    erros.append(f"{of_}: ficha sem item")
                if F.get("gabarito") not in ("C", "E"):
                    erros.append(f"{of_}: ficha sem gabarito C ou E (veio {F.get('gabarito')!r})")
                if not F.get("fundamento"):
                    erros.append(f"{of_}: ficha sem fundamento")
                checar_html([F.get("item") or "", F.get("fundamento") or ""], of_, erros)
            # questões A–E
            for k, Q in enumerate(lista(p.get("questoes")), 1):
                oq = f"{op}, questão {k}"
                if not isinstance(Q, dict):
                    erros.append(f"{oq}: não é objeto")
                    continue
                if not Q.get("enunciado"):
                    erros.append(f"{oq}: questão sem enunciado")
                alt = Q.get("alternativas")
                if not isinstance(alt, dict) or sorted(alt) != list("ABCDE") or not all(alt.values()):
                    erros.append(f"{oq}: questão precisa das alternativas A, B, C, D e E, todas com texto")
                else:
                    checar_html(list(alt.values()), f"{oq}.alternativas", erros)
                if Q.get("gabarito") not in list("ABCDE"):
                    erros.append(f"{oq}: questão sem gabarito A–E (veio {Q.get('gabarito')!r})")
                if not Q.get("comentario"):
                    erros.append(f"{oq}: questão sem comentário")
                if not isinstance(Q.get("origem"), str) or not ORIGEM_OK.match(Q.get("origem", "")):
                    erros.append(
                        f"{oq}: origem fora do padrão ('AOCP <prova>', 'Trilha', 'Simulado [n]' ou 'Revisão'): "
                        f"{Q.get('origem')!r}"
                    )
                checar_html([Q.get("enunciado") or "", Q.get("comentario") or ""], oq, erros)
            # ponte com a discursiva
            d = p.get("discursiva")
            if d is not None:
                if not isinstance(d, dict) or not d.get("peca"):
                    erros.append(f"{op}: 'discursiva' precisa de 'peca'")
                else:
                    checar_html([d.get("peca"), d.get("como") or ""], f"{op}.discursiva", erros)
    if conf and baixados:
        velho = min(data_valida(b) for b in baixados if data_valida(b))
        if (conf - velho).days > 30:
            avisos.append(
                f"lei seca oficial baixada em {velho:%d/%m/%Y}, mais de 30 dias antes da conferência: "
                "rode atualizar_lei_seca.bat (REVISAO_PLANO, rotina 1)"
            )
    return erros, avisos


# ------------------------------------------------------------------ montagem
def ordenar(mod):
    """Ordem por prioridade: pontos por escore (maior primeiro) e blocos pelo maior escore; letras A, B, C…"""
    blocos = copy.deepcopy(mod["blocos"])
    if mod.get("ordem", "prioridade") == "prioridade":
        for b in blocos:
            b["pontos"].sort(key=lambda p: -p["prioridade"]["escore"])
        blocos.sort(key=lambda b: -max(p["prioridade"]["escore"] for p in b["pontos"]))
    for i, b in enumerate(blocos):
        b["letra"] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
    return blocos


def rotulo_lei(L, lei):
    if L.get("rotulo"):
        return L["rotulo"]
    of = lei.get(f"{L['lei']}:{L['art']}", {})
    nome = (of.get("diploma") or L["lei"]).split(" — ")[0]
    r = f"{nome}, art. {art_rot(L['art'])}"
    if L.get("par"):
        r += f", {L['par']}"
    if L.get("inc"):
        r += f", inciso {L['inc']}"
    return r


def html_lei(L, lei):
    attrs = f'data-lei="{esc(L["lei"])}" data-art="{esc(L["art"])}"'
    if L.get("par"):
        attrs += f' data-par="{esc(L["par"])}"'
    if L.get("inc"):
        attrs += f' data-inc="{esc(L["inc"])}"'
    of = lei.get(f"{L['lei']}:{L['art']}", {})
    url = of.get("url")
    fonte = f'<span class="lei-fonte">texto oficial · baixado em {esc(of.get("baixado_em", "?"))}'
    casa = "Legisla Bahia" if of.get("fonte") == "legislabahia" else "Planalto"
    fonte += (
        f' · <a href="{esc(url)}" target="_blank" rel="noopener">{casa}</a></span>' if url else "</span>"
    )
    com = f'<p class="lei-com">{rico(L["comentario"])}</p>' if L.get("comentario") else ""
    return (
        f'<div class="lei-box"><span class="lei-ref">📜 {esc(rotulo_lei(L, lei))}</span>'
        f'<blockquote class="lei" {attrs}>{esc(L["texto"].strip())}</blockquote>{fonte}{com}</div>'
    )


def html_juris(J):
    attrs = (
        f'data-tribunal="{esc(J["tribunal"])}" data-fonte="{esc(J["fonte"])}" data-data="{esc(J["data"])}"'
    )
    if J.get("sumula"):
        attrs += f' data-sumula="{esc(J["sumula"])}"'
    com = f'<p class="juris-com">{rico(J["comentario"])}</p>' if J.get("comentario") else ""
    return (
        f'<div class="juris" {attrs}><span class="src">{esc(J["fonte"])} · {esc(J["data"])}</span>'
        f'<p class="juris-texto">{esc(J["texto"])}</p>{com}</div>'
    )


def html_esquema(e):
    tit = f'<p class="ideia"><b>{rico(e["titulo"])}</b></p>' if e.get("titulo") else ""
    if e["tipo"] == "tabela":
        th = "".join(f"<th>{rico(c)}</th>" for c in e["colunas"])
        hl = ' class="hl"'
        tr = "".join(
            "<tr>" + "".join(f"<td{hl if j == 0 else ''}>{rico(c)}</td>" for j, c in enumerate(ln)) + "</tr>"
            for ln in lista(e.get("linhas"))
        )
        return f'{tit}<div class="tbl-wrap"><table class="dtbl"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
    cls = ["", " alt", " alt2"]
    cols = "".join(
        f'<div class="cmp-col{cls[i % 3]}"><h4>{rico(c["titulo"])}</h4><ul>'
        + "".join(f"<li>{rico(x)}</li>" for x in lista(c["itens"]))
        + "</ul></div>"
        for i, c in enumerate(e["colunas"])
    )
    return f'{tit}<div class="cmp-grid">{cols}</div>'


def sec(chave, titulo, corpo, essencial=False):
    cls = f"sec sec-{chave}" + ("" if essencial else " nao-essencial")
    h = f"<h4>{titulo}</h4>" if titulo else ""
    return f'<div class="{cls}">{h}{corpo}</div>'


def card_ponto(p, letra, idx, itens, lei, cont):
    item = itens.get(p["id"], {})
    pid = "p-" + slug(p["id"])
    titulo = p.get("titulo") or item.get("label", p["id"])
    pr = p["prioridade"]
    nivel = pr.get("nivel") or item.get("priority") or ""
    prio_txt = (
        f"prioridade {esc(nivel)} · escore {num_br(pr['escore'])}"
        if nivel
        else f"escore {num_br(pr['escore'])}"
    )
    h = [
        f'<div class="card" id="{pid}" data-ponto="{esc(p["id"])}" data-escore="{pr["escore"]}">',
        f'<h3><span class="tag">{letra}{idx} · {esc(item.get("discipline", ""))} · item {esc(item.get("number", ""))} do edital</span>{rico(titulo)}</h3>',
        f'<div class="ponto-meta"><span class="badge b-edital">{esc(p["id"])}</span><span class="badge b-prio">{prio_txt}</span>'
        + (
            f'<span class="badge b-art">fonte da prioridade: {esc(pr["fonte"])}</span>'
            if pr.get("fonte")
            else ""
        )
        + "</div>",
    ]
    h.append(sec("cai", "O que cai", "".join(f"<p>{rico(t)}</p>" for t in lista(p["o_que_cai"])), True))
    if lista(p.get("lei_seca")):
        h.append(sec("lei", "Lei seca", "".join(html_lei(L, lei) for L in lista(p["lei_seca"])), True))
    if lista(p.get("jurisprudencia")):
        h.append(sec("juris", "Jurisprudência", "".join(html_juris(J) for J in lista(p["jurisprudencia"]))))
    if lista(p.get("pegadinhas")):
        h.append(
            sec(
                "pegadinhas",
                "",
                '<div class="alert alert-pegadinha"><div class="alt-label">🚨 Pegadinhas da AOCP</div><ul>'
                + "".join(f"<li>{rico(t)}</li>" for t in lista(p["pegadinhas"]))
                + "</ul></div>",
                True,
            )
        )
    if lista(p.get("dia_a_dia")):
        h.append(
            sec(
                "dia",
                "",
                '<div class="alert alert-case"><div class="alt-label">🏙️ No dia a dia do delegado</div>'
                + "".join(f"<p>{rico(t)}</p>" for t in lista(p["dia_a_dia"]))
                + "</div>",
            )
        )
    if lista(p.get("detalhe_tecnico")):
        h.append(
            sec(
                "detalhe",
                "",
                '<div class="alert alert-warn"><div class="alt-label">⚠️ Detalhe técnico</div>'
                + "".join(f"<p>{rico(t)}</p>" for t in lista(p["detalhe_tecnico"]))
                + "</div>",
            )
        )
    if p.get("esquema"):
        h.append(sec("esquema", "Esquema", html_esquema(p["esquema"])))
    if lista(p.get("fichas")):
        fs = []
        for k, F in enumerate(lista(p["fichas"]), 1):
            cont["fichas"] += 1
            fid = f"{pid}-f{k}"
            badge = (
                '<span class="badge b-ok">CERTO</span>'
                if F["gabarito"] == "C"
                else '<span class="badge b-no">ERRADO</span>'
            )
            fs.append(
                f'<div class="quiz-card" data-tipo="ce" data-ans="{F["gabarito"]}" data-id="{fid}">'
                f'<div class="quiz-q-num">FICHA {cont["fichas"]} · CERTO OU ERRADO</div>'
                f'<p class="quiz-statement">{rico(F["item"])}</p>'
                f'<button class="quiz-reveal-btn" onclick="revealQuiz(\'{fid}\')" type="button">Ver gabarito e fundamento</button>'
                f'<div class="quiz-answer" id="qa-{fid}">{badge}<p class="quiz-gabarito">📌 {rico(F["fundamento"])}</p></div></div>'
            )
        h.append(sec("fichas", "Fichas de certo ou errado", "".join(fs)))
    if lista(p.get("questoes")):
        qs = []
        for k, Q in enumerate(lista(p["questoes"]), 1):
            cont["questoes"] += 1
            qid = f"{pid}-q{k}"
            alts = "".join(
                f'<li><button class="mc-btn" type="button" data-op="{L}"><span class="mc-l">{L})</span>'
                f"<span>{rico(Q['alternativas'][L])}</span></button></li>"
                for L in "ABCDE"
            )
            qs.append(
                f'<div class="quiz-card mc-card" data-tipo="mc" data-ans="{Q["gabarito"]}" data-id="{qid}">'
                f'<div class="quiz-q-num">QUESTÃO {cont["questoes"]} · MÚLTIPLA ESCOLHA<span class="quiz-origem">· {esc(Q["origem"])}</span></div>'
                f'<p class="quiz-statement">{rico(Q["enunciado"])}</p><ol class="mc-alts">{alts}</ol>'
                f'<button class="quiz-reveal-btn" onclick="revealQuiz(\'{qid}\')" type="button">Ver gabarito e comentário</button>'
                f'<div class="quiz-answer" id="qa-{qid}"><span class="badge b-ok">GABARITO: {Q["gabarito"]}</span>'
                f'<p class="quiz-gabarito">📌 {rico(Q["comentario"])}</p></div></div>'
            )
        h.append(sec("questoes", "Questões objetivas", "".join(qs)))
    if p.get("discursiva"):
        d = p["discursiva"]
        corpo = f"<p><b>Peça:</b> {rico(d['peca'])}</p>" + (
            f"<p>{rico(d['como'])}</p>" if d.get("como") else ""
        )
        h.append(
            sec(
                "discursiva",
                "",
                f'<div class="alert alert-info"><div class="alt-label">✍️ Ponte com a discursiva</div>{corpo}</div>',
            )
        )
    if lista(p.get("checklist")):
        h.append(
            sec(
                "checklist",
                "Checklist do ponto",
                f'<ul class="checklist" data-ck="{pid}">'
                + "".join(f"<li>{rico(t)}</li>" for t in lista(p["checklist"]))
                + "</ul>",
            )
        )
    h.append("</div>")
    return pid, titulo, "\n".join(h)


def montar(mod, itens, lei, sumulas, b64, avisos):
    molde = (MOLDE / "caderno.html").read_text(encoding="utf-8")
    css = (MOLDE / "caderno.css").read_text(encoding="utf-8")
    js = (MOLDE / "caderno.js").read_text(encoding="utf-8")
    blocos = ordenar(mod)
    cont = {"fichas": 0, "questoes": 0}
    html_blocos, toc_blocos, ordem = [], [], []
    for b in blocos:
        L = b["letra"]
        cards, links = [], []
        for i, p in enumerate(b["pontos"], 1):
            pid, tit, h = card_ponto(p, L, i, itens, lei, cont)
            cards.append(h)
            links.append(f'<a href="#{pid}">{esc(re.sub("<[^>]+>", "", tit))}</a>')
            ordem.append((p["prioridade"]["escore"], pid, tit, p, L))
        intro = (
            f'<div class="alert alert-info block-intro"><div class="alt-label">🧭 Em uma frase</div><p>{rico(b["em_uma_frase"])}</p></div>'
            if b.get("em_uma_frase")
            else ""
        )
        ic = f"{esc(b['icone'])} " if b.get("icone") else ""
        html_blocos.append(
            f'<section class="block" id="bloco-{L.lower()}"><div class="block-title"><span class="num">{L}</span>'
            f"<h2>{ic}{rico(b['titulo'])}</h2></div>\n{intro}\n" + "\n".join(cards) + "\n</section>"
        )
        toc_blocos.append(
            f'<details class="toc-group"><summary>Bloco {L} — {esc(re.sub("<[^>]+>", "", b["titulo"]))}</summary>'
            f'<div class="toc-links">\n' + "\n".join(links) + "\n</div></details>"
        )
    ordem.sort(key=lambda x: -x[0])
    indice, toc_prio = [], []
    for n, (escore, pid, tit, p, L) in enumerate(ordem, 1):
        nivel = p["prioridade"].get("nivel") or itens.get(p["id"], {}).get("priority", "")
        t = esc(re.sub("<[^>]+>", "", tit))
        indice.append(
            f'<li><a href="#{pid}"><span class="prio-n">{n}</span><span class="prio-t">{t}<small>{esc(p["id"])} · Bloco {L}</small></span>'
            f'<span class="prio-esc">{esc(nivel + " · " if nivel else "")}{num_br(escore)}</span></a></li>'
        )
        toc_prio.append(f'<a href="#{pid}">{n}. {t}</a>')
    toc = (
        '<details class="toc-group" open><summary>📈 Por prioridade</summary><div class="toc-links">\n'
        + "\n".join(toc_prio)
        + "\n</div></details>\n"
        + "\n".join(toc_blocos)
    )

    # fichário da lei seca: trechos citados, agrupados por diploma, sem repetição
    grupos, vistos = {}, set()
    for b in blocos:
        for p in b["pontos"]:
            for Lc in lista(p.get("lei_seca")):
                chave = (Lc["lei"], Lc["art"], Lc.get("par") or "", Lc.get("inc") or "", norm(Lc["texto"]))
                if chave in vistos:
                    continue
                vistos.add(chave)
                grupos.setdefault(Lc["lei"], []).append((Lc, p["id"]))
    ls_toc, ls_cont, baixados = [], [], set()
    for gi, (sig, regs) in enumerate(grupos.items(), 1):
        regs.sort(
            key=lambda r: (
                int(re.match(r"\d+", str(r[0]["art"])).group(0)) if re.match(r"\d+", str(r[0]["art"])) else 0,
                str(r[0]["art"]),
            )
        )
        diploma = lei.get(f"{sig}:{regs[0][0]['art']}", {}).get("diploma", sig)
        ls_cont.append(f'<h2 class="ls-titulo" id="ls-tit-{gi}">{esc(diploma)}</h2>')
        chips = []
        for k, (Lc, ponto) in enumerate(regs, 1):
            of = lei.get(f"{sig}:{Lc['art']}", {})
            if of.get("baixado_em"):
                baixados.add(of["baixado_em"])
            gid = f"ls-{slug(sig)}-{slug(Lc['art'])}-{k}"
            onde = (
                "Art. "
                + art_rot(Lc["art"])
                + (f", {Lc['par']}" if Lc.get("par") else "")
                + (f", inciso {Lc['inc']}" if Lc.get("inc") else "")
            )
            ls_cont.append(
                f'<div class="ls-art-group" id="{gid}"><div class="ls-art-head"><span class="ls-art-num">{esc(onde)}</span>'
                f'<span class="ls-art-name">{esc(ponto)}</span></div><div class="ls-art-body"><p class="ls-caput">{esc(Lc["texto"].strip())}</p>'
                + (
                    f'<p class="ls-tagnote">texto oficial baixado em {esc(of.get("baixado_em", "?"))} · '
                    f'<a href="{esc(of["url"])}" target="_blank" rel="noopener">'
                    f'{"Legisla Bahia" if of.get("fonte") == "legislabahia" else "Planalto"}</a></p>'
                    if of.get("url")
                    else ""
                )
                + "</div></div>"
            )
            chips.append(
                f'<a href="#{gid}" class="toc-artchip">{esc(art_rot(Lc["art"]) + (" " + Lc["par"] if Lc.get("par") else "") + (" " + Lc["inc"] if Lc.get("inc") else ""))}</a>'
            )
        ls_toc.append(
            f'<details class="toc-group" open><summary>{esc(diploma.split(" — ")[0])}</summary><div class="toc-links">'
            f'<a href="#ls-tit-{gi}" class="toc-lvl1">{esc(diploma)}</a><div class="toc-artlist">{"".join(chips)}</div></div></details>'
        )
    if not ls_cont:
        ls_cont.append('<p class="ls-count">Este módulo não cita lei seca.</p>')

    # sensível a mudança: o declarado no módulo + os artigos com alteração de 2026
    sens = [rico(s) for s in lista(mod.get("sensivel_a_mudanca"))]
    for b in blocos:
        for p in b["pontos"]:
            for Lc in lista(p.get("lei_seca")):
                if lei.get(f"{Lc['lei']}:{Lc['art']}", {}).get("alteracao_2026"):
                    s = f"{esc(rotulo_lei(Lc, lei))}: redação alterada em 2026 (conferir na fonte oficial antes da prova)"
                    if s not in sens:
                        sens.append(s)
    sens_html = (
        ""
        if not sens
        else '<div class="alert alert-update"><div class="alt-label">🆕 Sensível a mudança</div>'
        '<p>Confira estes pontos na fonte oficial antes da prova:</p><ul class="sensivel">'
        + "".join(f"<li>{s}</li>" for s in sens)
        + "</ul></div>"
    )

    n_pontos = len(ordem)
    n_lei = sum(len(v) for v in grupos.values())
    ls_baixado = ("baixado em " + ", ".join(sorted(baixados))) if baixados else "sem lei citada"
    n_juris = sum(len(lista(p.get("jurisprudencia"))) for b in blocos for p in b["pontos"])
    carimbo = (
        f"lei seca: {n_lei} trecho(s) conferido(s) com o texto oficial ({ls_baixado}) · "
        f"jurisprudência: {n_juris} citação(ões) com fonte e data"
    )
    cfg = {
        "pfx": f"rev_pcba_{mod['modulo']}_",
        "modulo": mod["modulo"],
        "dicas": [rico(d) for d in lista(mod.get("dicas"))],
    }
    trocas = {
        "CONFERIDO_EM": esc(mod["conferido_em"]),
        "MODULO": esc(mod["modulo"]),
        "GERADO_EM": dt.datetime.now().strftime("%d/%m/%Y %H:%M"),
        "TITULO_PAGINA": esc("Revisão Delegado PC-BA · " + re.sub("<[^>]+>", "", mod["titulo"])),
        "AVATAR_B64": b64,
        "CSS": css,
        "TITULO": rico(mod["titulo"]),
        "SUBTITULO": rico(mod.get("subtitulo") or mod.get("disciplina") or ""),
        "KICKER": rico(mod.get("disciplina") or mod.get("subtitulo") or "módulo de revisão"),
        "APRESENTACAO": rico(
            mod.get("apresentacao")
            or "Os pontos do edital deste módulo, na ordem de prioridade, no nível de delegado."
        ),
        "CARIMBO_DETALHE": esc(carimbo),
        "N_PONTOS": str(n_pontos),
        "N_FICHAS": str(cont["fichas"]),
        "N_QUESTOES": str(cont["questoes"]),
        "N_LEI": str(n_lei),
        "INDICE_PRIORIDADE": "\n".join(indice),
        "SENSIVEL": sens_html,
        "TOC": toc,
        "BLOCOS": "\n".join(html_blocos),
        "LS_TOC": "\n".join(ls_toc),
        "LS_CONTEUDO": "\n".join(ls_cont),
        "LS_BAIXADO": esc(ls_baixado),
        "CFG_JSON": json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/"),
        "JS": js,
    }
    faltam = [k for k in trocas if "{{" + k + "}}" not in molde]
    if faltam:
        raise SystemExit(f"[FALHA] o molde não tem os marcadores {faltam}")
    out = re.sub(
        r"\{\{([A-Z_0-9]+)\}\}", lambda m: trocas[m.group(1)] if m.group(1) in trocas else m.group(0), molde
    )
    sobra = re.findall(r"\{\{[A-Z_0-9]+\}\}", out.replace(css, "").replace(js, ""))
    if sobra:
        raise SystemExit(f"[FALHA] marcadores sem valor no molde: {sorted(set(sobra))}")
    RP.verificar(out, f"módulo {mod['modulo']}")
    return out, {
        "pontos": n_pontos,
        "fichas": cont["fichas"],
        "questoes": cont["questoes"],
        "lei": n_lei,
        "juris": n_juris,
    }


def avatar_b64(lado=360):
    from PIL import Image

    im = Image.open(AVATAR).convert("RGB")
    w, h = im.size
    im = im.crop((int(w * 0.18), 0, int(w * 0.82), int(h * 0.62)))  # rosto e ombros, como nas apostilas
    im.thumbnail((lado, lado))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=84)
    return base64.b64encode(buf.getvalue()).decode()


def gerar_pdf(html_path, pdf_path):
    nav = next((p for p in NAVEGADORES if p.exists()), None)
    if not nav:
        raise SystemExit("[FALHA] nem Edge nem Chrome encontrados para gerar o PDF")
    if pdf_path.exists():
        pdf_path.unlink()
    r = subprocess.run(
        [
            str(nav),
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--virtual-time-budget=6000",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ],
        capture_output=True,
        text=True,
        timeout=240,
    )
    if not pdf_path.exists() or pdf_path.stat().st_size < 20_000:
        raise SystemExit(f"[FALHA] PDF não gerado: rc={r.returncode} {r.stderr[-400:]}")
    return nav.name


# ------------------------------------------------------------------ autoteste (em memória)
def _fixture():
    itens = {
        "T-1": {
            "id": "T-1",
            "label": "Ponto de teste",
            "priority": "Alta",
            "discipline": "TESTE",
            "number": "1",
        }
    }
    lei = {
        "CP:4": {
            "sigla": "CP",
            "art": "4",
            "diploma": "Código Penal — Decreto-Lei 2.848/1940",
            "texto": "Art. 4º - Considera-se praticado o crime no momento da ação ou\nomissão, ainda que outro seja o momento do resultado.(Redação dada pela Lei nº 7.209, de 1984)",
            "baixado_em": dt.date.today().strftime("%d/%m/%Y"),
            "url": "https://www.planalto.gov.br/",
        }
    }
    sumulas = {
        "SUM-STF-711": {
            "texto": "A lei penal mais grave aplica-se ao crime continuado ou ao crime permanente, se a sua vigência é anterior à cessação da continuidade ou da permanência."
        }
    }
    mod = {
        "esquema": 1,
        "modulo": "teste",
        "titulo": "Teste",
        "conferido_em": dt.date.today().strftime("%d/%m/%Y"),
        "blocos": [
            {
                "titulo": "Bloco",
                "pontos": [
                    {
                        "id": "T-1",
                        "prioridade": {"escore": 5},
                        "o_que_cai": ["Teoria da <b>atividade</b>."],
                        "lei_seca": [
                            {
                                "lei": "CP",
                                "art": "4",
                                "texto": "Considera-se praticado o crime no momento da ação ou omissão, ainda que outro seja o momento do resultado.",
                            }
                        ],
                        "jurisprudencia": [
                            {
                                "tribunal": "STF",
                                "sumula": "STF-711",
                                "fonte": "STF, Súmula 711",
                                "data": "24/09/2003",
                                "texto": "A lei penal mais grave aplica-se ao crime continuado ou ao crime permanente, se a sua vigência é anterior à cessação da continuidade ou da permanência.",
                            }
                        ],
                        "fichas": [{"item": "Item.", "gabarito": "E", "fundamento": "Art. 4º."}],
                        "questoes": [
                            {
                                "enunciado": "Q?",
                                "alternativas": {L: f"alt {L}" for L in "ABCDE"},
                                "gabarito": "B",
                                "comentario": "C.",
                                "origem": "Revisão",
                            }
                        ],
                    }
                ],
            }
        ],
    }
    return mod, itens, lei, sumulas


DEFEITOS = [
    (
        "id inexistente no edital",
        lambda m: m["blocos"][0]["pontos"][0].__setitem__("id", "DBA26-XXX-99"),
        "não existe em assets/items.json",
    ),
    ("ponto sem id", lambda m: m["blocos"][0]["pontos"][0].pop("id"), "ponto sem id do edital"),
    (
        "ficha sem gabarito",
        lambda m: m["blocos"][0]["pontos"][0]["fichas"][0].pop("gabarito"),
        "ficha sem gabarito",
    ),
    ("lei sem artigo", lambda m: m["blocos"][0]["pontos"][0]["lei_seca"][0].pop("art"), "lei sem artigo"),
    ("lei sem chave", lambda m: m["blocos"][0]["pontos"][0]["lei_seca"][0].pop("lei"), "lei sem chave"),
    (
        "lei com texto adulterado",
        lambda m: m["blocos"][0]["pontos"][0]["lei_seca"][0].__setitem__(
            "texto", "Considera-se praticado o crime no momento do resultado."
        ),
        "não confere com o oficial",
    ),
    (
        "juris sem fonte",
        lambda m: m["blocos"][0]["pontos"][0]["jurisprudencia"][0].pop("fonte"),
        "juris sem fonte",
    ),
    (
        "juris sem data",
        lambda m: m["blocos"][0]["pontos"][0]["jurisprudencia"][0].pop("data"),
        "juris sem data",
    ),
    (
        "súmula com texto trocado",
        lambda m: m["blocos"][0]["pontos"][0]["jurisprudencia"][0].__setitem__(
            "texto", "A lei penal mais benéfica aplica-se ao crime continuado."
        ),
        "não confere com assets/sumulas.json",
    ),
    (
        "questão sem gabarito",
        lambda m: m["blocos"][0]["pontos"][0]["questoes"][0].pop("gabarito"),
        "questão sem gabarito",
    ),
    (
        "questão com origem livre",
        lambda m: m["blocos"][0]["pontos"][0]["questoes"][0].__setitem__("origem", "internet"),
        "origem fora do padrão",
    ),
    (
        "HTML proibido",
        lambda m: m["blocos"][0]["pontos"][0]["o_que_cai"].append("<script>alert(1)</script>"),
        "tag <script>",
    ),
]


def autoteste():
    mod, itens, lei, sumulas = _fixture()
    e, _ = validar(mod, itens, lei, sumulas)
    if e:
        print(f"[AUTOTESTE FALHOU] o módulo válido foi reprovado: {e}")
        return 1
    falhas = []
    for rotulo, planta, espera in DEFEITOS:
        m = copy.deepcopy(mod)
        planta(m)
        e, _ = validar(m, itens, lei, sumulas)
        if any(espera in x for x in e):
            print(f"  acusou: {rotulo}")
        else:
            falhas.append(f"{rotulo} (erros: {e})")
    # e a referência proibida no texto final
    m = copy.deepcopy(mod)
    m["blocos"][0]["pontos"][0]["dia_a_dia"] = ["Questão do Projeto em Delta."]
    try:
        montar(m, itens, lei, sumulas, "", [])
    except SystemExit as ex:
        if "referências proibidas" in str(ex):
            print("  acusou: referência proibida no texto final")
        else:
            falhas.append(f"referência proibida: parou por outro motivo ({ex})")
    else:
        falhas.append("referência proibida não acusada")
    if falhas:
        print(f"[AUTOTESTE FALHOU] {falhas}")
        return 1
    print(f"[AUTOTESTE OK] o módulo válido passa e os {len(DEFEITOS) + 1} defeitos plantados foram acusados")
    return 0


# ------------------------------------------------------------------ principal
def opcao(argv, nome, padrao):
    if nome in argv:
        i = argv.index(nome)
        if i + 1 >= len(argv):
            raise SystemExit(2)
        return Path(argv[i + 1])
    return padrao


def main(argv):
    if "--autoteste" in argv:
        return autoteste()
    valores = {"--itens", "--lei", "--sumulas", "--saida"}
    pos, pular = [], False
    for a in argv:
        if pular:
            pular = False
            continue
        if a in valores:
            pular = True
            continue
        if not a.startswith("--"):
            pos.append(a)
    if len(pos) != 1:
        print(__doc__)
        return 2
    alvo = Path(pos[0])
    if alvo.suffix.lower() != ".json":
        alvo = CONTEUDO / f"{pos[0]}.json"
    mod = carregar_json(alvo, "módulo")
    lista_itens = carregar_json(opcao(argv, "--itens", ITENS), "edital verticalizado (items.json)")
    itens = {x["id"]: x for x in lista_itens} if isinstance(lista_itens, list) else lista_itens
    lei = carregar_json(
        opcao(argv, "--lei", LEI), "lei seca oficial (lei_seca_oficial.json; rode atualizar_lei_seca.bat)"
    )
    sumulas = carregar_json(opcao(argv, "--sumulas", SUMULAS), "súmulas (sumulas.json)")
    erros, avisos = validar(mod, itens, lei, sumulas)
    for a in avisos:
        print(f"[AVISO] {a}")
    if erros:
        print(f"[RECUSADO] {alvo.name}: {len(erros)} problema(s)")
        for e in erros:
            print(f"  - {e}")
        return 1
    if "--validar" in argv:
        print(f"[OK] {alvo.name}: módulo válido ({sum(len(b['pontos']) for b in mod['blocos'])} ponto(s))")
        return 0
    saida = opcao(argv, "--saida", SAIDA)
    saida.mkdir(parents=True, exist_ok=True)
    out, c = montar(mod, itens, lei, sumulas, avatar_b64(), avisos)
    h = saida / f"{mod['modulo']}.html"
    h.write_text(out, encoding="utf-8", newline="\n")
    print(
        f"[OK] {mod['modulo']}: {c['pontos']} ponto(s), {c['fichas']} ficha(s) C/E, {c['questoes']} questão(ões) A–E, "
        f"{c['lei']} trecho(s) de lei, {c['juris']} citação(ões) de jurisprudência"
    )
    print(f"     html: {h} ({h.stat().st_size:,} bytes)".replace(",", "."))
    if "--sem-pdf" not in argv:
        pdf = saida / f"{mod['modulo']}.pdf"
        nav = gerar_pdf(h, pdf)
        tam = f"{pdf.stat().st_size:,}".replace(",", ".")
        print(f"     pdf:  {pdf} ({tam} bytes, {nav})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
