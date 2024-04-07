import os
import math

os.system('cls')
'''
    Implementar um algoritmo para calcular o sen(X). O valor de X deverá ser 
    digitado em graus. O valor do seno de Xserá calculado pela soma dos 10 
    primeiros termos da série a seguir: 
'''
def calcFat(fat):
    if fat == 0 or fat == 1:
        return 1
    else:
        return fat * calcFat(fat-1)

x = int(input("Informe o valor de x: "))
n = 1
sen = 0

for i in range(10):
    sen += math.pow(x, n) / calcFat(n)
    n += 2

sen = math.sin(sen - x)

print(f"Seno da série é {sen}")

input("\n\nPressione o \"enter\" para encerrar...")
