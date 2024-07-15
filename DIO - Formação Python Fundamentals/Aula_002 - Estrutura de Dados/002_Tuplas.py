# Aula 01 - Conhecendo a Linguagem de Programação Python

import os
os.system('cls')


# As tuplas são compostas por valores imutáveis, até o final da execução do programa

FRUTAS = ("laranja", "Maça", "BANANA", "UVA",) # Como boa prática, manter sempre uma virgula no final

ESTADO = tuple("São Paulo") # Faz uso do construtor para criar uma tupla, cadas letra é uma posição

ESTADOS = tuple(["São Paulo", "Rio de Janeiro", "Bahia"]) # Faz uso do construtor para criar uma tupla apartir de uma lista

# Os métodos de acesso são iguaias as listas
print(ESTADO[0])
print(ESTADOS[1])

print("\n")
# A principal diferença na tupla é
print(ESTADOS.count("São Paulo"))       # Conta quantos elementos
print(ESTADOS.index("São Paulo"))       # Mostra o indice
print(len(ESTADOS))                      # Mostra o comprimento 

carros = ("gol")
print(isinstance(carros, tuple))