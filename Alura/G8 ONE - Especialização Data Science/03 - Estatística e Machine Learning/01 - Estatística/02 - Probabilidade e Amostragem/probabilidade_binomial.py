import pandas as pd
#import numpy, matplotlib
from scipy.special import comb
from scipy.stats import binom

dados = pd.read_csv('D:/GitHub/.Estudos-em-Python/Alura/G8 ONE - Especialização Data Science/03 - Estatística e Machine Learning/01 - Estatística/02 - Probabilidade e Amostragem/dados.csv')

print('\n', dados.head(10))

'''
PROBLEMA
Em um concurso para preencher uma vaga de Cientista de Dados, temos um total de 80 questões de múltipla escolha, cada uma com três alternativas possíveis. Estas 
têm o mesmo valor, e suporemos que um candidato que não tenha estudado absolutamente nada resolva fazer a prova e chute todos os resultados. Assumindo que a prova 
vale 10 pontos e que a nota de corte é 5, ou seja, passará se sua nota for 5 ou mais e reprovará se for menos que 5, qual seria a chance deste candidato passar para 
próxima etapa do processo seletivo?

p = probabilidade de sucesso
q = (q - p) = probabilidade de fracasso
n = numero de eventos
k = numero de eventos desejados que tenham sucesso

'''
# Total de questões
n = 10

num_alternativas_por_questao = 3
p = 1 / num_alternativas_por_questao
print('Probabilidade de sucesso: ', p)


q = 1 - p
print('Probabilidade de fracasso: ', q)

# Total de acertos desejados
k = 5

# Manual
probabilidade = (comb(n, k) * (p**k) * (q**(n-k)))
print('\n\nProbabilidade de acertar no mínimo 5 questões: %0.15f' % probabilidade)


# Automática
probabilidade = binom.pmf(k, n, p)
print('Probabilidade de acertar no mínimo 5 questões: %0.15f' % probabilidade)

# Probabilidade de se acertar 5 ou 6 ou 7 ou 8 ou 9 ou 10
probabilidade = binom.pmf(5, n, p) + binom.pmf(6, n, p) + binom.pmf(7, n, p) + binom.pmf(8, n, p) + binom.pmf(9, n, p) + binom.pmf(10, n, p)
print('Probabilidade de acertar 5 ou mais: %0.15f' % probabilidade)

# outra forma
probabilidade = binom.pmf([5, 6, 7, 8, 9, 10], n, p).sum()
print('Probabilidade de acertar 5 ou mais: %0.15f' % probabilidade)

# Probabilidade de acertar até 4
probabilidade = binom.pmf([0, 1, 2, 3, 4], n, p).sum()
print('Probabilidade de acertar até 4 questões: %0.15f' % probabilidade)

# outra forma
probabilidade = binom.cdf(4, n, p)
print('Probabilidade de acertar até 4 questões: %0.15f' % probabilidade)

# e para encontrar a partir de 5 também pode ser feito
probabilidade = 1 - binom.cdf(4, n, p)
print('Probabilidade de acertar a partir de 5 questões: %0.15f' % probabilidade)

# ou sem usar - 1 com
probabilidade = binom.sf(4, n, p)
print('Probabilidade de acertar a partir de 5 questões: %0.15f' % probabilidade)


