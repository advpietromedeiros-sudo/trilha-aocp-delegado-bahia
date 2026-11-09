# Pente Fino — esquema dos dados (07/11/2026)

Pedido do titular, 07/11/2026, 16h41: aba **PENTE FINO** ao lado de Simulados no Treino de Discursiva, com
assertivas de **certo ou errado comentadas**, por disciplina. **Rodada 1** = o básico de teoria e letra de lei de
TODOS os pontos do edital; **Rodada 2** = aprofundamento, liberada quando a Rodada 1 for concluída. Primeiro teste:
**Direito Processual Civil** (12 pontos, `DBA26-CPC-1` a `DBA26-CPC-12` em `assets/items.json`).

## Arquivo de dados

`discursiva/pente_fino_<disciplina>.js` (ex.: `pente_fino_cpc.js`), carregado por `<script>` no
`Treino_Discursiva.html` (abre com duplo clique, sem servidor):

```js
window.PENTE_FINO = window.PENTE_FINO || {};
window.PENTE_FINO.CPC = {
  disciplina: "Direito Processual Civil",
  conferido_em: "dd/mm/aaaa",          // data em que lei e jurisprudência foram conferidas
  fontes: ["Lei 13.105/2015 (CPC) — Planalto", "..."],
  pontos: [{ id: "DBA26-CPC-1", titulo: "Normas fundamentais..." }, ...],   // todos os do edital, na ordem
  rodadas: [
    { n: 1, titulo: "Rodada 1 · O essencial", itens: [ /* ITEM */ ] },
    { n: 2, titulo: "Rodada 2 · Aprofundamento", itens: [ /* ITEM */ ] }
  ]
};
```

## ITEM (uma assertiva)

```js
{
  id: "CPC-1-R1-01",                 // único
  ponto: "DBA26-CPC-1",              // id do edital
  tema: "Contraditório e vedação à decisão surpresa",
  assertiva: "texto da afirmação, como a banca escreveria",
  gabarito: "C" | "E",
  comentario: {
    resumo: "1 a 3 frases: por que está certa/errada. Palavras-chave em **negrito** (markdown simples).",
    regra: "a regra geral, curta",                       // opcional
    excecoes: ["exceção 1 (art. x)", "..."],             // opcional — a tela mostra em VERMELHO
    lei: [{ lei: "L13105", art: "10", par: "", inc: "", rotulo: "CPC, art. 10", texto: "trecho EXATO do oficial" }],
    juris: [{ tribunal: "STJ", fonte: "Tema 1.076 | REsp n | Súmula n", data: "dd/mm/aaaa", texto: "tese, curta" }],
    pegadinha: "como a AOCP costuma trocar o detalhe",   // opcional
    palavras_chave: ["contraditório", "decisão surpresa"]
  }
}
```

Regras de conteúdo: `lei[].texto` tem de estar contido, letra por letra, no artigo de `assets/lei_seca_oficial.json`
(chave `<lei>:<art>`); jurisprudência só com fonte e data conferidas em fonte oficial (STF/STJ) — data nunca da
memória; nada de texto copiado de material de terceiro e nenhum nome de curso, autor ou material.

## Aprofundamento do comentário (09/11/2026, pedido do titular)

Pedido: *"UMA MELHORIA NOS COMENTÁRIOS TANTO DO PENTE FINO QUANTO DA REVISÃO... PARA FICAR UM POUCO MAIS DETALHADO E
MAIS APROFUNDADO E MELHORAR O LAYOUT NOS COMENTÁRIOS"*. O `comentario` ganhou 4 campos opcionais. Eles vêm de uma
camada à parte, `ferramentas/pente_fino/aprofundar/<DISC>.json` (um JSON por disciplina, com o id do item como
chave), e o `construir.py` os junta ao item. Os arquivos de conteúdo conferidos não mudam.

- `correcao: {erro, certo}`: o que a assertiva diz de errado, ao lado da versão correta. Obrigatória no gabarito
  E e proibida no C. Na tela é o quadro 🔁 *Onde está o erro*.
- `aprofundamento`: de 2 a 5 parágrafos, separados por linha em branco (de 280 a 1.600 caracteres). Traz o
  fundamento, o funcionamento, as fronteiras com o instituto vizinho e como a banca explora o ponto. Na tela é o
  quadro 🔎 *Aprofundando*, e só o `**negrito**` escrito vira destaque: o vermelho automático das exceções não entra.
