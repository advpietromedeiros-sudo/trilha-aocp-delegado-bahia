"""Configuração das disciplinas do Pente Fino (usada por construir.py e conferir.py).
CPC: aprovado pelo titular (D-021) — os valores abaixo reproduzem, letra por letra, o arquivo já gerado.
CIV: Direito Civil e Empresarial (07/11/2026).
MLE: Medicina Legal (07/11/2026) — pontos com subitem (DBA26-MLE-5.1); volume próprio (R1 6–10, R2 5–8) e
assertiva só de doutrina admitida (a disciplina é doutrinária: nem todo sinal ou fenômeno tem lei por trás).
CRI: Criminologia (07/11/2026) — mesmo volume e mesma regra de doutrina sem fonte da MLE (disciplina doutrinária).
CPP: Direito Processual Penal (08/11/2026) — 41 pontos com subitens; volume próprio (R1 5–12, R2 3–8) e, como no CPC,
toda assertiva com lei ou jurisprudência (sem doutrina_sem_fonte).
PEN: Direito Penal (08/11/2026) — entregue em DUAS etapas na mesma sigla. Nesta entrega, só a PARTE GERAL
(DBA26-PEN-1 a PEN-9.2, 58 pontos), por isso a entrada traz `pontos_incluidos` (lista explícita): construir.py e
conferir.py usam essa lista no lugar de "todos os ids do edital com o prefixo" — e SÓ para a PEN; as demais
disciplinas, sem a chave, seguem exigindo todos os pontos. A PARTE ESPECIAL (PEN-10 a 10.14 e PEN-11) entra depois:
o próximo agente (1) cria os arquivos de conteúdo em pen/ (ex.: pen_p10_01_04.py, pen_p10_05_11.py, pen_p10_12_14.py,
pen_p11.py), (2) acrescenta os nomes em `modulos` e (3) acrescenta os ids em PEN_PARTE_ESPECIAL dentro de
`pontos_incluidos` — quando os 74 estiverem feitos, a chave pode simplesmente sair (volta a valer o edital inteiro)."""
import re


def ordem_ponto(pid):
    """DBA26-CIV-4 < DBA26-CIV-4-B2 < DBA26-CIV-5 e DBA26-MLE-5 < DBA26-MLE-5.1 < DBA26-MLE-5.2 < DBA26-MLE-6;
    para o CPC e o CIV dá a mesma ordem de antes (subitem 0 em todos)."""
    m = re.match(r'^DBA26-[A-Z]+-(\d+)(?:\.(\d+))?(?:-B(\d+))?$', pid)
    return (int(m.group(1)), int(m.group(2) or 0), int(m.group(3) or 0)) if m else (10 ** 6, 0, 0)


# Direito Penal — Parte Geral (entregue em 08/11/2026): títulos 1 a 9 do edital, com os subitens.
PEN_PARTE_GERAL = [
    'DBA26-PEN-1', 'DBA26-PEN-1.1', 'DBA26-PEN-1.2', 'DBA26-PEN-1.3', 'DBA26-PEN-1.4',
    'DBA26-PEN-2', 'DBA26-PEN-2.1', 'DBA26-PEN-2.2', 'DBA26-PEN-2.3', 'DBA26-PEN-2.4', 'DBA26-PEN-2.5',
    'DBA26-PEN-3', 'DBA26-PEN-3.1', 'DBA26-PEN-3.2', 'DBA26-PEN-3.3', 'DBA26-PEN-3.4', 'DBA26-PEN-3.5', 'DBA26-PEN-3.6',
    'DBA26-PEN-4'] + [f'DBA26-PEN-4.{i}' for i in range(1, 13)] + [
    'DBA26-PEN-5', 'DBA26-PEN-5.1',
    'DBA26-PEN-6'] + [f'DBA26-PEN-6.{i}' for i in range(1, 7)] + [
    'DBA26-PEN-7',
    'DBA26-PEN-8'] + [f'DBA26-PEN-8.{i}' for i in range(1, 14)] + [
    'DBA26-PEN-9', 'DBA26-PEN-9.1', 'DBA26-PEN-9.2']
# Parte Especial (a fazer): 'DBA26-PEN-10', 'DBA26-PEN-10.1' ... 'DBA26-PEN-10.14' e 'DBA26-PEN-11' (jurisprudência
# aplicada e legislação de cada tópico). Ao fazê-la, preencher esta lista e somá-la em pontos_incluidos.
PEN_PARTE_ESPECIAL = []

