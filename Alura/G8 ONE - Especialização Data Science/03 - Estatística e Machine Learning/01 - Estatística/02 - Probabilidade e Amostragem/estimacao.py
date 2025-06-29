import pandas as pd
import numpy as np

dados = pd.read_csv('D:/GitHub/.Estudos-em-Python/Alura/G8 ONE - Especialização Data Science/03 - Estatística e Machine Learning/01 - Estatística/02 - Probabilidade e Amostragem/dados.csv')

n = 2000
total_de_amostras = 1500

amostras = pd.DataFrame()

for i in range(total_de_amostras):
  _ = dados.Idade.sample(n)
  _.index = range(0, len(_))
  amostras['Amostra_' + str(i)] = _

print('\n', amostras)

print('\n', amostras.mean())

print('\n', dados.Idade.mean()) 

print('\n', amostras.mean().mean())

print('\n', amostras.mean().std())

print('\n', dados.Idade.std() / np.sqrt(n))