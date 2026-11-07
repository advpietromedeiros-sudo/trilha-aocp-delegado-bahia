#!/usr/bin/env python3
"""Incidência de cada ponto do edital nas provas AOCP e o mapa de prioridade da revisão (D-018, Fase 0).

Uso:  python ferramentas/classificar_incidencia.py            classifica, grava os mapas e o docs/REVISAO_PRIORIDADE.md
      python ferramentas/classificar_incidencia.py --amostra N imprime N classificações sorteadas (semente fixa) para
                                                               conferência à mão; o veredito vai em
                                                               revisao/amostra_conferida.json
      python ferramentas/classificar_incidencia.py --autoteste prova que a régua casa o que deve e recusa o que não deve

Entradas: revisao/dados/questoes_aocp.json (fora do Git, gerado por extrair_provas_aocp.py), revisao/mapa_palavras.json
(régua curada, no Git), assets/items.json (503 pontos do edital).
Saídas:   revisao/dados/classificacao_aocp.json (fora do Git: tem trecho de questão), revisao/mapa_prioridade.json e
          docs/REVISAO_PRIORIDADE.md (no Git: só ids, números, rótulos do edital e contagens).
Sem API externa: só palavras-chave (REGRA ZERO: o que não casa fica NÃO classificado, contado e listado — §F10).
"""
from __future__ import annotations

import json
import random
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
QUESTOES = RAIZ / "revisao" / "dados" / "questoes_aocp.json"
CLASSIF = RAIZ / "revisao" / "dados" / "classificacao_aocp.json"
MAPA_PALAVRAS = RAIZ / "revisao" / "mapa_palavras.json"
AMOSTRA = RAIZ / "revisao" / "amostra_conferida.json"
SAIDA = RAIZ / "revisao" / "mapa_prioridade.json"
DOC = RAIZ / "docs" / "REVISAO_PRIORIDADE.md"

# ---------------------------------------------------------------------------------------------------------------
# Peso da disciplina na prova objetiva (questões em 100).
# OFICIAL (edital, Tabela 7.1, p. 10): 40 questões de Conhecimentos Gerais + 60 de Conhecimentos Específicos, 1,0
# ponto cada; o Anexo I (pp. 26-31) diz quais disciplinas são gerais (7) e quais específicas (10).
# O edital NÃO diz quantas questões cada disciplina tem. A divisão dentro de cada bloco é ESTIMATIVA: a média dos
# 4 simulados DPC-BA (4 × 100 questões, material de terceiro, uso local, D-017), que somam exatamente 40 e 60.
# ---------------------------------------------------------------------------------------------------------------
PESOS = {
    "LÍNGUA PORTUGUESA": ("gerais", 8.0), "RACIOCÍNIO LÓGICO": ("gerais", 8.0), "LEGISLAÇÃO GERAL": ("gerais", 8.0),
    "ATUALIDADES": ("gerais", 4.0), "INFORMÁTICA": ("gerais", 4.0),
    "PROMOÇÃO DA IGUALDADE RACIAL E DE GÊNERO": ("gerais", 4.0), "MEDICINA LEGAL": ("gerais", 4.0),
    "DIREITO ADMINISTRATIVO": ("específicos", 8.0), "DIREITO CONSTITUCIONAL": ("específicos", 8.0),
    "DIREITO PROCESSUAL PENAL": ("específicos", 7.75), "DIREITO PENAL": ("específicos", 7.25),
    "DIREITO CIVIL E EMPRESARIAL": ("específicos", 7.0),
    "LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE": ("específicos", 7.0), "CRIMINOLOGIA": ("específicos", 6.0),
    "DIREITO PROCESSUAL CIVIL": ("específicos", 3.0), "DIREITO TRIBUTÁRIO": ("específicos", 3.0),
    "DIREITO AMBIENTAL": ("específicos", 3.0),
}

