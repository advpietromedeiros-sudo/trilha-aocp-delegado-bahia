# HARNESS — Trilha AOCP Delegado Bahia

> Não é referência. É ORDEM. Lido inteiro na abertura de cada sessão.
>
> Semente do roteiro de fundação v1.0 (§9.3), adotado como regra canônica pelo titular em
> 31/10/2026 para **todo** projeto da pasta (harness da pasta-mãe, Parte IV). Vale também o harness
> completo da pasta-mãe (`C:\Users\advpi\Repositório\0 Readme First\HARNESS.md`); **na dúvida, o
> mais restritivo dos dois.** O Trilha segue o método (governança, portão, CI); a **pilha** do
> roteiro entra quando ele virar funcionalidade do portal Pietro Medeiros.

## O teste de 5 segundos — antes de CADA comando, script, SQL ou afirmação

1. Qual shell? PowerShell não é Bash. Vou aninhar aspas? → ARQUIVO.
2. Escreve em produção? → EU NÃO EXECUTO. Proponho; o operador do servidor roda.
3. Vou afirmar um número? → medi AGORA? Datei a medição?
4. Vou dizer "pronto"? → em qual CAMADA? Cobri todas?
5. Vou APAGAR? → o dado está ERRADO ou só FALTANDO? Faltando não se apaga.

## REGRA ZERO — nunca supor; verificar na fonte, sempre

Afirmação sem medição é palpite com cara de fato. Não sei → digo que não sei.

## REGRA UM — o que ficou pela metade se declara, sem ser perguntado

"Feito" escondendo um passo pulado é pior que "não feito".

## REGRA DOIS — o repositório não é a execução

O app roda do `servidor.py` local; arquivo commitado não é servidor reiniciado.

## REGRA TRÊS — nome não se adivinha

Rota, campo de JSON, variável: ler na fonte antes de escrever.

## REGRA CINCO — o instrumento também mente

Todo verificador tem autoteste que prova que ele acusa. Verde que nunca falha não é controle.

## Bloqueios ativos

(nenhum em 31/10/2026 — cada bloqueio novo entra aqui com data, motivo e o que NÃO se faz enquanto durar)

## Regras deste projeto (crescem a cada erro, na mesma correção)

- **R1 — Hook do repositório cede a vez ao do usuário** (31/10/2026). Na estação do titular o
  relógio e a guarda já rodam por `~/.claude/settings.json`; os daqui saem calados lá e valem nas
  outras máquinas.
- **R2 — A pasta é `0 Readme First/`, com espaços** (roteiro §3.1), contra a §F58. Todo comando que
  a toca põe o caminho entre aspas.
- **R3 — O `.env` tem a chave de API e não se lê** (§F59). Por isso o Storybook não serve pasta do
  disco: as stories leem o `index.html` como texto. **Cobrada:** guarda de shell.
- **R4 — Quatro assets derivados de terceiros ficam fora do Git** (D-002, `docs/PROCEDENCIA.md`).
  **Cobrada:** `.gitignore`.
