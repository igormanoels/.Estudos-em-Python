import os
import math

os.system('cls')
'''
    Criar um algoritmo que entre com o valor dex calcule e imprima o valor de f(x) 
'''

x = int(input("Informe o valor de 'x': "))

if x < -4 or x > 4:
    fx = ((5 * x) + 3) / (math.sqrt(math.pow(x, 2) - 16))
    print(f"Resultado F(x) = {fx}")
else: 
    print("Esse cálculo para F(x) não pode ser feito.")

input("\n\nPressione o \"enter\" para encerrar...")
