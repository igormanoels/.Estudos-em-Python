import os

os.system('cls')
# O maior número entre dos 3

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

if n1 > n2:
    if n1 > n3:
        max = n1
    else:
        max = n3
else:
    if n2 > n3:
        max = n2
    else:
        max = n3

print(f"\nO maior dos três números é {max}")
input("\n\nPressione o \"enter\" para encerrar...")
