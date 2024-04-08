import os

os.system('cls')
'''
    Criar um algoritmo que deixe escolher qual a tabuada de multiplicar que se deseja imprimir. 
'''

tab = int(input("Informe qual tabuada você deseja saber: "))

print(f"\nTabuada do {tab}")
for i in range(11):
    res = tab * i
    print(f"{tab} x {i} = {res}")
    
input("\n\nPressione o \"enter\" para encerrar...")
