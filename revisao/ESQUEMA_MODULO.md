# Esquema do módulo de revisão (versão 1)

> Motor da Revisão Delegado PC-BA (D-018, plano em `docs/REVISAO_PLANO.md`). Escrito em 06/11/2026.
> O gerador é `ferramentas/gerar_revisao.py`; o molde, `revisao/molde/`. O conteúdo
> (`revisao/conteudo/<modulo>.json`) e a saída (`revisao/saida/`) ficam **fora do Git**: usam material de
> terceiro.

## Como gerar

```powershell
# máquina local · pasta do projeto · o _exemplo volta em 10 a 30 s; um módulo de 300 páginas, em 1 a 3 min
# (o PDF sai pelo Edge/Chrome headless via CDP, em partes de 40 páginas juntadas com o PyMuPDF; pede o Node)
python ferramentas/gerar_revisao.py _exemplo             # HTML + PDF em revisao/saida/
python ferramentas/gerar_revisao.py _exemplo --validar   # só valida, não escreve nada
python ferramentas/gerar_revisao.py _exemplo --sem-pdf   # só o HTML
python ferramentas/testar_revisao.py                     # gera o exemplo e testa no navegador
python ferramentas/testar_revisao.py m02_penal_parte_geral --sem-pdf   # idem para um módulo pelo nome
python ferramentas/testar_revisao.py --autoteste         # REGRA CINCO: planta defeitos e exige a recusa
```

Saídas do gerador: **0** gerado (ou válido) · **1** recusado ou falha · **2** uso errado. Recusa imprime
`[RECUSADO]` e a lista de problemas, um por linha, com o bloco, o ponto e o campo.

## O arquivo

Um JSON em UTF-8. Campos marcados com **\*** são obrigatórios.

### Módulo

| campo | tipo | o que é |
| --- | --- | --- |
| `esquema`\* | número | sempre `1` |
| `modulo`\* | texto | nome do arquivo de saída: minúsculas, números, `_` e `-` (ex. `penal-geral`) |
| `titulo`\* | texto rico | título do caderno |
| `subtitulo` | texto rico | linha de baixo do topo |
| `disciplina` | texto rico | aparece acima do título |
| `apresentacao` | texto rico | parágrafo da capa |
| `conferido_em`\* | `dd/mm/aaaa` | **carimbo de conferência**; vira `<meta name="conferido-em">` no topo do HTML. Não pode estar no futuro |
| `ordem` | `"prioridade"` (padrão) ou `"fixa"` | `prioridade`: pontos por escore (maior primeiro) e blocos pelo maior escore; as letras A, B, C… saem dessa ordem |
| `sensivel_a_mudanca` | lista de texto rico | o que conferir na fonte antes da prova. O gerador **acrescenta sozinho** todo artigo citado que tenha `alteracao_2026` no texto oficial |
| `dicas` | lista de texto rico | falas do avatar do Professor Pietro Medeiros |
| `blocos`\* | lista | blocos de pontos correlatos (abaixo) |

### Bloco

| campo | tipo | o que é |
| --- | --- | --- |
| `titulo`\* | texto rico | nome do bloco |
| `icone` | texto | um emoji antes do título |
| `em_uma_frase` | texto rico | quadro "Em uma frase" na abertura do bloco |
| `pontos`\* | lista | pontos do edital (abaixo) |

### Ponto do edital

| campo | tipo | o que é |
| --- | --- | --- |
| `id`\* | texto | id de `assets/items.json` (ex. `DBA26-PEN-2.2`). Id que não existe lá **reprova** |
| `prioridade`\* | objeto | `escore`\* (número; ordena o módulo), `nivel` (ex. `"Alta"`; se faltar, vem do items.json), `fonte` (de onde veio o escore, ex. `docs/REVISAO_PRIORIDADE.md`) |
| `titulo` | texto rico | se faltar, usa o rótulo do edital |
| `o_que_cai`\* | texto rico ou lista | núcleo em nível de delegado (um parágrafo por item). Entra no modo "Só o essencial" |
| `lei_seca` | lista de **lei** | entra no "Só o essencial" e no Fichário · Lei Seca |
| `jurisprudencia` | lista de **juris** | |
| `pegadinhas` | lista de texto rico | quadro "Pegadinhas da AOCP". Entra no "Só o essencial" |
| `dia_a_dia` | texto rico ou lista | quadro "No dia a dia do delegado" |
| `detalhe_tecnico` | texto rico ou lista | quadro "Detalhe técnico" |
| `esquema` | **esquema** | tabela ou comparativo |
| `fichas` | lista de **ficha** | certo ou errado, com verso |
| `questoes` | lista de **questão** | múltipla escolha A–E |
| `discursiva` | objeto | ponte com a discursiva: `peca`\* (qual peça) e `como` (texto rico) |
| `checklist` | lista de texto rico | checklist marcável do ponto |

