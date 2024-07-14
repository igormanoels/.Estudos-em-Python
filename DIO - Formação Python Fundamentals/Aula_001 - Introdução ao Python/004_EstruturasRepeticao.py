# Aula 01 - Conhecendo a Linguagem de Programação Python

import os
os.system('cls')

print("\n\nESTRUTURA DE REPETIÇÃO\nUSANDO WHILE")
contador = 0

while contador < 10:
    contador += 1
    print(contador, end=" ")


print("\n\nUSANDO FOR")
texto = input("Digite uma palavra para descobir quais as vogais: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

print("\n\nUSANDO FOR USANDO RANGE, conta somando 1")
for numero in range(0, 11):
    print(numero, end=" ")

    
print("\n\nUSANDO FOR USANDO RANGE, conta de 5 em 5")
for numero in range(0, 51, 5):
    print(numero, end=" ")