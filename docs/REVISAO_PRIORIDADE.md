# Revisão por prioridade — o mapa medido (Fase 0)

> Gerado por `ferramentas/classificar_incidencia.py` em 06/11/2026 22:20. Não edite à mão: rode de novo.
> Dados de máquina: `revisao/mapa_prioridade.json`. Plano: `docs/REVISAO_PLANO.md` (D-018).

## Método

1. **Provas AOCP** (24 cadernos exportados de uma plataforma de questões, na pasta Downloads do titular;
   procedência em `docs/PROCEDENCIA.md`) foram lidas por
   `ferramentas/extrair_provas_aocp.py`. O negrito dos cadernos (enunciado, número, letra e gabarito) é desenho
   vetorial, sem texto: o enunciado vem do OCR do próprio Windows (pt-BR) e o gabarito da forma do glifo, calibrada
   pelos círculos A–E de cada questão e conferida contra o OCR. Saída fora do Git (`revisao/dados/`).
2. **Questões únicas:** 443 extraídas, 60 repetidas entre cadernos (mesmo id da
   plataforma) → **383 únicas**, a base da incidência.
3. **Classificação** em (disciplina, item do edital) por palavras-chave: a régua é `revisao/mapa_palavras.json`
   (termos tirados do rótulo de cada item + sinônimos jurídicos escritos à mão). A disciplina dada pela plataforma
   limita as candidatas; o assunto dado pela plataforma vale 3, o enunciado e as alternativas valem 1; termo de
   várias palavras vale o dobro; cada termo é dividido pelo número de itens da disciplina que o usam (termo
   genérico pesa pouco). Classifica com **2,0 ponto** ou mais; abaixo disso fica **não classificada**.
4. **Peso da disciplina:** ver a tabela abaixo.

## Peso de cada disciplina na prova objetiva

O edital (Tabela 7.1, **p. 10**) dá só os blocos: **40 questões de Conhecimentos Gerais e 60 de Conhecimentos
Específicos**, 1,0 ponto cada, mínimo de 70 pontos. O Anexo I (**pp. 26–31**) diz o que é geral (7 disciplinas,
pp. 26–28) e o que é específico do Delegado (10 disciplinas, pp. 28–31). ⚠️ **O edital não diz quantas questões
cada disciplina tem.** A divisão dentro do bloco é **estimativa**: a média dos 4 simulados DPC-BA (que somam
exatamente 40 + 60). Se a banca distribuir diferente, a régua erra na mesma proporção.

| disciplina (items.json) | no Anexo I do edital | bloco | questões (estimadas) | questões AOCP classificadas |
| --- | --- | --- | ---: | ---: |
| LEGISLAÇÃO GERAL | mesmo nome, p. 28 | gerais | 8,00 | 0 |
| LÍNGUA PORTUGUESA | mesmo nome, p. 26 | gerais | 8,00 | 123 |
| RACIOCÍNIO LÓGICO | mesmo nome, p. 27 | gerais | 8,00 | 45 |
| ATUALIDADES | mesmo nome, p. 27 | gerais | 4,00 | 2 |
| INFORMÁTICA | mesmo nome, p. 27 | gerais | 4,00 | 94 |
| MEDICINA LEGAL | mesmo nome, p. 27 | gerais | 4,00 | 6 |
| PROMOÇÃO DA IGUALDADE RACIAL E DE GÊNERO | mesmo nome, p. 27 | gerais | 4,00 | 0 |
| DIREITO ADMINISTRATIVO | mesmo nome, p. 28 | específicos | 8,00 | 9 |
| DIREITO CONSTITUCIONAL | mesmo nome, p. 29 | específicos | 8,00 | 17 |
| DIREITO PROCESSUAL PENAL | mesmo nome, p. 29 | específicos | 7,75 | 18 |
| DIREITO PENAL | mesmo nome, p. 29 | específicos | 7,25 | 22 |
| DIREITO CIVIL E EMPRESARIAL | mesmo nome, p. 28 | específicos | 7,00 | 10 |
| LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE | mesmo nome, p. 30 | específicos | 7,00 | 8 |
| CRIMINOLOGIA | mesmo nome, p. 31 | específicos | 6,00 | 7 |
| DIREITO AMBIENTAL | mesmo nome, p. 30 | específicos | 3,00 | 8 |
| DIREITO PROCESSUAL CIVIL | mesmo nome, p. 30 | específicos | 3,00 | 1 |
| DIREITO TRIBUTÁRIO | mesmo nome, p. 30 | específicos | 3,00 | 4 |

Soma: 100,00 questões.

## A fórmula

