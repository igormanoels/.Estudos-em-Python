import os

os.system('cls')
'''
    Ler 200 números inteiros e imprimir quantos são pares e quantos são ímpares.
'''

c = 1

while c <= 200:
    num = int(input(f"Informe o {c}º número: "))
    if num % 2 == 0:
        print(f"{num} é par.")
    else: 
        print(f"{num} é impar.")
    c += 1
        
input("\n\nPressione o \"enter\" para encerrar...")
