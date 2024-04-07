import os

os.system('cls')
'''
    Criar um algoritmo que imprima os 10 primeiros termos da série 
    de Fibonacci. Observação: os dois primeiros termos desta série 
    são 1 e 1 e os demais são gerados a partir da soma dos anteriores. 
        Exemplos: 1 + 1 -> 2    
        terceiro termo; 1 + 2-> 3 quarto termo etc.
'''

quant = int(input("Informe a quantidade de termos desejada: "))
fibo = [1, 1]

for i in range(2, quant):
    fibo.append(fibo[i-2] + fibo[i-1])
        
print("Sequência: ", end="")
for i in fibo:
    print(f"{i}", end=" ")

input("\n\nPressione o \"enter\" para encerrar...")