# Nome da disciplina como está no Anexo I do edital e a página onde começa (medida no texto do PDF, 06/11/2026).
# Os 17 nomes do Anexo I são os mesmos 17 `discipline` do items.json, letra por letra.
EDITAL_NOME_PAG = {
    "LÍNGUA PORTUGUESA": ("LÍNGUA PORTUGUESA", 26), "RACIOCÍNIO LÓGICO": ("RACIOCÍNIO LÓGICO", 27),
    "ATUALIDADES": ("ATUALIDADES", 27), "INFORMÁTICA": ("INFORMÁTICA", 27),
    "PROMOÇÃO DA IGUALDADE RACIAL E DE GÊNERO": ("PROMOÇÃO DA IGUALDADE RACIAL E DE GÊNERO", 27),
    "MEDICINA LEGAL": ("MEDICINA LEGAL", 27), "LEGISLAÇÃO GERAL": ("LEGISLAÇÃO GERAL", 28),
    "DIREITO ADMINISTRATIVO": ("DIREITO ADMINISTRATIVO", 28),
    "DIREITO CIVIL E EMPRESARIAL": ("DIREITO CIVIL E EMPRESARIAL", 28),
    "DIREITO CONSTITUCIONAL": ("DIREITO CONSTITUCIONAL", 29), "DIREITO PENAL": ("DIREITO PENAL", 29),
    "DIREITO PROCESSUAL PENAL": ("DIREITO PROCESSUAL PENAL", 29),
    "DIREITO PROCESSUAL CIVIL": ("DIREITO PROCESSUAL CIVIL", 30), "DIREITO TRIBUTÁRIO": ("DIREITO TRIBUTÁRIO", 30),
    "DIREITO AMBIENTAL": ("DIREITO AMBIENTAL", 30),
    "LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE": ("LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE", 30),
    "CRIMINOLOGIA": ("CRIMINOLOGIA", 31),
}

MODULOS = [  # os 12 módulos correlatos do docs/REVISAO_PLANO.md
    ("Penal (geral e especial)", ["DIREITO PENAL"]),
    ("Processo Penal e inquérito", ["DIREITO PROCESSUAL PENAL"]),
    ("Legislação penal extravagante", ["LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE"]),
    ("Constitucional", ["DIREITO CONSTITUCIONAL"]),
    ("Administrativo", ["DIREITO ADMINISTRATIVO"]),
    ("Criminologia e Medicina Legal", ["CRIMINOLOGIA", "MEDICINA LEGAL"]),
    ("Tributário", ["DIREITO TRIBUTÁRIO"]),
    ("Civil, Empresarial e Processo Civil", ["DIREITO CIVIL E EMPRESARIAL", "DIREITO PROCESSUAL CIVIL"]),
    ("Ambiental", ["DIREITO AMBIENTAL"]),
    ("Igualdade racial e de gênero, Legislação geral e Atualidades",
     ["PROMOÇÃO DA IGUALDADE RACIAL E DE GÊNERO", "LEGISLAÇÃO GERAL", "ATUALIDADES"]),
    ("Língua Portuguesa", ["LÍNGUA PORTUGUESA"]),
    ("Informática e Raciocínio Lógico", ["INFORMÁTICA", "RACIOCÍNIO LÓGICO"]),
]

ORDEM_PRIOR = {"Alta": 0, "Média-alta": 1, "Regular": 2}
LIMIAR = 2.0  # pontos mínimos: 1 termo exclusivo do item no assunto do QC (3), ou 2 no texto da questão
# (1.0 deixava uma palavra solta do enunciado decidir — amostra 1, 06/11/2026)


def norm(s: str | None) -> str:
    s = unicodedata.normalize("NFKD", (s or "").lower()).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", s).strip()


