import os

os.system('cls')
# Criar um algoritmo que leia um número entre O e 60 e imprimir o seu sucessor, sabendo que o sucessor de 60 é 0.
# Não pode ser utilizado nenhum comando de seleção e nem de repetição.

num = int(input("Informe um número de 0 a 60: "))
sucessor = (num+1) % 61

print("\nSucessor: ", sucessor)
input("\n\nPressione o \"enter\" para encerrar...")
