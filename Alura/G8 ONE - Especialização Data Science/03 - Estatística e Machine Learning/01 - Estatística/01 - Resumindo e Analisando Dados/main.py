import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = 'https://raw.githubusercontent.com/alura-cursos/estatistica-r-frequencias-medidas/refs/heads/main/dados/vendas_ecommerce.csv'
df = pd.read_csv(url)
print(df.head())


print('Quantidade de linhas x colunas: ', df.shape, '\n\n')


print(df.info())


categorias = df['categoria_produto'].unique() # Retorna um array com todas as categorias
print('\n\nCategorias: ', categorias )


quantidade_vendas = df['categoria_produto'].value_counts().reset_index()
print('\n\nQuantidade de vendas por categoria\n', quantidade_vendas )


plt.barh(quantidade_vendas['categoria_produto'], quantidade_vendas['count'])
plt.show()


avaliacao = sorted(df['avaliacao'].unique())
print('\n\nAvaliações: ', avaliacao)


avaliacao = {1: 'Péssimo', 2: 'Ruim', 3: 'Regular', 4: 'Bom', 5:'Ótimo'}
df['avaliacao_indicador'] = df['avaliacao'].map(avaliacao)
print('\n\n', df[['avaliacao_indicador', 'avaliacao', 'sexo_biologico']].head(10))


teste = df[['avaliacao', 'avaliacao_indicador']].drop_duplicates()
print('\n\nTestando se os valores estão corretos: \n', teste)


quantidades = df['quantidade'].unique()
print(quantidades)
print(f"\n\nVendemos de {min(df['quantidade'])} até {max(df['quantidade'])} unidades de produto por registro")


total_compra = df['total_compra'].unique()
print(f"\n\nTivemos vendas a partir de R$ {min(df['total_compra']):,.2f} até R$ {max(df['total_compra']):,.2f}")


df_ordenado = df.sort_values(by='total_compra') # É possivel reordenar todo o dataframe a partir de uma coluna
print('\n\n', df_ordenado.head())





# 1 Demanda
# Frequencia Absoluta
frequencia_avaliacoes = (df.groupby('avaliacao_indicador', observed=True)).size().reset_index(name='frequencia_absoluta').sort_values(by='avaliacao_indicador', ascending=True)
print('\n\n', frequencia_avaliacoes)

# Frequencia Relativa
frequencia_avaliacoes['frequencia_relativa'] = round((frequencia_avaliacoes['frequencia_absoluta'] / frequencia_avaliacoes['frequencia_absoluta'].sum()) * 100, 1)
print('\n\n', frequencia_avaliacoes)

frequencia_avaliacoes.columns = ['Avaliação', 'Quantidade', 'Porcentagem (%)']
print('\n\n', frequencia_avaliacoes)


plt.figure(figsize=(10, 6))
sns.barplot(data=frequencia_avaliacoes, x='Avaliação', y='Quantidade')
# Adicionando título e rótulos aos eixos
plt.title("Distribuição de Frequências das Avaliações")
plt.xlabel("Avaliação")
plt.ylabel("Frequência")
# Adicionando os rótulos com valores de frequência e porcentagem
for index, row in frequencia_avaliacoes.iterrows():
    plt.text(index, row['Quantidade'] + 0.1, f"{row['Quantidade']} ({row['Porcentagem (%)']:.1f}%)",
             ha='center', va='bottom', fontsize=12)
plt.show()





# 2 Demanda
tab_avaliacoes_regiao = pd.crosstab(df['avaliacao indicador'], df['regiao_cliente']) # Faz uma combinação entre duas ou mais variaveis
print('\n\n', tab_avaliacoes_regiao)

tab_avaliacoes_regiao_relativa = pd.crosstab(df['avaliacao indicador'], df['regiao_cliente'], normalize = 'columns') * 100
tab_avaliacoes_regiao_relativa = round(tab_avaliacoes_regiao_relativa, 1)
print('\n\n', tab_avaliacoes_regiao_relativa)

tab_avaliacoes_filtrada = tab_avaliacoes_regiao_relativa[tab_avaliacoes_regiao_relativa.index.isin(['Ótimo', 'Bom'])]
resultado = tab_avaliacoes_filtrada.sum()
print('\n\nRegiões com avaliações positivas\n', resultado)

