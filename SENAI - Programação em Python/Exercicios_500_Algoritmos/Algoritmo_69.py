import os

os.system('cls')
# Criar um algoritmo que leia o numerador e o denominador de uma fração e trans formá-lo em um número decimal.

nume = input("Informe o valor do numerador: ")
denomi = input("Informe o valor do denominador: ")

div = int(nume) / int(denomi)

print("\nResultado: ", div)
input("\n\nPressione o \"enter\" para encerrar...")