def padrao(termo: str) -> re.Pattern:
    """Termo curto (até 4 letras) casa a palavra inteira; o longo casa como prefixo (plural, flexão)."""
    t = re.escape(termo)
    fim = r"(?![a-z0-9])" if len(termo) <= 4 else ""
    if len(termo) > 5 and re.fullmatch(r"[a-z]+", termo):  # plural irregular: -ão → -ões/-ães, -al → -ais
        if termo.endswith("ao"):
            t = re.escape(termo[:-2]) + "(?:ao|oes|aes|aos)"
        elif termo.endswith(("al", "el", "ol")):
            t = re.escape(termo[:-1]) + "(?:l|is)"
    return re.compile(r"(?<![a-z0-9])" + t + fim)


class Regua:
    def __init__(self, mapa: dict):
        self.mapa_disc = {norm(k): v for k, v in mapa["disciplinas_plataforma"].items()}
        self.peso = mapa["peso"]
        self.itens = mapa["itens"]
        self.termos: dict[str, list[tuple[str, re.Pattern, bool]]] = {}
        df: dict[str, Counter] = defaultdict(Counter)
        for iid, it in self.itens.items():
            ts = [(t, False) for t in it["termos_do_rotulo"]] + [(t, True) for t in it["sinonimos"]]
            vistos, lista = set(), []
            for t, sin in ts:
                t = norm(t)
                if t and t not in vistos:
                    vistos.add(t)
                    lista.append((t, padrao(t), sin))
                    df[it["disciplina"]][t] += 1
            self.termos[iid] = lista
        self.df = df

    def disciplinas(self, disc_qc: str | None) -> list[str] | None:
        d = norm(disc_qc)
        if not d:
            return None
        if d in self.mapa_disc:
            return self.mapa_disc[d]
        for k, v in self.mapa_disc.items():
            if d.startswith(k) or k.startswith(d):
                return v
        return None

    def pontuar(self, iid: str, assunto: str, corpo: str) -> tuple[float, float, list[str]]:
        """Pontos no assunto do QConcursos e pontos no enunciado+alternativas, separados."""
        disc = self.itens[iid]["disciplina"]
        pa, pc, casados = 0.0, 0.0, []
        for t, rx, _sin in self.termos[iid]:
            mult = (self.peso["sinonimo_multipalavra"] if " " in t else 1) / self.df[disc][t]
            if rx.search(assunto):
                pa += self.peso["assunto_qc"] * mult
                casados.append(t)
            elif rx.search(corpo):
                pc += self.peso["enunciado_e_alternativas"] * mult
                casados.append(t)
        return pa, pc, casados

    def classificar(self, q: dict) -> dict:
        assunto = norm(q.get("assunto_qc"))
        corpo = norm(q.get("enunciado", "") + " " + " ".join(q.get("alternativas", {}).values()))
        cand_disc = self.disciplinas(q.get("disciplina_qc"))
        ids = [i for i, it in self.itens.items() if cand_disc is None or it["disciplina"] in cand_disc]
        notas = []
        for iid in ids:
            pa, pc, c = self.pontuar(iid, assunto, corpo)
            if pa + pc > 0:
                prof = self.itens[iid]["numero"].count(".")
                notas.append((round(pa + pc, 4), round(pa, 4), prof, iid, c))
        # ordem: o assunto marcado por gente no QConcursos decide primeiro; o texto da questão desempata
        notas.sort(key=lambda x: (-x[1], -x[0], -x[2]))
        if not notas or notas[0][0] < LIMIAR:
            melhor = max(notas, key=lambda x: x[0]) if notas else None
            return {"item": None, "pontos": melhor[0] if melhor else 0.0, "termos": melhor[4] if melhor else [],
                    "candidatas": [n[3] for n in notas[:3]], "disciplinas_candidatas": cand_disc}
        p, _, _, iid, c = notas[0]
        seg = notas[1][0] if len(notas) > 1 else 0.0
        return {"item": iid, "disciplina": self.itens[iid]["disciplina"], "pontos": p, "termos": c,
                "n_termos": len(c), "margem": round(p - seg, 4),
                "confianca": "alta" if (p >= 3 and p - seg >= 1) else ("média" if p >= 2 else "baixa"),
                "candidatas": [n[3] for n in notas[:3]], "disciplinas_candidatas": cand_disc}


