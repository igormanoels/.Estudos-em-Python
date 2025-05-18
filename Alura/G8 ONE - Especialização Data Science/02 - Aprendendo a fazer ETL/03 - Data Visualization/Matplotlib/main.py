import matplotlib.pyplot as  plt
import pandas as pd



# FORMATANDO OS DADOS PARA PLOTAGEM GRÁFICA
arquivo = 'Alura/G8 ONE - Especialização Data Science/02 - Aprendendo a fazer ETL/03 - Data Visualization/Matplotlib/dados/imigrantes_canada.csv'
imigrantes = pd.read_csv(arquivo)

print('\n', imigrantes.head(10))
print('\n', imigrantes.info()) # Apenas dados do tipo String e Int, não há dados nulos

# Tendencias de imigração do brasil
imigrantes.set_index('País', inplace=True) # set_index, indica que a coluna parametro passa a ser o indice, e inplace aplica sobre o dataframe atual

anos = list(map(str, range(1980,2014))) # Criando um array com os anos
print(anos)

# Localiza dentro do dataframe todos os valores correspondentes ao parametro1, nas colunas parametro2
brasil = imigrantes.loc['Brasil', anos] 
# Criando um dicionario, 1 coluna recebe de brasil os dados dos anos, convertendo a series em lista. O mesmo acontece depois pegando os valores tbm criando uma lista
brasil_dict = {'ano':brasil.index.tolist(), 'imigrantes':brasil.values.tolist()}
# convertendo os dicionários em um dataframe
dados_brasil = pd.DataFrame(brasil_dict)
print('\n', dados_brasil)










# CRIANDO UM GRÁFICO DE PLOTAGEM
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes']) # Primeiro parametro vai no eixo 'x', segundo no eixo 'y'
plt.show()










# SEGUNDO GRÁFICO EM PLOTAGEM
plt.figure(figsize=(8,4)) # Altera o tamanho do gráfico, medidas são informadas em polegadas
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
plt.title('Gráfico de Imigração do Brasil para o Canadá') # Incluindo título
plt.xlabel('Ano') # Rótulo do eixo 'x'
plt.ylabel('Número de imigrantes') # Rótulo do eixo 'y'
# Apartir de uma lista, modifica os valores possiveis do eixo 'x', gerando um intervalo maior
plt.xticks(['1980','1985','1990','1995','2000','2005','2010','2015'])
# E o mesmo também se aplica ao eixo 'y'. Essas modificações devem ser de acordo com o tipo de dado da coluna do dataframe
plt.yticks([1000,2000,3000])
plt.show() # Exibindo os dados da plotagem










# CRIANDO UMA FIGURA COM GRÁFICO
fig, ax = plt.subplots(figsize=(8,4)) # Permite criar uma figura, 'ax' representa o eixo
ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
ax.set_title('Imigração do Brasil para o Canadá\n1980 a 2013') # titulo
ax.set_xlabel('Ano') # Rótulo do eixo 'x'
ax.set_ylabel('Número de Imigrantes') # Rótulo do eixo 'x'
ax.xaxis.set_major_locator(plt.MultipleLocator(5)) # Faz com que a frequencia das ocorrencias sejam de 5 anos
plt.show()










# CRIANDO DOIS GRÁFICOS EM UMA MESMA FIGURA
fig, axs = plt.subplots(1, 2, figsize=(15, 5) ) # Número de linhas e quantidade de gráficos, tamanho da figura
# primeiro gráfico
axs[0].plot(dados_brasil['ano'], dados_brasil['imigrantes'])
axs[0].set_title('Imigração do Brasil para o Canadá\n1980 a 2013')
axs[0].set_xlabel('Ano') 
axs[0].set_ylabel('Número de Imigrantes')
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))
axs[0].grid() 
# segundo gráfico
axs[1].boxplot(dados_brasil['imigrantes']) # apenas é necessário colocar o eixo 'y'
axs[1].set_title('BoxPlot - Imigração do Brasil para o Canadá\n1980 a 2013')
axs[1].set_xlabel('Ano') 
axs[1].set_ylabel('Número de Imigrantes')
axs[1].grid()
plt.show()










