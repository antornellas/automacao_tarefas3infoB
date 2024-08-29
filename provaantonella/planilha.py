import pandas as pd
from main import preencher 

plan = pd.read_excel('PlanilhaLancamento.xlsx')

if plan[plan['Nome'] == 'ANTONELLA DOS SANTOS ORNELAS' ] :
    for (i, linha) in plan.iterrows():
        preencher(linha['Nome'], linha['Nota'],
                 linha['Atividade'])