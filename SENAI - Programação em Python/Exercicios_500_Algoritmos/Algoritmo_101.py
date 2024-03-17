import os

os.system('cls')
# Construir um algoritmo que indique se o número digitado está compreendido entre 20 e 90 ou não.

num = int(input("Digite um número: "))

if num >= 20 and num <= 90:
    print(f"\n{num} está dentro do intevalo de 20 a 90.")
else:
    print(f"\n{num} não está dentro do intervalo de 20 a 90.")

input("\n\nPressione o \"enter\" para encerrar...")
