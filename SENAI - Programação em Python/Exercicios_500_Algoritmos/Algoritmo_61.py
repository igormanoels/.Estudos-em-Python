import math
import os

os.system('cls')
# razão de uma PG e o valor do 1 2termo. Calcular e imprimir o 5 termo da série

termo = int(input("Informe qual o termo: "))
razao = int(input("Informe qual a razão: "))

quintoTermo = termo * math.pow(razao, 4)
print("\nO quinto termo é ", quintoTermo)

input("\n\nPressione o \"enter\" para encerrar...")
