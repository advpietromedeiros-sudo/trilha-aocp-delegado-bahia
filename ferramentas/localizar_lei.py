"""Régua ÚNICA da Revisão Delegado PC-BA para conferir citação de lei seca e súmula.

O gerador (ferramentas/gerar_revisao.py) e o verificador de atualidade (ferramentas/verificar_atualidade.py)
importam ESTE módulo: o gerador recusa exatamente o que o verificador recusa (07/11/2026). Antes, cada um
tinha a sua régua, e o gerador aprovava o que o verificador reprovava — alínea marcada como inciso, "Il"
(erro do Planalto) no lugar de "II", "§ 2°" (sinal de grau) no lugar de "§ 2º".

O que se confere numa citação ({lei, art, par, inc, ali, texto}):
  1. lei e art presentes, e lei:art existe no texto oficial baixado;
  2. o trecho (8+ caracteres) está CONTIDO no artigo oficial, comparado por normalizar(): saem as anotações
     do Planalto ("(Redação dada…)", "(Incluído…)", "(Vide…)"…), as aspas; hífens, travessões, espaços e
     º/°/o depois de algarismo se unificam; caixa não conta;
  3. par ("§ 2º", "§ 4º-A", "parágrafo único"), inc (romano: "II", "I-B") e ali (letra: "a") são
     LOCALIZADOS na estrutura do artigo, um dentro do outro: o inciso dentro do parágrafo citado, a alínea
     dentro do inciso (ou do parágrafo). Algarismo romano com I/l/1 confundidos ("Il" no CPP, art. 78) é
     aceito só quando é inequívoco: um único candidato, com ao menos um algarismo romano de verdade.

Uso: python ferramentas/localizar_lei.py --autoteste   (REGRA CINCO: prova que acusa)
"""

from __future__ import annotations

import re
import sys
import unicodedata

# anotações do Planalto que não fazem parte do texto normativo
ANOTACAO = re.compile(
    r"\((?:Reda[cç][aã]o|Inclu[ií]d|Revogad|Vide|Vig[eê]ncia|Renumerad|Acrescid|"
    r"Express[aã]o|Promulga|Regulament|Produ[cç][aã]o de efeito)[^)]*\)",
    re.I,
)
_ASPAS = re.compile("[\"“”„‟«»]")
_APOS = re.compile("[‘’‚‛`´]")
_HIFEN = re.compile("[‐‑‒–—―−]")
# depois do NFKC o "º" (U+00BA) já virou "o"; o "°" (grau, U+00B0) continua "°". Os três viram "º".
_ORDINAL = re.compile("(\\d)\\s?[°o](?![a-zà-ú])")
ORD = "º"


def _base(t: str) -> str:
    t = unicodedata.normalize("NFKC", str(t or ""))
    t = ANOTACAO.sub(" ", t)
    t = _HIFEN.sub("-", t)
    t = _ORDINAL.sub(lambda m: m.group(1) + ORD, t)
    return t.replace(" ", " ")


def normalizar(t: str) -> str:
    """Texto para comparar trecho citado × artigo oficial (a MESMA função nos dois lados)."""
    t = _APOS.sub("'", _ASPAS.sub("", _base(t)))
    return re.sub(r"\s+", " ", t).strip().casefold()


def confere_trecho(citado: str, oficial: str) -> bool:
    return normalizar(citado).strip("'").strip() in normalizar(oficial)


# ------------------------------------------------------------------ estrutura do artigo
def _estrutura(t: str) -> str:
    """Mantém as quebras de linha (marcam início de dispositivo) e a caixa (romano é maiúsculo)."""
    t = _base(t)
    t = re.sub(r"§\s+", "§ ", t)  # o Planalto quebra linha no meio ("§\n1º")
    t = re.sub(r"[ \t]+", " ", t)
    return t


