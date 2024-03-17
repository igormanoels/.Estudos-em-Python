import os

os.system('cls')
'''
    Construir um algoritmo que leia dois números e efetue a adição. Caso o valor somado 
    seja maior que 20, este deverá ser apresentado somando-se a ele mais 8; caso o valor 
    somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.
'''

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

res = (num1 + num2)

if (res > 20):
    res +=8
    print(f"\nResultado: {res}")
else:
    res -=5
    print(f"\nResultado: {res}")
    
input("\n\nPressione o \"enter\" para encerrar...")
