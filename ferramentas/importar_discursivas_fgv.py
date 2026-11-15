"""Importa o e-book "Questões Discursivas e Peças Práticas — Delegado de Polícia — Banca FGV" para a aba
"PED — FGV" do Treino de Discursiva.

Pedido do titular (15/11/2026): uma aba só para esse material — ler o enunciado, escrever a resposta (ou a peça) e
conferir pelo espelho (sugestão de resposta, gabarito da banca e jurisprudência relacionada).

- A FONTE é um PDF de terceiro, protegido por senha, que mora SÓ na cópia privada do titular (fora do repositório).
  A senha NÃO fica no código (§F59): vem por --senha ou pela variável QD_SENHA.
- A SAÍDA, discursiva/questoes_fgv_ped.js, é derivada de material de terceiro: entra no .gitignore, fica só no disco
  e NUNCA vai para o Git nem para o link público (D-002/D-025). O gerador do pacote privado a embute na cópia completa.
- Depende do pdftotext do Poppler (o do PATH pode ser o Xpdf, que recusa a senha deste PDF).

Uso:
  python ferramentas/importar_discursivas_fgv.py --senha SENHA [--pdf "caminho.pdf"]
  QD_SENHA=SENHA python ferramentas/importar_discursivas_fgv.py
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
SAIDA = os.path.join(RAIZ, "discursiva", "questoes_fgv_ped.js")
PDF_PADRAO = os.path.join(
    os.path.expanduser("~"), "OneDrive", "Trilha AOCP - versao completa (privada)",
    "_fonte", "PED_novo.pdf")

DISCIPLINAS = ["DIREITO CONSTITUCIONAL", "DIREITO ADMINISTRATIVO", "DIREITO TRIBUTÁRIO",
               "DIREITO PENAL", "DIREITO PROCESSUAL PENAL", "PEÇAS PRÁTICAS"]


def candidatos_pdftotext(override):
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


def e_prova(s):
    return bool(re.search(r"ANO:\s*\d{4}|DELEGADO DE POL[IÍ]CIA.*(FGV|UFPR|\d{4})", s))


def e_disc(s):
    return s.strip() in DISCIPLINAS


def e_ans(s):
    return s.strip().startswith(("SUGESTÃO DE RESPOSTA", "GABARITO DA BANCA", "JURISPRUDÊNCIA RELACIONADA"))


def rotulo_ans(s):
    s = s.strip()
    if s.startswith("SUGESTÃO"):
        return "SUGESTÃO DE RESPOSTA"
    if s.startswith("GABARITO"):
        return "GABARITO DA BANCA EXAMINADORA"
    return "JURISPRUDÊNCIA RELACIONADA"


def e_topico(s):
    s = s.strip()
    if not s or e_disc(s) or e_prova(s) or e_ans(s) or s.startswith("PEÇA PRÁTICA"):
        return False
    return (bool(re.match(r"^[A-ZÀ-Ú0-9][A-ZÀ-Ú0-9ÇÃÕÉÊÍÓÚÂÁ ,/\(\)\-–]{3,55}$", s))
            and not s.endswith(".") and len(s) <= 55)


def paragrafos(ls):
    ls = [l for l in ls if not re.match(r"^\s*\d{1,3}\s*$", l)]  # tira números de página
    out, cur = [], []
    for l in ls:
        if l.strip() == "":
            if cur:
                out.append(re.sub(r"\s+", " ", " ".join(cur)).strip())
                cur = []
        else:
            cur.append(l.strip())
    if cur:
        out.append(re.sub(r"\s+", " ", " ".join(cur)).strip())
    return [p for p in out if p]


def parsear(texto):
    # tira a marca d'água (site, "E-book comprado por ..." e a linha do CPF) e começa no corpo
    raw = [ln for ln in texto.split("\n")
           if "questoesdiscursivas" not in ln and "E-book comprado" not in ln and "CPF:" not in ln]
    try:
        ini = next(i for i, l in enumerate(raw) if l.strip() == "DIREITO CONSTITUCIONAL")
    except StopIteration:
        raise SystemExit("❌ não achei o início do corpo (DIREITO CONSTITUCIONAL).")
    body = raw[ini:]

    itens = []
    disc = topico = prova = ""
    enun, esp, fase = [], [], "pre"

    def flush():
        nonlocal enun, esp
        q = paragrafos(enun)
        if q and esp:
            espp = []
            for rot, ls in esp:
                txts = paragrafos(ls)
                if txts:
                    espp.append("【" + rot + "】")
                    espp += txts
            if espp:
                itens.append({"p": disc, "t": topico, "prova": prova, "q": " ".join(q), "e": espp})
        enun, esp = [], []

    for s in body:
        st = s.strip()
        if e_disc(st):
            flush(); disc = st; topico = ""; prova = ""; fase = "pre"; continue
        if e_prova(st):
            if esp:
                flush()
            prova = st; fase = "pre"; continue
        if st.startswith("PEÇA PRÁTICA"):
            if esp:
                flush()
            fase = "enun"; enun = [s]; continue
        if e_topico(st):
            if esp:
                flush()
            topico = st; fase = "pre"; continue
        if e_ans(st):
            esp.append((rotulo_ans(st), [])); fase = "esp"; continue
        if fase in ("pre", "enun"):
            fase = "enun"; enun.append(s)
        elif fase == "esp":
            esp[-1][1].append(s)
    flush()
    return itens


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

    itens = parsear(extrair_texto(a.pdf, a.senha, a.pdftotext))
    cab = ('/* Material de terceiro: "Questões Discursivas e Peças Práticas — Delegado de Polícia — Banca FGV".\n'
           "   Uso pessoal do titular (D-002/D-025): FORA do Git e do link público; entra só na cópia privada.\n"
           "   Gerado por ferramentas/importar_discursivas_fgv.py a partir do PDF (senha do titular). "
           + str(len(itens)) + " itens (questões + peças). */\n")
    with open(SAIDA, "w", encoding="utf-8", newline="\n") as f:
        f.write(cab + "window.QD_FGV=" + json.dumps(itens, ensure_ascii=False, separators=(",", ":")) + ";\n")
    kb = os.path.getsize(SAIDA) / 1024
    por = collections.Counter(o["p"] for o in itens)
    vazios = sum(1 for o in itens if not o["q"] or not o["e"])
    print(f"[OK ] {len(itens)} itens, {kb:,.1f} KB · por disciplina: {dict(por)} · incompletos: {vazios}")
    return 0 if not vazios else 1


if __name__ == "__main__":
    sys.exit(main())
