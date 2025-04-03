import os
os.system('cls')

# 19. Receba 2 valores reais. Calcule e mostre o maior deles.

valorA = float(input("Informe o primeiro valor: "))
valorB = float(input("Informe o segundo valor: "))

if valorA > valorB:
    print(f"O maior valor é {valorA}")
else:
    print(f"O maior valor é {valorB}")