```
escore(item) = peso_da_disciplina × (1 + incidência_do_item) ÷ (N_disciplina + K_disciplina)
  incidência_do_item = questões AOCP únicas classificadas no item
  N_disciplina       = questões AOCP únicas classificadas na disciplina
  K_disciplina       = número de itens da disciplina no edital
desempate: prioridade antiga (Alta > Média-alta > Regular), depois o id
```

**Por que ajustei** a fórmula do plano (`peso × (1 + incidência)`): a quantidade de questões AOCP por disciplina
depende de **quais cadernos foram baixados** (há 121 questões de Português e 25 de Penal porque havia 9 cadernos
de Português), não da prova. Sem dividir pelo tamanho da amostra da disciplina, Português e Informática passariam
à frente de tudo por acaso. Com a divisão, o `(1 + n)` vira a **fatia do item dentro da disciplina** (suavizada:
item sem questão ainda tem fatia > 0) e o escore passa a ser **quantas questões se espera do item numa prova de
100** — a soma dos 503 escores é 100,00. O peso da disciplina continua
multiplicando, e a incidência continua decidindo a ordem **dentro** da disciplina.

## Ordem dos 12 módulos

Ordenados pelo escore somado (= questões esperadas do módulo na objetiva). A coluna *por item* mostra a
densidade: quanto rende cada ponto estudado.

| ordem | módulo | itens | escore (questões esperadas) | por item | questões AOCP |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | Igualdade racial e de gênero, Legislação geral e Atualidades | 25 | 16,00 | 0,640 | 2 |
| 2 | Informática e Raciocínio Lógico | 57 | 12,00 | 0,210 | 139 |
| 3 | Civil, Empresarial e Processo Civil | 26 | 10,00 | 0,385 | 11 |
| 4 | Criminologia e Medicina Legal | 45 | 10,00 | 0,222 | 13 |
| 5 | Língua Portuguesa | 10 | 8,00 | 0,800 | 123 |
| 6 | Constitucional | 62 | 8,00 | 0,129 | 17 |
| 7 | Administrativo | 71 | 8,00 | 0,113 | 9 |
| 8 | Processo Penal e inquérito | 41 | 7,75 | 0,189 | 18 |
| 9 | Penal (geral e especial) | 74 | 7,25 | 0,098 | 22 |
| 10 | Legislação penal extravagante | 40 | 7,00 | 0,175 | 8 |
| 11 | Ambiental | 16 | 3,00 | 0,188 | 8 |
| 12 | Tributário | 36 | 3,00 | 0,083 | 4 |

**Soma dos itens: 503** (o edital tem 503 — §D7).

## Os 40 pontos de maior prioridade

