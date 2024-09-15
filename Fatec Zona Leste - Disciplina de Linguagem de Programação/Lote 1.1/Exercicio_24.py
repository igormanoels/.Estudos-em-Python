import os
os.system('cls')

# Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

num = float(input("Informe o número desejado: "))

if num % 2 == 0 and num % 3 == 0:
    print("O número é divisivel por 2 e 3.")
else:
    print("O número não é divisivel por 2 e 3.")
