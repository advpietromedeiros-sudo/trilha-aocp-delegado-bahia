"""Empacota o Treino de Discursiva num único .html que funciona offline, com dois cliques.

Pedido do titular (04/11/2026): um arquivo para enviar a um colega, funcionando tudo localmente.
Envio autorizado pelo titular nessa data (opção 1; ver docs/PROCEDENCIA.md).

Embute os scripts locais de discursiva/ no HTML. Para se algum <script src> não for achado, se sobrar
algum script externo ou se algum script contiver "</script", que fecharia a tag antes da hora.

Uso: python -I ferramentas/empacotar_discursiva.py [arquivo-de-saída]
"""

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "discursiva"
SAIDA_PADRAO = RAIZ / ".scratch" / "Treino_Discursiva_Delegado_PCBA.html"


def empacotar() -> str:
    html = (PASTA / "Treino_Discursiva.html").read_text(encoding="utf-8")
    # material de terceiro só local (data-local, D-017): NUNCA vai no arquivo de envio
    html, n_local = re.subn(r'<script src="[^"]+" data-local="[^"]*"></script>\n?', "", html)
    if n_local:
        print(f"retirado(s) do envio: {n_local} script(s) de uso local (material de terceiro)")
    tags = re.findall(r'<script src="([^"]+)"></script>', html)
    if not tags:
        sys.exit("ERRO: nenhum <script src> achado; o HTML mudou de formato")
    for nome in tags:
        arq = PASTA / nome
        if not arq.is_file():
            sys.exit(f"ERRO: script {nome} não existe em discursiva/")
        js = arq.read_text(encoding="utf-8")
        if "</script" in js.lower():
            sys.exit(f"ERRO: {nome} contém </script e quebraria o arquivo único")
        tag = f'<script src="{nome}"></script>'
        if html.count(tag) != 1:
            sys.exit(f"ERRO: a tag de {nome} aparece {html.count(tag)} vezes; esperava 1")
        html = html.replace(tag, f"<script>/* {nome} */\n{js}\n</script>")
    if re.search(r"<script[^>]+src=|<link[^>]+href=", html):
        sys.exit("ERRO: sobrou script ou estilo externo")
    return html


def main() -> None:
    saida = Path(sys.argv[1]) if len(sys.argv) > 1 else SAIDA_PADRAO
    saida.parent.mkdir(parents=True, exist_ok=True)
    texto = empacotar()
    saida.write_text(texto, encoding="utf-8", newline="\n")
    tam = f"{saida.stat().st_size:,}".replace(",", ".")
    print(f"gerado: {saida} · {tam} bytes")


if __name__ == "__main__":
    main()
