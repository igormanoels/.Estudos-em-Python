import os

os.system('cls')
'''
    ex. Enquanto 01
'''

num = int(input("Informe o número desejado: "))

while (num > 0):
    print(f"Dobro = {num*2}")
    num -= 1

input("\n\nPressione o \"enter\" para encerrar...")
