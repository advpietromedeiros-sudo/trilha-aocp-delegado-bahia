"""Prova de cobertura da aba 📚 Revisão: cada bloco de texto do material contra o JSON de assertivas C/E.

O material é de terceiro e fica só no disco (revisao/material/, fora do Git); este verificador é autoral.

Itens: <pasta>/itens/<BLOCO>_01.json, _02.json ... ({"itens": [...]}), juntados na ordem.
Uso: python -I ferramentas/validar_revisao_material.py <pasta nfpss> <BLOCO> [<BLOCO> ...]   |   --autoteste
Sai 0 só se: toda página com conteúdo tem item; todo número de julgado/lei do texto aparece em
algum item; densidade >= 1 item por 650 caracteres; gabarito E entre 35% e 65%; sem CPF nem nome
de curso; sem assertiva repetida; campos obrigatórios presentes.
"""
import json, re, sys
from pathlib import Path

MARCA = re.compile(
    r"\b(?:Info(?:rmativo)?s?\.?|Tema|RE|REsp|AREsp|ARE|ADI|ADC|ADO|ADPF|HC|RHC|MS|RMS|AgRg|AgInt|EREsp|"
    r"IAC|IRDR|Rcl|MI|Pet|AO|AP|Inq|ACO|Lei|LC|Súmulas?|Súm\.?|Enunciado|SV|EC|Decreto|Resolução|Res\.)\s*(?:n[º°o.]*\s*)?(\d[\d.]*\d)", re.I)
CPF = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}")
PROIBIDO = re.compile(r"NFPSS|Ciclos M[ée]todo|#[A-Z]{4,}", re.I)
OBRIG = ("ponto", "tema", "pag", "assertiva", "gabarito", "resumo")
DENS = 650

def num(s):
    return s.replace(".", "").lstrip("0")

def marcas(txt):
    return {num(m.group(1)) for m in MARCA.finditer(txt) if len(num(m.group(1))) >= 2}

def paginas(txt):
    """Página -> caracteres de conteúdo (sem a marca de página)."""
    out, cur = {}, None
    for parte in re.split(r"(\[\[p\.\d+\]\])", txt):
        m = re.fullmatch(r"\[\[p\.(\d+)\]\]", parte)
        if m:
            cur = int(m.group(1)); out.setdefault(cur, 0)
        elif cur is not None:
            out[cur] += len(re.sub(r"\s+", "", parte))
    return out

