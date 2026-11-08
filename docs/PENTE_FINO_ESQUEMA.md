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
