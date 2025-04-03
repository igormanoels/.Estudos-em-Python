import os
os.system('cls')

# Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.

anguloA = float(input("Informe o valor do angulo A: "))
anguloB = float(input("Informe o valor do angulo B: "))

anguloC = (180 - (anguloA + anguloB))
print(f"O valor do terceiro angulo é de {anguloC:.2f}º")