| # | id | disciplina | item | escore | incidência AOCP | prioridade antiga |
| ---: | --- | --- | --- | ---: | ---: | --- |
| 1 | DBA26-ATU-1 | Atualidades | 1 Atualidades em âmbito internacional, nacional e do Estado da Bahia: Conflitos geopolíti… | 3,000 | 2 | Regular |
| 2 | DBA26-POR-4 | Língua Portuguesa | 4 Sintaxe: termos da oração e relações sintático-semânticas estabelecidas entre termos, o… | 2,406 | 39 | Regular |
| 3 | DBA26-POR-1 | Língua Portuguesa | 1 Compreensão e interpretação de texto; tipologia e gêneros textuais; elementos da comuni… | 2,226 | 36 | Regular |
| 4 | DBA26-LGE-1 | Legislação Geral | 1 Lei Estadual nº 6.677/1994 - Estatuto do Servidor Público do Estado da Bahia. | 1,600 | 0 | Média-alta |
| 5 | DBA26-LGE-2 | Legislação Geral | 2 Lei Estadual nº 14.634/2023 - Normas de licitações e contratos administrativos aplicáve… | 1,600 | 0 | Média-alta |
| 6 | DBA26-LGE-3 | Legislação Geral | 3 Lei Estadual nº 12.209/2011 - Dispõe sobre o processo administrativo, no âmbito da Admi… | 1,600 | 0 | Média-alta |
| 7 | DBA26-LGE-4 | Legislação Geral | 4 Lei Estadual nº 11.370/2009 - Lei Orgânica da Polícia Civil do Estado da Bahia e altera… | 1,600 | 0 | Média-alta |
| 8 | DBA26-LGE-5 | Legislação Geral | 5 Lei Federal nº 8.906/1994 – Estatuto da Advocacia. | 1,600 | 0 | Média-alta |
| 9 | DBA26-RAC-10.5 | Raciocínio Lógico | 10.5 Diagramas lógicos. | 1,529 | 12 | Regular |
| 10 | DBA26-RAC-10.1 | Raciocínio Lógico | 10.1 Proposições simples e compostas. | 1,412 | 11 | Regular |
| 11 | DBA26-RAC-14 | Raciocínio Lógico | 14 Raciocínio lógico envolvendo problemas aritméticos, geométricos e matriciais. | 1,412 | 11 | Regular |
| 12 | DBA26-RAC-8 | Raciocínio Lógico | 8 Compreensão de estruturas lógicas. | 1,177 | 9 | Regular |
| 13 | DBA26-ATU-2 | Atualidades | 2 Comunicação: conceitos, efeitos e implicações sociais, econômicas, políticas e culturais. | 1,000 | 0 | Regular |
| 14 | DBA26-INF-3.6 | Informática | 3.6 Conceitos de segurança da informação: procedimentos de segurança; programas maliciosos,… | 0,969 | 30 | Regular |
| 15 | DBA26-CRI-3.1 | Criminologia | 3.1 Teorias sociológicas. | 0,968 | 4 | Média-alta |
| 16 | DBA26-POR-7 | Língua Portuguesa | 7 Elementos de coesão e suas funções no texto (referenciação, sequenciação). | 0,962 | 15 | Regular |
| 17 | DBA26-CIV-4-B2 | Direito Civil E Empresarial | 4 Da responsabilidade civil (CC, Parte Especial, Livro I, Título IX). | 0,875 | 2 | Regular |
| 18 | DBA26-CIV-5-B2 | Direito Civil E Empresarial | 5 Da posse (CC, Parte Especial, Livro III, Título I). | 0,875 | 2 | Regular |
| 19 | DBA26-CIV-7 | Direito Civil E Empresarial | 7 Lei de Introdução às normas do Direito Brasileiro. | 0,875 | 2 | Regular |
| 20 | DBA26-POR-2 | Língua Portuguesa | 2 Semântica: significação de palavras e expressões; relações de sinonímia e de antonímia;… | 0,842 | 13 | Regular |
| 21 | DBA26-POR-3 | Língua Portuguesa | 3 Morfologia: estrutura e formação de palavras; ortografia; acentuação gráfica; classes d… | 0,842 | 13 | Regular |
| 22 | DBA26-CPP-2.1 | Direito Processual Penal | 2.1 Histórico; natureza; conceito; finalidade; características; fundamento; titularidade; g… | 0,788 | 5 | Alta |
| 23 | DBA26-CRI-1.2 | Criminologia | 1.2 Objetos da Criminologia: delito, delinquente, vítima, controle social. | 0,774 | 3 | Média-alta |
| 24 | DBA26-CPP-2.2 | Direito Processual Penal | 2.2 Jurisdição; competência; conexão e continência; prevenção; questões e procedimentos inc… | 0,657 | 4 | Alta |
| 25 | DBA26-CPP-7.6 | Direito Processual Penal | 7.6 Meios de prova: perícias, interrogatório, confissão, testemunhas, reconhecimento de pes… | 0,657 | 4 | Alta |
| 26 | DBA26-CPP-8.5 | Direito Processual Penal | 8.5 Princípio da necessidade, prisão especial, liberdade provisória. | 0,657 | 4 | Alta |
| 27 | DBA26-CIV-1 | Direito Civil E Empresarial | 1 Das pessoas (CC, Parte Geral, Livro I). | 0,583 | 1 | Regular |
| 28 | DBA26-CIV-11 | Direito Civil E Empresarial | 11 Lei Federal nº 11.101/2005. | 0,583 | 1 | Regular |
| 29 | DBA26-CIV-2 | Direito Civil E Empresarial | 2 Dos bens (CC, Parte Geral, Livro II). | 0,583 | 1 | Regular |
| 30 | DBA26-CIV-5 | Direito Civil E Empresarial | 5 Do direito de empresa (CC, Parte Especial, Livro II). | 0,583 | 1 | Regular |
| 31 | DBA26-CON-48 | Direito Constitucional | 48 Defesa do Estado e das instituições Democráticas. | 0,506 | 4 | Média-alta |
| 32 | DBA26-AMB-12 | Direito Ambiental | 12 Responsabilidade ambiental: conceito de dano, reparação ambiental e responsabilidade ci… | 0,500 | 3 | Regular |
| 33 | DBA26-CPC-5 | Direito Processual Civil | 5 Da tutela provisória. | 0,462 | 1 | Regular |
| 34 | DBA26-MLE-4 | Medicina Legal | 4 Lesões e mortes por ação contundente, por instrumentos cortantes, perfurantes, perfuroc… | 0,444 | 2 | Média-alta |
| 35 | DBA26-LPE-8 | Legislação Penal E Processual Penal Extravagante | 8 Lei Federal nº 12.850/2013 - Organizações Criminosas. | 0,438 | 2 | Alta |
| 36 | DBA26-INF-2.2 | Informática | 2.2 Planilha Eletrônica - Excel: área de trabalho, barras de ferramentas, botões e menus do… | 0,438 | 13 | Regular |
| 37 | DBA26-CON-39 | Direito Constitucional | 39 Poder Legislativo: fundamento, atribuições, garantias de independência. | 0,405 | 3 | Média-alta |
| 38 | DBA26-PEN-9.1 | Direito Penal | 9.1 Conceito, causas gerais e específicas, momentos de ocorrência. | 0,378 | 4 | Alta |
| 39 | DBA26-AMB-5-B2 | Direito Ambiental | 5 Lei Federal nº 9.605/1998 e respectivos regulamentos - Poder de Polícia Ambiental. Crim… | 0,375 | 2 | Regular |
| 40 | DBA26-POR-6 | Língua Portuguesa | 6 Emprego dos sinais de pontuação e sua função no texto. | 0,361 | 5 | Regular |

