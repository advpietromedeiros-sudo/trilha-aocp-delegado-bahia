"""Verificador de referências proibidas no texto final da Revisão Delegado PC-BA.

Nada de nome de outra banca, de cursinho ou de material de terceiro no material entregue, e o autor
se escreve "Professor Pietro Medeiros" (nunca abreviado). A regex parte da usada nas apostilas do
titular (apostilas-direito-penal/ferramentas/gerar_apostilas.py, 05/11/2026) e acrescenta o
"Projeto em Delta", "Delta" e nomes de cursinhos.

Uso:  python ferramentas/referencias_proibidas.py ARQUIVO...   (sai 1 se achar referência)
      python ferramentas/referencias_proibidas.py --autoteste  (REGRA CINCO: planta referências
                                                                 e só sai 0 se o verificador ACUSAR)
Também é importado por ferramentas/gerar_revisao.py, que recusa gerar o módulo com achado.
"""

import re
import sys
from pathlib import Path

# 1) a regex das apostilas, sem mudança
_APOSTILAS = (
    r"CEBRASPE|Cebraspe|FGV|VUNESP|PC-PR|PCSP|PCRN|DPF/|\bMP[A-Z]{2}/\d|\bTJ[A-Z]{2}/\d|"
    r"material do curso|material-base|material de aula|Resumo Destacado|Prof\. Pietro"
)
# 2) acréscimos da revisão: o curso de origem do material, outras bancas e cursinhos
_ACRESCIMOS = (
    r"Projeto em Delta|\bDelta\b|\bDELTA\b|"
    r"\bCESPE\b|\bCespe\b|\bFCC\b|Funda[cç][aã]o Carlos Chagas|\bIBFC\b|\bIDECAN\b|\bIADES\b|"
    r"\bQuadrix\b|\bFUNDATEC\b|\bFUMARC\b|\bNUCEPE\b|\bCESGRANRIO\b|\bCesgranrio\b|\bConsulplan\b|"
    r"Instituto Acesso|\bFAPEC\b|\bUPENET\b|"
    r"Estrat[eé]gia Concursos|Estrat[eé]gia Carreira|\bGran Cursos\b|\bGran Concursos\b|\bCERS\b|"
    r"Dam[aá]sio|\bLFG\b|\bAlfaCon\b|\bAlfacon\b|\bMege\b|\bMEGE\b|Supremo TV|\bQConcursos\b|"
    r"\bQconcursos\b|TEC Concursos|Tec Concursos|Aprova Concursos|Casa do Concurseiro|"
    r"Dire[cç][aã]o Concursos|Focus Concursos|[ÊE]nfase Concursos|Curso F[oó]rum|"
    r"Dizer o Direito|Juspodivm|JusPodivm|Ponto dos Concursos|Prof\. "
)
PROIBIDO = re.compile(_APOSTILAS + "|" + _ACRESCIMOS)


def achados(texto):
    """Lista ordenada (sem repetição) das referências proibidas encontradas."""
    return sorted(set(m.group(0) for m in PROIBIDO.finditer(texto)))


def verificar(texto, nome):
    """Para com SystemExit se o texto tiver referência proibida."""
    a = achados(texto)
    if a:
        raise SystemExit(f"[FALHA] {nome}: referências proibidas: {a}")


def autoteste():
    plantados = {
        "banca das apostilas": "QUESTÃO 1 · ESTILO CEBRASPE",
        "curso de origem": "Simulado 3 do Projeto em Delta, questão 12",
        "nome curto do curso": "comentário do Delta sobre o art. 4º",
        "cursinho": "resumo do Estratégia Concursos",
        "outra banca": "questão da FCC de 2019",
        "autor abreviado": "Prof. Pietro Medeiros",
    }
    falhas = []
    for rotulo, txt in plantados.items():
        try:
            verificar(txt, rotulo)
        except SystemExit:
            print(f"  acusou: {rotulo}")
        else:
            falhas.append(rotulo)
    limpo = (
        "Revisão Delegado PC-BA · Professor Pietro Medeiros · pegadinhas da AOCP · Delegado de Polícia · "
        "delegacia · Lei 13.964/2019 · STF, Súmula 145 · deltas e DELEGADO não são o curso"
    )
    try:
        verificar(limpo, "texto limpo")
    except SystemExit as e:
        falhas.append(f"falso positivo no texto limpo: {e}")
    if falhas:
        print(f"[AUTOTESTE FALHOU] {falhas}")
        return 1
    print(f"[AUTOTESTE OK] acusou as {len(plantados)} referências plantadas e aprovou o texto limpo")
    return 0


def main(argv):
    if "--autoteste" in argv:
        return autoteste()
    arquivos = [a for a in argv if not a.startswith("--")]
    if not arquivos:
        print(__doc__)
        return 2
    rc = 0
    for a in arquivos:
        p = Path(a)
        enc = achados(p.read_text(encoding="utf-8"))
        if enc:
            print(f"[FALHA] {p.name}: {enc}")
            rc = 1
        else:
            print(f"[OK] {p.name}: nenhuma referência proibida")
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
