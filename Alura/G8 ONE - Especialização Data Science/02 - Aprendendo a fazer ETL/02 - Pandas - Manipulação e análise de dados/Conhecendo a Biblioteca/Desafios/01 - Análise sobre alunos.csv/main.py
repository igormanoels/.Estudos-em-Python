import pandas as pd

# 1) Importe o arquivo alunos.csv e armazene seu conteúdo em um DataFrame Pandas.
arquivo = 'Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/Desafios/01 - Análise sobre alunos.csv/alunos.csv'
dados = pd.read_csv(arquivo,sep=',')

# 2) Visualize as primeiras 7 linhas do DataFrame e as 5 últimas.
print('\n', dados.head(7))

# 3) Confira a quantidade de linhas e colunas desse DataFrame.
print('\n', dados.shape)

# 4) Explore as colunas do DataFrame e analise os tipos dos dados presentes em cada coluna.
print('\n', dados[['Idade', 'Aprovado']])


# Extra: Calcule algumas estatísticas descritivas básicas dos dados do DataFrame (média, desvio padrão, etc). Dica: pesquise pelo método describe.
print('\n', dados.fillna(0)) # Trata os valores nulos atribuindo um valor
#print('\n', dados.shape)

print('\nMédia de idade: ', dados['Idade'].mean) 
print('\nMédia de notas: ', dados['Notas'].mean)

aprovados = pd.Series(dados['Aprovado'])
print('\nQtd Aprovados: ', aprovados.sum())
print('\nQtd Reprovados : ', (~aprovados).sum())
 