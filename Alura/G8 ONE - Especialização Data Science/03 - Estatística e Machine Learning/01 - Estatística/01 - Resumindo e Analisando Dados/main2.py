import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

url = 'https://raw.githubusercontent.com/alura-cursos/Estatisticas-Python-frequencias-medidas/refs/heads/main/dados/colaboradores.csv'
colaboradores = pd.read_csv(url)



# Demanda 8
print('\n\n', colaboradores.head())

n = len(colaboradores)
k = int(1 + (10/3) * math.log10(n))

faixas = colaboradores.copy()
faixas['faixa_salarial'] = pd.cut(faixas['remuneracao'], bins=int(k), include_lowest=True) # Quebra um campo numérico em classes
print('\n\n', faixas.head())


tabela_frequencias = faixas.groupby('faixa_salarial', observed=False ).size().reset_index(name='frequencia')
# Calculando a porcentagem
tabela_frequencias['porcentagem'] = (tabela_frequencias['frequencia'] / len(colaboradores)) * 100
print('\n\n', tabela_frequencias)

# Histograma 
plt.figure(figsize=(15, 6))
sns.histplot(data=faixas, x='remuneracao')
plt.show()

# 14 barras no histograma
sns.histplot(bins=int(k), data=colaboradores, x='remuneracao', kde=True)
plt.show()





# Demanda 9
quartis = {
    'Q1': colaboradores['remuneracao'].quantile(0.25),
    'Q2': colaboradores['remuneracao'].quantile(0.50),
    'Q3': colaboradores['remuneracao'].quantile(0.75)
}
print('\n\n', quartis) 


# Visualizando quartis em um histograma
plt.figure(figsize=(15, 6))
sns.histplot(binwidth = 500, data=colaboradores, x='remuneracao')
plt.axvline(quartis['Q1'], color='red', linestyle='dashed')
plt.axvline(quartis['Q2'], color='red', linestyle='dashed')
plt.axvline(quartis['Q3'], color='red', linestyle='dashed')
plt.show()

# Buscando quem está em 1% dos salário
percentil_99 = colaboradores['remuneracao'].quantile(0.99)
print('\n\n', percentil_99)

# Contagem dos coordenadores
coordenadores = colaboradores[colaboradores['cargo'] == 'Coordenador(a)']
num_coordenadores = len(coordenadores)

# Buscando o número de coloboradores que estão com um salário a 1% dos salários 
coordenadores_alta_remuneracao = colaboradores[(colaboradores['cargo'] == 'Coordenador(a)') & (colaboradores['remuneracao'] > percentil_99)]
num_coordenadores_alta_remuneracao = len(coordenadores_alta_remuneracao)
print('\n\nQuantidade de colaboradores que possuem um alto salário', num_coordenadores_alta_remuneracao)





# Demanda 11
plt.figure(figsize=(15, 6))
sns.histplot(data=colaboradores, x='idade', bins= 10, cumulative=True, stat='proportion', kde=True )
plt.axhline(0.20, color='red', linestyle='dashed')
plt.show()

idades_classificacao = colaboradores.copy()
idades_classificacao.head()

idades_classificacao = idades_classificacao.sort_values(by='idade') # 1. Ordenar os dados pela coluna 'idade'
idades_classificacao['cumulativo'] = (idades_classificacao.reset_index().index + 1) / len(idades_classificacao) # 2. Adicionar a coluna 'cumulativo' (posição relativa de cada linha)
idades_classificacao['qualificado'] = idades_classificacao['cumulativo'] <= 0.20 # 3. Adicionar a coluna 'qualificado' com base no valor de 'cumulativo'
idades_qualificados = idades_classificacao[idades_classificacao['qualificado'] == True]  # noqa: E712

print('\n\n', idades_qualificados, 'Quantidade: ', len(idades_qualificados))





# Demanda 12
plt.figure(figsize=(8, 6))
sns.boxplot(x=colaboradores['remuneracao'], color='steelblue')
plt.title('Boxplot de Salários')
plt.xlabel('Salário (R$)')
plt.ylim(-1, 1)
plt.show()

# Análisando os dados
print('\n\n', colaboradores.remuneracao.describe())

plt.figure(figsize=(8, 6))
ax = sns.boxplot(x='remuneracao', y='sexo_biologico', data=colaboradores, hue='sexo_biologico')
plt.title('Boxplot de Salários por Sexo Biológico')
plt.xlabel('Salário (R$)')
plt.ylabel('Sexo Biológico')
plt.show()

# Filtro de coloboradores onde a remuneração está menor que 10k
colaboradores_filtrados = colaboradores[colaboradores['remuneracao'] <= 10e3]
print('\n\n', colaboradores_filtrados.head())

plt.figure(figsize=(8, 6))
ax = sns.boxplot(x='remuneracao', y='sexo_biologico', data=colaboradores_filtrados, hue='sexo_biologico')
plt.title('Boxplot de Salários por Sexo Biológico')
plt.xlabel('Salário (R$)')
plt.ylabel('Sexo Biológico')
plt.show()



estat_remuneracao = colaboradores.groupby('sexo_biologico')['remuneracao'].agg(
    Q1 = lambda x: x.quantile(0.25),
    mediana = 'median',
    media = 'mean',
    Q3 = lambda x: x.quantile(0.75),
    IIQ = lambda x: x.quantile(0.75) - x.quantile(0.25)
).reset_index()
print('\n\n', estat_remuneracao)