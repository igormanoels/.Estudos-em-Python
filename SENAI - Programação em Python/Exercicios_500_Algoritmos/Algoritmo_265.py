import os
os.system('cls')
'''
    Ler vários números e informar quantos números entre 100 e 200 foram digitados.
    Quando o valor O (zero) for lido, o algoritmo deverá cessar sua execução.     
'''
quant = 0
print("Algoritmo que conta quantos números entre 100 e 200 foram inseridos")

while True:
    n = int(input("Informe um número, ou digite 0 para encerrar: "))
    if n != 0:
        if 100 <= n <= 200:
            quant += 1
    else:
        print(f"A quantidade de número para o intervalo é de {quant}")
        print("Programa Encerrado!")
        break

input("\n\nPressione o \"enter\" para encerrar...")
