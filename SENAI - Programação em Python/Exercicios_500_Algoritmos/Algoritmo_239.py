import os
import math

os.system('cls')
'''
    Implementar um algoritmo para calcular o valor de e^x O valor de x devera 
    ser digitado. O valor de eX será calculado pela soma dos 10 primeiros 
    termos da serie a seguir 
'''

def calcFat(fat):
    if fat == 0 or fat == 1:
        return 1
    else:
        return fat * calcFat(fat-1)

res = 1
x = int(input("Informe o valor de x: "))

for i in range(10):
    res += (math.pow(x, (i+1)) / calcFat(i+1))
    
print("Resultado da Série: ", res)

input("\n\nPressione o \"enter\" para encerrar...")
