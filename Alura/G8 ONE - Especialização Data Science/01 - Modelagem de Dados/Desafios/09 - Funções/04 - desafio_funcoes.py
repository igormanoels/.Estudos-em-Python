'''
4. Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.

'''
from math import pow

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_quad = list(map(lambda x: pow(x,2), lista))
print(lista_quad)





