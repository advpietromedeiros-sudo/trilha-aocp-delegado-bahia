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
