import os
os.system('cls')

'''
    Entrar com numeros e imprimir o triplo de cada numero, o algoritmo acaba quando entrar o numero -999
'''

print("Algoritmo que cálcula o triplo de um número.")

while True:
    num = int(input("Informe um número, ou -999 para encerrar: "))
    if num == -999:
        print("Programa encerrado!")
        break
    else:
        num = num * 3
        print(f"O triplo é {num}")

input("\n\nPressione o \"enter\" para encerrar...")