- `exemplo`: um caso hipotético curto. Na tela é o quadro 🧩 *Na prática*.
- `memorize`: uma linha de até 220 caracteres. Na tela é a faixa 🧠 *Para memorizar*.

A trava está em `ferramentas/validar_aprofundamento.py`, que é porta do portão. **Nenhum número entra no texto
novo sem já estar no item**: artigo, lei, súmula, tema, ano ou prazo. O redator explica o que foi conferido; não cita
dispositivo de memória. Itens que os redatores apontaram como possivelmente errados no original ficam listados no
FAROL, para conferir.

## Medicina Legal (07/11/2026)

`pente_fino_mle.js` (`--disc MLE`, conteúdo em `ferramentas/pente_fino/mle/`): os pontos têm subitem
(`DBA26-MLE-5.1` → ids `MLE-5.1-R1-01`); volume próprio (R1 6–10, R2 5–8, `volume` em `disciplinas.py`) e
`doutrina_sem_fonte`: assertiva só de doutrina (sinais, fenômenos, classificações) entra sem `lei` nem `juris` — o
conferidor conta quantas são. Prazos de fenômenos cadavéricos divergem entre autores: o comentário diz quando.

## Criminologia (07/11/2026)

`pente_fino_cri.js` (`--disc CRI`, conteúdo em `ferramentas/pente_fino/cri/`): 24 pontos (`DBA26-CRI-1` a `CRI-16`, com
subitens; o `CRI-8` traz no rótulo também o tópico 9 do edital, subcultura e anomia). Mesmo volume e mesma
`doutrina_sem_fonte` da MLE: a disciplina é doutrinária, e a lei entra só onde o tema tem base (vítima no CPP, Lei
13.431/2017, Lei 9.099/1995, LEP, CF art. 144, Lei 12.830/2013). Classificações com divergência (escolas, vitimização
terciária, velocidades do Direito Penal) seguem a posição mais cobrada, e o comentário declara a divergência.

## Processo Penal (08/11/2026)

`pente_fino_cpp.js` (`--disc CPP`, conteúdo em `ferramentas/pente_fino/cpp/`, jurisprudência em `cpp/cpp_juris.py`): 41
pontos (`DBA26-CPP-1` a `CPP-15`, com subitens, `CPP-4.2-B2` e `CPP-15-B2` → ids `CPP-4.2-B2-R1-01`). Volume próprio
(R1 5–12, R2 3–8, `volume` em `disciplinas.py`: os pontos grandes — inquérito, competência, ação penal, provas,
prisões — passam de 7). Como no CPC, **toda assertiva tem lei ou jurisprudência** (sem `doutrina_sem_fonte`).
Particularidades: (1) a lei seca guarda redações de 2025–2026 (audiência de custódia por videoconferência, art. 310;
decadência de 12 meses na violência doméstica, art. 38, § 2º; § 5º do art. 171 do CP revogado) — o conferidor avisa
"alteração de 2026" e o item cita a linha vigente; (2) juiz das garantias e art. 28 seguem a interpretação do STF nas
ADIs 6.298/6.299/6.300/6.305 (competência até o **oferecimento** da denúncia; exclusões; art. 157, § 5º,
inconstitucional), dita no comentário quando a letra do CPP diverge; (3) dispositivos tidos por não recepcionados
(arts. 21, 198 parte final, 241, 260 para interrogatório) aparecem só como pegadinha, nunca como regra; (4) súmula
vinculante leva como data a publicação no DJe, que é a que a página oficial traz.

## Penal (08/11/2026) — entregue em duas etapas, completo

