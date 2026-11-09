"""Verificador do aprofundamento dos comentários (Pente Fino e Revisão), pedido do titular em 09/11/2026.

Cada assertiva ganha, numa camada à parte (o conteúdo conferido do item não muda):
  aprofundamento  — 2 a 5 parágrafos curtos: fundamento, lógica da regra, ligação com institutos vizinhos (obrigatório);
  correcao        — {"erro": o que a assertiva diz de errado, "certo": a versão correta} (obrigatório se gabarito E);
  exemplo         — um caso concreto curto (opcional);
  memorize        — uma linha para fixar (opcional).

A trava que mantém o Pente Fino conferido: nenhum número (artigo, lei, súmula, tema, informativo, ano, prazo
em algarismos) pode aparecer no texto novo sem já estar no item — o redator explica o que foi conferido, não cita
dispositivo novo de memória.

Uso: python -I ferramentas/validar_aprofundamento.py <entrada.json> <saida.json ou pasta com <lote>_NN.json>
     python -I ferramentas/validar_aprofundamento.py --autoteste
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CPF = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}")
PROIBIDO = re.compile(r"NFPSS|Ciclos M[ée]todo|#[A-Z]{4,}", re.I)
MIN_AP, MAX_AP = 280, 1600
CAMPOS = {"aprofundamento", "correcao", "exemplo", "memorize"}


def _nums(texto: str) -> set[str]:
    t = re.sub(r"(?<=\d)\.(?=\d{3})", "", texto)
    t = re.sub(r"(\d)[º°ª]", r"\1", t)
    return set(re.findall(r"\d+", t))


def _novos_numeros(novo: str, base: str) -> list[str]:
    """Números do texto novo que não estão no item. Ignora 1 dígito solto (enumeração), exceto após art./§/inciso."""
    tem = _nums(base)
    t = re.sub(r"(?<=\d)\.(?=\d{3})", "", novo)
    t = re.sub(r"(\d)[º°ª]", r"\1", t)
    faltam = []
    for m in re.finditer(r"\d+", t):
        n = m.group(0)
        antes = t[max(0, m.start() - 8):m.start()].lower()
        if len(n) == 1 and not re.search(r"(art\.?|arts\.?|§|inc\.?|inciso)\s*$", antes):
            continue
        if n not in tem:
            faltam.append(n)
    return sorted(set(faltam))


def validar(entrada: dict, saida: dict) -> list[str]:
    erros: list[str] = []
    itens = {i["id"]: i for i in entrada["itens"]}
    for k in saida:
        if k not in itens:
            erros.append(f"{k}: id que não existe no lote")
    for iid, it in itens.items():
        a = saida.get(iid)
        if not isinstance(a, dict):
            erros.append(f"{iid}: sem aprofundamento")
            continue
        extra = set(a) - CAMPOS
        if extra:
            erros.append(f"{iid}: campo desconhecido {sorted(extra)}")
        ap = str(a.get("aprofundamento", ""))
        if not MIN_AP <= len(ap) <= MAX_AP:
            erros.append(f"{iid}: aprofundamento com {len(ap)} caracteres (de {MIN_AP} a {MAX_AP})")
        res = re.sub(r"\W+", "", str(it.get("resumo", "")).lower())
        if res and len(res) > 60 and res in re.sub(r"\W+", "", ap.lower()):
            erros.append(f"{iid}: aprofundamento repete o resumo")
        c = a.get("correcao")
        if it["gabarito"] == "E":
            if not (isinstance(c, dict) and len(str(c.get("erro", ""))) >= 15 and len(str(c.get("certo", ""))) >= 15):
                erros.append(f"{iid}: gabarito E sem correcao {{erro, certo}}")
        elif c:
            erros.append(f"{iid}: correcao em assertiva CERTA")
        novo = json.dumps(a, ensure_ascii=False)
        if CPF.search(novo):
            erros.append(f"{iid}: CPF")
        m = PROIBIDO.search(novo)
        if m:
            erros.append(f"{iid}: texto proibido {m.group(0)!r}")
        faltam = _novos_numeros(" ".join(str(v) for v in _textos(a)), json.dumps(it, ensure_ascii=False))
        if faltam:
            erros.append(f"{iid}: número que não está no item: {', '.join(faltam)}")
        if len(str(a.get("memorize", ""))) > 220:
            erros.append(f"{iid}: memorize com mais de 220 caracteres")
    return erros


def _textos(a: dict):
    for k, v in a.items():
        if isinstance(v, dict):
            yield from v.values()
        else:
            yield v


def carregar_saida(caminho: Path, lote: str) -> dict:
    if caminho.is_file():
        return json.loads(caminho.read_text(encoding="utf-8"))["itens"]
    out: dict = {}
    for arq in sorted(caminho.glob(f"{lote}_*.json")):
        out.update(json.loads(arq.read_text(encoding="utf-8"))["itens"])
    return out


def autoteste() -> int:
    ent = {"itens": [
        {"id": "X-1", "gabarito": "E", "assertiva": "O prazo é de 15 dias (art. 335).", "resumo": "O prazo é de 30 dias."},
        {"id": "X-2", "gabarito": "C", "assertiva": "Vale a Súmula 7/STJ.", "resumo": "Reexame de prova."}]}
    ap = "Fundamento: " + "a regra protege a parte e organiza o procedimento. " * 7
    bom = {"X-1": {"aprofundamento": ap + " O art. 335 conta 30 dias, e não 15.",
                   "correcao": {"erro": "diz que o prazo é de 15 dias", "certo": "o prazo é de 30 dias"}},
           "X-2": {"aprofundamento": ap + " A Súmula 7 barra o reexame.", "memorize": "REsp não reexamina prova."}}
    casos = [("passa o bom", bom, None)]
    r = json.loads(json.dumps(bom)); r["X-1"]["aprofundamento"] += " Veja o art. 336."
    casos.append(("acusa número inventado (art. 336)", r, "336"))
    r = json.loads(json.dumps(bom)); del r["X-1"]["correcao"]
    casos.append(("acusa E sem correção", r, "sem correcao"))
    r = json.loads(json.dumps(bom)); del r["X-2"]
    casos.append(("acusa item sem aprofundamento", r, "sem aprofundamento"))
    r = json.loads(json.dumps(bom)); r["X-2"]["aprofundamento"] = "curto"
    casos.append(("acusa aprofundamento curto", r, "caracteres"))
    r = json.loads(json.dumps(bom)); r["X-2"]["exemplo"] = "Fulano, " + ".".join(["000"] * 3) + "-00, ajuizou."
    casos.append(("acusa CPF (montado em execução)", r, "CPF"))
    falhas = 0
    for nome, s, espera in casos:
        e = validar(ent, s)
        ok = (not e) if espera is None else any(espera in x for x in e)
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} {nome}" + ("" if ok else f" — {e}"))
    return 1 if falhas else 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    if "--autoteste" in sys.argv:
        return autoteste()
    ent_p, sai_p = Path(sys.argv[1]), Path(sys.argv[2])
    ent = json.loads(ent_p.read_text(encoding="utf-8"))
    erros = validar(ent, carregar_saida(sai_p, ent.get("lote", ent_p.stem)))
    nome = ent.get("lote", ent_p.stem)
    print(f"[{' X ' if erros else 'OK '}] {nome}: {len(ent['itens'])} itens")
    for x in erros[:40]:
        print("      ", x)
    if len(erros) > 40:
        print(f"       ... e mais {len(erros) - 40}")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
