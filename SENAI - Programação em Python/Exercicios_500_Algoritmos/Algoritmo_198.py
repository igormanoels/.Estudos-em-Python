import os

os.system('cls')
'''
    Criar um algoritmo que leia os limites inferior e superior de um intervalo e imprima 
    todos os números naturais no intervalo fechado. Suponha que os dados digitados são 
    para um intervalo crescente. Exemplo: 
        Limite inferior: 5          Saída: 5 6 7 8 9 10 11 12 
        Limite superior: 12 
'''

limInf = int(input("Informe o limite inferior: "))
limSup = int(input("Informe o limite superior: "))

print("\nSequência: ", end="")
while limInf <= limSup:
    print(f"{limInf}", end=" ")
    limInf += 1

input("\n\nPressione o \"enter\" para encerrar...")