RX_PAR = re.compile(r"§ ?(\d+)\s*" + ORD + r"?(?:-([A-Z])\b)?|par[aá]grafo [uú]nico", re.I)
ROMANO = r"[IVXLC]+"


def _rx_inciso(rom: str) -> str:
    return r"(?<![A-Za-z0-9])" + rom + r"\s*-\s"


def _rx_alinea(letra: str) -> str:
    return r"(?<![A-Za-z0-9])" + re.escape(letra) + r"\)\s"


def _inicio_de_linha(t: str, pos: int) -> bool:
    i = pos - 1
    while i >= 0 and t[i] == " ":
        i -= 1
    return i < 0 or t[i] == "\n"


def _achar(t: str, rx: str, ini: int, fim: int) -> list[int]:
    """Posições do marcador entre ini e fim; as de início de linha (dispositivo) vêm primeiro."""
    achados = [m.start() for m in re.finditer(rx, t[ini:fim])]
    estruturais = [ini + p for p in achados if _inicio_de_linha(t, ini + p)]
    return estruturais or [ini + p for p in achados]


def _fim_paragrafo(t: str, pos: int, fim: int) -> int:
    for m in RX_PAR.finditer(t, pos + 2, fim):
        if _inicio_de_linha(t, m.start()):
            return m.start()
    return fim


def _chave_par(par: str):
    p = _estrutura(par).strip()
    if re.fullmatch(r"par[aá]grafo [uú]nico", p, re.I):
        return ("pu",)
    m = re.fullmatch(r"§ ?(\d+)\s*" + ORD + r"?(?:\s*-\s*([A-Za-z]))?", p)
    if not m:
        return None
    return ("§", int(m.group(1)), (m.group(2) or "").upper())


def _chave_de(m) -> tuple:
    if m.group(1) is None:
        return ("pu",)
    return ("§", int(m.group(1)), (m.group(2) or "").upper())


def localizar(texto_oficial: str, par=None, inc=None, ali=None) -> tuple[list[str], list[str]]:
    """Localiza par, inc e ali no artigo. Devolve (erros, avisos); erro reprova a citação."""
    erros, avisos = [], []
    t = _estrutura(texto_oficial)
    ini, fim = 0, len(t)
    par = (par or "").strip()
    inc = (inc or "").strip()
    ali = (ali or "").strip()
    if par:
        chave = _chave_par(par)
        if chave is None:
            erros.append(f"par={par!r} (data-par) fora do formato ('§ 2º', '§ 4º-A' ou 'parágrafo único')")
            return erros, avisos
        cands = [m for m in RX_PAR.finditer(t) if _chave_de(m) == chave]
        estr = [m for m in cands if _inicio_de_linha(t, m.start())]
        if not cands:
            erros.append(f"par={par!r} (data-par) não aparece no artigo oficial")
            return erros, avisos
        m = (estr or cands)[0]
        ini, fim = m.start(), _fim_paragrafo(t, m.start(), len(t))
    if inc:
        m = re.fullmatch(r"(" + ROMANO + r")(?:-([A-Z]))?", inc)
        if re.fullmatch(r"[a-z]\)?", inc):
            erros.append(f"inc={inc!r} (data-inc) é ALÍNEA, não inciso: use o campo 'ali' (data-ali)")
            return erros, avisos
        if not m:
            erros.append(f"inc={inc!r} (data-inc) fora do formato: inciso em algarismo romano (ex. 'II', 'I-B')")
            return erros, avisos
        rom = re.escape(inc)
        pos = _achar(t, _rx_inciso(rom), ini, fim)
        if not pos and "I" in m.group(1):
            # I/l/1 confundidos no texto oficial: aceito só se inequívoco
            fuzzy = "".join("[Il1]" if c == "I" else c for c in m.group(1)) + (
                "-" + m.group(2) if m.group(2) else ""
            )
            cands = []
            for p in _achar(t, _rx_inciso("(" + fuzzy + ")"), ini, fim):
                tok = re.match(fuzzy, t[p:]).group(0)
                if re.search(r"[IVXLC]", tok) and tok not in cands:
                    cands.append(tok)
            if len(cands) == 1:
                pos = _achar(t, _rx_inciso(re.escape(cands[0])), ini, fim)
                avisos.append(f"inc={inc!r}: o texto oficial traz {cands[0]!r} (I/l/1 trocados no Planalto)")
            elif len(cands) > 1:
                erros.append(f"inc={inc!r} (data-inc) ambíguo no artigo oficial: {cands}")
                return erros, avisos
        if not pos:
            onde = f" dentro de {par}" if par else ""
            erros.append(f"inc={inc!r} (data-inc) não aparece como inciso{onde} no artigo oficial")
            return erros, avisos
        p0 = pos[0]
        prox = [
            x.start()
            for x in re.finditer(_rx_inciso(ROMANO + r"(?:-[A-Z])?"), t[p0 + 1 : fim])
            if _inicio_de_linha(t, p0 + 1 + x.start())
        ]
        ini, fim = p0, (p0 + 1 + prox[0]) if prox else fim
    if ali:
        letra = ali.rstrip(")").strip()
        if not re.fullmatch(r"[a-z]", letra):
            erros.append(f"ali={ali!r} (data-ali) fora do formato: alínea é uma letra minúscula (ex. 'a')")
            return erros, avisos
        if not _achar(t, _rx_alinea(letra), ini, fim):
            onde = f" dentro de {', '.join(x for x in (par, inc and 'inciso ' + inc) if x)}" if (par or inc) else ""
            erros.append(f"ali={ali!r} (data-ali) não aparece como alínea{onde} no artigo oficial")
    return erros, avisos