def carregar() -> tuple[list[dict], dict, list[dict]]:
    dados = json.loads(QUESTOES.read_text(encoding="utf-8"))
    mapa = json.loads(MAPA_PALAVRAS.read_text(encoding="utf-8"))
    itens = json.loads((RAIZ / "assets" / "items.json").read_text(encoding="utf-8"))
    return dados["questoes"], mapa, itens


def calcular(questoes: list[dict], regua: Regua, itens: list[dict]) -> dict:
    unicas = [q for q in questoes if not q.get("repetida_de")]
    resultado = []
    for q in unicas:
        r = regua.classificar(q)
        resultado.append({"id_qc": q["id_qc"], "prova_arquivo": q["prova_arquivo"], "numero": q["numero"],
                          "orgao": q.get("orgao"), "cargo": q.get("cargo"), "ano": q.get("ano"),
                          "disciplina_qc": q.get("disciplina_qc"), "assunto_qc": q.get("assunto_qc"), **r})
    incid = Counter(r["item"] for r in resultado if r["item"])
    por_disc_n = Counter(r["disciplina"] for r in resultado if r["item"])
    k_disc = Counter(i["discipline"] for i in itens)
    linhas = []
    for i in itens:
        d = i["discipline"]
        bloco, peso = PESOS[d]
        n = incid.get(i["id"], 0)
        # escore = questões esperadas do item na prova de 100 (ver docs/REVISAO_PRIORIDADE.md, "A fórmula")
        escore = peso * (1 + n) / (por_disc_n[d] + k_disc[d])
        linhas.append({"id": i["id"], "disciplina": d, "numero": i["number"], "rotulo": i["label"],
                       "bloco": bloco, "peso_disciplina": peso, "incidencia_aocp": n,
                       "prioridade_antiga": i["priority"], "escore": round(escore, 4)})
    linhas.sort(key=lambda x: (-x["escore"], ORDEM_PRIOR[x["prioridade_antiga"]], x["id"]))
    for pos, ln in enumerate(linhas, 1):
        ln["posicao"] = pos
    mods = []
    for nome, discs in MODULOS:
        its = [ln for ln in linhas if ln["disciplina"] in discs]
        mods.append({"modulo": nome, "disciplinas": discs, "itens": len(its),
                     "escore": round(sum(ln["escore"] for ln in its), 2),
                     "questoes_esperadas_por_item": round(sum(ln["escore"] for ln in its) / len(its), 3),
                     "incidencia_aocp": sum(ln["incidencia_aocp"] for ln in its)})
    mods.sort(key=lambda m: (-m["escore"], -m["questoes_esperadas_por_item"]))
    for o, m in enumerate(mods, 1):
        m["ordem"] = o
    return {"resultado": resultado, "linhas": linhas, "modulos": mods, "unicas": len(unicas),
            "repetidas": len(questoes) - len(unicas)}


