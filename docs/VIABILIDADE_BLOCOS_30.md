# Viabilidade — gerar em blocos de 30 e passar pelos 503 pontos do edital

> Análise de 31/10/2026, 19h05, pedida pelo titular. **Medido** = lido ou contado nesta data;
> **deduzido** vem marcado como tal. Nenhum PDF de terceiro foi copiado para o repositório.

## Veredito

**É viável.** O Trilha já gera do acervo local (o servidor busca trechos dos PDFs indexados para cada
questão) e já tem o controle do edital verticalizado. O que falta é: (1) o **bloco de 30** com
pré-geração do próximo bloco, (2) o **arquivo acumulado** que cresce a cada bloco, (3) a **baixa por
correlação** e (4) **indexar o acervo grande** que hoje não entra na geração.

## O que existe hoje (medido)

- Geração: **1 questão por ponto, por rodada** (2 rodadas), uma a uma, com pré-geração só da próxima
  (`servidor.py`, `generate` / `submit`, 2 geradores em paralelo). Auditoria dupla ligada por padrão.
- Acervo já indexado (`ferramentas/construir_base.py`): LD Delegado AOCP, LD Juris, Atualizações
  2026.1, Lei 15.487, 7 esclarecimentos, 6 aulas Delta PE, súmulas por disciplina e 11 leis secas —
  **744 páginas de 26 arquivos** em `fontes_paginas.json`.
- **Não registra** tempo, número de chamadas nem tokens por questão. *Deduzido* pelas datas do cache
  de 27/10: ~1,5 a 2 min por questão com 2 geradores, numa versão anterior do servidor.

## Acervo local que AINDA NÃO entra na geração (medido)

Pasta `Área de Trabalho/DELEGADO BA` — todos com texto extraível:

| material | páginas |
| --- | ---: |
| Resumo Destacado — Direito Administrativo | 862 |
| Resumo Destacado — Direito Constitucional | 908 |
| Resumo Destacado — Penal, Parte Especial | 766 |
| Resumo Destacado — Penal, Parte Geral | 578 |
| Resumo Destacado — Processual Penal | 943 |
| Resumo Destacado — Direitos Humanos | 530 |
| Resumo Destacado — Legislação Penal Extravagante | 416 |
| Resumo Destacado — Criminologia | 99 |
| Resumo Destacado — Medicina Legal | 124 |
| Jurisprudência — Informativos 2023 a 2026 | 1.082 |
| Jurisprudência — Súmulas STF, STJ e TSE · Teses RG · Repetitivos | 726 |

⚠️ Os 4 arquivos "RESUMO DESTACADO-DELEGADO PCPR-1 a 4.pdf" **não são PDF: são ZIP renomeados**. O
PCPR-1 tem **26 resumos de leis extravagantes** (Drogas, Maria da Penha, Desarmamento, Abuso de
Autoridade, Tortura, Lavagem…); o PCPR-2, 3 e 4 têm **o mesmo conteúdo** (16 resumos de Penal, parte
geral) — três cópias.

## Cobertura dos 503 pontos (deduzida do casamento disciplina × material)

| situação | disciplinas | pontos |
| --- | --- | ---: |
| **Bem coberta** (resumo + lei seca + jurisprudência) | Penal 74 · Administrativo 71 · Constitucional 62 · Proc. Penal 41 · Extravagante 40 · Criminologia 24 · Medicina Legal 21 · Ambiental 16 | **349 (69,4%)** |
| **Parcial** (só questões AOCP de estilo, ou material indireto) | Informática 34 · Raciocínio Lógico 23 · Igualdade Racial e de Gênero 18 · Português 10 | **85 (16,9%)** |
| **Fraca** (sem material local) | Tributário 36 · Civil e Empresarial 14 · Proc. Civil 12 · Legislação Geral 5 · Atualidades 2 | **69 (13,7%)** |

Soma conferida: 349 + 85 + 69 = 503. **Remédio para a faixa fraca:** a lei seca oficial (CTN, Código
Civil, CPC, leis estaduais da Bahia) se baixa do Planalto e da Casa Civil da BA — fonte pública,
pelo `atualizar_lei_seca.py` já existente; a doutrina dessas matérias fica com o modelo, e o
comentário precisa dizer isso.

## Provas da AOCP para a "engenharia reversa" da banca (medido)

Em `Downloads/AOCP*.pdf` (exportações do Qconcursos): **257 questões distintas** por código, de
**2006 a 2026**. Só **~55 são de Direito em concurso de Delegado** (PC-PA 2021, PC-GO 2022); o resto é
Português, Informática e Raciocínio Lógico de outros cargos. `AOCP INFO 05,.pdf` é cópia do INFO 04.
**Basta para um perfil de estilo** (tamanho do enunciado, "assinale a correta/incorreta", padrão das
alternativas, pegadinhas recorrentes); **não basta** para estatística por assunto do edital da BA.

## Os links do ChatGPT

- **Link compartilhado** (`/share/6ae663f0…`): lido pelo HTML cru (3,2 MB). É a **conversa em que o
  próprio Trilha foi construído** — não traz base de dados além da que já está aqui. Cita 6 arquivos
  que **não estão nesta máquina** (CF no DOU, súmulas do STJ, repercussão geral do STF, um livro de
  Direitos Humanos e dois outros), todos de fonte pública ou já cobertos.
- **Link do projeto** (`/g/g-p-…/project`): **exige o login do titular** — não acessível daqui.
  Se houver arquivos lá que não estão no computador, baixá-los para a pasta DELEGADO BA.

## Desenho proposto

1. **Indexar o acervo grande** (ampliar `construir_base.py`): os 9 resumos, os informativos, os 26
   resumos do PCPR-1 e **um** dos PCPR-2/3/4. Material de terceiro: **só local, fora do Git** (D-002).
2. **Bloco de 30**: os próximos 30 pontos pendentes, na ordem da trilha, 1 questão por ponto. Ao
   abrir um bloco, o servidor já começa a gerar o seguinte. Comando na tela: "Gerar próximo bloco".
3. **Arquivo acumulado**: um único arquivo (`historico/trilha_acumulada.json` + exportação em HTML
   para ler/imprimir) **sobrescrito a cada bloco, sempre com tudo** — questão, resposta, gabarito,
   lei, jurisprudência, comentário e data. Nada se apaga (§F17).
4. **Baixa por correlação**: o comentário aponta pontos correlatos **só da lista do `items.json`**
   (validado); a tela marca como "visto por correlação" — distinto de "respondido".
5. **Medir antes de escalar** (§F15): cada questão passa a registrar duração, chamadas e tokens; o
   primeiro bloco dá o custo e o tempo **reais** de um bloco de 30.

## O que só o titular decide

- A baixa por correlação é **automática** ou **sugerida e confirmada** por ele?
- O arquivo acumulado é só dentro do app, ou também um **HTML/PDF** para ler fora?
- Manter a **auditoria dupla** (mais caro e mais lento, menos erro) nos blocos de 30?
