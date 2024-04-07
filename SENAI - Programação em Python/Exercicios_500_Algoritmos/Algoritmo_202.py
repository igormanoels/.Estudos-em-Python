import os 

os.system('cls')
'''
    Criar um algoritmo que leia um número (num) da entrada e imprima os múltiplos 
    de 3 e 5 ao mesmo tempo no intervalo de 1 a num. Exemplo: 
        Numero lido: 50         Saída: 15 30 45 
'''

num = int(input("Informe o número limite: "))

print("Múltiplos de 3 e 5: ", end="")
for i in range(num+1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}", end=" ")

input("\n\nPressione o \"enter\" para encerrar...")
