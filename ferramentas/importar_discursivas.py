"""Importa o banco de QUESTÕES DISCURSIVAS RESPONDIDAS (Penal e Processual Penal) para a aba "900 Discursivas"
do Treino de Discursiva.

Pedido do titular (14/11/2026): uma aba só para esse material — ler a pergunta, escrever a resposta e conferir
pelo espelho (a resposta modelo do PDF).

- A FONTE é um PDF de terceiro, protegido por senha, que mora SÓ na cópia privada do titular (fora do repositório).
  A senha NÃO fica no código (§F59): vem por argumento --senha ou pela variável de ambiente QD_SENHA.
- A SAÍDA, discursiva/questoes_discursivas_penal.js, é derivada de material de terceiro: entra no .gitignore,
  fica só no disco e NUNCA vai para o Git nem para o link público (D-002/D-025). O gerador do pacote privado
  (gerar_pacote_privado.py) a embute na cópia completa.
- Depende do pdftotext (Poppler), já disponível nesta máquina (no PATH).

Uso:
  python ferramentas/importar_discursivas.py --senha SENHA [--pdf "caminho/do/arquivo.pdf"]
  QD_SENHA=SENHA python ferramentas/importar_discursivas.py
"""
import argparse
import collections
import glob
import json
import os
import re
import shutil
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, "discursiva", "questoes_discursivas_penal.js")
PDF_PADRAO = os.path.join(
    os.path.expanduser("~"), "OneDrive", "Trilha AOCP - versao completa (privada)",
    "_fonte", "900_discursivas.pdf")

NUM = re.compile(r"^(\d+)\s*[–\-]\s+(.*)$")
PARTE = re.compile(r"^PARTE\s+\d+\s*[–\-]\s*(.+)$")
TEMA = re.compile(r"^TEMA\s+\d+\s*[–\-]\s*(.+)$")


def candidatos_pdftotext(override):
    """Lista os pdftotext a tentar. O do PATH pode ser o Xpdf, que recusa a senha deste PDF;
    o Poppler (winget) a aceita — por isso procuramos o Poppler por glob (sem fixar a versão)."""
    cs = []
    if override:
        cs.append(override)
    if os.environ.get("QD_PDFTOTEXT"):
        cs.append(os.environ["QD_PDFTOTEXT"])
    cs += glob.glob(os.path.join(os.path.expanduser("~"), "AppData", "Local", "Microsoft",
                    "WinGet", "Packages", "*Poppler*", "poppler-*", "Library", "bin", "pdftotext.exe"))
    if shutil.which("pdftotext"):
        cs.append(shutil.which("pdftotext"))
    return cs


def extrair_texto(pdf, senha, override=None):
    """Tenta cada pdftotext com a senha de usuário até um decifrar; devolve o texto em UTF-8."""
    cands = candidatos_pdftotext(override)
    if not cands:
        raise SystemExit("❌ pdftotext não encontrado (instale o Poppler ou passe --pdftotext).")
    ultimo = ""
    for exe in cands:
        try:
            r = subprocess.run([exe, "-upw", senha, "-enc", "UTF-8", pdf, "-"], capture_output=True)
        except OSError:
            continue
        if r.returncode == 0 and r.stdout:
            return r.stdout.decode("utf-8", "ignore")
        ultimo = r.stderr.decode("utf-8", "ignore")[:200]
    raise SystemExit("❌ nenhum pdftotext decifrou o PDF (senha errada ou PDF ausente): " + ultimo)


def paragrafos(linhas):
    saida, atual = [], []
    for ln in linhas:
        if ln.strip() == "":
            if atual:
                saida.append(re.sub(r"\s+", " ", " ".join(atual)).strip())
                atual = []
        else:
            atual.append(ln.strip())
    if atual:
        saida.append(re.sub(r"\s+", " ", " ".join(atual)).strip())
    return [p for p in saida if p]


