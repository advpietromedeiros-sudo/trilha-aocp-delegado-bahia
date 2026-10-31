# TRILHA AOCP — Delegado de Polícia Civil da Bahia 2026

## O que está pronto

- Interface HTML/CSS/JavaScript responsiva, com visualização por matéria, árvore verticalizada completa, pesquisa e filtros.
- **503 entradas numeradas**, em 17 disciplinas, importadas da trilha verticalizada do Anexo I do edital SAEB 02/2026. A ordem é intercalada e priorizada, não necessariamente a ordem em que os conteúdos aparecem no documento oficial.
- Cinco numerações duplicadas *na fonte* foram mantidas para exibição, mas receberam IDs internos distintos para evitar mistura de respostas e correções.
- **Três questões autorais iniciais** prontas (PEN-1, CPP-1 e CON-1), com alternativas, gabarito e comentários estruturados. Não são questões oficiais AOCP.
- Resposta da Questão 001 já registrada como **C/correta**, conforme o andamento anterior do estudo. O sistema inicia no item 002 (Direito Processual Penal).
- Comentário oculto até a resposta; correção de A a E; aulas em tópicos, referências, pegadinhas, mapa mental e lacunas para a próxima rodada.
- Progresso e anotações salvos no navegador; exportação/importação de backup JSON, navegação por teclado, tema escuro e tela cheia.
- Integração opcional com **API OpenAI Responses** ou **API Anthropic Messages** por servidor Python local; pré-geração automática da próxima questão e de todo o seu comentário; cache de questões para evitar pagamento repetido; auditoria formal + revisão independente opcional.
- Índice local de excertos das fontes de estudo anexadas (com nome e página), para orientar o modelo na construção das questões. A indexação não substitui verificação jurídica da norma em fonte oficial.

## Teste rápido (sem instalar nada)

Abra `index.html` com duplo clique. A árvore verticalizada funciona. Você pode revisar as três questões iniciais e suas correções. **As outras 500 dependem de geração via API.** O arquivo HTML, isoladamente, não tem acesso nem autorização para conectar de modo seguro à sua conta ChatGPT ou Claude.

## Habilitar geração automática das 503 questões no Windows

1. Tenha **Python 3.10 ou posterior** instalado e disponível como `py -3` ou `python` no Windows.
2. Na pasta do projeto, **copie** `.env.exemplo` para um arquivo chamado `.env` (cuidado: o Explorador pode ocultar extensões).
3. Abra `.env` no Bloco de Notas, cole **uma chave de API do provedor escolhido** após `OPENAI_API_KEY=` **ou** `ANTHROPIC_API_KEY=`. Nunca coloque chaves no HTML.
4. Confirme o identificador do modelo disponível para a sua conta (`OPENAI_MODEL` ou `CLAUDE_MODEL`). Os padrões são apenas sugestões configuráveis e estão sujeitos à disponibilidade da API.
5. Dê duplo clique em `iniciar_windows.bat`. Ele abrirá o navegador em **http://127.0.0.1:8765/** e manterá o servidor ativo em uma janela de terminal.
6. Na aplicação, clique em **Configurar** para selecionar GPT ou Claude e mantenha **Preparar automaticamente o próximo item** habilitado.
7. Ao selecionar um item não preparado, o servidor pede uma questão e seu comentário completos, valida a estrutura, pode auditá-los novamente, salva em `cache/` e apresenta a questão. Logo que ela aparece, o sistema solicita a geração da próxima.

Para outros sistemas, execute `python3 servidor.py` na pasta e acesse `http://127.0.0.1:8765/`.

## Como a pré-geração funciona

- **Questão atual pronta → dispara próxima em segundo plano.** Não é preciso solicitar outro prompt manualmente.
- Cada questão e comentário é gerada e salva uma única vez por `ID + rodada` na pasta `cache`.
- **Resposta → gabarito completo imediatamente**, quando o conteúdo já está preparado (a questão, o gabarito e a aula são gerados juntos).
- Na segunda rodada, a geração recebe a lista de lacunas identificadas na primeira, quando estiver registrada neste navegador.
- A pré-geração reduz o tempo de espera, mas **não promete latência zero** se você avançar mais rápido do que o provedor responder, se houver rate limit ou se a auditoria reprovar o conteúdo.

## Auditoria e fontes

O sistema solicita uma questão original de alta densidade, cinco alternativas, um único gabarito, comentário de A a E e revisão estrutural. Existem verificações formais (estrutura, cobertura, equilíbrio de tamanho, duplicidade de alternativas) e uma segunda chamada independente ao modelo quando `DEEP_AUDIT=1`. Isso reduz erros, mas **não certifica juridicamente a correção de todas as 503 questões**: referências legais e precedentes devem ser confrontados com fontes oficiais; caso os excertos sejam insuficientes, a IA deve reconhecer a lacuna.

**Marco temporal:** publicação do edital em 29/07/2026; legislação superveniente não é automaticamente exigível, ressalvadas as exceções expressas do edital. O índice de material exclui a apostila específica da Lei 15.487/2026 do contexto principal por ser posterior ao marco, e a separação deverá ser revista em caso de regra expressa de exigibilidade.

## Privacidade e custos

- O servidor só escuta em `127.0.0.1` (seu computador). A chave fica em `.env` e nunca deve ser exibida no navegador ou enviada ao GitHub.
- O servidor **não expõe** o `.env`, arquivos privados de cache, índice integral de excertos nem código-fonte por HTTP.
- As APIs de GPT/Claude possuem **cobrança própria por uso**, separada da assinatura do ChatGPT ou Claude. A segunda auditoria gera chamadas adicionais. Para reduzir custos, altere `DEEP_AUDIT=0` com perda de uma camada de revisão.
- Perguntas e trechos de fontes relevantes são enviados à API escolhida quando o recurso está ativo. Avalie as políticas de tratamento de dados do provedor.
- Sua resolução é guardada em `localStorage` no navegador; faça backup JSON periodicamente. O cache de perguntas fica na pasta `cache/`. Para migrar computador, transporte a pasta e importe o backup.
- Nunca publique este pacote completo em um site estático público: uma versão em nuvem exige backend, autenticação, limite de gastos e banco de dados hospedado. **GitHub Pages não executa o `servidor.py`.**

## Arquivos

- `index.html`: aplicação visual; também funciona parcialmente sozinho.
- `servidor.py`: conexão segura com OpenAI/Anthropic, geração, auditoria, pré-geração e cache.
- `.env.exemplo`: configuração de modelo e chave.
- `iniciar_windows.bat`: atalho do Windows.
- `assets/items.json`: 503 entradas importadas do edital verticalizado.
- `assets/banco_inicial.json`: três questões autorais iniciais.
- `assets/fontes_paginas.json`: índice de páginas de materiais de estudo, com marcas pessoais suprimidas.
- `cache/`: arquivos de questões geradas automaticamente (quando houver API).

**Estado de implementação:** arquivos e endpoints locais validados. A comunicação real com OpenAI/Anthropic não foi executada nesta entrega por não haver uma chave de API fornecida/configurada. Portanto, a conexão externa permanece **pronta para configuração**, não homologada contra uma conta real.