`pente_fino_pen.js` (`--disc PEN`, conteúdo em `ferramentas/pente_fino/pen/`, jurisprudência em `pen/pen_juris.py`):
os **74 pontos** do edital (ids `PEN-4.10-R1-01`, `PEN-10.12-R2-03`).
**PARTE GERAL** (1ª etapa, commit 89b701a): os 58 pontos `DBA26-PEN-1` a `PEN-9.2` (títulos 1 a 9, com subitens), em
`pen_p01_02.py`, `pen_p03.py`, `pen_p04.py`, `pen_p05_07.py`, `pen_p08.py` e `pen_p09.py` — 553 assertivas.
**PARTE ESPECIAL** (2ª etapa): os 16 pontos `PEN-10`, `PEN-10.1` a `PEN-10.14` (crimes em espécie) e `PEN-11`, em
`pen_p10_01.py` (10 e 10.1), `pen_p10_02_06.py` (10.2 a 10.6), `pen_p10_07_10.py` (10.7 a 10.10),
`pen_p10_11_14.py` (10.11 a 10.14) e `pen_p11.py` — 185 assertivas (R1 113, R2 72). A reconstrução reproduz, item por
item, as 553 assertivas da Parte Geral.

- **Lista explícita:** a entrada PEN de `disciplinas.py` traz `pontos_incluidos` (`PEN_PARTE_GERAL` +
  `PEN_PARTE_ESPECIAL`), que agora cobre o edital inteiro — o conferidor informa **0 pendentes**. A chave ficou como
  registro das duas etapas; tirá-la não muda o arquivo gerado. A regra só vale para quem tem a chave: CPC, CIV, MLE,
  CRI e CPP continuam exigindo todos os pontos do edital.
- **PEN-10** (rótulo "Crimes.") faz a visão de conjunto da Parte Especial: hediondez (Lei 8.072/1990), ação penal dos
  crimes sexuais e as reformas de 2024–2026. **PEN-10.3** (propriedade imaterial) cobre a **propriedade industrial**
  (Lei 9.279/1996, que revogou os arts. 187 a 196 do CP) e **PEN-10.4** (propriedade intelectual) o **direito autoral**
  (CP, arts. 184 e 186) e o **programa de computador** (Lei 9.609/1998). **PEN-11** é ponto de **fechamento**:
  jurisprudência transversal (súmulas e teses aplicáveis a vários crimes), toda conferida.
- Volume próprio (R1 5–12, R2 3–8): R1 5–6 e R2 3–4 na média; os de maior incidência AOCP (`PEN-9.1`, `1.1`, `7`,
  `1.2`, `2.2`, `8.11`…), a prescrição (`9.2`) e os grandes da Parte Especial (`10.1`, `10.2` e `10.12` com 12/8,
  `10.7` com 11/7, `10.11` com 9/6) vão além. Como no CPP, **toda assertiva tem lei ou jurisprudência**.
- Parte Especial — particularidades: (1) a base guarda as redações de 2025–2026 e o item cita a linha vigente, com a
  antiga só como pegadinha: Lei 15.397/2026 (furto 1 a 6 anos e repouso noturno de metade; roubo 6 a 10; latrocínio 24
  a 30; receptação 2 a 6; **revogação do § 5º do art. 171** — estelionato volta à ação pública incondicionada; conta
  laranja, art. 171, § 2º, VII; art. 266), Lei 15.280/2025 (penas dos arts. 217-A, 218, 218-A, 218-B e 218-C; art.
  338-A), Lei 15.353/2026 (art. 217-A, § 4º-A: presunção **absoluta** de vulnerabilidade), Lei 15.384/2026
  (vicaricídio, art. 121-B, hediondo), Lei 15.358/2026 (marco do crime organizado: arts. 121, § 2º-D, 148, § 3º, 157,
  §§ 4º–5º...), Lei 15.402/2026 (arts. 359-M-A e 359-M-B), Lei 15.425/2026 (art. 282), Lei 15.245/2025 (art. 288,
  §§ 1º–2º), LC 225/2026 (devedor contumaz, arts. 168-A e 337-A, § 5º); (2) **feminicídio** é crime autônomo (art.
  121-A, Lei 14.994/2024) e a qualificadora do inciso VI aparece só como pegadinha; (3) o conferidor acusa como
  "redação superada" a linha citada quando as duas seguintes começam com o mesmo marcador (ex.: `I-B` seguido de `I-C`
  na Lei 8.072/1990, art. 1º; o caput do art. 359-M seguido do art. 359-M-A) — nesses casos cita-se outra linha do
  mesmo dispositivo (a pena, ou o inciso seguinte) e o comentário explica; (4) o art. 339 traz na base o "à" em forma
  decomposta (a + acento combinante): o recorte começa depois dele.