'''
    Função do pandas que retorna vários dados como:
    contagem, média, soma, minimo, percentual entre 25,50 e 75% e maximo.
'''
print(dados_brasil.describe()) 










# CRIANDO UMA FIGURA COM 4 GRÁFICOS
fig, axs = plt.subplots(2,2, figsize=(10,6)) 
fig.subplots_adjust(hspace=0.5, wspace=0.3) # Ajusta o espaçamento entre as figuras
fig.suptitle('Imigração dos quatro maiores paises da américa do sul para o canadá\n1980 a 2013')

axs[0,0].plot(imigrantes.loc['Brasil', anos])
axs[0,0].set_title('Brasil')

axs[0,1].plot(imigrantes.loc['Colômbia', anos])
axs[0,1].set_title('Colômbia')

axs[1,0].plot(imigrantes.loc['Argentina', anos])
axs[1,0].set_title('Argentina')

axs[1,1].plot(imigrantes.loc['Peru', anos])
axs[1,1].set_title('Peru')

ymin = 0
ymax = 7000
# Ao invés de reescrever o mesmo código, é possivel com um loop 'for' aplicar essas mudanças a todas as figuras
for ax in axs.flat:
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))
    ax.set_xlabel('Ano')
    ax.set_ylabel('Imigrantes')
    ax.set_ylim(ymin, ymax)

plt.show()










# APLICANDO ESTILO A FIGURA
fig, ax = plt.subplots(figsize=(10,5))
# Define a espessura da linha, inclui marcadores nas linhas, parametro da cor usando a inicial
ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'], lw=3, marker='o', color='green') 

ax.set_title('Imigração do Brasil para o Canadá\n1980 a 2013', fontsize=18, loc='left') # Altera o tamanho da fonte, posição de alinhamento do texto
ax.set_xlabel('Ano', fontsize=14)
ax.set_ylabel('Número de Imigrantes', fontsize=14)
ax.xaxis.set_tick_params(labelsize=10) # Altera o tamanho da fonte do eixo x
ax.yaxis.set_tick_params(labelsize=10) # Altera o tamanho da fonte do eixo y
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
'''
    Adiciona uma grade atrás dos dados, o parametro se refere ao tipo de linha
    - Pode ser aplicado por plt.grid(parametros) ou ax.grid(parametros)
    - linestyle: Define o estilo da linha da grade, pode ser: 
        '-' (linha sólida)
        '--' (linha tracejada)
        '-.' (linha traço-ponto)
        ':' (linha pontilhada
    - linewidth: altera a espessura
    - color: é a cor
    - alpha: Define a transparência da linha da grade (um valor entre 0 e 1, onde 0 é totalmente transparente e 1 é totalmente opaco). 

    E também é possivel aplicar a linha de fundo apenas para o eixo desejado com:
    - plt.grid(axis='x') ou ax.grid(axis='x'): Exibe a grade apenas no eixo X.
    - plt.grid(axis='y') ou ax.grid(axis='y'): Exibe a grade apenas no eixo Y. 
'''
ax.grid(True, linestyle='--', linewidth=0.5, color='lightgray', alpha=0.5)
plt.show()










# CRIANDO UMA FIGURA COM GRÁFICO DE BARRAS
cores = ['royalblue', 'orange', 'forestgreen', 'orchid', 'purple', 'brown', 'slateblue', 'gray', 'olive', 'navy', 'teal', 'tomato']
america_sul = imigrantes.query('Região == "América do Sul"')
print('\n', america_sul)
fig, ax = plt.subplots(figsize=(12,5))
ax.bar(america_sul.index, america_sul['Total'], color=cores) # aplicando cores distantas em um gráfico
ax.set_title('Imigração da América do Sul para o Canadá\n1980 a 2013', fontsize=18)
ax.set_xlabel('')
ax.set_ylabel('Total de imigrantes', fontsize=14)
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
'''
    Outras formas de fazer a remoção dos frames
ax.spines.top.set_visible(False)
ax.spines['top'].set_visible(False) # Remove a linha superior, pode ser usada botton
ax.spines['right'].set_visible(False) # remove a linha da direita, pode ser usada como left
'''
ax.spines[['top', 'right']].set_visible(False)
plt.show()









