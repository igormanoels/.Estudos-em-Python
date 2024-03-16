import os

os.system('cls')

'''
    Refazer esta lista colocando todos os testes, usando o comando se, quando você aprender, nos exercícios necessários: 
        - testar se o divisor é diferente de O. 
'''

dividendo = int(input("Informe o dividendo: "))
divisor = int(input("Informe o divisor: "))

if divisor != 0:
    res = dividendo / divisor
else:
    divisor = int(input("O divisor precisa ser diferente de zero: "))
    res = dividendo / divisor

input("\n\nPressione o \"enter\" para encerrar...")
