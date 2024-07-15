# Aula 01 - Conhecendo a Linguagem de Programação Python

import os
os.system('cls')

# Estrutura de dados SET, o conjunto é uma coleção de dados únicos
# Um ponto é que o SET não garante a ordem dos dados, portando eles não suportam indices

print(set([1,2,3,4,5,6,8,9,1,2])) # basta passar uma lista pelo contrutor SET que os dados duplicados serão removidos

print(set("ABACAXI"))

cores = ["vermelho", "azul", "verde", "azul"]
print(set(cores))

print("\n")
# Também é possivel declarar conjuntos a partir de chaves
conjunto = {1,2,2,3,5,1,5,5,6,8}
print(conjunto)     # Apenas os valores únicos serão exibitos

# MÉTODOS
print("\n")
conjunto_a = {1,2,3}
conjunto_b = {1,2,8,9,4,5}

print(conjunto_a.union(conjunto_b))                     # Mostra a união dos conjuntos
print(conjunto_a.intersection(conjunto_b))              # Mostra a interseção, valores que são similares em ambos
print(conjunto_b.difference(conjunto_a))                # Mostra o que o conjunto x, tem de diferente do conjunto y
print(conjunto_a.symmetric_difference(conjunto_b))      # Mostra o que há de diferente nos dois conjuntos

# Retorna um booleano, verificando se todos os elementos do conjunto A pertencem ao conjunto b
print(conjunto_a.issubset(conjunto_b), "Retorna false, pq 3 não é um elemento em comum")                  

# Retorna um booleano, verificando se todos os elementos do conjunto B pertencem ao conjunto A
print(conjunto_a.issuperset(conjunto_b), "Retorna false, pq 8,9,4,5 não é um elemento em comum")

# Retorna um boolean, verificando se todos os elementos são distintos
print(conjunto_a.isdisjoint(conjunto_b))


print("\n")
numeros = {15, 42}

numeros.add(5)      # Adiciona o valor
numeros.add(15)     # Mas se for repetido ele não é adcionado    
print(numeros)

# também é possivel usar 
novos_numeros = numeros.copy()           # Copia o conjunto
numeros.discard(15)                      # Apaga um elemento
numeros.clear()                          # Apaga o conjunto inteiro
novos_numeros.pop()                      # Remove o último elemento
tamanho = len(novos_numeros)             # Pega o tamanho
novos_numeros.remove(7)                  # Também consegue remover um item, porém caso ele não existe um erro é apresentado
verifica = 1 in numeros                  # Retorna um boleano se um valor está presente em um conjunto