## Qualidade da régua

- Classificadas: **374 de 383** questões únicas; confiança alta 348, média 26, baixa 0.
- **Não classificadas: 9** (lista abaixo).
- **Amostra conferida à mão** (06/11/2026, 21h58, sorteio de semente fixa): **26 de 30 certas** (86,7%). As erradas e o porquê estão em `revisao/amostra_conferida.json`.
  - Q1992072: classificada em DBA26-CPP-8.5, o certo seria DBA26-CPP-8.4 — prisão preventiva; o assunto-pai 'Da Prisão e da Liberdade Provisória' puxou para liberdade provisória.
  - Q4218195: classificada em DBA26-POR-1, o certo seria DBA26-POR-4 — orações coordenadas e conectivos; o assunto genérico 'Compreensão e Interpretação' venceu.
  - Q4090560: classificada em DBA26-POR-1, o certo seria DBA26-POR-2 — denotação e conotação; o sinônimo curado era 'conotativo', não 'conotacao'.
  - Q4118232: classificada em DBA26-INF-3.7, o certo seria não classificar — hardware e memórias não estão no edital; devia ficar não classificada.
- Antes dos ajustes, a primeira amostra deu 21 de 30 (06/11/2026, 21h53); os erros dela guiaram os ajustes e a amostra acima foi sorteada depois.

### Questões não classificadas (§F10)

| id na plataforma | caderno | nº | disciplina na plataforma |
| --- | --- | ---: | --- |
| Q1992050 | AOCP_04 | 2 | Direito Penal |
| Q4247472 | AOCP_INFO_01 | 16 | Atualidades |
| Q4219368 | AOCP_INFO_03 | 15 | Noções de Informática |
| Q4218220 | AOCP_INFO_04 | 10 | Atualidades |
| Q4215994 | AOCP_INFO_06 | 3 | Noções de Informática |
| Q4098365 | AOCP_INFO_06 | 18 | Noções de Informática |
| Q4225506 | AOCP_PORTUGUES_01 | 13 | Português |
| Q4118190 | AOCP_PORTUGUES_08 | 11 | Português |
| Q4218206 | AOCP_RAC_LOG_01 | 16 | Raciocínio Lógico |

## Limites da régua (declarados)

- **Amostra torta:** as questões de Direito (e 5 de Português) vêm de provas de **Delegado** (PC-GO 2022 e
  PC-PA 2021) — e são só parte daquelas provas, não as provas inteiras; o resto de Português, Informática e
  Raciocínio Lógico vem de provas AOCP de outros cargos (2026). Mostram o jeito da banca, não o recorte do Delegado.
- **Pouca questão por disciplina específica** (de 1 a 22): a ordem dentro delas é frágil;
  a suavização evita que item sem questão vá a zero, mas não inventa incidência.
- **Disciplinas sem nenhuma questão AOCP nos cadernos:** LEGISLAÇÃO GERAL, PROMOÇÃO DA IGUALDADE RACIAL E DE GÊNERO. Nelas o escore
  é só o peso estimado dividido pelos itens — por isso as 5 leis da Legislação Geral (8 questões estimadas em 5
  itens) sobem ao topo. É conta, não incidência medida.
- **Peso por disciplina é estimativa** (o edital só fixa 40 + 60). A discursiva (só específicos) e o desempate
  pela nota de específicos (edital, 9.1) **não** entram no escore — o edital não dá a distribuição por disciplina.
- **Cada questão conta para um item só** (o de maior pontuação). Item-título (ex.: "Crimes.", "Prisão.")
  tende a zero porque os filhos levam a questão; no módulo ele anda junto com os filhos.
- **Itens de "Jurisprudência aplicada"** não têm palavra própria e não recebem questão.
- **Palavra-chave não entende contexto:** a amostra conferida mede o erro; o resto não foi lido um a um.