def gravar(calc: dict, regua: Regua, questoes: list[dict]) -> dict:
    res = calc["resultado"]
    nao = [r for r in res if not r["item"]]
    soma_itens = sum(m["itens"] for m in calc["modulos"])
    amostra = json.loads(AMOSTRA.read_text(encoding="utf-8")) if AMOSTRA.exists() else None
    CLASSIF.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    meta = {
        "gerado_em": datetime.now().strftime("%d/%m/%Y %H:%M"), "gerado_por": "ferramentas/classificar_incidencia.py",
        "formula": "escore = peso_disciplina × (1 + incidência_do_item) ÷ (questões AOCP classificadas na disciplina + "
                   "itens da disciplina); desempate: prioridade antiga (Alta > Média-alta > Regular), depois o id",
        "pesos_fonte": "edital (Tabela 7.1, p. 10; Anexo I, pp. 26-31): 40 gerais + 60 específicos; divisão por "
                       "disciplina = ESTIMATIVA pela média dos 4 simulados DPC-BA (o edital não a traz)",
        "questoes_aocp": {"total_extraidas": len(questoes), "unicas": calc["unicas"], "repetidas": calc["repetidas"],
                          "classificadas": len(res) - len(nao), "nao_classificadas": len(nao)},
        "nao_classificadas": [{"id_qc": r["id_qc"], "prova": r["prova_arquivo"], "numero": r["numero"],
                               "disciplina_qc": r["disciplina_qc"]} for r in nao],
        "soma_itens_modulos": soma_itens,
        "amostra_conferida": amostra and {"conferidas": len(amostra["casos"]),
                                          "certas": sum(1 for c in amostra["casos"] if c["veredito"] == "certa")},
        "modulos": calc["modulos"], "itens": calc["linhas"],
    }
    SAIDA.write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    DOC.write_text(montar_md(meta, calc, amostra), encoding="utf-8", newline="\n")
    return meta


