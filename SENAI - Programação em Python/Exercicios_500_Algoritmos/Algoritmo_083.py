import os

os.system('cls')
# Ler um número e, se ele for positivo, imprimir seu inverso; caso contrário, imprimir o valor absoluto do número.

num = int(input("Favor informar um número desejado: "))

if num == 0:
    num = int(input("O número informado não pode ser zero, insira um número novamente: "))

if num > 0:
    res = 1 / num
    print(f"O inverso de {num} é {res}")
else:
    res = num * -1
    print(f"O absoluto de {num} é {res}")

input("\n\nPressione o \"enter\" para encerrar...")