- Parte Geral — particularidades: (1) a lei seca guarda redações de 2024–2026 — CP, arts. 61, II, m (Lei 15.159/2025), 65, I, e 115
  (Lei 15.160/2025: ressalva da violência sexual contra a mulher), 92 (Leis 14.994/2024, 15.358/2026 e 15.487/2026),
  91-A, § 5º (Lei 15.358/2026), 103, par. ún. (Lei 15.438/2026: decadência de 12 meses na violência doméstica); LEP,
  art. 112 (Leis 14.843/2024, 15.358/2026 e 15.402/2026: caput com 1/6, hediondo primário 70%, feminicídio 75%), art.
  126, § 9º (Lei 15.402/2026) — o conferidor avisa "alteração de 2026" e o item cita a linha vigente; a regra antiga
  aparece só como pegadinha (ex.: 40% do hediondo, decadência de 6 meses); (2) art. 43, III, do CP tem na base uma linha
  antiga ("limitação de fim de semana", inciso vetado em 1998): cita-se o inciso VI; (3) Súmulas 545 e 630 do STJ estão
  na **redação revisada** (Tema 1.194, 10/09/2025) e a antiga aparece só como pegadinha; (4) divergências doutrinárias
  (teorias da conduta, da culpabilidade, natureza da desistência, ofendículos) são ditas como doutrina, sem atribuir a
  tribunal; posição de tribunal só com julgado conferido em `pen_juris.py`.

## Legislação Extravagante (08/11/2026)

`pente_fino_lpe.js` (`--disc LPE`, conteúdo em `ferramentas/pente_fino/lpe/`, jurisprudência em `lpe/lpe_juris.py`): os
**40 pontos** do edital (`DBA26-LPE-1` a `LPE-40`, uma lei por ponto → ids `LPE-17-R1-03`), em `lpe_p01_05.py`,
`lpe_p06_09.py`, `lpe_p10_14.py`, `lpe_p15_20.py`, `lpe_p21_30.py` e `lpe_p31_40.py` — 430 assertivas (R1 263, R2 167),
entregues de uma vez (sem `pontos_incluidos`: o conferidor exige os 40).

- Volume da CPP/PEN (R1 5–12, R2 3–8): leis menores com 5/3; as de maior incidência e peso (Lei de Drogas 11/7,
  organizações criminosas 10/6, Estatuto do Desarmamento, abuso de autoridade, ECA, LEP, Maria da Penha e Lei
  15.358/2026 com 9/6) vão além. Como no CPP e na PEN, **toda assertiva tem lei ou jurisprudência**.
- `lpe_juris.py` **reaproveita** as entradas de `pen/pen_juris.py` e `cpp/cpp_juris.py` (importa os dois dicionários,
  sem mudar uma letra) e acrescenta as novas; a PEN e o CPP não foram tocados (a reconstrução deles não muda).
- **LPE-40** ("jurisprudência aplicada... de cada tópico") é ponto de **fechamento**, como o PEN-11: só jurisprudência
  transversal conferida (busca pessoal, ingresso em domicílio, temporária, presídio federal, medidas socioeducativas).
  LPE-26 e LPE-28 (Leis 9.279/1996 e 9.609/1998) evitam repetir os temas já cobertos em PEN-10.3 e 10.4.
