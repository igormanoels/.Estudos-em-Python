import os 

os.system('cls')
'''
    Criar um algoritmo que imprima os numeros pares no intervalo de 1 a 600.
'''

c = 1

while c <= 600:
    if c % 2 == 0:
        print(f"{c} é par.")
    c += 1

input("\n\nPressione o \"enter\" para encerrar...")
