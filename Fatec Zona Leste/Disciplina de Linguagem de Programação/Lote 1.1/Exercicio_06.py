import os
os.system('cls')

# Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.

valorA = input("Informe o primeiro valor: ")
valorB = input("Informe o segundo valor: ")

alter = valorA
valorA = valorB
valorB = alter

print("Novo valor de A = ", valorA, ", e novo valor de B = ", valorB)