### Lei (`lei_seca[]`)

| campo | tipo | o que é |
| --- | --- | --- |
| `lei`\* | texto | **chave** de `assets/lei_seca_oficial.json`: a parte antes de `:` (ex. `CP`, `CPP`, `CF`, `L11343`) |
| `art`\* | texto | artigo como está na chave (ex. `"2"`, `"121"`). `lei:art` tem de existir no oficial |
| `par` | texto | parágrafo, como se lê (ex. `"§ 1º"`, `"parágrafo único"`) |
| `inc` | texto | inciso em romano (ex. `"XL"`, `"I-B"`). **Alínea não é inciso**: `"a"` em `inc` reprova — vai em `ali` |
| `ali` | texto | alínea, uma letra minúscula (ex. `"a"`). Fica dentro do `inc` (se houver) ou do `par` (se houver) |
| `texto`\* | texto puro | **trecho exato** do texto oficial (8 caracteres ou mais). Conferido assim: tiram-se as anotações do Planalto ("(Redação dada…)", "(Incluído…)", "(Vide…)" etc.) e as aspas; juntam-se espaços e quebras; hífens e travessões viram `-`; `º`, `°` (grau) e `o` depois de algarismo viram `º`; maiúscula e minúscula não contam. O trecho tem de estar **contido** no artigo oficial. Palavra trocada reprova |

**Régua única (07/11/2026).** O gerador e o verificador de atualidade conferem a citação pela **mesma** função,
`ferramentas/localizar_lei.py` (`conferir_citacao`): o gerador recusa exatamente o que o `--conferir` recusa, e o
`--autoteste` do gerador prova isso citação a citação. Além do trecho, `par`, `inc` e `ali` são **localizados** na
estrutura do artigo, um dentro do outro: o inciso dentro do parágrafo citado, a alínea dentro do inciso ou do
parágrafo; `"§ 4º"` não casa com `"§ 4º-A"` e `XI` não casa com `XL`. O Planalto às vezes troca o `I` por `l`
minúsculo ou `1` (CPP, art. 78, "Il"): o inciso `"II"` é aceito, com aviso, **só se** houver um único candidato.
| `rotulo` | texto | substitui o rótulo automático ("Código Penal, art. 2º, parágrafo único") |
| `comentario` | texto rico | nota abaixo do quadro da lei |

Sai no HTML, sempre neste formato (lido pelo verificador de atualidade):

```html
<blockquote class="lei" data-lei="CP" data-art="2" data-par="parágrafo único">texto exato</blockquote>
```

`data-par`, `data-inc` e `data-ali` só aparecem quando o campo existe (ex. `data-par="§ 2º" data-ali="a"`).

### Juris (`jurisprudencia[]`)

| campo | tipo | o que é |
| --- | --- | --- |
| `tribunal`\* | texto | `STF`, `STJ`… |
| `fonte`\* | texto | de onde veio (ex. `"STJ, Súmula 567 (Terceira Seção)"`, `"STF, HC 000.000/UF, Informativo 000"`) |
| `data`\* | `dd/mm/aaaa` | data do julgamento ou da aprovação |
| `texto`\* | texto puro | enunciado ou tese |
| `sumula` | texto | `STJ-n`, `STF-n` ou `SV-n` (súmula vinculante, do STF; ex. `STJ-593`, `SV-14`). Chave em `assets/sumulas.json`: `SUM-STJ-n`, `SUM-STF-n`, `SV-n`. O tribunal tem de bater com `tribunal` (SV é `STF`); se a súmula está no `sumulas.json`, o `texto` tem de estar contido no texto de lá e ela não pode estar **cancelada ou superada** (senão reprova); se não está, sai **aviso**. As correções do `sumulas.json` conferidas na fonte oficial estão em `ferramentas/corrigir_sumulas.py` |
| `comentario` | texto rico | |

