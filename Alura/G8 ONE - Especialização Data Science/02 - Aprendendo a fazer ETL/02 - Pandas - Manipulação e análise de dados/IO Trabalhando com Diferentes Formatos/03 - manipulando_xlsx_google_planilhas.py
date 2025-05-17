import pandas as pd

link = 'https://docs.google.com/spreadsheets/d/12Xng6V4Jx3ow8i8nSiU6abXA6trUuWrdn_Kf9kE-IT8/edit?usp=sharing'

# trecho do próprio link
sheet_id = '12Xng6V4Jx3ow8i8nSiU6abXA6trUuWrdn_Kf9kE-IT8'

# parametro para que seja usado a API da google para acessar os dados: '/gviz/tq' 
# parametro para que o tipo de retorno das informações: 'tqx=out:csv'
# parametro para que todos os dados retornem: '&sheet'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'
dados = pd.read_csv(url)
print('\n',dados.head())


# Visualizando uma página em especifico
sheet_name = 'emissoes_percapita'
url_percapita = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
dados_percapita = pd.read_csv(url_percapita)
print('\n',dados_percapita.head())