def validar(texto, dados, nome="?"):
    erros = []
    itens = dados.get("itens", [])
    for i, it in enumerate(itens):
        for c in OBRIG:
            if not it.get(c) and it.get(c) != 0:
                erros.append(f"item {i}: falta {c}")
        if it.get("gabarito") not in ("C", "E"):
            erros.append(f"item {i}: gabarito {it.get('gabarito')!r}")
        if it.get("gabarito") == "E" and not it.get("resumo"):
            erros.append(f"item {i}: errado sem correção no resumo")
        if len(it.get("assertiva", "")) < 40:
            erros.append(f"item {i}: assertiva curta demais")
    tudo = json.dumps(itens, ensure_ascii=False)
    if CPF.search(tudo): erros.append("CPF no JSON")
    for m in PROIBIDO.finditer(tudo): erros.append(f"texto proibido no JSON: {m.group(0)}"); break
    vistas = set()
    for it in itens:
        a = re.sub(r"\W+", "", it.get("assertiva", "").lower())
        if a in vistas: erros.append(f"assertiva repetida: {it['assertiva'][:60]}")
        vistas.add(a)
    pags = paginas(texto)
    # O bloco pode começar no meio de uma página (corte por título): o trecho antes da 1ª marca é a página
    # anterior; vale item com essa página ou com a da 1ª marca (09/11/2026).
    ini = texto.split("[[p.", 1)[0]
    m1 = re.search(r"\[\[p\.(\d+)\]\]", texto)
    if m1 and len(re.sub(r"\s+", "", ini)) >= 250:
        p1 = int(m1.group(1))
        if not any(str(it.get("pag")) in (str(p1 - 1), str(p1)) for it in itens):
            erros.append(f"trecho inicial (antes da p. {p1}) sem item")
    chars_ini = len(re.sub(r"\s+", "", ini))
    cobertas = {int(it.get("pag", -1)) for it in itens if str(it.get("pag", "")).isdigit() or isinstance(it.get("pag"), int)}
    for p, n in sorted(pags.items()):
        if n >= 250 and p not in cobertas:
            erros.append(f"página {p} ({n} caracteres) sem item")
    plano = re.sub(r"(?<=\d)\.(?=\d)", "", tudo)
    tokens = set(re.findall(r"\d{2,}", plano))
    faltam = sorted(m for m in marcas(texto) if m not in tokens)
    for m in faltam: erros.append(f"número citado no texto e ausente dos itens: {m}")
    chars = sum(pags.values()) + chars_ini
    minimo = max(1, chars // DENS)
    if len(itens) < minimo:
        erros.append(f"densidade: {len(itens)} itens; mínimo {minimo} para {chars} caracteres")
    if itens:
        e = sum(it.get("gabarito") == "E" for it in itens) / len(itens)
        if not 0.35 <= e <= 0.65: erros.append(f"gabarito: {e:.0%} de E (fora de 35% a 65%)")
    return erros, len(itens), minimo

def autoteste():
    txt = "[[p.3]]\n" + "x" * 300 + " Info 1.234 e RE 669367/RJ\n[[p.4]]\ncurto"
    bom = {"itens": [{"ponto": "P", "tema": "T", "pag": 3, "gabarito": g,
                      "assertiva": f"Assertiva de teste número {k} com tamanho suficiente.",
                      "resumo": "Info 1234; RE 669.367."} for k, g in enumerate("CE")]}
    falhas = 0
    e, *_ = validar(txt, bom); falhas += bool(e); print("passa o bom:", not e, e)
    ruim = json.loads(json.dumps(bom)); ruim["itens"][0]["resumo"] = "sem números"; ruim["itens"][1]["resumo"] = "x"
    e, *_ = validar(txt, ruim); ok = any("1234" in x for x in e); falhas += not ok; print("acusa julgado perdido:", ok)
    ruim = json.loads(json.dumps(bom)); ruim["itens"][0]["pag"] = 9; ruim["itens"][1]["pag"] = 9
    e, *_ = validar(txt, ruim); ok = any("página 3" in x for x in e); falhas += not ok; print("acusa página sem item:", ok)
    ruim = json.loads(json.dumps(bom)); ruim["itens"][0]["resumo"] += " " + ".".join(["000"] * 3) + "-00"  # montado em execução: nenhum CPF escrito
    e, *_ = validar(txt, ruim); ok = any("CPF" in x for x in e); falhas += not ok; print("acusa CPF:", ok)
    ruim = json.loads(json.dumps(bom)); ruim["itens"][1]["gabarito"] = "C"
    e, *_ = validar(txt, ruim); ok = any("gabarito" in x for x in e); falhas += not ok; print("acusa gabarito torto:", ok)
    pre = "y" * 300 + chr(10) + txt
    e, *_ = validar(pre, bom); ok = not any("trecho inicial" in x for x in e); falhas += not ok
    print("aceita trecho inicial coberto pela 1ª página:", ok)
    e, *_ = validar("z" * 300 + chr(10) + "[[p.9]]" + chr(10) + "w" * 300, bom); ok = any("trecho inicial" in x for x in e); falhas += not ok
    print("acusa trecho inicial sem item:", ok)
    return 1 if falhas else 0

def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if "--autoteste" in sys.argv: return autoteste()
    base = Path(sys.argv[1]); rc = 0
    for nome in sys.argv[2:]:
        txt = (base / "blocos" / f"{nome}.txt").read_text(encoding="utf-8")
        arqs = sorted((base / "itens").glob(f"{nome}_*.json"))
        if not arqs: print(f"[ X ] {nome}: sem itens/{nome}_NN.json"); rc = 1; continue
        itens = []
        for a in arqs:
            itens += json.loads(a.read_text(encoding="utf-8"))["itens"]
        erros, n, minimo = validar(txt, {"itens": itens}, nome)
        print(f"[{' X ' if erros else 'OK '}] {nome}: {n} itens (mínimo {minimo})")
        for x in erros[:40]: print("      ", x)
        if len(erros) > 40: print(f"       ... e mais {len(erros)-40}")
        rc |= bool(erros)
    return rc

if __name__ == "__main__":
    sys.exit(main())
