from cProfile import label
from matplotlib import markers
from matplotlib.lines import lineStyles
import matplotlib.pyplot as  plt
import pandas as pd

arquivo = 'Alura/G8 ONE - Especialização Data Science/02 - Aprendendo a fazer ETL/03 - Matplotlib - Data Visualization/dados/imigrantes_canada.csv'
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




# Criando os gráficos em plotagem
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes']) # Primeiro parametro vai no eixo 'x', segundo no eixo 'y'
plt.show()


# Segundo gráfico em plotagem
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




# Criando uma figura
fig, ax = plt.subplots(figsize=(8,4)) # Permite criar uma figura, 'ax' representa o eixo
ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
ax.set_title('Imigração do Brasil para o Canadá\n1980 a 2013') # titulo
ax.set_xlabel('Ano') # Rótulo do eixo 'x'
ax.set_ylabel('Número de Imigrantes') # Rótulo do eixo 'x'
ax.xaxis.set_major_locator(plt.MultipleLocator(5)) # Faz com que a frequencia das ocorrencias sejam de 5 anos
plt.show()



# Criando dois gráficos em uma mesma figura
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



# Criando 1 figura com 4 gráficos
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




# Aplicando estilo a figura
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'], lw=3, markers='o') # Define a espessura da linha, inclui marcadores nas linhas
ax.set_title('Imigração do Brasil para o Canadá\n1980 a 2013', fontsize=18, loc='left') # Altera o tamanho da fonte, posição de alinhamento do texto
ax.set_xlabel('Ano', fontsize=14)
ax.set_ylabel('Número de Imigrantes', fontsize=14)
ax.xaxis.set_tick_params(labelsize=10) # Altera o tamanho da fonte do eixo x
ax.yaxis.set_tick_params(labelsize=10) # Altera o tamanho da fonte do eixo y
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
plt.grid(linestyles='--') # Adiciona uma grade atrás dos dados, o parametro se refere ao tipo de linha
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
  fig, ax = plt.subplots(figsize=(8, 4))
  ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'], lw=3)
  ax.set_title('Imigração do Brasil para o Canadá\n1980 a 2013', fontsize=20, loc='left')
  ax.set_ylabel('Número de imigrantes', fontsize=14)
  ax.set_xlabel('Ano', fontsize=14)
  ax.yaxis.set_tick_params(labelsize=12)
  ax.xaxis.set_tick_params(labelsize=12)
  ax.xaxis.set_major_locator(plt.MultipleLocator(5))
  plt.show()