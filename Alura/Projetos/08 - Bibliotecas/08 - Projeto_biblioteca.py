'''
8. Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio 
chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 
para compor a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo 
com a lista abaixo:
'''

from random import choice


frutas = ["maçã", "banana", "uva", "pêra", "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

salada = []

for i in range(0,3):
    salada.append(choice(frutas))


print(f'Sua salada de frutas surpresa conterá: {salada[0]}, {salada[1]} e {salada[2]}')