def conferir_citacao(c: dict, oficial: dict) -> tuple[list[str], list[str]]:
    """Confere uma citação {lei, art, par, inc, ali, texto} contra a base oficial {chave: {texto…}}.
    Devolve (erros, avisos). As frases trazem os dois vocabulários (campo do JSON e atributo do HTML)."""
    erros, avisos = [], []
    lei, art = c.get("lei"), c.get("art")
    if not lei:
        erros.append("lei sem chave ('lei', ex. CP) — citação sem data-lei")
    if not art:
        erros.append("lei sem artigo ('art') — citação sem data-art")
    if not lei or not art:
        return erros, avisos
    chave = f"{lei}:{art}"
    of = oficial.get(chave)
    if not of:
        erros.append(
            f"'{chave}' não existe em assets/lei_seca_oficial.json "
            "(não está no texto oficial baixado: não dá para conferir, lacuna a coletar)"
        )
        return erros, avisos
    txt = c.get("texto")
    if not isinstance(txt, str) or len(normalizar(txt).strip("'").strip()) < 8:
        erros.append("falta 'texto' (trecho exato do texto oficial): trecho citado vazio ou curto demais para conferir")
    elif not confere_trecho(txt, of.get("texto", "")):
        erros.append(
            f"texto não confere com o oficial de {chave}: o texto citado DIFERE do vigente "
            f"(baixado em {of.get('baixado_em')}): {normalizar(txt)[:90]!r}"
        )
    e, a = localizar(of.get("texto", ""), c.get("par"), c.get("inc"), c.get("ali"))
    return erros + e, avisos + a


# ------------------------------------------------------------------ súmulas
def id_sumula(rotulo: str) -> str | None:
    """'STJ-593' → 'SUM-STJ-593'; 'STF-473' → 'SUM-STF-473'; 'SV-13' → 'SV-13' (chaves de assets/sumulas.json)."""
    m = re.fullmatch(r"\s*(STJ|STF|SV)\s*-?\s*(\d+)\s*", rotulo or "", re.I)
    if not m:
        return None
    trib, num = m[1].upper(), m[2]
    return f"SV-{num}" if trib == "SV" else f"SUM-{trib}-{num}"


