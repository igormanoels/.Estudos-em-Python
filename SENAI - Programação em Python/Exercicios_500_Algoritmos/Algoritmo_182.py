import os

os.system('cls')
'''
    Entrar com 10 números e imprimir a metade de cada número. 
'''

for i in range(10):
    num = int(input("Informe o número desejado: "))
    metade = num / 2
    print(f"A metade de {num} é {metade}\n")

input("\n\nPressione o \"enter\" para encerrar...")
