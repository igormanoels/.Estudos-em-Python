import math
import os

os.system('cls')

# Entrar com um número e imprimir o logaritmo desse número na base 10.
num = int(input("Informe o número desejado para saber seu log10: "))
log = math.log10(num)

print("Resultado: ", log)
