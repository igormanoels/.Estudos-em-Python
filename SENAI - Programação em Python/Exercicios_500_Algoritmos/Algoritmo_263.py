import os
os.system('cls')
'''
    Entrar com números enquanto forem positivos e imprimir quantos números foram digitados. 
'''

quant = 0
print("Algoritmo que conta quantos números posivos foram inseridos")

while True:
    n = int(input("Digite um número: "))
    if n > 0:
        quant += 1
    else:
        print(f"Quantidade de números pares inseridos {quant}")
        print("Programa encerrado!")
        break

input("\n\nPressione o \"enter\" para encerrar...")
