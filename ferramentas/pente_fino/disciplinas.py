"""Configuração das disciplinas do Pente Fino (usada por construir.py e conferir.py).
CPC: aprovado pelo titular (D-021) — os valores abaixo reproduzem, letra por letra, o arquivo já gerado.
CIV: Direito Civil e Empresarial (07/11/2026)."""
import re


def ordem_ponto(pid):
    """DBA26-CIV-4 < DBA26-CIV-4-B2 < DBA26-CIV-5; para o CPC dá a mesma ordem numérica de antes."""
    m = re.match(r'^DBA26-[A-Z]+-(\d+)(?:-B(\d+))?$', pid)
    return (int(m.group(1)), int(m.group(2) or 0)) if m else (10 ** 6, 0)


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
        cabecalho='// Pente Fino — Direito Civil e Empresarial (DBA26-CIV-1 a 12, com CIV-4-B2 e CIV-5-B2). Gerado por ferramentas/pente_fino/construir.py --disc CIV em 07/11/2026.',
        fontes=['Lei 10.406/2002 (Código Civil) — Planalto', 'Decreto-Lei 4.657/1942 (LINDB) — Planalto',
                'Lei 8.078/1990 (CDC) — Planalto', 'Lei 10.741/2003 (Estatuto da Pessoa Idosa) — Planalto',
                'Lei 13.146/2015 (Estatuto da Pessoa com Deficiência) — Planalto',
                'Lei 11.101/2005 (Recuperação e Falência) — Planalto',
                'Súmulas do STJ — processo.stj.jus.br/SCON/sumstj', 'Temas repetitivos do STJ — processo.stj.jus.br/repetitivos',
                'Súmulas do STF — PDF oficial "Enunciados das Súmulas do STF 1 a 736" (stf.jus.br)',
                'STF — Temas 786 e 1.127/RG e ADIs 4.815 e 5.357 (portal.stf.jus.br e notícias oficiais)']),
}
