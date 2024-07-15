# Aula 02 - Estrutura de Dados com Python

import os
os.system('cls')


# O vetor é chamado de lista
frutas = ["Laranja", "Pera", "Uva", "Maça"]
print(frutas[0])    
print(frutas[-2])
print("\n")


# A matriz é conhecidaa por lista encadeada
estoque_frutas = [
    ["Banana", 1.5, 150],
    ["Maça", 2.49, 34],
    ["Abacaxi", 7.48, 18]
]
print(estoque_frutas[1])
print(estoque_frutas[-1])
print("Preço:",estoque_frutas[1][1]) # pegando apenas um elemento


# As listas podem ser acessadas segundo o fatiamento do mesma forma que as strings
print("\n")
for fruta in frutas:
    print(fruta, end=" ") # Imprime a lista


print("\n")
for indice, fruta in enumerate(frutas):
    print(f"{indice+1}º - {fruta}")


print("\n")
numeros = [0,1,85,9,45,69,40,8,6,235,4]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) # Append adiciona um valor a última posição na lista
        print(numero, end=" ")


print("\n")
# Outra forma 
pares2 = [numero for numero in numeros if numero % 2 == 0]
print(pares2)


print("\n")
quadrados = [numero ** 2 for numero in numeros]
print(quadrados)


print("\n")
pares.clear()     # Limpa todos os valores da lista
print(pares)


print("\n")
lista2 = numeros.copy() # Copia todos os vamos da lista de números
print(lista2)


print("\n")
cores = ["vermelho", "azul", "verde", "azul"]
quant_azul = cores.count("azul") # Conta quantas vezes um valor está presente
print("Quantidade da cor azul",quant_azul)


print("\n")
nova_lista = []
nova_lista.extend(numeros)  # Junta as listas, e não elimita valores duplicados
nova_lista.extend(cores)
print(nova_lista) 


print("\n")
print(nova_lista.index("vermelho"))    # Retorna o indice dessa ocorrencia, sempre a primeira ocorrencia q ele encontrar


print("\n")
print("Mostrando lista: ", nova_lista)
print("Remove o último lista: ",nova_lista.pop())    # remove a última ocorrência da lista
print("Mostrando a lista sem o valor removido: ",nova_lista)

nova_lista.remove(45)   # Remove um item especifico, sempre a primeira ocorrencia q ele encontrar
print("Mostrando a lista sem o valor removido: ",nova_lista)


print("\n")
print(frutas)

frutas.reverse()    # inverte a lista
print(frutas) 

frutas.sort()       # Ordena
print(frutas)

frutas.sort(reverse=True)       # Ordena# Ordena invertido
print(frutas)

#outra forma
print(sorted(frutas, reverse=True))

print("\n")
print("Comprimento: ",len(frutas)) # retorna o tamanho da lista




