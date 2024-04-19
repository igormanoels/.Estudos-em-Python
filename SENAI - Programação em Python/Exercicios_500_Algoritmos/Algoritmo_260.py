import os

os.system('cls')
'''
        ex. Enquanto 03
'''

c = int(input("Digite o número de vezes para repetir: "))

while (c > 0):
    num = int(input("\nInforme o número para descobrir seu dobro: "))
    print(f"O dobro de {num} é {num*2}")
    c -= 1

input("\n\nPressione o \"enter\" para encerrar...")
