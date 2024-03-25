import os
os.system('cls')

def entrada1 ():
    num = int(input("Digite um número: "))
    return num

def entrada2 ():
    num = int(input("Digite um número: "))
    return num

def calcular(a, b):
    res = a + b
    return res

resposta = calcular(entrada1(), entrada2())
print(f"\nResposta: {resposta}\n")
