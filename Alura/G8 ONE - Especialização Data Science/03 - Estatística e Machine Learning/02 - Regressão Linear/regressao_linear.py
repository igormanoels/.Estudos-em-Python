import pandas as pd

# Lendo dados
dados = pd.read_csv("D:/GitHub/.Estudos-em-Python/Alura/G8 ONE - Especialização Data Science/03 - Estatística e Machine Learning/02 - Regressão Linear/Preços_de_casas.csv")

dados.info()

dados = dados.drop(columns = "Id")

# Correlação
corr = dados.corr()

corr['preco_de_venda']