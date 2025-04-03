import os
import math
os.system('cls')

'''
Receba 3 coeficientes A, B, e C de uma equação do 2º grau da fórmula AX²+BX+C=0. 
Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
'''

valorA = float(input("Informe o valor de A: "))
valorB = float(input("Informe o valor de B: "))
valorC = float(input("Informe o valor de C: "))

delta = (math.pow(valorB, 2)) - (4 * valorA * valorC)

if delta > 0:
    res1 = (-valorB) + (math.sqrt(delta)) / (2 * valorA)
    res2 = (-valorB) - (math.sqrt(delta)) / (2 * valorA)
    print("x1= ", res1, "  e  x2= ", res2)
elif delta == 0:
    res = (-valorB) / 2 * valorA
    print("x1 e x2 = ", res)
else:
    print("Não existem raízes reais")