- Particularidades: (1) a lei seca guarda as redações de 2025–2026 e o item cita a linha vigente, com a antiga só como
  pegadinha — Lei 15.358/2026 (marco do crime organizado: facção com **3** ou mais pessoas, pena de 20 a 40 anos; arma
  a serviço do tráfico, Lei 10.826/2003, art. 21-A; Lei 11.343/2006, art. 40-A; LEP, arts. 41-A, 52, § 6º, e 112, V),
  Lei 15.402/2026 (LEP, art. 112, caput: 1/6 como regra), Lei 15.487/2026 (ECA, arts. 240 a 241-E — "conteúdo de
  violência sexual"; Lei 8.072/1990, art. 1º, par. ún., VII; Lei 12.850/2013, art. 2º, § 4º, I), Leis 15.380, 15.383 e
  15.384/2026 (Maria da Penha, arts. 7º, VI, 12-D, 16, par. ún., 16-A e 24-A, § 4º), Lei 15.410/2026 (tortura, art.
  1º, III), Lei 15.517/2026 (Lei 8.176/1991, arts. 1º-A a 1º-C), Lei 15.355/2026 (Lei 9.605/1998, art. 32, § 1º-C),
  Lei 15.295/2025 (identificação criminal, art. 3º, VII) e Lei 15.163/2025 (ECA, art. 230, § 2º; Estatuto da Pessoa
  Idosa, art. 94, par. ún., e 99; Lei 13.146/2015, art. 90); (2) **SV 9 cancelada** (Informativo STF 1.193) e **Súmula
  512/STJ cancelada** aparecem só como pegadinha; o tráfico privilegiado segue a **SV 63** e o art. 112, § 5º, da LEP;
  (3) a linha do I-B (feminicídio) do art. 1º da Lei 8.072/1990 é lida pelo conferidor como redação superada (vem
  seguida do I-C): cita-se o art. 121-A do CP; a mesma linha guarda o "í" decomposto; (4) dispositivos com
  inconstitucionalidade declarada e não conferida hoje (Lei 10.826/2003, art. 21; Lei 11.343/2006, art. 44, caput,
  quanto à liberdade provisória e às restritivas; Lei 9.613/1998, art. 17-D) ficaram de fora; posição de tribunal só
  com julgado conferido em `lpe_juris.py`.

## Informática (08/11/2026)

`pente_fino_inf.js` (`--disc INF`, conteúdo em `ferramentas/pente_fino/inf/`, fontes técnicas em `inf/inf_fontes.py`): os
**34 pontos** do edital (`DBA26-INF-1` a `INF-3.7`), com subitens de até **três níveis** (`DBA26-INF-2.1.1` → ids
`INF-2.1.1-R1-01`), em `inf_p01.py` (Windows 11), `inf_p02_1.py` (Microsoft 365 e Word), `inf_p02_2.py` (Excel),
`inf_p02_3.py` (PowerPoint) e `inf_p03.py` (redes, internet e intranet, nuvem, navegadores, deep e dark web, correio
eletrônico, segurança, backup) — 314 assertivas (R1 193, R2 121), entregues de uma vez.

- `ordem_ponto` (em `disciplinas.py`) passou a ler o **3º nível** (2.1 < 2.1.1 < 2.1.5 < 2.2); nas outras disciplinas
  o 3º nível é 0 e a reconstrução delas não muda uma letra.
- Volume próprio (R1 5–10, R2 3–7): 5/3 nos pontos sem incidência; os de maior incidência AOCP (`revisao/mapa_prioridade.json`:
  3.6 segurança 10/7, 2.2 Excel 8/5, 3.1 internet 8/5, 2.1 Word 7/4, 2.2.2 funções 7/5) vão além.
- `doutrina_sem_fonte`, como na MLE/CRI: a disciplina é técnica, e a lei entra só onde há tipo penal (CP, arts. 154-A,
  154-B e 171, §§ 2º-A e 2º-B), recortada da base oficial. Fato técnico volátil — **atalho, menu, nome de função,
  operador de busca** — leva no fim do resumo a frase "Fonte: ..." com a página oficial e a data de consulta (Suporte
  Microsoft, Ajuda da Pesquisa Google, Cartilha CERT.br, NIST SP 800-145), listadas também em `fontes`.
- Versões de referência: **Windows 11** e **Microsoft 365** em português; quando a versão importa, o item diz (guias do
  Explorador só no Windows 11 22H2; PROCX, CLASSIFICAR e Transformar no Microsoft 365/2021; atalhos do LibreOffice 7.x/24.x).
- As páginas de atalhos da Microsoft avisam que seguem o **layout de teclado dos EUA** e, na versão em português, trazem
  linhas trocadas (ex.: alinhar à direita, selecionar tudo). Por isso só entraram atalhos em que a página e o Office em
  português coincidem sem dúvida (Ctrl + N/I/S, Ctrl + E, Ctrl + J, Ctrl + 1/2/5, Ctrl + Enter, Ctrl + Shift + Enter,
  F7, F12; no Excel, F2, F4, F11, Ctrl + D, Ctrl + 1, Ctrl + Alt + V); "selecionar tudo" no Excel é cobrado pelo botão.