Sai assim:

```html
<div class="juris" data-tribunal="STJ" data-fonte="..." data-data="dd/mm/aaaa" data-sumula="STJ-567">…</div>
```

### Esquema

- Tabela: `{"tipo": "tabela", "titulo": "...", "colunas": ["A", "B"], "linhas": [["a1", "b1"], ...]}` — cada
  linha com o mesmo número de colunas.
- Comparativo: `{"tipo": "comparativo", "titulo": "...", "colunas": [{"titulo": "...", "itens": ["...", ...]}, ...]}`
  — ao menos 2 colunas.

### Ficha (`fichas[]`)

`item`\* (texto rico) · `gabarito`\* (`"C"` ou `"E"`) · `fundamento`\* (texto rico, vai no verso).

### Questão (`questoes[]`)

`enunciado`\* · `alternativas`\* (objeto com as cinco chaves `A` a `E`, todas com texto) · `gabarito`\* (`A`–`E`) ·
`comentario`\* · `origem`\*, que só aceita:

- `"AOCP <prova>"` — questão de prova da banca (ex. `"AOCP PC-ES 2019"`);
- `"Trilha"` — questão gerada na Trilha (`cache/`);
- `"Simulado"` ou `"Simulado <n>"` — dos simulados da discursiva (sem nome do curso de origem);
- `"Revisão"` — escrita para o módulo.

## Texto rico

Texto com estas tags, **sem atributo**: `b`, `strong` (marca-texto), `i`, `em`, `mark`, `u`, `br`, `sub`,
`sup`, `small`, `code`. Atalho: `==trecho==` vira marca-texto. Quebra de linha vira `<br>`. Qualquer outra
tag (ou atributo) **reprova**. Lei e juris são texto puro, sem HTML.

## O que reprova (sai 1)

Ponto sem id ou com id fora do `items.json`; id repetido; prioridade sem `escore` numérico; ponto sem
`o_que_cai`; lei sem chave, sem artigo, com `lei:art` fora do oficial, com texto que não confere ou curto demais,
com `par`, `inc` ou `ali` que não se localiza no artigo (ou alínea posta em `inc`); juris sem
tribunal, fonte ou data, data fora de `dd/mm/aaaa`, súmula fora do padrão, cancelada/superada ou com texto
diferente do `sumulas.json`; PDF não gravado; ficha sem gabarito C/E, sem item ou sem fundamento; questão sem as 5 alternativas, sem gabarito
A–E, sem comentário ou com origem fora da lista; esquema malformado; HTML fora da lista; `conferido_em` ausente,
inválido ou no futuro; e **referência proibida** no HTML final (`ferramentas/referencias_proibidas.py`: outras
bancas, cursinhos, o curso de origem dos simulados, "Prof." abreviado).

**Avisos** (não reprovam): súmula que não está no `sumulas.json`; inciso achado com I/l/1 trocados no texto
oficial; artigo com alteração de 2026; lei seca
oficial baixada há mais de 30 dias da data de conferência (rode `atualizar_lei_seca.bat`).

## O que o HTML entrega

Molde do caderno (folha pautada, letra manuscrita, abas "Caderno da Aula" e "Fichário · Lei Seca", índice
lateral com busca, cartão e avatar do Professor Pietro Medeiros, barra do estojo), mais: **índice por
prioridade** na capa e no índice lateral; **carimbo** "Conferido em"; quadro **Sensível a mudança**; **Só o
essencial** (fica o que cai, a lei e as pegadinhas); **marcar ponto revisado** com progresso "X de N pontos"
(guardado no `localStorage` do aparelho, chave `rev_pcba_<modulo>_…`); **Fichas que errei** (as fichas e
questões erradas voltam zeradas para refazer); checklist marcável; leitura no celular sem rolagem horizontal.
O PDF sai com os versos das fichas abertos e os gabaritos marcados.

## Exemplo

`revisao/conteudo/_exemplo.json` (fora do Git): `DBA26-PEN-2.2` (lei penal no tempo e no espaço) e
`DBA26-PEN-4.12` (crime impossível), com escores **provisórios** — o escore medido sai de
`docs/REVISAO_PRIORIDADE.md`, da outra frente.
