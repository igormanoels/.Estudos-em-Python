import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


arquivo = 'Alura/G8 ONE - Especialização Data Science/02 - Aprendendo a fazer ETL/03 - Data Visualization/Matplotlib/dados/imigrantes_canada.csv'
imigrantes = pd.read_csv(arquivo)

# ADCIONANDO TEMA PADRÃO, OU PASSANDO PARAMETRO PARA O TEMA DESEJADO
sns.set_theme()





# CRIANDO UM GRÁFICO DE BARRAS
top_10 = imigrantes.sort_values('Total', ascending=False).head(10) # Ordena os dados pela coluna total e pega os 10 primeiros
print('\nTOP 10\n', top_10) # Verificamos se deu certo
sns.barplot(data=top_10, x='País', y='Total') # Primeiro o dataframe, depois o eixo 'x' e 'y'
plt.show()

# INVERTENDO O GRÁFICO DE BARRAS
sns.barplot(data=top_10, x='Total', y='País', orient='h') # Invertendo o gráfico e incluindo a orientação em horizontal
plt.show()










# TESTANDO AS PALETAS DE CORES PARA OS DADOS DO GRÁFICO
def gerar_grafico(paleta):
    fig, ax = plt.subplots(figsize=(12,8))
    ax = sns.barplot(data=top_10, x='Total', y='País', orient='h', palette=paleta)
    ax.set_title("Top 10 países com maior imigração para o Canadá\n1980 a 2013", fontsize=18)
    ax.set_xlabel('Número de imigrantes', fontsize=12)
    ax.set_ylabel('', fontsize=12)
    plt.show()

gerar_grafico('Blues') # Conform a paleta
gerar_grafico('Blues_r') # Inverte as cores da paleta
gerar_grafico('rocket')
gerar_grafico('coolwarm_r')
gerar_grafico('tab10')

# ALTERANDO O ESTILO
sns.set_theme(style='dark') # Possui um fundo com um tom mais escuro liso
gerar_grafico('tab10')

sns.set_theme(style='whitegrid') # Possui um fundo com tom branco e inclui um grid de fundo
gerar_grafico('tab10')

sns.set_theme(style='white') # Possui um fundo com tom branco liso
gerar_grafico('tab10')

sns.set_theme(style='ticks') # Possui um fundo com tom branco liso e inclui marcadores no eixo x e y
gerar_grafico('tab10')










# CRIANDO A FIGURA SEM A CAIXA
fig, ax = plt.subplots(figsize=(12,8))
ax = sns.barplot(data=top_10, x='Total', y='País', orient='h', palette='tab10')
ax.set_title("Top 10 países com maior imigração para o Canadá\n1980 a 2013", fontsize=18)
ax.set_xlabel('Número de imigrantes', fontsize=12)
ax.set_ylabel('', fontsize=12)
sns.despine()
plt.show()
