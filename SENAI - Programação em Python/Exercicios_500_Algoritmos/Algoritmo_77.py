import math
import os

os.system('cls')
# Ler dois números reais e imprimir o quadrado da diferença do primeiro valor pelo segundo e a diferença dos quadrados.

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

qDif = math.pow((num1 - num2), 2)
difQuad = math.pow(num1, 2 ) - math.pow(num2, 2)

print("\nQuadrado da Diferença: ", qDif,
      "\nDirença dos Quadrados: ", difQuad)
input("\n\nPressione o \"enter\" para encerrar...")
