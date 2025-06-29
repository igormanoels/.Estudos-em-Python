import numpy as np
from scipy.stats import poisson

'''
Um restaurante recebe em média 20 pedidos por hora, e deveremos descobrir qual a chance do restaurante receber 15 pedidos em uma determinada hora escolhida ao acaso.
Conseguiremos resolvera questão utilizando a Distribuição de Probabilidade Poisson.
Essa Distribuição é empregada para descrever número de ocorrências em um intervalo de tempo ou espaço específico, que nos permite contabilizar o sucesso, mas é 
impossível contar os fracassos, por exemplo.
'''
media = 20
k = 15
probabilidade = ((np.e ** (-media)) * (media ** k)) / (np.math.factorial(k))
print('%0.8f' % probabilidade)



probabilidade = poisson.pmf(k, media)
print('%0.8f' % probabilidade)


'''
O número médio de clientes que entram em uma padaria por hora é igual a 20. Obtenha a probabilidade de, na próxima hora, entrarem exatamente 25 clientes.
'''
# Média de clientes por hora
media = 20  

# Número de clientes desejado (k)
k = 25  

# Cálculo manual da fórmula de Poisson
probabilidade_manual = ((np.e ** (-media)) * (media ** k)) / (np.math.factorial(k))
print('Probabilidade (cálculo manual): %0.8f' % probabilidade_manual)

# Cálculo usando a função poisson.pmf do SciPy
probabilidade_scipy = poisson.pmf(k, media)
print('Probabilidade (SciPy): %0.8f' % probabilidade_scipy)