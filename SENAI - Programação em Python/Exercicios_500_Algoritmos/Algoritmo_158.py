import os

os.system('cls')
'''
    Criar um algoritmo que entre com o valor de x, 
    calcule e imprima o valor de f(x). 
'''

x = int(input("Informe o valor de 'x': "))

if x != 2:
    fx = (8 / (2 - x))
    print(f"F(x)= {fx}")
else: 
    print("O cálculo não pode ser feito.")
    
input("\n\nPressione o \"enter\" para encerrar...")
 