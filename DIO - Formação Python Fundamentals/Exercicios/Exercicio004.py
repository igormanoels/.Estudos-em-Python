# Descrição
# Desenvolva uma função em Python que recebe uma tupla de números inteiros e retorna a soma de todos os elementos dessa tupla. 
# A função deve ser capaz de lidar com tuplas de qualquer tamanho, contanto que todos os elementos sejam números inteiros. O objetivo é praticar a manipulação de tuplas e a utilização de funções em Python.
# 
# Explicação de Resolução:
# 1. Converta cada string na "lista_strings" em um número inteiro utilizando a função "int()".
# 2. Use a função "map()" para aplicar a função "int()" a cada elemento da "lista_strings".
# 3. Armazene o resultado em uma variável chamada "elementos".

# No "TODO", abaixo: Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:
import os
os.system('cls')

def somar(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = input()
    elementos = tuple(map(int, entrada.split()))
    
resultado = somar(elementos)
print(f"A soma dos elementos da tupla é: {resultado}")