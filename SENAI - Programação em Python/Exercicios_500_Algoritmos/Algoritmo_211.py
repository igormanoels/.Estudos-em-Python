import os

os.system('cls')
'''
    Criar um algoritmo que imprima todos os números inteiros e positivos no 
    intervalo aberto entre 10 e 100 de modo que: 
        - não terminem em zero;
        - se o dígito da direita for removido, o número restante é divisor 
        do número original
        Exemplos:
            26: 2é divisor de 26
            80: 8 é divisor de 80
'''

print("Sequência: ", end="")
for i in range(10, 101):
    if i % 10 != 0:
        div = i // 10
        if i % div != 0:
            print(f"{i}", end=" ")
            
input("\n\nPressione o \"enter\" para encerrar...")
