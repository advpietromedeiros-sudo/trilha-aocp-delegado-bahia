#!/usr/bin/env python3
"""Extrai as questões das provas AOCP (cadernos exportados do QConcursos) para revisao/dados/ (FORA do Git, D-018).

Uso:  python ferramentas/extrair_provas_aocp.py [pasta_dos_pdfs]      (padrão: ~/Downloads, arquivos "AOCP*.pdf")
      python ferramentas/extrair_provas_aocp.py --autoteste

O que se mediu nos PDFs (06/11/2026) e decidiu o método:
  * o texto comum (alternativas, cabeçalho "Q1234567 > Disciplina > assunto", linha da prova) sai como texto;
  * o NEGRITO (enunciado, número da questão, letra das alternativas e o gabarito "Respostas") é desenhado como
    vetor — não há texto a extrair. Por isso cada página é lida pelo OCR do próprio Windows (Windows.Media.Ocr,
    idioma pt-BR), sem instalar nada e sem API externa; o resultado do OCR fica guardado (cache) por página;
  * as ligaduras (fi, fl, ffi) vêm como caracteres de controle com código que muda de fonte para fonte: o texto das
    alternativas também se toma do OCR, que as lê certo; o texto bruto do PDF fica guardado como está (§F30).
Saídas (todas em revisao/dados/, no .gitignore):
  questoes_aocp.json            uma entrada por questão
  provas_texto/<prova>.txt      texto bruto do PDF + OCR, página a página
  ocr/<prova>/pNN.json          cache do OCR (linhas com caixa em pontos do PDF)
Sai 1 se alguma prova não fechar a contagem achadas × gabarito (§D7).
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unicodedata
import warnings
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "revisao" / "dados"
ESCALA = 3  # renderização 216 dpi: OCR estável no corpo 8-9 pt dos cadernos

_PS_OCR = r"""param([string]$Lista)
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$g = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]
function Await($t, $tipo) { $n = $g.MakeGenericMethod($tipo).Invoke($null, @($t)); $n.Wait(-1) | Out-Null; $n.Result }
[Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime] | Out-Null
[Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics, ContentType = WindowsRuntime] | Out-Null
[Windows.Globalization.Language, Windows.Globalization, ContentType = WindowsRuntime] | Out-Null
$motor = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language]::new('pt-BR'))
if ($null -eq $motor) { Write-Error 'OCR pt-BR do Windows indisponivel'; exit 3 }
foreach ($par in [IO.File]::ReadAllLines($Lista, [Text.Encoding]::UTF8)) {
    if (-not $par) { continue }
    $png, $saida = $par -split "`t"
    $f = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($png)) ([Windows.Storage.StorageFile])
    $s = Await ($f.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
    $dec = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($s)) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bmp = Await ($dec.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $r = Await ($motor.RecognizeAsync($bmp)) ([Windows.Media.Ocr.OcrResult])
    $linhas = foreach ($l in $r.Lines) {
        $ws = @($l.Words)
        $x0 = ($ws | ForEach-Object { $_.BoundingRect.X } | Measure-Object -Minimum).Minimum
        $y0 = ($ws | ForEach-Object { $_.BoundingRect.Y } | Measure-Object -Minimum).Minimum
        $x1 = ($ws | ForEach-Object { $_.BoundingRect.X + $_.BoundingRect.Width } | Measure-Object -Maximum).Maximum
        $y1 = ($ws | ForEach-Object { $_.BoundingRect.Y + $_.BoundingRect.Height } | Measure-Object -Maximum).Maximum
        [pscustomobject]@{ t = $l.Text; b = @($x0, $y0, $x1, $y1) }
    }
    $s.Dispose()
    [IO.File]::WriteAllText($saida, (ConvertTo-Json -InputObject @($linhas) -Depth 4 -Compress), (New-Object Text.UTF8Encoding($false)))
}
"""


def slug(nome: str) -> str:
    s = unicodedata.normalize("NFKD", Path(nome).stem).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")


def ocr_paginas(doc, pasta: Path) -> list[list[dict]]:
    """OCR de todas as páginas (com cache). Caixas convertidas para pontos do PDF."""
    import pymupdf

    pasta.mkdir(parents=True, exist_ok=True)
    faltam = []
    for i, pg in enumerate(doc):
        js = pasta / f"p{i + 1:02d}.json"
        if not js.exists():
            png = pasta / f"p{i + 1:02d}.png"
            pg.get_pixmap(matrix=pymupdf.Matrix(ESCALA, ESCALA)).save(str(png))
            faltam.append((png, js))
    if faltam:
        lista = pasta / "_lista.txt"
        lista.write_text("\n".join(f"{p}\t{j}" for p, j in faltam), encoding="utf-8")
        ps1 = DADOS / "ocr" / "_ocr_windows.ps1"
        ps1.write_text(_PS_OCR, encoding="utf-8-sig")
        r = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(ps1),
                            "-Lista", str(lista)], capture_output=True, text=True)
        for p, _ in faltam:
            p.unlink(missing_ok=True)
        lista.unlink(missing_ok=True)
        if r.returncode != 0 or any(not j.exists() for _, j in faltam):
            raise RuntimeError(f"OCR falhou (rc {r.returncode}): {r.stderr[-600:]}")
    out = []
    for i in range(doc.page_count):
        linhas = json.loads((pasta / f"p{i + 1:02d}.json").read_text(encoding="utf-8")) or []
        out.append([{"t": ln["t"], "b": [v / ESCALA for v in ln["b"]]} for ln in linhas])
    return out


RX_ID = re.compile(r"^Q(\d{5,9})\s*$")
RX_PROVA = re.compile(r"^(?P<banca>.+?)\s+-\s+(?P<ano>\d{4})\s+-\s+(?P<orgao>.+?)\s+-\s+(?P<cargo>.+)$")
RX_GAB = re.compile(r"(\d{1,3})\s*[:;]\s*([A-Ea-e])\b")


def limpar(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip()


def _sem_acento(s: str) -> str:
    return unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()


LIGADURAS = ("fi", "fl", "ff", "ffi", "ffl")


def resolver_ligaduras(texto: str, referencia: str) -> tuple[str, int]:
    """Troca o caractere de controle da ligadura pela forma que aparece no OCR da mesma página.

    O código da ligadura muda de fonte para fonte (\\x01 é 'fi' numa e 'ffi' noutra), então não há tabela fixa:
    a palavra candidata que existir no OCR vence; sem nenhuma, fica 'fi' (a mais frequente) e conta como dúvida.
    """
    ref = set(re.findall(r"\w+", _sem_acento(referencia)))
    duvidas = 0

    def troca(m: re.Match) -> str:
        nonlocal duvidas
        palavra = m.group(0)
        for lig in LIGADURAS:
            cand = re.sub(r"[\x01-\x08]", lig, palavra)
            if _sem_acento(cand) in ref:
                return cand
        duvidas += 1
        return re.sub(r"[\x01-\x08]", "fi", palavra)

    return re.sub(r"\w*[\x01-\x08][\w\x01-\x08]*", troca, texto), duvidas


def assinatura(d) -> str:
    """Forma do glifo vetorial: a sequência de operações do caminho (l = reta, c = curva)."""
    return "".join(i[0] for i in d["items"])


CALIB_GLOBAL: dict[str, str] = {}


def _texto_bloco(b) -> str:
    # spans da mesma linha se juntam SEM espaço: a ligadura vem num span próprio ("tipi" + "\x02" + "cada")
    return " ".join("".join(s["text"] for s in ln["spans"]).strip() for ln in b["lines"])


def extrair_prova(pdf: Path) -> tuple[dict, list[dict], str]:
    import pymupdf

    doc = pymupdf.open(str(pdf))
    nome = slug(pdf.name)
    ocr = ocr_paginas(doc, DADOS / "ocr" / nome)
    bruto, metas, alts, numeros_gab, glifos_gab = [], [], [], [], []
    for pi, pg in enumerate(doc):
        txt = pg.get_text()
        bruto.append(f"===== página {pi + 1} — texto do PDF =====\n{txt}\n===== página {pi + 1} — OCR =====\n"
                     + "\n".join(ln["t"] for ln in ocr[pi]))
        dic = pg.get_text("dict")["blocks"]
        blocos = [b for b in dic if b["type"] == 0]
        desenhos = pg.get_drawings()
        circulos = [d["rect"] for d in desenhos
                    if d["rect"].x0 < 3 and 10 <= d["rect"].width <= 14 and 10 <= d["rect"].height <= 14]
        # letra dentro de cada círculo: glifo vetorial pequeno no miolo do círculo
        miolos = [(c, [d for d in desenhos if c.x0 < d["rect"].x0 and d["rect"].x1 < c.x1 and d["rect"].width < 8
                       and c.y0 < d["rect"].y0 and d["rect"].y1 < c.y1]) for c in circulos]
        for b in blocos:
            linhas = [" ".join(s["text"] for s in ln["spans"]).strip() for ln in b["lines"]]
            m = RX_ID.match(linhas[0]) if linhas else None
            if m:
                resto = [x for x in linhas[1:] if x != ">"]
                if not resto:  # assunto longo: o id fica num bloco e "> Disciplina / assunto" em blocos à direita
                    viz = sorted((v for v in blocos if 70 <= v["bbox"][0] <= 130
                                  and b["bbox"][1] - 10 <= v["bbox"][1] <= b["bbox"][1] + 25), key=lambda v: v["bbox"][1])
                    resto = [x for v in viz for x in ("".join(s["text"] for s in ln["spans"]).strip()
                                                      for ln in v["lines"]) if x and x != ">"]
                    resto = [re.sub(r"^>\s*", "", x) for x in resto]
                metas.append({"pag": pi, "y": b["bbox"][1], "id": "Q" + m.group(1),
                              "disc_qc": resto[0] if resto else None,
                              "assunto_qc": " ".join(resto[1:]) or None, "bbox": b["bbox"]})
            elif b["bbox"][0] >= 18:
                cy0, cy1 = b["bbox"][1], b["bbox"][3]
                dentro = [(c, g) for c, g in miolos if cy0 - 2 <= (c.y0 + c.y1) / 2 <= cy1 + 2]
                if dentro:
                    alts.append({"pag": pi, "y": cy0, "bbox": b["bbox"], "texto": _texto_bloco(b),
                                 "glifo": assinatura(dentro[0][1][0]) if dentro[0][1] else None})
        ref_pag = "\n".join(ln["t"] for ln in ocr[pi])
        for b in blocos:
            linhas = ["".join(s["text"] for s in ln["spans"]).strip() for ln in b["lines"]]
            # bloco cinza "2022 | INSTITUTO AOCP | PC-GO": ano, banca e órgão, sempre em 3 linhas
            if b["bbox"][0] < 30 and len(linhas) == 3 and re.fullmatch(r"\d{4}", linhas[0]):
                for mt in metas:
                    if mt["pag"] == pi and 0 < b["bbox"][1] - mt["bbox"][1] < 40 and "ano" not in mt:
                        mt["ano"], mt["banca"] = int(linhas[0]), linhas[1]
                        mt["orgao"] = resolver_ligaduras(linhas[2], ref_pag)[0]
                        break
            # linha da prova, ao lado do "Ano:" — se o órgão é longo, continua num bloco logo abaixo, à esquerda
            linha = _texto_bloco(b)
            if b["bbox"][0] > 150 and linha.startswith("INSTITUTO"):
                cont = [v for v in blocos if v["bbox"][0] < 30 and 0 <= v["bbox"][1] - b["bbox"][3] <= 12
                        and not re.match(r"^\d{4}$", _texto_bloco(v))]
                linha = resolver_ligaduras(linha, ref_pag)[0]
                for mt in metas:
                    if mt["pag"] == pi and 0 < b["bbox"][1] - mt["bbox"][1] < 40 and "prova" not in mt:
                        mt["prova"] = linha
                        mt["cab_fim"] = b["bbox"][3]  # fim do cabeçalho: o enunciado começa abaixo
                        mt["cont_fim"] = cont[0]["bbox"][3] if cont else None
                        # candidata a continuação: só se usa se a linha não trouxer o órgão inteiro (ver montagem)
                        mt["prova_cont"] = resolver_ligaduras(_texto_bloco(cont[0]), ref_pag)[0] if cont else None
                        break
        # gabarito: cada "N:" do texto do PDF + o glifo vetorial logo à direita (a letra, em negrito)
        for b in blocos:
            for ln in b["lines"]:
                for s in ln["spans"]:
                    mm = re.match(r"^\s*(\d{1,3}):\s*$", s["text"])
                    if not mm:
                        continue
                    bb = s["bbox"]
                    perto = [d for d in desenhos if bb[2] - 1 <= d["rect"].x0 <= bb[2] + 12
                             and abs((d["rect"].y0 + d["rect"].y1) / 2 - (bb[1] + bb[3]) / 2) < 6]
                    numeros_gab.append(int(mm.group(1)))
                    glifos_gab.append(assinatura(perto[0]) if perto else None)
    metas.sort(key=lambda m: (m["pag"], m["y"]))
    for mt in metas:  # reserva pelo OCR do cabeçalho: "Q123 Disciplina > assunto" e "Ano: ... Prova: ..."
        perto = sorted((ln for ln in ocr[mt["pag"]] if -12 <= ln["b"][1] - mt["y"] <= 40), key=lambda x: x["b"][1])
        disc_ruim = not mt["disc_qc"] or "," in mt["disc_qc"] or len(mt["disc_qc"]) > 45 or "\x02" in mt["disc_qc"]
        for ln in perto:
            t = ln["t"]
            if disc_ruim and re.search(r"Q[l1I]?\s?\d{5,}", t) and ">" in t:
                cab = re.split(r"Q[l1I]?\s?\d{5,}\s*", t, maxsplit=1)[-1]
                mt["disc_qc"], _, mt["assunto_qc"] = (x.strip() for x in cab.partition(">"))
                mt["disc_fonte"] = "ocr"
                disc_ruim = False
            if "prova" not in mt and "Prova:" in t:
                mt["prova"] = t.split("Prova:", 1)[1].strip()
                mt["prova_fonte"] = "ocr"
    referencia =["\n".join(ln["t"] for ln in pag) for pag in ocr]

    def chave(pag, y):
        return pag * 10000 + y

    # calibração das letras pelos círculos: o k-ésimo círculo de cada questão é a letra "ABCDE"[k]
    calib: dict[str, set] = {}
    for k, mt in enumerate(metas):
        ini = chave(mt["pag"], mt["y"])
        fim = chave(metas[k + 1]["pag"], metas[k + 1]["y"]) if k + 1 < len(metas) else 10 ** 9
        mins = sorted((a for a in alts if ini < chave(a["pag"], a["y"]) < fim), key=lambda a: chave(a["pag"], a["y"]))
        for i, a in enumerate(mins[:5]):
            if a["glifo"]:
                calib.setdefault(a["glifo"], set()).add("ABCDE"[i])
    letra_de = {g: next(iter(s)) for g, s in calib.items() if len(s) == 1}
    # reserva: a forma do glifo é a mesma em todos os cadernos (mesma fonte); o que este não calibrou vem dos outros
    for g, letra in CALIB_GLOBAL.items():
        if letra not in letra_de.values():
            letra_de.setdefault(g, letra)
    CALIB_GLOBAL.update({g: v for g, v in letra_de.items() if g not in CALIB_GLOBAL})
    gab_vetor = {n: letra_de.get(g) if g else None for n, g in zip(numeros_gab, glifos_gab, strict=True)}
    # conferência: o OCR da lista "Respostas"
    gab_ocr, vendo = {}, False
    for pi in range(doc.page_count):
        for ln in sorted(ocr[pi], key=lambda x: (x["b"][1], x["b"][0])):
            if ln["t"].strip().lower().startswith("respostas"):
                vendo = True
                continue
            if vendo:
                for n, letra in RX_GAB.findall(ln["t"]):
                    gab_ocr.setdefault(int(n), letra.upper())
    ordem_gab = sorted(set(numeros_gab))  # numeração contínua do caderno (ex.: 21..40)

    questoes, duvidas_lig = [], 0
    for k, mt in enumerate(metas):
        ini = chave(mt["pag"], mt["y"])
        fim = chave(metas[k + 1]["pag"], metas[k + 1]["y"]) if k + 1 < len(metas) else 10 ** 9
        minhas = sorted((a for a in alts if ini < chave(a["pag"], a["y"]) < fim), key=lambda a: chave(a["pag"], a["y"]))
        lim_enun = chave(minhas[0]["pag"], minhas[0]["y"]) - 1 if minhas else fim
        # o enunciado começa depois do cabeçalho (linha "Ano/Banca/Órgão/Prova" e, se houver, a continuação dela)
        if mt.get("cab_fim"):
            prefixo = f"{mt.get('banca')} - {mt.get('ano')} - {mt.get('orgao')} - "
            usa_cont = mt.get("cont_fim") and not limpar(mt.get("prova") or "").startswith(prefixo)
            ini = chave(mt["pag"], (mt["cont_fim"] if usa_cont else mt["cab_fim"]) + 1)
        enun = []
        for pi in range(mt["pag"], (metas[k + 1]["pag"] if k + 1 < len(metas) else doc.page_count - 1) + 1):
            for ln in sorted(ocr[pi], key=lambda x: (x["b"][1], x["b"][0])):
                c = chave(pi, ln["b"][1])
                t = ln["t"].strip()
                if not (ini < c < lim_enun) or ln["b"][2] - ln["b"][0] < 12:
                    continue  # fora da faixa, ou letra/número solto
                if t.startswith(("Ano:", "Qconcursos", "www.qconcursos", "Banca:", "Prova:", "Provas:")) \
                        or re.match(r"^\d{0,3}\s*Q[l1I]?\s?\d{5,}", t):
                    continue
                if t.lower().startswith("respostas"):
                    break
                enun.append(t)
        alternativas = []
        for a in minhas:
            txt, dv = resolver_ligaduras(a["texto"], referencia[a["pag"]])
            duvidas_lig += dv
            alternativas.append(limpar(txt))
        num_caderno = ordem_gab[k] if k < len(ordem_gab) else None
        g_v, g_o = gab_vetor.get(num_caderno), gab_ocr.get(num_caderno)
        prova_txt = limpar(mt.get("prova") or "")
        cargo = None
        if mt.get("orgao") and prova_txt:
            prefixo = f"{mt['banca']} - {mt['ano']} - {mt['orgao']} - "
            if not prova_txt.startswith(prefixo) and mt.get("prova_cont"):
                prova_txt = limpar(prova_txt + " " + mt["prova_cont"])
            cargo = prova_txt[len(prefixo):] if prova_txt.startswith(prefixo) else None
        if cargo is None and RX_PROVA.match(prova_txt):
            cargo = RX_PROVA.match(prova_txt)["cargo"]
        disc = mt["disc_qc"]
        if disc and ("," in disc or len(disc) > 45):  # assunto no lugar da disciplina: cabeçalho quebrado
            disc = None
        questoes.append({
            "arquivo": pdf.name, "prova_arquivo": nome, "numero": k + 1, "numero_no_caderno": num_caderno,
            "id_qc": mt["id"], "banca": mt.get("banca"), "ano": mt.get("ano"), "orgao": mt.get("orgao"),
            "cargo": cargo, "prova_qc": prova_txt or None, "disciplina_qc": disc,
            "assunto_qc": mt["assunto_qc"] if disc else " ".join(x for x in (mt["disc_qc"], mt["assunto_qc"]) if x),
            "enunciado": limpar(" ".join(enun)),
            "alternativas": {"ABCDE"[i] if i < 5 else str(i + 1): t for i, t in enumerate(alternativas)},
            "gabarito": g_v or g_o, "gabarito_fonte": "glifo" if g_v else ("ocr" if g_o else None),
            "gabarito_ocr_confere": (g_v == g_o) if (g_v and g_o) else None,
        })
    resumo = {"arquivo": pdf.name, "paginas": doc.page_count, "achadas": len(questoes),
              "esperadas_gabarito": len(set(numeros_gab)), "gabaritos_lidos": sum(1 for q in questoes if q["gabarito"]),
              "gabarito_glifo_x_ocr": [sum(1 for q in questoes if q["gabarito_ocr_confere"] is True),
                                       sum(1 for q in questoes if q["gabarito_ocr_confere"] is False)],
              "letras_calibradas": "".join(sorted(letra_de.values())),
              "sem_texto": sum(len(p.get_text().strip()) < 50 for p in doc),
              "sem_enunciado": [q["numero"] for q in questoes if len(q["enunciado"]) < 15],
              "alternativas_por_questao": sorted({len(q["alternativas"]) for q in questoes}),
              "ligaduras_em_duvida": duvidas_lig}
    return resumo, questoes, "\n\n".join(bruto)


def _autoteste() -> int:
    """Prova que os leitores ACUSAM: gabarito, linha da prova e id (REGRA CINCO)."""
    casos = [
        (RX_GAB.findall("11: A 12: E 13: c"), [("11", "A"), ("12", "E"), ("13", "c")]),
        (RX_GAB.findall("18: A 19: B 20: D"), [("18", "A"), ("19", "B"), ("20", "D")]),
        (RX_GAB.findall("Respostas sem letra 7:"), []),
        (bool(RX_PROVA.match("INSTITUTO AOCP - 2022 - PC-GO - Delegado de Polícia Substituto")), True),
        (bool(RX_PROVA.match("Direito Ambiental")), False),
        (bool(RX_ID.match("Q1992134")), True),
        (bool(RX_ID.match("Q19 > Direito")), False),
    ]
    falhas = 0
    for obtido, esperado in casos:
        ok = obtido == esperado
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} {esperado!r:.60}")
    return 1 if falhas else 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    if "--autoteste" in sys.argv:
        return _autoteste()
    warnings.filterwarnings("ignore")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    pasta = Path(args[0]) if args else Path.home() / "Downloads"
    pdfs = sorted(pasta.glob("AOCP*.pdf"))
    if not pdfs:
        print(f"nenhum AOCP*.pdf em {pasta}")
        return 2
    (DADOS / "provas_texto").mkdir(parents=True, exist_ok=True)
    todas, resumos, falha = [], [], False
    for pdf in pdfs:
        resumo, qs, bruto = extrair_prova(pdf)
        (DADOS / "provas_texto" / f"{slug(pdf.name)}.txt").write_text(bruto, encoding="utf-8")
        todas += qs
        resumos.append(resumo)
        bate = resumo["achadas"] == resumo["esperadas_gabarito"]
        falha |= not bate
        print(f"  {'OK ' if bate else 'DIF'} {pdf.name:28} achadas {resumo['achadas']:3} × gabarito diz "
              f"{resumo['esperadas_gabarito']:3} | gabaritos {resumo['gabaritos_lidos']:3} (glifo×OCR: "
              f"{resumo['gabarito_glifo_x_ocr'][0]} iguais, {resumo['gabarito_glifo_x_ocr'][1]} diferentes) | "
              f"letras {resumo['letras_calibradas']} | alt/questão {resumo['alternativas_por_questao']} | "
              f"sem enunciado {resumo['sem_enunciado']} | ligaduras em dúvida {resumo['ligaduras_em_duvida']}")
    # repetidas entre cadernos (mesmo id do QConcursos)
    vistos: dict[str, str] = {}
    for q in todas:
        q["repetida_de"] = vistos.get(q["id_qc"])
        vistos.setdefault(q["id_qc"], f"{q['prova_arquivo']}#{q['numero']}")
    saida = {"gerado_por": "ferramentas/extrair_provas_aocp.py", "resumo_por_prova": resumos,
             "total_questoes": len(todas), "unicas": len(vistos),
             "sem_gabarito": sum(1 for q in todas if not q["gabarito"]), "questoes": todas}
    (DADOS / "questoes_aocp.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n  total {len(todas)} questões | únicas (id QC) {len(vistos)} | sem gabarito {saida['sem_gabarito']}")
    return 1 if falha else 0


if __name__ == "__main__":
    sys.exit(main())
