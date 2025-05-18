import plotly.express as px
import pandas as pd


arquivo = 'Alura/G8 ONE - Especialização Data Science/02 - Aprendendo a fazer ETL/03 - Data Visualization/Matplotlib/dados/imigrantes_canada.csv'
imigrantes = pd.read_csv(arquivo)

# CRIANDO DADOS DO BRASIL NOVAMENTE
imigrantes.set_index('País', inplace=True)
anos = list(map(str, range(1980,2014)))
brasil = imigrantes.loc['Brasil', anos] 
brasil_dict = {'ano':brasil.index.tolist(), 'imigrantes':brasil.values.tolist()}
dados_brasil = pd.DataFrame(brasil_dict)






# CRIANDO UM GRÁFICO INTERATIVO
fig = px.line(dados_brasil, x='ano', y='imigrantes')
fig.show() # gera a visualizaação do gráfico que é aberto no navegador



# CRIANDO UM GRÁFICO INTERATIVO
fig = px.line(dados_brasil, x='ano', y='imigrantes', title='Imigração do Brasil para o Canadá\n1980 a 2013')
fig.update_traces(line_color='green', line_width=3) # cor da linha e espessura
# largura, altura e posição da legenda do eixo x, estilos da fonte e titulo, legenda eixo x e legenda eixo y
fig.update_layout(width=1000, 
                  height=500, 
                  xaxis={'tickangle':-45},
                  font_family='Arial',
                  font_size=14,
                  font_color='grey',
                  title_font_color='black',
                  title_font_size=22, 
                  xaxis_title='Ano',
                  yaxis_title='Número de imigrantes') 
fig.show() # gera a visualizaação do gráfico que é aberto no navegador










# GERANDO UM GRÁFICO COM TODOS OS DADOS
america_sul = imigrantes.query('Região == "América do Sul"')
america_sul_filtrada = america_sul.drop(['Continente', 'Região', 'Total'], axis=1)
america_sul_final = america_sul_filtrada.T # Transpõe os dados, alterando os dados para uma linha por ano e uma coluna por pais

fig = px.line(america_sul_final, 
              x=america_sul_final.index, 
              y=america_sul_final.columns, 
              color='País', 
              title='Imigração dos Países da America do Sul para o Canadá\n1980 a 2013')
fig.update_layout(width=1000, 
                  height=500, 
                  xaxis={'tickangle':-45},
                  font_family='Arial',
                  font_size=14,
                  font_color='grey',
                  title_font_color='black',
                  title_font_size=22, 
                  xaxis_title='Ano',
                  yaxis_title='Número de imigrantes') 
fig.show()





# SALVANDO EM HTML
fig.write_html('imigracao_america_sul.html')

