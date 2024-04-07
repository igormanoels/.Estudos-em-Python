import os

os.system('cls')
'''
    Entrar com um numero e imprimir todos os seus divisores
'''

num = int(input("Informe o número desejado: "))

for i in range(1, 10):
    if num % i == 0:
        print(f"{num} pode ser dividido por {i}")
    
input("\n\nPressione o \"enter\" para encerrar...")
