import os
os.system('cls')

# Receba um número inteiro. Calcule e mostre o seu fatorial.

fatorial = int(input("Informe um número para saber seu fatorial: "))

if fatorial == 1 or fatorial == 0:
    print(f"O fatorial é {fatorial}")
elif fatorial > 1:
    while fatorial > 1:
        res =+ (fatorial * (fatorial - 1))
        fatorial-=1
    print(f"O fatorial é {res}")