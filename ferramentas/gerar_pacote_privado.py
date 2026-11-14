"""Gera a versão COMPLETA e PRIVADA do Treino de Discursiva e do Olho de Águia, cada tela num arquivo único.

Pedido do titular (14/11/2026, 10h57): manter o link público (sem material de terceiro) e criar, à parte, uma cópia
privada com tudo, para estudar fora desta máquina (opção 1: pasta pessoal na nuvem).

- Cada <script src="..."> local é embutido no próprio HTML, então a tela abre sozinha (sem os .js ao lado), inclusive
  baixada no celular. Os dados de terceiro (simulados_delta.js, revisao_nfpss.js, olho_aguia_*.js) entram AQUI e
  em nenhum outro lugar: a saída fica FORA do repositório e NUNCA vai para o Git nem para o link público (D-002, D-025).
- Uso: python ferramentas/gerar_pacote_privado.py ["pasta de saída"]
       padrão: C:/Users/advpi/OneDrive/Trilha AOCP - versao completa (privada)
       python ferramentas/gerar_pacote_privado.py --autoteste
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISC = os.path.join(RAIZ, "discursiva")
TELAS = ["Treino_Discursiva.html", "Olho_de_Aguia.html"]
SAIDA_PADRAO = os.path.join(os.path.expanduser("~"), "OneDrive", "Trilha AOCP - versao completa (privada)")
TAG = re.compile(r'<script\s+src="([^"]+)"[^>]*>\s*</script>', re.I)


def embutir(html, base):
    faltam, feitos = [], []

    def troca(m):
        src = m.group(1)
        if re.match(r"^(https?:)?//", src):
            return m.group(0)
        cam = os.path.normpath(os.path.join(base, src))
        if not os.path.isfile(cam):
            faltam.append(src)
            return m.group(0)
        js = io.open(cam, encoding="utf-8").read()
        js = re.sub(r"</(script)", r"<\\/\1", js, flags=re.I)  # não fecha a tag antes da hora
        feitos.append(src)
        return "<script>/* embutido de " + src + " */\n" + js + "\n</script>"

    return TAG.sub(troca, html), feitos, faltam


def gerar(saida):
    if os.path.commonpath([os.path.abspath(saida), RAIZ]) == RAIZ:
        print("❌ a saída não pode ficar dentro do repositório (iria parar no Git)")
        return 1
    os.makedirs(saida, exist_ok=True)
    rc = 0
    for tela in TELAS:
        html = io.open(os.path.join(DISC, tela), encoding="utf-8").read()
        novo, feitos, faltam = embutir(html, DISC)
        destino = os.path.join(saida, tela)
        io.open(destino, "w", encoding="utf-8", newline="\n").write(novo)
        kb = os.path.getsize(destino) / 1024
        tam = f"{kb:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"[{'OK ' if not faltam else 'ERR'}] {tela}: {len(feitos)} arquivo(s) embutido(s), {tam} KB")
        if faltam:
            print("      faltam no disco: " + ", ".join(faltam))
            rc = 1
    io.open(os.path.join(saida, "LEIA-ME.txt"), "w", encoding="utf-8").write(
        "Trilha AOCP - versao COMPLETA e PRIVADA (com Simulados, Revisao e Olho de Aguia).\n"
        "NAO compartilhe esta pasta: contem material de curso de terceiro, para estudo pessoal.\n"
        "Abra Treino_Discursiva.html ou Olho_de_Aguia.html no navegador (Chrome ou Edge).\n"
        "No celular: baixe o arquivo pelo app do OneDrive e abra no navegador.\n"
        "Os grifos e o progresso ficam salvos no navegador em que voce abrir.\n"
        "Gerado por ferramentas/gerar_pacote_privado.py.\n")
    return rc


def autoteste():
    html = '<p>x</p><script src="a.js"></script><script src="https://cdn/x.js"></script><script src="nao.js" data-o="1"></script>'
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        io.open(os.path.join(d, "a.js"), "w", encoding="utf-8").write('var s="</script>";')
        novo, feitos, faltam = embutir(html, d)
    ok = (feitos == ["a.js"] and faltam == ["nao.js"] and '<\\/script>' in novo and 'src="https://cdn/x.js"' in novo
          and 'src="a.js"' not in novo)
    dentro = gerar(os.path.join(RAIZ, ".scratch", "nao_pode")) == 1
    print("AUTOTESTE " + ("OK" if ok and dentro else "FALHOU") + ": embute local, preserva CDN, acusa ausente, escapa </script>, recusa saída no repositório")
    return 0 if ok and dentro else 1


if __name__ == "__main__":
    if "--autoteste" in sys.argv:
        sys.exit(autoteste())
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sys.exit(gerar(args[0] if args else SAIDA_PADRAO))
