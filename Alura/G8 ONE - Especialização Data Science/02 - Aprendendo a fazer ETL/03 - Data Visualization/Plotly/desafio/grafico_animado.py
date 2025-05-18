'''
Na atividade anterior foi possível compreender como criar uma animação com a biblioteca Plotly. Agora vem mais um desafio!

Lembra que nós criamos uma figura estática contendo os dados de imigração do Brasil e Argentina? Sua tarefa é criar um 
gráfico animado com o Plotly que mostre esses dados. O gráfico deve ter as seguintes características:

Duas linhas: uma para o Brasil e outra para a Argentina.
Um botão "Play" para iniciar a animação, mostrando o aumento ou diminuição do número de imigrantes ao longo dos anos.
As configurações de animação devem fazer com que as duas linhas sejam exibidas e animadas ao mesmo tempo.
Dicas:

Crie um DataFrame com os dados da Argentina e não se esqueça de deixar a coluna de anos no tipo int(inteiro).
Use o código fornecido para o Brasil como base e adapte-o para incluir os dados da Argentina.
Para configurar as animações você pode fazer um Loop for para percorrer o DataFrame dados_brasil e para cada iteração, 
criar uma nova lista contendo dois objetos do tipo go.Scatter, um para cada país. Em seguida, cada lista pode ser usada 
para criar um objeto go.Frame, que é adicionado à lista de frames. Por fim, a lista de frames pode ser atribuída ao objeto 
fig, que é a figura do gráfico a ser animado. Com isso, quando a animação for iniciada, o gráfico exibirá as duas linhas em 
movimento, uma para o Brasil e outra para a Argentina.

'''

import plotly.graph_objs as go
import pandas as pd

arquivo = 'Alura/G8 ONE - Especialização Data Science/02 - Aprendendo a fazer ETL/03 - Data Visualization/Matplotlib/dados/imigrantes_canada.csv'
imigrantes = pd.read_csv(arquivo)

# CRIANDO DADOS DO BRASIL NOVAMENTE
imigrantes.set_index('País', inplace=True)
anos = list(map(str, range(1980,2014)))
brasil = imigrantes.loc['Brasil', anos] 
brasil_dict = {'ano':brasil.index.tolist(), 'imigrantes':brasil.values.tolist()}
dados_brasil = pd.DataFrame(brasil_dict)

argentina = imigrantes.loc['Argentina', anos] 
argentina_dict = {'ano':argentina.index.tolist(), 'imigrantes':argentina.values.tolist()}
dados_argentina = pd.DataFrame(argentina_dict)

# Criando uma figura
fig = go.Figure()

# Adicionando a linha com os dados do Brasil 
fig.add_trace(
    go.Scatter(x=[dados_brasil['ano'].iloc[0]], y=[dados_brasil['imigrantes'].iloc[0]], mode='lines', name='Imigrantes do Brasil', line=dict(width=4))
)

# Adicionando a linha com os dados da Argentina
fig.add_trace(
    go.Scatter(x=[dados_argentina['ano'].iloc[0]], y=[dados_argentina['imigrantes'].iloc[0]], mode='lines', name='Imigrantes da Argentina', line=dict(width=4))
)

# Definindo as configurações de layout
fig.update_layout(
    title=dict(
        text='<b>Imigração do Brasil e da Argentina para o Canadá no período de 1980 a 2013',
        x=0.1,

        font=dict(size=18)
    ),
    xaxis=dict(range=[1980, 2013], autorange=False, title='<b>Ano</b>'),
    yaxis=dict(range=[0, 3000], autorange=False, title='<b>Número de imigrantes</b>'),
    updatemenus=[dict(
        type='buttons',
        showactive=False,
        buttons=[dict(
            label='Play',
            method='animate',
            args=[None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}]
        )]
    )],
    width=1200, # largura da figura em pixels
    height=600 # altura da figura em pixels
)

# Definindo as configurações de animação
frames = []
for i in range(len(dados_brasil)):
    frame_data = [
        go.Scatter(x=dados_brasil['ano'].iloc[:i+1], y=dados_brasil['imigrantes'].iloc[:i+1]),
        go.Scatter(x=dados_argentina['ano'].iloc[:i+1], y=dados_argentina['imigrantes'].iloc[:i+1])
    ]
    frame = go.Frame(data=frame_data)
    frames.append(frame)
fig.frames = frames

# Mostrando a figura
fig.show()