def tribunal_sumula(rotulo: str) -> str | None:
    sid = id_sumula(rotulo)
    if not sid:
        return None
    return "STF" if sid.startswith("SV-") else sid.split("-")[1]


RX_CANCELADA = re.compile(r"(?:^|[.•;]\s*)(cancelada|superada)(\s+em\s+parte)?\s*\.?\s*(?:•|$)", re.I | re.M)


def situacao_sumula(s: dict) -> str | None:
    """A base não tem campo de situação: o texto traz '• Cancelada.' ou 'Superada.' ao fim. Campo 'situacao', se
    um dia existir, vale primeiro."""
    sit = (s.get("situacao") or "").strip().lower()
    if sit in ("cancelada", "superada", "superada em parte"):
        return sit
    m = RX_CANCELADA.search(s.get("texto", ""))
    if m:
        return (m[1] + (" em parte" if m[2] else "")).lower()
    return None


# ------------------------------------------------------------------ autoteste
def autoteste() -> int:
    cp13 = (
        "Art. 13 - O resultado, de que depende a existência do crime, somente é imputável a quem lhe deu causa.\n"
        "Superveniência de causa independente (Incluído pela Lei nº 7.209, de 11.7.1984)\n"
        "§ 1º - A superveniência de causa relativamente independente exclui a imputação quando, por si só, "
        "produziu o resultado.\n"
        "§ 2º - A omissão é penalmente relevante quando o omitente devia e podia agir para evitar o resultado. "
        "O dever de agir incumbe a quem:(Incluído pela Lei nº 7.209, de 11.7.1984)\n"
        "a) tenha por lei obrigação de cuidado, proteção ou vigilância;\n"
        "b) de outra forma, assumiu a responsabilidade de impedir o resultado;\n"
        "c) com seu comportamento anterior, criou o risco da ocorrência do resultado."
    )
    cpp78 = (
        "Art. 78. Na determinação da competência por conexão ou continência, serão observadas as seguintes "
        "regras:\nI - no concurso entre a competência do júri e a de outro órgão, prevalecerá a do júri;\n"
        "Il - no concurso de jurisdições da mesma categoria:\na) preponderará a do lugar da infração;\n"
        "III - no concurso de jurisdições de diversas categorias, predominará a de maior graduação;\n"
        "IV - no concurso entre a jurisdição comum e a especial, prevalecerá esta."
    )
    l7960 = (
        "Art. 2° A prisão temporária será decretada pelo Juiz.\n§ 1° Na hipótese de representação, o Juiz "
        "ouvirá o Ministério Público.\n§ 2° O despacho que decretar a prisão temporária deverá ser fundamentado."
        "\n§ 4º-A O mandado de prisão conterá o período.\n§ 7º Decorrido o prazo, o preso em liberdade."
    )
    cp7 = (
        "Art. 7º - Ficam sujeitos à lei brasileira:\nI - os crimes:\na) contra a vida do Presidente;\n"
        "II - os crimes:\na) que, por tratado, o Brasil se obrigou a reprimir;\n"
        "§ 2º - Nos casos do inciso II, a aplicação depende das condições:\na) entrar o agente no território "
        "nacional;\nb) ser o fato punível também no país;"
    )
    cf5 = "Art. 5º Todos são iguais:\nXI - a casa é asilo;\nXL - a lei penal não retroagirá;\nXLI - a lei punirá;"
    lmp = "Art. 12. Feito o registro:\nI - ouvir a ofendida;\nI-A - colher provas;\nI-B - solicitar;\nII - ouvir"
    amb = "Art. 9. Regras:\nIl - primeira;\nlI - segunda;"
    casos = [  # (nome, texto, par, inc, ali, deve passar?, motivo que o erro tem de citar)
        ("alínea com par passa (CP 13, § 2º, a)", cp13, "§ 2º", None, "a", True, None),
        ("alínea marcada como inciso acusa (CP 13, § 2º, inc 'a')", cp13, "§ 2º", "a", None, False, "ALÍNEA"),
        ("alínea inexistente no parágrafo acusa (CP 13, § 1º, d)", cp13, "§ 1º", None, "d", False, "data-ali"),
        ("alínea de outro parágrafo acusa (CP 13, § 1º, a)", cp13, "§ 1º", None, "a", False, "data-ali"),
        ("'Il' do Planalto aceito como II (CPP 78)", cpp78, None, "II", None, True, None),
        ("alínea dentro do inciso 'Il' passa (CPP 78, II, a)", cpp78, None, "II", "a", True, None),
        ("alínea fora do inciso acusa (CPP 78, III, a)", cpp78, None, "III", "a", False, "data-ali"),
        ("inciso inexistente acusa (CPP 78, V)", cpp78, None, "V", None, False, "data-inc"),
        ("'§ 2º' acha '§ 2°' (sinal de grau, Lei 7.960)", l7960, "§ 2º", None, None, True, None),
        ("'§ 2o' (letra o) acha '§ 2°'", l7960, "§ 2o", None, None, True, None),
        ("§ 4º-A passa", l7960, "§ 4º-A", None, None, True, None),
        ("§ 4º sem o A acusa (não confunde com § 4º-A)", l7960, "§ 4º", None, None, False, "data-par"),
        ("§ 3º inexistente acusa", l7960, "§ 3º", None, None, False, "data-par"),
        ("CP 7, § 2º, a passa", cp7, "§ 2º", None, "a", True, None),
        ("CP 7, § 2º, c acusa (só há a e b no trecho)", cp7, "§ 2º", None, "c", False, "data-ali"),
        ("XI não casa com XL (romano exato)", cf5, None, "XI", None, True, None),
        ("XLII inexistente acusa", cf5, None, "XLII", None, False, "data-inc"),
        ("I-B passa", lmp, None, "I-B", None, True, None),
        ("I-C inexistente acusa", lmp, None, "I-C", None, False, "data-inc"),
        ("I/l confundido e AMBÍGUO acusa", amb, None, "II", None, False, "ambíguo"),
        ("par fora do formato acusa", cp13, "segundo parágrafo", None, None, False, "fora do formato"),
    ]
    falhas = 0
    for nome, txt, par, inc, ali, deve, motivo in casos:
        e, _ = localizar(txt, par, inc, ali)
        ok = (not e) if deve else (bool(e) and any(motivo in x for x in e))
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} {nome}{'' if not e else ' · ' + e[0][:80]}")
    # o trecho: anotação no meio, º × °, aspas e travessão não acusam; letra trocada acusa
    of = "§ 2° O despacho (Redação dada pela Lei nº 1) que decretar a prisão – deverá ser fundamentado."
    for nome, cit, deve in (
        ("trecho com anotação no meio e º/° trocados passa", "“§ 2º O despacho que decretar a prisão - deverá", True),
        ("trecho com uma palavra trocada acusa", "O despacho que revogar a prisão", False),
    ):
        ok = confere_trecho(cit, of) == deve
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} {nome}")
    for rot, esperado in (("SV-14", "SV-14"), ("STJ-593", "SUM-STJ-593"), ("STF-711", "SUM-STF-711"),
                          ("STJ-V-1", None)):
        ok = id_sumula(rot) == esperado
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} id_sumula({rot!r}) = {id_sumula(rot)!r}")
    ok = tribunal_sumula("SV-14") == "STF"
    falhas += not ok
    print(f"  {'✅' if ok else '❌'} súmula vinculante é do STF")
    print("[AUTOTESTE OK]" if not falhas else f"[AUTOTESTE FALHOU] {falhas} caso(s)")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if "--autoteste" in sys.argv:
        sys.exit(autoteste())
    print(__doc__)
    sys.exit(2)
