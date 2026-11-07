# Revisão por prioridade — Delegado PC-BA (AOCP)

> Pedido do titular, 06/11/2026, 20h55 (D-018). Plano escrito às 21h01. Nada de conteúdo gerado ainda.

## O que é

Um material de revisão no **estilo caderno** (o mesmo dos cadernos de Lei Maria da Penha e de Crimes contra a
Administração Pública, em `../apostilas-direito-penal/entregas/`): folha pautada, blocos, quadros "No dia a dia" e
"Detalhe técnico", fichas de certo ou errado, fichário da lei seca, saída em HTML interativo e PDF. Ele passa por
**todos os 503 pontos do edital verticalizado** (`assets/items.json`), na **ordem de prioridade para o concurso**,
no nível de delegado, para revisar rápido e com qualidade.

## Fontes, todas já na máquina

| fonte | onde | entra como |
| --- | --- | --- |
| Edital verticalizado (503 itens, 17 disciplinas) | `assets/items.json` | esqueleto e cobertura (nenhum ponto fica de fora) |
| Edital (distribuição de questões por disciplina) | `../DELEGADO BA/EDITAL DELEGADO BAHIA.pdf` | peso de cada disciplina |
| Provas AOCP (6 gerais, 6 de Informática, 9 de Português, 3 de Raciocínio Lógico) | `Downloads/AOCP *.pdf` | **incidência** de cada ponto e o jeito da banca cobrar |
| Questões objetivas da Trilha | `cache/*.json` (66 pontos gerados) | fichas e exercícios |
| Simulados DPC-BA (4 × 100) e as 18 peças da discursiva | `discursiva/` | exercícios e a ponte com a discursiva |
| Base do curso | `../DELEGADO BA/` (144 PDFs) | doutrina e esquemas (uso pessoal) |
| Lei seca oficial (Planalto) e súmulas/teses | `assets/lei_seca_oficial.json`, `sumulas.json`, `teses_rg.json` | texto de lei e jurisprudência |

## Prioridade — como se mede

A prioridade que veio no edital verticalizado (Alta, Média-alta, Regular) **não diz como foi calculada**. A nova é
medida: **peso da disciplina na prova** (quantas questões o edital dá a ela) × **incidência do ponto nas provas
AOCP** (quantas vezes ele aparece), com a prioridade antiga como desempate. O método e a tabela ficam em
`docs/REVISAO_PRIORIDADE.md`, com o que a régua não conseguiu classificar **contado e listado** (§F10).

## Módulos correlatos

**Ordem decidida (D-019, por rendimento):** 1. Igualdade racial e de gênero, Legislação geral e Atualidades ·
2. Língua Portuguesa · 3. Informática e Raciocínio Lógico · 4. Penal · 5. Processo Penal e inquérito ·
6. Legislação penal extravagante · 7. Criminologia e Medicina Legal · 8. Civil, Empresarial e Processo Civil ·
9. Constitucional · 10. Administrativo · 11. Ambiental · 12. Tributário. A medida está em
`docs/REVISAO_PRIORIDADE.md`. A lista abaixo é a do plano original, agrupada por assunto:

Penal (geral e especial) · Processo Penal e inquérito · Legislação penal extravagante · Constitucional ·
Administrativo · Criminologia e Medicina Legal · Tributário · Civil, Empresarial e Processo Civil · Ambiental ·
Igualdade racial e de gênero, Legislação geral e Atualidades · Língua Portuguesa · Informática e Raciocínio Lógico.

Cada ponto do edital, dentro do módulo, tem: **o que cai** (núcleo em nível de delegado) · **lei seca** com o texto
oficial · **jurisprudência** com fonte e data · **pegadinhas da AOCP** · **no dia a dia do delegado** · **fichas de
certo ou errado** e questões · **checklist** do ponto.

## Rotina contra conteúdo desatualizado

1. **Antes de gerar qualquer módulo**, a lei seca oficial é baixada de novo se tiver mais de 30 dias
   (`atualizar_lei_seca.bat`).
2. **Todo artigo citado é conferido** contra o texto oficial vigente: diferença reprova a geração.
3. **Toda jurisprudência leva fonte e data**; súmula cancelada ou superada é barrada.
4. **Cada módulo traz o carimbo** "conferido em DD/MM/AAAA" e a lista do que é sensível a mudança.
5. **O verificador** (`ferramentas/verificar_atualidade.py`, com `--autoteste`) vira porta do portão e roda
   **toda semana** sozinho, com relatório do que mudou.

## Onde fica e o Git

O gerador, o mapa de prioridade e o verificador entram no Git. **Os módulos gerados ficam fora do Git**, porque
usam material de terceiro (a pasta DELEGADO BA não entra em Git nenhum, CLAUDE.md da pasta-mãe; mesma solução da
D-017). A Trilha é estudo pessoal e não vai para o portal (D-009).

## Ordem de trabalho

1. **Fase 0:** mapa de prioridade medido + rotina de atualidade + extração das provas AOCP.
2. **Piloto:** o módulo de maior prioridade, para o titular aprovar o formato.
3. **Ondas de 2 módulos** (§F19), até cobrir os 503 pontos, conferindo a cobertura a cada onda.

**Fica de fora, por enquanto:** áudio e vídeo. **Lacuna declarada:** o método da prioridade antiga.

## Prazo — prova objetiva em 06/12/2026 (titular, 06/11/2026, 21h09: *"6 de dezembro"*)

Contados a partir de 06/11/2026: **30 dias**. Calendário proposto (a ordem dos módulos sai da prioridade medida):

| período | o quê |
| --- | --- |
| até 13/11 | todos os 12 módulos gerados (2 por dia depois do piloto aprovado); o titular já estuda o 1º e o 2º |
| 07/11 a 27/11 | primeira passada por todos os 503 pontos, na ordem de prioridade (≈ 24 pontos por dia em 21 dias; os de prioridade baixa no modo "Só o essencial") |
| 28/11 a 03/12 | segunda passada só nos pontos de prioridade alta e nas fichas erradas + simulados |
| 04/12 e 05/12 | lei seca dos pontos de maior incidência e descanso; a rotina de atualidade roda uma última vez em 04/12 |
