import os
import math

os.system('cls')
'''
    Entrar com o valor de x e imprimir y:
        1, se x <=1 
        2; 5e 1 <x<_ 2 
        x ,se2<x<=3 
        x 3 , sex >3
'''

x = int(input("Informe o valor de 'x': "))

if x <= 1:
    y = 1
elif x <= 2:
    y = 2
elif x <=3:
    y = math.pow(x, 2)
else: 
    y = math.pow(x, 3)
    
print(f"Valor de x ---> {x}, valor de y ---> {y}")

input("\n\nPressione o \"enter\" para encerrar...")
