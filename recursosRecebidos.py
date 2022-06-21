#Api portal de transparencia
#Apis https://api.portaldatransparencia.gov.br/swagger-ui.html

import requests
import json
import pandas as pd
import time


url = "http://api.portaldatransparencia.gov.br/api-de-dados/despesas/recursos-recebidos"
codigoFavorecido = input('Informe o CNPJ do favorecido XX.XXX.XXX/XXXX-XX-> ') # 76.659.820/0001-51

mesAnoInicio = input('Informe o mês e ano inicial com o seguinte formato: MM/AAAA -> ')
mesAnoFim = input('Informe o mês e ano final com o seguinte formato: MM/AAAA -> ')
uf = input('Informe o código da Unidade Federativa em maiusculo XX -> ')
# SIAF: Ministério da educação : 26000; http://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/anexos/lei10933-04/10933Anexo_III.pdf

orgaoSuperior = input('informe o código do orgão superior: ex. MEC: 26000'\n "-> ")
params={"mesAnoFim": mesAnoFim, "mesAnoInicio": mesAnoInicio, "codigoFavorecido": codigoFavorecido, "pagina": 1 }
chaveAPidados = input('informe a chave-api-dados > ')
headers = {"chave-api-dados": chaveAPIdados}
resultado = requests.get(url, params=params, headers=headers)
print(resultado)
j = resultado.json()
dfRecursosRecebidos = pd.DataFrame.from_dict(j)
print(dfRecursosRecebidos.describe())
display(dfRecursosRecebidos.sort_values(by=['anoMes']))