tab_avaliacoes_filtrada = tab_avaliacoes_regiao_relativa[tab_avaliacoes_regiao_relativa.index.isin(['Ruim', 'Péssimo'])]
resultado = tab_avaliacoes_filtrada.sum()
print('\n\nRegiões com avaliações negativas\n', resultado)





# Demanda 3
ticket_medio = round(pd.crosstab(df['sexo_biologico'], df['regiao_cliente'], values=df['total_compra'], aggfunc='mean'), 2)
print('\n\n', ticket_medio) 





# Demanda 4
media_entrega =df['tempo_entrega'].mean()
print('\n\nMédia do tempo de entrega: ', media_entrega)

media_entrega_cat = df.groupby('categoria_produto')['tempo_entrega'].mean().reset_index().round(1)
print('\n\nMédia de entrega por categoria', media_entrega_cat)

media_entrega_cat.columns = ['categoria_produto', 'media_tempo'] # Dessa forma renomeamos as colunas
media_entrega_cat = media_entrega_cat.sort_values(by='media_tempo', ascending=False) # Os dados serão ordenados de forma invertida
print('\n\nMédia de entrega por categoria', media_entrega_cat)

# Criando o gráfico de barras com seaborn
plt.figure(figsize=(8, 6))
sns.barplot(data=media_entrega_cat, x='media_tempo', y='categoria_produto')
plt.axvline(media_entrega, color='red') # Cria uma barra vertical com o valor de média para auxiliar na análise dos valores que estão acima da média
plt.xlabel('Tempo de Entrega')
plt.ylabel('Categoria de Produto')
plt.show()





# Demanda 5
dados_nordeste = df[(df['regiao_cliente'] == 'Nordeste') & (df['categoria_produto'] == 'Eletrônicos')]
dados_nordeste = dados_nordeste.sort_values('total_compra')
print('\n\n', dados_nordeste.head())

n = len(dados_nordeste)
print('\n\nQuantidade de dados ', n)

elemento_md = int(n /2)

# Calculando a média entre o valor no índice 'elemento_md' e o próximo valor
mediana1 = round((dados_nordeste['total_compra'].iloc[elemento_md - 1] + dados_nordeste['total_compra'].iloc[elemento_md]) / 2,2)
# outra forma de cálcular
mediana2 = dados_nordeste.total_compra.median()
print('\n\nComparando valores de mediana', mediana1, ' = ', mediana2)
'''
UTILIZAR A MEDIANA PARA UMA ANÁLISE DE DADOS PARA VENDAS, É MAIS EFICAZ POIS, A MEDIANA PARA ESSES CENÁRIOS REFLETE QUAL O VALOR GASTO POR METADE DOS CONSUMIDORES. 
ENQUANTO A MÉDIA APONTA VALORES DISCREPANTES EM VIRTUDE DE TENDER A VALORES MUITO ALTOS E MUITO BAIXOS, O QUE GERA UMA DISTORÇÃO NA ANÁLISE
'''

sns.histplot(dados_nordeste.total_compra, bins=30)
plt.show()





# Demanda 6
print('\n\n', df['regiao_cliente'].value_counts())

dados_filtrados = df[df['categoria_produto'] == 'Livros']
print('\n\n', dados_filtrados.head())

moda = dados_filtrados.quantidade.mode()
print('\n\nBuscando a moda: ', moda)





# Demanda 7
sns.histplot(bins=21, data=df, x='tempo_entrega', kde=True, kde_kws={'bw_adjust':2})
plt.show()

# Criando um dicionário com com valores para análise
tempo_entrega_resumo = {
    'media': df['tempo_entrega'].mean(),
    'mediana': df['tempo_entrega'].median(),
    'moda': df['tempo_entrega'].mode()[0]
}
print('\n\n', tempo_entrega_resumo)

dados_nota_5 = df[df['avaliacao'] == 5]
dados_nota_5.head()

sns.histplot(bins=21, data=dados_nota_5, x='tempo_entrega', kde=True, kde_kws={'bw_adjust':2})
plt.show()


resumo = {
    'media': dados_nota_5['tempo_entrega'].mean(),
    'mediana': dados_nota_5['tempo_entrega'].median(),
    'moda': dados_nota_5['tempo_entrega'].mode()[0]
}
print('\n\n', resumo)





