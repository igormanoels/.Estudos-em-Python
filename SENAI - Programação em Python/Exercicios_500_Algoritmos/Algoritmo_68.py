import os

os.system('cls')
'''
    Ler dois valores para as variáveis A e B, efetuar a troca dos valores de forma que a 
    variávelA passe a ter o valor da variável B e que a variável B passe a ter o valor da variável A. 
    Apresentar os valores trocados. 
'''

valorA = input("Informe o valor de A: ")
valorB = input("Informe o valor de B: ")

aux = valorA
valorA = valorB
valorB = aux

print("\nO \"valor de A\" agora é ", valorA, " e o \"valor de B\" é ", valorB, ".")
input("\n\nPressione o \"enter\" para encerrar...")
