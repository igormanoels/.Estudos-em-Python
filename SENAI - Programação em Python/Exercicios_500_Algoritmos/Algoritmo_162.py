import os

os.system('cls')
'''
    Criar um algoritmo que imprima todos os números pares no intervalo 1-10. 
'''

for i in range(11):
    if i % 2 == 0:
        print(f"O número {i} é par.")
    else:
        print(f"O número {i} é impar.")

input("\n\nPressione o \"enter\" para encerrar...")
