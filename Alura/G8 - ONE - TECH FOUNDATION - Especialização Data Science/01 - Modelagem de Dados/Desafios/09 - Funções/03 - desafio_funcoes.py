'''
3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

Utilize o return na função e salve a nova lista na variável mult_3.

'''
from math import pow

lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]


def aoCubo (lt):
    return list(map(lambda x: pow(x,3), lt))


mult_3 = aoCubo(lista)
print(mult_3)