# CRIANDO UMA FIGURA COM GRÁFICO DE BARRAS INVERTIDO
america_sul = imigrantes.query('Região == "América do Sul"')
print('\n', america_sul)
fig, ax = plt.subplots(figsize=(12,5))
ax.barh(america_sul.index, america_sul['Total'], color=cores) # barh --> barra horizontal
ax.set_title('Imigração da América do Sul para o Canadá\n1980 a 2013', fontsize=18)
ax.set_xlabel('Total de imigrantes', fontsize=14)
ax.set_ylabel('')
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
plt.show()











# CRIANDO UMA FIGURA COM GRÁFICO DE BARRAS INVERTIDO COM DADOS ORDENADOS
america_sul_sorted = america_sul.sort_values('Total', ascending=True) # Realiza a odenação dos dados do maior para o menor
cores = []

for pais in america_sul_sorted.index:
    if pais == 'Brasil':
        cores.append('green')
    else:
      cores.append('silver')

america_sul = imigrantes.query('Região == "América do Sul"')
print('\n', america_sul)
fig, ax = plt.subplots(figsize=(12,7))
ax.barh(america_sul_sorted.index, america_sul_sorted['Total'], color=cores) # barh --> barra horizontal
ax.set_title('América do Sul: Brasil foi o quarto pais com mais imigrantes para o Canadá\nem 1980 a 2013', fontsize=18)
ax.set_xlabel('Total de imigrantes', fontsize=14)
ax.set_ylabel('')
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

for i, v in enumerate(america_sul_sorted['Total']):
   ax.text(v + 20, i, str(v), color='black', fontsize=10, ha='left', va='center')

ax.set_frame_on(False) # remove o frame do gráfico
ax.get_xaxis().set_visible(False) # remove o eixo x
''' 
    primeiro parametro é a qual eixo vc se refere
    depois de qual vc quer remover
    por ultimo o tamanho do marcador, colocando zero agt remove
    você pode escolher o eixo x ou y e length para aumentar o tamanho do marcador
'''
ax.tick_params(axis='both', which='both', length=0) #both quer dizer ambos
plt.show()










'''
 Outra forma de aplicar estilos é usando um dos estilos disponíveis é baseado em um site de notícias 
 e análises de dados chamado FiveThirtyEight, que cobre assuntos como política, economia, cultura, ciência e esportes.
'''
print(plt.style.available) # Retorna uma lista de estilos disponíveis para o uso
lista_atual = ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 
               'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 
               'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 
               'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 
               'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

'''
Portanto, para evitar que o estilo seja aplicado a todos os gráficos plotados no mesmo notebook, 
podemos utilizar um código que cria uma cópia das configurações padrão de plotagem da biblioteca 
Matplotlib e as atribui à variável IPython_default. Isso pode ser útil para armazenar e reutilizar 
as configurações padrão de plotagem ou para restaurá-las depois de terem sido modificadas:
'''
IPython_default = plt.rcParams.copy()
plt.style.use('fivethirtyeight') # Altera o estilo da biblioteca para o desejado


with plt.style.context('fivethirtyeight'): # coloca dentro do contexto o estilo deseado
  fig, ax = plt.subplots(figsize=(15, 8))
  ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'], lw=3)
  ax.set_title('Imigração do Brasil para o Canadá\n1980 a 2013', fontsize=20, loc='left')
  ax.set_ylabel('Número de imigrantes', fontsize=14)
  ax.set_xlabel('Ano', fontsize=14)
  ax.yaxis.set_tick_params(labelsize=12)
  ax.xaxis.set_tick_params(labelsize=12)
  ax.xaxis.set_major_locator(plt.MultipleLocator(5))
  plt.show()









# SANLVANDO FIGURA COM GRÁFICO
print('\n\n\n', fig.canvas.get_supported_filetypes()) # Retorna os formatos em que o gráfico pode ser salvo

'''
    transparent: fundo transparente ou não, no caso o false faz com q ele fique branco
    dpi: resolução
    bbox_inches: ajusta os limites da figura ao gráfico 
'''
fig.savefig('imigracao_brasil_canada.png', transparent=False, dpi=300, bbox_inches='tight')




