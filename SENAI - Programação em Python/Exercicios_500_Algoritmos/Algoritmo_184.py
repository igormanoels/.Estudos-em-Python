import os
import math

os.system('cls')
'''
    Entrar com 8 números e, para cada número, imprimir o logaritmo desse número na base 10. 
'''

for i in range(8):
    num = int(input("Informe o número desejado: "))
    log = math.log10(num)
    print(f"log de {num} na base 10 é ---> {log}\n")

input("\n\nPressione o \"enter\" para encerrar...")
