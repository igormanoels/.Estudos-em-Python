import pandas as pd

'''
Considerando o exemplo visto em aula, marque a forma correta de obtermos uma amostra aleatória simples do nosso dataset dados.

Para este problema, considere que queremos uma amostra de tamanho 1000.
'''

dados = pd.read_csv('D:/GitHub/.Estudos-em-Python/Alura/G8 ONE - Especialização Data Science/03 - Estatística e Machine Learning/01 - Estatística/02 - Probabilidade e Amostragem/dados.csv')


amostra = dados.sample(1000)
print('\n', amostra)
