import os 

os.system('cls')
'''
    Criar um algoritmo que leia um número (num) da entrada. Em seguida, 
    ler n números da entrada e imprimir o triplo de cada um. Exemplo: 
'''

n = int(input("Informe o número de entrada que deseja fazer: "))

for i in range(n):
    num = int(input("\nInforme o número desejado: "))
    res = num * 3
    print(f"O triplo de {num} é ---> {res}.")

input("\n\nPressione o \"enter\" para encerrar...")
