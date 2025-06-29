from scipy.stats import binom
from scipy.special import comb

'''
Jogo de loteria
'''
n = 60 # numeros possiveis
k = 6 # numeros desejados
combinacoes = comb(n, k)
print('Número de combinações possíveis: ', combinacoes)
probabilidade = 1 / combinacoes
print('Probabilidade de acertar: %0.15f' % probabilidade)



'''
Suponha que acabamos de criar um jogo de loteria, chamado Show de prêmios da Alura. Neste nosso novo jogo, o apostador marca 20 números, 
dentre os 25 disponíveis no bilhete, e pode ganhar até 1 milhão de reais.
'''
combinacoes = comb(25, 20)
print('\nNúmero de combinações possíveis: ', combinacoes)
probabilidade = 1 / combinacoes
print('Probabilidade de acertar: %0.15f' % probabilidade)


'''
Uma moeda, perfeitamente equilibrada, é lançada para o alto quatro vezes. Utilizando a distribuição binomial, obtenha a probabilidade de a 
moeda cair com a face coroa voltada para cima duas vezes.
'''
combinacoes = comb(4, 2)
print('\nNúmero de combinações possíveis: ', combinacoes)
probabilidade = 1 / combinacoes
print('\nProbabilidade de cair cara: %0.15f' % probabilidade)


'''
Um dado, perfeitamente equilibrado, é lançado para o alto dez vezes. Utilizando a distribuição binomial, obtenha a probabilidade de o dado 
cair com o número cinco voltado para cima pelo menos três vezes.
'''
p = 1 / 6   # Probabilidade de sair o número CINCO
n = 10      # Total de lançamentos
probabilidade = binom.sf(2, n, p)
print("\nProbabilidade de cair o número 5, 3 vezez: {0:.2%}".format(probabilidade))

'''
Suponha que a probabilidade de um casal ter filhos com olhos azuis seja de 22%. Em 50 famílias, com 3 crianças cada uma, quantas podemos esperar
que tenham dois filhos com olhos azuis?

'''
p = 0.22
n = 3
k = 2
N = 50

probabilidade = binom.pmf(k, n, p)

media = probabilidade * N