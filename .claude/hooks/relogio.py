#!/usr/bin/env python3
"""relogio.py — injeta a DATA E HORA REAIS no começo de cada turno (hook `UserPromptSubmit`).

🔴 ORDEM CANÔNICA DO TITULAR (13/10/2026), textual: *"Acrescente como regra canônica em todos os
repositorios para você informar a data completa com hora e minutos em cada resposta que você
apresentar durante as interações de chat"*. A regra é a **G1.6** do HARNESS; este arquivo é
o **enforcement** dela. Desde 24/10/2026 lembra também a **G1.7** (*"me informar do progresso de
suas atividades"*).

💥 POR QUE UM HOOK, E NÃO SÓ A REGRA ESCRITA. A data que o sistema me entrega na abertura é a do
INÍCIO da sessão, e uma sessão pode durar **vários dias** — o `/abertura` existe justamente
porque isso já me fez dizer "hoje" sobre anteontem. Sem este hook, cumprir a G1.6 exigiria rodar
`date` antes de cada resposta: 1 chamada de ferramenta por turno, ou — o que de fato aconteceria —
eu repetindo de memória a hora da última vez que olhei. Regra que depende da minha memória já
falhou oito vezes num único bloco de trabalho (20/jul/2026).

⚡ CUSTO MEDIDO: ~250 ms, uma vez por mensagem do titular (é a partida do Python no Windows, não o
trabalho, medido em 22/08/2026). Não roda por ferramenta: numa
sessão de 500 chamadas, custa zero a mais. Por isso é hook de `UserPromptSubmit`, nunca de
`PostToolUse`.

🔒 NÃO LÊ NADA. O corpo do prompt chega no stdin e é **ignorado** — este hook não abre o stdin, não
grava arquivo, não faz rede. Só imprime a hora do relógio da máquina.

🔑 O FUSO É MEDIDO, NÃO FIXADO. O titular pode estar em qualquer fuso, mas quem responde é o relógio
da estação: se um dia a sessão rodar de outra máquina ou de outro fuso, a linha diz o fuso de lá, e
não uma afirmação minha sobre onde ele está (REGRA ZERO).

Autoteste: `python relogio.py --autoteste`
"""

from __future__ import annotations

import sys
from datetime import datetime

DIAS = (
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
    "sábado",
    "domingo",
)


def linha(agora: datetime) -> str:
    """A linha que vai para o contexto do turno. Pura, para o autoteste provar o formato."""
    dia = DIAS[agora.weekday()]
    # `%z` vem como "-0300"; vira "GMT-3" (e "GMT-3:30" onde o fuso tiver meia hora).
    bruto = agora.strftime("%z") or "+0000"
    sinal, hh, mm = bruto[0], int(bruto[1:3]), int(bruto[3:5])
    fuso = f"GMT{sinal}{hh}" + (f":{mm:02d}" if mm else "")
    return (
        f"🕐 AGORA: {agora:%d/%m/%Y} ({dia}), {agora:%H}h{agora:%M} ({fuso}) — "
        f"a G1.6 manda ABRIR a resposta com esta data e hora, e a G1.7, relatar o PROGRESSO "
        f"(passo contado entre as ferramentas; feito, pendente e próximo no fim)."
    )


def _autoteste() -> int:
    from datetime import timedelta, timezone

    falhas = []

    def prova(desc: str, obtido: object, esperado: object) -> None:
        if obtido == esperado:
            print(f"  ✅ {desc}")
        else:
            falhas.append(desc)
            print(f"  ❌ {desc}\n       obtido   {obtido!r}\n       esperado {esperado!r}")

    tz3 = timezone(timedelta(hours=-3))
    prova(
        "terça-feira 13/10/2026 21h29 em GMT-3",
        linha(datetime(2026, 10, 13, 21, 29, tzinfo=tz3)),
        "🕐 AGORA: 13/10/2026 (terça-feira), 21h29 (GMT-3) — "
        "a G1.6 manda ABRIR a resposta com esta data e hora, e a G1.7, relatar o PROGRESSO "
        "(passo contado entre as ferramentas; feito, pendente e próximo no fim).",
    )
    prova(
        "a linha lembra a G1.7 (progresso)",
        "G1.7" in linha(datetime(2026, 10, 24, 5, 55, tzinfo=tz3)),
        True,
    )
    prova(
        "meia-noite e um minuto sai com os dois zeros",
        linha(datetime(2026, 1, 5, 0, 1, tzinfo=tz3)).split(", ")[1].split(" — ")[0],
        "00h01 (GMT-3)",
    )
    prova(
        "domingo é o último dia da semana (weekday 6)",
        linha(datetime(2026, 10, 18, 9, 0, tzinfo=tz3)).split("(")[1].split(")")[0],
        "domingo",
    )
    prova(
        "fuso de meia hora não some",
        linha(datetime(2026, 10, 13, 12, 0, tzinfo=timezone(timedelta(hours=5, minutes=30))))
        .split(" (")[2]
        .split(" — ")[0],
        "GMT+5:30)",
    )
    prova(
        "sem fuso na data, assume GMT+0 em vez de quebrar",
        "GMT+0" in linha(datetime(2026, 10, 13, 12, 0)),
        True,
    )
    print()
    if falhas:
        print(f"❌ {len(falhas)} falha(s): {falhas}")
        return 1
    print("✅ autoteste verde — 6 casos")
    return 0


if __name__ == "__main__":
    # §A7: fora do hook (ex.: `python -I`, portão de outra máquina) o console do Windows cai no
    # cp1252 e o "🕐" derruba o print. A saída é sempre UTF-8, independa do ambiente (31/10/2026).
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001 — stdout sem reconfigure (ex.: redirecionado exótico)
        pass
    if "--autoteste" in sys.argv:
        sys.exit(_autoteste())
    # HARNESS §P12.2: com o relógio do usuário registrado nesta máquina, este cede a vez — senão a
    # linha da hora sairia duas vezes a cada turno (§F22, ruído).
    from pathlib import Path

    try:
        _cfg = (Path.home() / ".claude" / "settings.json").read_text(encoding="utf-8")
        if Path(__file__).resolve().parent != (Path.home() / ".claude" / "hooks").resolve() and (
            ".claude/hooks/relogio.py" in _cfg.replace("\\", "/")
        ):
            sys.exit(0)
    except OSError:
        pass
    try:
        print(linha(datetime.now().astimezone()))
    except Exception as e:  # noqa: BLE001 — o relógio NUNCA pode derrubar o turno do titular
        print(
            f"[relogio] nao consegui ler a hora ({type(e).__name__}) — rode `date` antes de datar."
        )
    sys.exit(0)
