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

## Penal (08/11/2026) — entrega em duas etapas

`pente_fino_pen.js` (`--disc PEN`, conteúdo em `ferramentas/pente_fino/pen/`, jurisprudência em `pen/pen_juris.py`).
**Esta entrega traz só a PARTE GERAL**: os 58 pontos `DBA26-PEN-1` a `PEN-9.2` (títulos 1 a 9 do edital, com
subitens; ids `PEN-4.10-R1-01`), em `pen_p01_02.py`, `pen_p03.py`, `pen_p04.py`, `pen_p05_07.py`, `pen_p08.py` e
`pen_p09.py`. Ficam para a **PARTE ESPECIAL** `PEN-10` a `PEN-10.14` (crimes em espécie) e `PEN-11` (jurisprudência e
legislação aplicadas a cada tópico).

- **Entrega parcial explícita:** a entrada PEN de `disciplinas.py` traz `pontos_incluidos` (lista `PEN_PARTE_GERAL` +
  `PEN_PARTE_ESPECIAL`, esta vazia por ora). `construir.py` grava em `pontos` só esses ids (a tela não mostra ponto
  vazio) e `conferir.py` exige exatamente eles, na ordem, e **imprime os pendentes do edital**. A regra só vale para
  quem tem a chave: CPC, CIV, MLE, CRI e CPP continuam exigindo todos os pontos do edital.
- **Como acrescentar a Parte Especial:** (1) criar os arquivos de conteúdo em `pen/` (sugestão: `pen_p10_01_04.py`,
  `pen_p10_05_11.py`, `pen_p10_12_14.py`, `pen_p11.py`), reaproveitando `pen_juris.py` e acrescentando julgados
  conferidos; (2) somar os nomes em `modulos`; (3) pôr os ids em `PEN_PARTE_ESPECIAL`. Com os 74 feitos, a chave
  `pontos_incluidos` pode sair (volta a valer o edital inteiro). Revisar então `cabecalho`, `fontes` e `volume`.
- Volume próprio (R1 5–12, R2 3–8): R1 5–6 e R2 3–4 na média; os de maior incidência AOCP (`PEN-9.1`, `1.1`, `7`,
  `1.2`, `2.2`, `8.11`…) e a prescrição (`9.2`) vão além. Como no CPP, **toda assertiva tem lei ou jurisprudência**.
- Particularidades: (1) a lei seca guarda redações de 2024–2026 — CP, arts. 61, II, m (Lei 15.159/2025), 65, I, e 115
  (Lei 15.160/2025: ressalva da violência sexual contra a mulher), 92 (Leis 14.994/2024, 15.358/2026 e 15.487/2026),
  91-A, § 5º (Lei 15.358/2026), 103, par. ún. (Lei 15.438/2026: decadência de 12 meses na violência doméstica); LEP,
  art. 112 (Leis 14.843/2024, 15.358/2026 e 15.402/2026: caput com 1/6, hediondo primário 70%, feminicídio 75%), art.
  126, § 9º (Lei 15.402/2026) — o conferidor avisa "alteração de 2026" e o item cita a linha vigente; a regra antiga
  aparece só como pegadinha (ex.: 40% do hediondo, decadência de 6 meses); (2) art. 43, III, do CP tem na base uma linha
  antiga ("limitação de fim de semana", inciso vetado em 1998): cita-se o inciso VI; (3) Súmulas 545 e 630 do STJ estão
  na **redação revisada** (Tema 1.194, 10/09/2025) e a antiga aparece só como pegadinha; (4) divergências doutrinárias
  (teorias da conduta, da culpabilidade, natureza da desistência, ofendículos) são ditas como doutrina, sem atribuir a
  tribunal; posição de tribunal só com julgado conferido em `pen_juris.py`.
