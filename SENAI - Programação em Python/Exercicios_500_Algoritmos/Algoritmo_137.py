import os
import math

os.system('cls')
'''
    Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de segundo grau, 
    apresentando: as duas raízes, separa os valores informados for possível fazer o cálculo 
    (deita positivo ou zero); a mensagem "Não há raízes reais", se não for possível fazer o cálculo 
    (deita negativo); e a mensagem "Não é equação do segundo grau", se o valor de a for iguala zero. 
'''

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

if a == 0:
    print("Não é uma equação de segundo grau!")
else:
    delta = math.pow(b, 2) - 4 * a * c
    if delta > 0:
        x1 = (-b + (math.sqrt(delta))) / (2 * a)
        x2 = (-b - (math.sqrt(delta))) / (2 * a)
        print(f"x1 = {x1} e x2 = {x2}")
    else:
        print("Não há raizes!")

input("\n\nPressione o \"enter\" para encerrar...")
