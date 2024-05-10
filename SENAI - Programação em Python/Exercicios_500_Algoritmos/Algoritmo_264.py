import os
os.system('cls')
'''
    Entrar com vários números positivos e imprimira média dos números digitados.
'''
quant = 0
soma = 0
print("Algoritmo que cálcula a média dos números positivos")

while True:
    n = int(input("Informe um número, ou digite 0 para encerrar: "))
    if n != 0:
        if n > 0:
            quant += 1
            soma += n
    else:
        media = soma / quant
        print(f"A média dos números pares informados é de {media}")
        print("Programa encerrado!")
        break

input("\n\nPressione o \"enter\" para encerrar...")