def br(x: float, casas: int = 2) -> str:
    s = f"{x:,.{casas}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def montar_md(meta: dict, calc: dict, amostra: dict | None) -> str:
    q = meta["questoes_aocp"]
    res = calc["resultado"]
    conf = Counter(r.get("confianca") for r in res if r["item"])
    por_disc = Counter(r["disciplina"] for r in res if r["item"])
    L = [
        "# Revisão por prioridade — o mapa medido (Fase 0)",
        "",
        f"> Gerado por `ferramentas/classificar_incidencia.py` em {meta['gerado_em']}. Não edite à mão: rode de novo.",
        "> Dados de máquina: `revisao/mapa_prioridade.json`. Plano: `docs/REVISAO_PLANO.md` (D-018).",
        "",
        "## Método",
        "",
        "1. **Provas AOCP** (24 cadernos exportados de uma plataforma de questões, na pasta Downloads do titular;",
        "   procedência em `docs/PROCEDENCIA.md`) foram lidas por",
        "   `ferramentas/extrair_provas_aocp.py`. O negrito dos cadernos (enunciado, número, letra e gabarito) é desenho",
        "   vetorial, sem texto: o enunciado vem do OCR do próprio Windows (pt-BR) e o gabarito da forma do glifo, calibrada",
        "   pelos círculos A–E de cada questão e conferida contra o OCR. Saída fora do Git (`revisao/dados/`).",
        f"2. **Questões únicas:** {q['total_extraidas']} extraídas, {q['repetidas']} repetidas entre cadernos (mesmo id da",
        f"   plataforma) → **{q['unicas']} únicas**, a base da incidência.",
        "3. **Classificação** em (disciplina, item do edital) por palavras-chave: a régua é `revisao/mapa_palavras.json`",
        "   (termos tirados do rótulo de cada item + sinônimos jurídicos escritos à mão). A disciplina dada pela plataforma",
        "   limita as candidatas; o assunto dado pela plataforma vale 3, o enunciado e as alternativas valem 1; termo de",
        "   várias palavras vale o dobro; cada termo é dividido pelo número de itens da disciplina que o usam (termo",
        f"   genérico pesa pouco). Classifica com **{br(LIMIAR, 1)} ponto** ou mais; abaixo disso fica **não classificada**.",
        "4. **Peso da disciplina:** ver a tabela abaixo.",
        "",
        "## Peso de cada disciplina na prova objetiva",
        "",
        "O edital (Tabela 7.1, **p. 10**) dá só os blocos: **40 questões de Conhecimentos Gerais e 60 de Conhecimentos",
        "Específicos**, 1,0 ponto cada, mínimo de 70 pontos. O Anexo I (**pp. 26–31**) diz o que é geral (7 disciplinas,",
        "pp. 26–28) e o que é específico do Delegado (10 disciplinas, pp. 28–31). ⚠️ **O edital não diz quantas questões",
        "cada disciplina tem.** A divisão dentro do bloco é **estimativa**: a média dos 4 simulados DPC-BA (que somam",
        "exatamente 40 + 60). Se a banca distribuir diferente, a régua erra na mesma proporção.",
        "",
        "| disciplina (items.json) | no Anexo I do edital | bloco | questões (estimadas) | questões AOCP classificadas |",
        "| --- | --- | --- | ---: | ---: |",
    ]
    for d, (bloco, peso) in sorted(PESOS.items(), key=lambda x: (x[1][0] != "gerais", -x[1][1], x[0])):
        nome, pag = EDITAL_NOME_PAG[d]
        igual = "mesmo nome" if nome == d else nome
        L.append(f"| {d} | {igual}, p. {pag} | {bloco} | {br(peso)} | {por_disc[d]} |")
    L += ["", f"Soma: {br(sum(p for _, p in PESOS.values()))} questões.", "",
          "## A fórmula", "",
          "```",
          "escore(item) = peso_da_disciplina × (1 + incidência_do_item) ÷ (N_disciplina + K_disciplina)",
          "  incidência_do_item = questões AOCP únicas classificadas no item",
          "  N_disciplina       = questões AOCP únicas classificadas na disciplina",
          "  K_disciplina       = número de itens da disciplina no edital",
          "desempate: prioridade antiga (Alta > Média-alta > Regular), depois o id",
          "```",
          "",
          "**Por que ajustei** a fórmula do plano (`peso × (1 + incidência)`): a quantidade de questões AOCP por disciplina",
          "depende de **quais cadernos foram baixados** (há 121 questões de Português e 25 de Penal porque havia 9 cadernos",
          "de Português), não da prova. Sem dividir pelo tamanho da amostra da disciplina, Português e Informática passariam",
          "à frente de tudo por acaso. Com a divisão, o `(1 + n)` vira a **fatia do item dentro da disciplina** (suavizada:",
          "item sem questão ainda tem fatia > 0) e o escore passa a ser **quantas questões se espera do item numa prova de",
          f"100** — a soma dos 503 escores é {br(sum(ln['escore'] for ln in calc['linhas']))}. O peso da disciplina continua",
          "multiplicando, e a incidência continua decidindo a ordem **dentro** da disciplina.",
          "",
          "## Ordem dos 12 módulos",
          "",
          "Ordenados pelo escore somado (= questões esperadas do módulo na objetiva). A coluna *por item* mostra a",
          "densidade: quanto rende cada ponto estudado.",
          "",
          "| ordem | módulo | itens | escore (questões esperadas) | por item | questões AOCP |",
          "| ---: | --- | ---: | ---: | ---: | ---: |"]
    for m in calc["modulos"]:
        L.append(f"| {m['ordem']} | {m['modulo']} | {m['itens']} | {br(m['escore'])} | "
                 f"{br(m['questoes_esperadas_por_item'], 3)} | {m['incidencia_aocp']} |")
    L += ["", f"**Soma dos itens: {meta['soma_itens_modulos']}** (o edital tem 503 — §D7).", "",
          "## Os 40 pontos de maior prioridade", "",
          "| # | id | disciplina | item | escore | incidência AOCP | prioridade antiga |",
          "| ---: | --- | --- | --- | ---: | ---: | --- |"]
    for ln in calc["linhas"][:40]:
        rot = ln["rotulo"].replace("|", "/")
        rot = rot if len(rot) <= 90 else rot[:87] + "…"
        L.append(f"| {ln['posicao']} | {ln['id']} | {ln['disciplina'].title()} | {ln['numero']} {rot} | "
                 f"{br(ln['escore'], 3)} | {ln['incidencia_aocp']} | {ln['prioridade_antiga']} |")
    L += ["", "## Qualidade da régua", "",
          f"- Classificadas: **{q['classificadas']} de {q['unicas']}** questões únicas; confiança alta {conf['alta']}, "
          f"média {conf['média']}, baixa {conf['baixa']}.",
          f"- **Não classificadas: {q['nao_classificadas']}** (lista abaixo)."]
    if amostra:
        c = amostra["casos"]
        certas = sum(1 for x in c if x["veredito"] == "certa")
        L.append(f"- **Amostra conferida à mão** ({amostra['conferida_em']}, sorteio de semente fixa): **{certas} de "
                 f"{len(c)} certas** ({br(100 * certas / len(c), 1)}%). As erradas e o porquê estão em "
                 "`revisao/amostra_conferida.json`.")
        erradas = [x for x in c if x["veredito"] != "certa"]
        for x in erradas:
            L.append(f"  - {x['id_qc']}: classificada em {x['item']}, o certo seria "
                     f"{x.get('certo_seria') or 'não classificar'} — {x['por_que']}.")
        ant = amostra.get("amostra_anterior")
        if ant:
            L.append(f"- Antes dos ajustes, a primeira amostra deu {ant['certas']} de {ant['conferidas']} "
                     f"({ant['conferida_em']}); os erros dela guiaram os ajustes e a amostra acima foi sorteada depois.")
    else:
        L.append("- ⚠️ Amostra conferida à mão: **ainda não feita** (`--amostra 30`).")
    L += ["", "### Questões não classificadas (§F10)", "",
          "| id na plataforma | caderno | nº | disciplina na plataforma |", "| --- | --- | ---: | --- |"]
    for r in sorted((r for r in res if not r["item"]), key=lambda r: (r["prova_arquivo"], r["numero"])):
        L.append(f"| {r['id_qc']} | {r['prova_arquivo']} | {r['numero']} | {r['disciplina_qc'] or '(não lida)'} |")
    especificos = [d for d, (b, _) in PESOS.items() if b == "específicos"]
    n_esp = [por_disc[d] for d in especificos]
    zeradas = sorted(d for d in PESOS if por_disc[d] == 0)
    L += ["", "## Limites da régua (declarados)", "",
          "- **Amostra torta:** as questões de Direito (e 5 de Português) vêm de provas de **Delegado** (PC-GO 2022 e",
          "  PC-PA 2021) — e são só parte daquelas provas, não as provas inteiras; o resto de Português, Informática e",
          "  Raciocínio Lógico vem de provas AOCP de outros cargos (2026). Mostram o jeito da banca, não o recorte do Delegado.",
          f"- **Pouca questão por disciplina específica** (de {min(n_esp)} a {max(n_esp)}): a ordem dentro delas é frágil;",
          "  a suavização evita que item sem questão vá a zero, mas não inventa incidência.",
          f"- **Disciplinas sem nenhuma questão AOCP nos cadernos:** {', '.join(zeradas) or 'nenhuma'}. Nelas o escore",
          "  é só o peso estimado dividido pelos itens — por isso as 5 leis da Legislação Geral (8 questões estimadas em 5",
          "  itens) sobem ao topo. É conta, não incidência medida.",
          "- **Peso por disciplina é estimativa** (o edital só fixa 40 + 60). A discursiva (só específicos) e o desempate",
          "  pela nota de específicos (edital, 9.1) **não** entram no escore — o edital não dá a distribuição por disciplina.",
          "- **Cada questão conta para um item só** (o de maior pontuação). Item-título (ex.: \"Crimes.\", \"Prisão.\")",
          "  tende a zero porque os filhos levam a questão; no módulo ele anda junto com os filhos.",
          "- **Itens de \"Jurisprudência aplicada\"** não têm palavra própria e não recebem questão.",
          "- **Palavra-chave não entende contexto:** a amostra conferida mede o erro; o resto não foi lido um a um.",
          ""]
    return "\n".join(L)


