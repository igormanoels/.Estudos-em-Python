import os

os.system('cls')
'''
    Entrar com dois números e imprimir todos os números no intervalo 
    fechado, do menor para o maior.
'''

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if num1 > num2:
    aux = num1
    num1 = num2
    num2 = aux

while num1 < num2-1:
    num1 += 1
    print(num1, end=" ")
    
input("\n\nPressione o \"enter\" para encerrar...")
