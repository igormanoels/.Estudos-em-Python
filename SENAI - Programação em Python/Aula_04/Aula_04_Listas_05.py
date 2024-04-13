import os
os.system('cls')

def combinarListas (lista1, lista2, condicao): 
    listaCombinada = []
    for elemento1, elemento2 in zip(lista1, lista2):
        if condicao(elemento1, elemento2):
            listaCombinada.append(elemento1)
        else: 
            listaCombinada.append(elemento2)
    return listaCombinada

lista1 = [1,2,3,4,5,6]
lista2 = ["A", "B", "C", "D", "E", "F"]
condicao = lambda num, string: num % 2 == 0 and len(string) % 2 == 1
'''
    lambda é uma função anonima, para condicionar a ação que será executada
    pelo módulo
    A condição separa o vetor segundo, num para imprimir apenas o valores que são pares
    e das letras ele busca os dados pelas posições impares
'''

lista = combinarListas(lista1, lista2, condicao)

for i in lista:
    print(i, end=" ")

print("\n")