def amostra(n: int) -> int:
    questoes, mapa, itens = carregar()
    regua = Regua(mapa)
    calc = calcular(questoes, regua, itens)
    por_id = {q["id_qc"]: q for q in questoes}
    rot = {i["id"]: i["label"] for i in itens}
    classif = [r for r in calc["resultado"] if r["item"]]
    random.Random(20261106).shuffle(classif)
    for r in classif[:n]:
        q = por_id[r["id_qc"]]
        print(f"\n### {r['id_qc']} ({r['prova_arquivo']} #{r['numero']}) QC: {r['disciplina_qc']} > {r['assunto_qc']}")
        print(f"    → {r['item']} '{rot[r['item']][:90]}'  pts {r['pontos']} termos {r['termos'][:6]}")
        print(f"    enunciado: {q['enunciado'][:260]}")
    return 0


def autoteste() -> int:
    """REGRA CINCO: a régua tem de casar o que deve e recusar o que não deve."""
    mapa = {"disciplinas_plataforma": {"Direito Penal": ["DIREITO PENAL"]},
            "peso": {"assunto_qc": 3, "enunciado_e_alternativas": 1, "sinonimo_multipalavra": 2},
            "itens": {"X-1": {"disciplina": "DIREITO PENAL", "numero": "1", "rotulo": "Prescrição.",
                              "termos_do_rotulo": ["prescricao"], "sinonimos": ["pretensao punitiva"]},
                      "X-2": {"disciplina": "DIREITO PENAL", "numero": "2", "rotulo": "Tortura.",
                              "termos_do_rotulo": [], "sinonimos": ["tor"]}}}
    r = Regua(mapa)
    casos = [
        (r.classificar({"disciplina_qc": "Direito Penal", "assunto_qc": "Prescrições penais", "enunciado": ""})["item"],
         "X-1", "prefixo casa o plural"),
        (r.classificar({"disciplina_qc": "Direito Penal", "assunto_qc": "", "enunciado": "a torre caiu"})["item"],
         None, "termo curto não casa dentro de outra palavra (tor ≠ torre)"),
        (r.classificar({"disciplina_qc": "Direito Penal", "assunto_qc": "", "enunciado": "nada a ver"})["item"],
         None, "sem termo: fica NÃO classificada"),
        (r.classificar({"disciplina_qc": "Direito Penal", "assunto_qc": "",
                        "enunciado": "Sobre a pretensão punitiva"})["item"], "X-1", "sinônimo de 2 palavras no corpo"),
        (r.disciplinas("Português"), None, "disciplina fora do mapa não vira Penal"),
    ]
    falhas = 0
    for obtido, esperado, nome in casos:
        ok = obtido == esperado
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} {nome} (obtido {obtido!r})")
    return 1 if falhas else 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    if "--autoteste" in sys.argv:
        return autoteste()
    if "--amostra" in sys.argv:
        return amostra(int(sys.argv[sys.argv.index("--amostra") + 1]))
    if not QUESTOES.exists():
        print(f"  falta {QUESTOES.relative_to(RAIZ)} — rode antes ferramentas/extrair_provas_aocp.py")
        return 2
    questoes, mapa, itens = carregar()
    regua = Regua(mapa)
    calc = calcular(questoes, regua, itens)
    meta = gravar(calc, regua, questoes)
    q = meta["questoes_aocp"]
    print(f"  questões únicas {q['unicas']} | classificadas {q['classificadas']} | NÃO classificadas "
          f"{q['nao_classificadas']}")
    for m in calc["modulos"]:
        print(f"  {m['ordem']:2}. {m['modulo']:62} itens {m['itens']:3}  escore {br(m['escore']):>6}")
    print(f"  soma dos itens dos módulos: {meta['soma_itens_modulos']} (edital: 503)")
    if meta["soma_itens_modulos"] != 503 or len(calc["linhas"]) != 503:
        print("  ❌ a decomposição não fecha com 503 (§D7)")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
