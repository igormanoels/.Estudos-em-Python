import os

os.system('cls')
'''
    ex. Enquanto 02
'''

num = int(input("Informe o número desejado: "))
c = num

while c > 0:
    print(f"O dobro de {num} é {num*2}")
    c -= 1

input("\n\nPressione o \"enter\" para encerrar...")
