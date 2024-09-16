import os
os.system('cls')

# Receba um número inteiro. Calcule e mostre o seu fatorial.

fatorial = int(input("Informe um número para saber seu fatorial: "))

if fatorial == 1 or fatorial == 0:
    print("O fatorial é 1")
elif fatorial > 1:
    res = 1
    while fatorial > 1:
        res += (res * (fatorial - 1))
        fatorial-=1
    print(f"O fatorial é {res}")