def parsear(texto):
    # tira a marca d'água de licença (repetida em toda página) e começa na Parte 1
    linhas = [ln for ln in texto.split("\n") if "marcianolima" not in ln]
    txt = "\n".join(linhas)
    txt = txt[txt.find("PARTE 1 "):]
    raw = txt.split("\n")

    # 1) acha os inícios REAIS de questão: numeração sequencial por escopo
    #    (Parte 1, Parte 2 e cada TEMA da Parte 3 reiniciam em 1); tolera salto de até +2,
    #    rejeita retrocesso (listas internas) e salto enorme (número de acórdão).
    parte = tema = ""
    esperado = 1
    marcas = []
    for i, ln in enumerate(raw):
        if PARTE.match(ln):
            parte, tema, esperado = ln.strip(), "", 1
            continue
        if TEMA.match(ln):
            tema, esperado = ln.strip(), 1
            continue
        if ln.startswith("QUESTÃO INÉDITA"):
            marcas.append((i, parte, tema, ln.split("–", 1)[-1].split("-", 1)[-1].strip()))
            continue
        m = NUM.match(ln)
        if m:
            n = int(m.group(1))
            if esperado <= n <= esperado + 2:
                marcas.append((i, parte, tema, m.group(2).strip()))
                esperado = n + 1

    # 2) de cada início até o próximo, separa pergunta (até o 1º "?"; sem "?", até o 1º ".") do espelho
    idx = [mk[0] for mk in marcas]
    qs = []
    for j, (li, parte, tema, first) in enumerate(marcas):
        fim = idx[j + 1] if j + 1 < len(idx) else len(raw)
        ps = paragrafos([first] + raw[li + 1:fim])
        if not ps:
            continue
        full = " ␟ ".join(ps)  # marcador de parágrafo
        qm = full.find("?")
        if 0 <= qm <= 700:
            corte = qm + 1
        else:
            dm = re.search(r"\.(\s|␟|$)", full[:700])
            corte = (dm.end() - len(dm.group(1))) if dm else (full.find("␟") + 1)
            if corte <= 0:
                corte = len(ps[0])
        perg = re.sub(r"\s+", " ", full[:corte].replace("␟", " ")).strip()
        esp = [re.sub(r"\s+", " ", p).strip() for p in full[corte:].split("␟")]
        esp = [p for p in esp if p]
        qs.append({
            "p": re.sub(r"^PARTE\s+\d+\s*[–\-]\s*", "", parte).strip(),
            "t": re.sub(r"^TEMA\s+\d+\s*[–\-]\s*", "", tema).strip(),
            "q": perg, "e": esp})
    return qs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--senha", default=os.environ.get("QD_SENHA"))
    ap.add_argument("--pdf", default=PDF_PADRAO)
    ap.add_argument("--pdftotext", default=None, help="caminho de um pdftotext específico (Poppler)")
    a = ap.parse_args()
    if not a.senha:
        raise SystemExit("❌ informe a senha do PDF em --senha ou na variável QD_SENHA (não fica no código, §F59).")
    if not os.path.isfile(a.pdf):
        raise SystemExit("❌ PDF não encontrado: " + a.pdf)

    qs = parsear(extrair_texto(a.pdf, a.senha, a.pdftotext))
    vazias = sum(1 for o in qs if not o["e"])
    cab = ("/* Material de terceiro (Questões Discursivas Respondidas — Penal e Processual Penal).\n"
           "   Uso pessoal do titular (D-002/D-025): FORA do Git e do link público; entra só na cópia privada.\n"
           "   Gerado por ferramentas/importar_discursivas.py a partir do PDF (senha do titular). "
           + str(len(qs)) + " questões. */\n")
    with open(SAIDA, "w", encoding="utf-8", newline="\n") as f:
        f.write(cab + "window.QD_PENAL=" + json.dumps(qs, ensure_ascii=False, separators=(",", ":")) + ";\n")
    kb = os.path.getsize(SAIDA) / 1024
    por = collections.Counter(o["p"] for o in qs)
    print(f"[OK ] {len(qs)} questões, {kb:,.1f} KB · por parte: {dict(por)} · espelhos vazios: {vazias}")
    if vazias:
        print("      ⚠️ há questões sem espelho — conferir o PDF.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
