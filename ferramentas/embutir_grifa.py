"""Embute a paleta de grifos (assets/grifa.js, fonte única) em todas as telas do Trilha.

10/11/2026, pedido do titular: "sempre que eu apertar G aparece uma paleta de grifos... em todas as telas".

Por que EMBUTIR e não <script src>: o servidor.py só entrega "/" e "/index.html" (o resto responde 403, de
propósito, para nunca servir o .env), e o Treino de Discursiva e os cadernos da Revisão abrem com duplo clique
(file://). Embutido, o mesmo código vale nas três formas de abrir.

Uso:
  python ferramentas/embutir_grifa.py              grava (ou regrava) o bloco em cada tela
  python ferramentas/embutir_grifa.py --conferir   rc 1 se alguma tela do Git não tiver o bloco ou tiver cópia
                                                   diferente da fonte (porta do portão)
  python ferramentas/embutir_grifa.py --autoteste  prova que o --conferir ACUSA (REGRA CINCO)

Telas: index.html, discursiva/Treino_Discursiva.html e revisao/molde/caderno.html (no Git), mais os cadernos já
gerados em revisao/saida/*.html (fora do Git; o gerador os refaz a partir do molde, que já leva o bloco).
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FONTE = RAIZ / "assets" / "grifa.js"
TELAS_GIT = ["index.html", "discursiva/Treino_Discursiva.html", "revisao/molde/caderno.html"]
INICIO = "<!-- grifa:inicio (gerado de assets/grifa.js por ferramentas/embutir_grifa.py; não editar aqui) -->"
FIM = "<!-- grifa:fim -->"


def bloco(js: str) -> str:
    return f"{INICIO}\n<script>\n{js.rstrip()}\n</script>\n{FIM}"


def checar_fonte(js: str) -> str | None:
    if "</script" in js.lower():
        return "a fonte contém '</script' e fecharia a tag embutida"
    if "{{" in js:
        return "a fonte contém '{{', que o gerador da Revisão trataria como marcador do molde"
    return None


def embutir(html: str, js: str) -> str:
    novo = bloco(js)
    i, f = html.find(INICIO), html.find(FIM)
    if i >= 0 and f > i:
        return html[:i] + novo + html[f + len(FIM):]
    p = html.lower().rfind("</body>")
    if p < 0:
        raise ValueError("tela sem </body>")
    return html[:p] + novo + "\n" + html[p:]


def conferir(arquivo: Path, js: str) -> str | None:
    if not arquivo.exists():
        return "arquivo não existe"
    h = arquivo.read_text(encoding="utf-8")
    if h.count(INICIO) != 1 or h.count(FIM) != 1:
        return "sem o bloco da paleta (ou com mais de um)"
    i, f = h.find(INICIO), h.find(FIM) + len(FIM)
    if h[i:f] != bloco(js):
        return "cópia embutida diferente de assets/grifa.js (rode ferramentas/embutir_grifa.py)"
    return None


def _ler(arq: Path) -> str:
    return arq.read_text(encoding="utf-8")


def gravar_todas() -> int:
    js = _ler(FONTE)
    erro = checar_fonte(js)
    if erro:
        print(f"[ X ] {erro}")
        return 1
    alvos = [RAIZ / t for t in TELAS_GIT] + sorted((RAIZ / "revisao" / "saida").glob("*.html"))
    for arq in alvos:
        if not arq.exists():
            print(f"[ X ] {arq.relative_to(RAIZ)}: não existe")
            return 1
        antes = _ler(arq)
        depois = embutir(antes, js)
        if depois != antes:
            arq.write_text(depois, encoding="utf-8", newline="")
        print(f"[OK ] {arq.relative_to(RAIZ).as_posix()}: {'gravado' if depois != antes else 'já estava igual'}")
    return 0


def conferir_todas(raiz: Path = RAIZ) -> int:
    js = _ler(raiz / "assets" / "grifa.js")
    falhas = []
    erro = checar_fonte(js)
    if erro:
        falhas.append(f"assets/grifa.js: {erro}")
    for t in TELAS_GIT:
        e = conferir(raiz / t, js)
        if e:
            falhas.append(f"{t}: {e}")
    for f in falhas:
        print(f"[ X ] {f}")
    if not falhas:
        print(f"[OK ] paleta de grifos igual à fonte nas {len(TELAS_GIT)} telas do Git")
    return 1 if falhas else 0


def autoteste() -> int:
    js = "/* teste */ console.log(1);"
    base = "<!doctype html><html><body><p>x</p></body></html>"
    casos = [
        ("tela sem o bloco", base, True),
        ("tela com cópia antiga", embutir(base, js.replace("1", "2")), True),
        ("tela com dois blocos", embutir(base, js) + bloco(js), True),
        ("tela certa", embutir(base, js), False),
    ]
    ok = True
    with tempfile.TemporaryDirectory() as d:
        raiz = Path(d)
        (raiz / "assets").mkdir()
        (raiz / "assets" / "grifa.js").write_text(js, encoding="utf-8")
        for nome, html, deve_acusar in casos:
            for t in TELAS_GIT:
                p = raiz / t
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(embutir(base, js), encoding="utf-8")
            (raiz / TELAS_GIT[1]).write_text(html, encoding="utf-8")
            print(f"--- caso: {nome}")
            acusou = conferir_todas(raiz) == 1
            certo = acusou == deve_acusar
            ok &= certo
            print(f"  {'✅' if certo else '❌'} {nome}: {'acusou' if acusou else 'passou'}")
        fonte_ruim = "var x = '</scr' + 'ipt>'; /* {{CFG}} */"
        acusou = checar_fonte("</script>") is not None and checar_fonte("{{X}}") is not None
        ok &= acusou and checar_fonte(fonte_ruim.replace("{{CFG}}", "")) is None
        print(f"  {'✅' if acusou else '❌'} fonte com '</script' ou '{{{{' é recusada")
    print("AUTOTESTE " + ("OK: o --conferir acusa os 3 defeitos e passa a tela certa" if ok else "FALHOU"))
    return 0 if ok else 1


if __name__ == "__main__":
    # 10/11/2026: com "python -I" o PYTHONIOENCODING é ignorado e o console do Windows cai no cp1252, que não
    # imprime ✅ — o autoteste morria com UnicodeEncodeError (HARNESS §A7). O script não depende do ambiente.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if "--autoteste" in sys.argv:
        sys.exit(autoteste())
    if "--conferir" in sys.argv:
        sys.exit(conferir_todas())
    sys.exit(gravar_todas())
