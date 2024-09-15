# 5. Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0).
# Calcule e mostre as raízes reais (considerar que a equação possue2 raízes).
import math

valorA = int(input("Favor informar o valor de A: "))
valorB = int(input("Favor informar o valor de B: "))
valorC = int(input("Favor informar o valor de C: "))

delta = (math.pow(valorB,2)) - (4 * valorA * valorC)

res1 = (-valorB) + (math.sqrt(delta)) / (2 * valorA)
res2 = (-valorB) - (math.sqrt(delta)) / (2 * valorA)


print("x1= ", res1, "  e  x2= ",res2)
