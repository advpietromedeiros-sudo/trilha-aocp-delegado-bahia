# Jurisprudência do Pente Fino de Medicina Legal — cada entrada CONFERIDA em 07/11/2026:
#  STJ súmulas: processo.stj.jus.br/SCON/sumstj (data = "julgado em").
#  STJ HC 653.515/RJ: Informativo de Jurisprudência 720 (processo.stj.jus.br), julgado em 23/11/2021, Sexta Turma,
#  relator para o acórdão Min. Rogerio Schietti Cruz.
#  STF Súmula 361: PDF oficial "Enunciados das Súmulas do STF 1 a 736" (.scratch/pente_fino/stf_sumulas.txt;
#  data = Sessão Plenária de aprovação).
from base import _s

SCON = 'processo.stj.jus.br/SCON/sumstj'
STFPDF = 'stf.jus.br — Enunciados das Súmulas do STF 1 a 736 (PDF oficial)'
J = {
    'S542': _s('STJ', 'Súmula 542/STJ', '26/08/2015', 'A ação penal relativa ao crime de lesão corporal resultante de violência doméstica contra a mulher é pública incondicionada.', SCON),
    'S593': _s('STJ', 'Súmula 593/STJ', '25/10/2017', 'O estupro de vulnerável se configura com a conjunção carnal ou o ato libidinoso com menor de 14 anos, sendo irrelevantes o eventual consentimento da vítima, sua experiência sexual anterior ou relacionamento amoroso com o agente.', SCON),
    'S600': _s('STJ', 'Súmula 600/STJ', '22/11/2017', 'Para a configuração da violência doméstica e familiar prevista no art. 5º da Lei 11.340/2006, não se exige a coabitação entre autor e vítima.', SCON),
    'HC653515': _s('STJ', 'HC 653.515/RJ, 6ª Turma (Informativo 720)', '23/11/2021', 'A quebra da cadeia de custódia não gera, por si só, nulidade ou inadmissibilidade da prova: as irregularidades devem ser sopesadas pelo juiz com os demais elementos da instrução, para aferir se a prova é confiável.', 'processo.stj.jus.br — Informativo de Jurisprudência 720'),
    'STF361': _s('STF', 'Súmula 361/STF', '13/12/1963', 'No processo penal, é nulo o exame realizado por um só perito, considerando-se impedido o que tiver funcionado, anteriormente, na diligência de apreensão.', STFPDF),
}
