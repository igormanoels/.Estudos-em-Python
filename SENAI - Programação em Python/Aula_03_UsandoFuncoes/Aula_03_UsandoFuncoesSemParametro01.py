import os
os.system('cls')

def verificarPar():
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        print(f"\n{num} é par.")
    else:
        print(f"\n{num} é impar")

verificarPar()