DISC = {
    'CPC': dict(
        prefixo='DBA26-CPC-',
        modulos=['c01_04', 'c05_08', 'c09_12'],
        disciplina='Direito Processual Civil',
        conferido_em='07/11/2026',
        cabecalho='// Pente Fino — Direito Processual Civil (DBA26-CPC-1 a 12). Gerado por ferramentas/pente_fino/construir.py em 07/11/2026.',
        fontes=['Lei 13.105/2015 (CPC) — Planalto', 'Lei 7.347/1985 (Ação Civil Pública) — Planalto',
                'Lei 4.717/1965 (Ação Popular) — Planalto', 'Lei 12.016/2009 (Mandado de Segurança) — Planalto',
                'Lei 9.099/1995 (Juizados Especiais) — Planalto', 'Lei 12.153/2009 (Juizados da Fazenda Pública) — Planalto',
                'Súmulas do STJ — processo.stj.jus.br/SCON/sumstj', 'Temas repetitivos do STJ — processo.stj.jus.br/repetitivos',
                'Súmulas do STF — PDF oficial "Enunciados das Súmulas do STF 1 a 736" (stf.jus.br)',
                'STF — Tema 1.075/RG (portal.stf.jus.br) e ADI 4.296 (Informativo STF 1.021)']),
    'CIV': dict(
        prefixo='DBA26-CIV-',
        pasta='civ',
        modulos=['civ_p01_03', 'civ_p04', 'civ_p05_07', 'civ_p08_12'],
        disciplina='Direito Civil e Empresarial',
        conferido_em='07/11/2026',
        volume=((8, 17), (6, 14)),  # reforço de Empresarial (CIV-4, CIV-5, CIV-11), aprovado pelo titular
        cabecalho='// Pente Fino — Direito Civil e Empresarial (DBA26-CIV-1 a 12, com CIV-4-B2 e CIV-5-B2). Gerado por ferramentas/pente_fino/construir.py --disc CIV em 07/11/2026.',
        fontes=['Lei 10.406/2002 (Código Civil) — Planalto', 'Decreto-Lei 4.657/1942 (LINDB) — Planalto',
                'Lei 8.078/1990 (CDC) — Planalto', 'Lei 10.741/2003 (Estatuto da Pessoa Idosa) — Planalto',
                'Lei 13.146/2015 (Estatuto da Pessoa com Deficiência) — Planalto',
                'Lei 11.101/2005 (Recuperação e Falência) — Planalto',
                'Súmulas do STJ — processo.stj.jus.br/SCON/sumstj', 'Temas repetitivos do STJ — processo.stj.jus.br/repetitivos',
                'Súmulas do STF — PDF oficial "Enunciados das Súmulas do STF 1 a 736" (stf.jus.br)',
                'STF — Temas 786 e 1.127/RG e ADIs 4.815 e 5.357 (portal.stf.jus.br e notícias oficiais)']),
    'MLE': dict(
        prefixo='DBA26-MLE-',
        pasta='mle',
        modulos=['mle_p01_03', 'mle_p04_05', 'mle_p06_09', 'mle_p10_13'],
        disciplina='Medicina Legal',
        conferido_em='07/11/2026',
        volume=((6, 10), (5, 8)),
        doutrina_sem_fonte=True,
        cabecalho='// Pente Fino — Medicina Legal (DBA26-MLE-1 a 13, com os subitens). Gerado por ferramentas/pente_fino/construir.py --disc MLE em 07/11/2026.',
        fontes=['Decreto-Lei 3.689/1941 (CPP) — Planalto', 'Decreto-Lei 2.848/1940 (Código Penal) — Planalto',
                'Lei 10.406/2002 (Código Civil) — Planalto', 'Lei 9.434/1997 (Transplantes) — Planalto',
                'Lei 11.340/2006 (Maria da Penha) — Planalto', 'Lei 8.069/1990 (ECA) — Planalto',
                'Lei 13.431/2017 (escuta especializada e depoimento especial) — Planalto',
                'Lei 10.741/2003 (Estatuto da Pessoa Idosa) — Planalto', 'Lei 13.146/2015 (Estatuto da Pessoa com Deficiência) — Planalto',
                'Lei 12.037/2009 (Identificação criminal) e Lei 7.210/1984 (LEP) — Planalto',
                'Lei 9.503/1997 (CTB) e Lei 11.343/2006 (Drogas) — Planalto',
                'Súmulas do STJ — processo.stj.jus.br/SCON/sumstj',
                'Súmulas do STF — PDF oficial "Enunciados das Súmulas do STF 1 a 736" (stf.jus.br)',
                'STJ — HC 653.515/RJ (Informativo 720, processo.stj.jus.br)',
                'Doutrina médico-legal: redação própria, posição majoritária; divergências declaradas no comentário']),
    'CRI': dict(
        prefixo='DBA26-CRI-',
        pasta='cri',
        modulos=['cri_p01_02', 'cri_p03', 'cri_p04_06', 'cri_p08_16'],
        disciplina='Criminologia',
        conferido_em='07/11/2026',
        volume=((6, 10), (5, 8)),
        doutrina_sem_fonte=True,
        cabecalho='// Pente Fino — Criminologia (DBA26-CRI-1 a 16, com os subitens; o CRI-8 traz também o tópico 9 do edital). Gerado por ferramentas/pente_fino/construir.py --disc CRI em 07/11/2026.',
        fontes=['Constituição Federal de 1988 — Planalto', 'Decreto-Lei 2.848/1940 (Código Penal) — Planalto',
                'Decreto-Lei 3.689/1941 (CPP) — Planalto', 'Lei 7.210/1984 (LEP) — Planalto',
                'Lei 9.099/1995 (Juizados Especiais) — Planalto', 'Lei 11.340/2006 (Maria da Penha) — Planalto',
                'Lei 12.830/2013 (investigação criminal pelo delegado de polícia) — Planalto',
                'Lei 13.431/2017 (escuta especializada e depoimento especial) — Planalto',
                'Lei 13.869/2019 (Abuso de Autoridade), art. 15-A incluído pela Lei 14.321/2022 — Planalto',
                'Doutrina criminológica: redação própria, posição mais cobrada em concurso; divergências declaradas no comentário']),
    'CPP': dict(
        prefixo='DBA26-CPP-',
        pasta='cpp',
        modulos=['cpp_p01', 'cpp_p02_03', 'cpp_p04_06', 'cpp_p07', 'cpp_p08', 'cpp_p09_15'],
        disciplina='Direito Processual Penal',
        conferido_em='08/11/2026',
        volume=((5, 12), (3, 8)),  # 41 pontos (com subitens): R1 5–7 e R2 3–5 na média; os grandes (inquérito, competência, ação penal, provas, prisões) vão além
        cabecalho='// Pente Fino — Direito Processual Penal (DBA26-CPP-1 a 15, com os subitens, CPP-4.2-B2 e CPP-15-B2). Gerado por ferramentas/pente_fino/construir.py --disc CPP em 08/11/2026.',
        fontes=['Decreto-Lei 3.689/1941 (CPP), com a Lei 13.964/2019 (Pacote Anticrime) — Planalto',
                'Constituição Federal de 1988 — Planalto', 'Decreto-Lei 2.848/1940 (Código Penal) — Planalto',
                'Lei 9.099/1995 (Juizados Especiais) — Planalto', 'Lei 12.830/2013 (investigação criminal pelo delegado) — Planalto',
                'Lei 7.960/1989 (prisão temporária) e Lei 8.072/1990 (crimes hediondos) — Planalto',
                'Lei 9.296/1996 (interceptação telefônica) e Lei 12.850/2013 (organizações criminosas) — Planalto',
                'Lei 11.340/2006 (Maria da Penha), Lei 12.037/2009 (identificação criminal) e Lei 13.869/2019 (abuso de autoridade) — Planalto',
                'Súmulas do STJ — processo.stj.jus.br/SCON/sumstj',
                'Súmulas do STF — PDF oficial "Enunciados das Súmulas do STF 1 a 736" (stf.jus.br) e Súmulas Vinculantes (portal.stf.jus.br)',
                'STF — ADIs 6.298/6.299/6.300/6.305, ADIs 3.360 e 4.109, ADPFs 395 e 444, HC 185.913, Temas 184 e 280/RG (portal.stf.jus.br e notícias oficiais)',
                'STJ — HC 598.886/SC e RHC 158.580/BA (Informativos 684 e 735)']),
    'PEN': dict(
        prefixo='DBA26-PEN-',
        pasta='pen',
        modulos=['pen_p01_02', 'pen_p03', 'pen_p04', 'pen_p05_07', 'pen_p08', 'pen_p09'],
        # Parte Especial: acrescentar aqui os módulos novos (ver docstring do arquivo).
        pontos_incluidos=PEN_PARTE_GERAL + PEN_PARTE_ESPECIAL,
        disciplina='Direito Penal',
        conferido_em='08/11/2026',
        volume=((5, 12), (3, 8)),  # 58 pontos da Parte Geral: R1 5–6 e R2 3–4 na média; os de maior incidência AOCP (9.1, 1.1, 7, 1.2, 2.2...) vão além
        cabecalho='// Pente Fino — Direito Penal, Parte Geral (DBA26-PEN-1 a PEN-9.2, com os subitens; a Parte Especial entra depois). Gerado por ferramentas/pente_fino/construir.py --disc PEN em 08/11/2026.',
        fontes=['Decreto-Lei 2.848/1940 (Código Penal), Parte Geral, com as Leis 13.964/2019, 14.994/2024, 15.159/2025, 15.160/2025, 15.358/2026 e 15.438/2026 — Planalto',
                'Constituição Federal de 1988 — Planalto', 'Lei 7.210/1984 (LEP) — Planalto',
                'Lei 8.072/1990 (crimes hediondos), Lei 9.099/1995 e Decreto-Lei 3.688/1941 (LCP) — Planalto',
                'Lei 9.605/1998 (crimes ambientais) e Lei 11.343/2006 (Drogas) — Planalto',
                'Súmulas do STJ — processo.stj.jus.br/SCON/sumstj', 'Temas repetitivos do STJ — processo.stj.jus.br/repetitivos',
                'Súmulas do STF — PDF oficial "Enunciados das Súmulas do STF 1 a 736" (stf.jus.br) e Súmulas Vinculantes (portal.stf.jus.br)',
                'STF — ADPF 779, HC 176.473, HC 84.412 e Tema 788/RG (portal.stf.jus.br e notícias oficiais)']),
}
