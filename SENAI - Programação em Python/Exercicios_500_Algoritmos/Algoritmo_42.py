import os
import math

os.system('cls')
# Entrar com um ângulo em graus e imprimir: seno, co-seno, tangente, secante, co-secante e co-tangente deste ângulo.
angulo = float(input("Informe o ângulo para o cálculo: "))

angulo = ((math.pi * angulo) / 180)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tang = math.tan(angulo)
secante = 1 / cosseno
coSecante = 1 / seno
cotangente = 1 / tang

print("ângulo: ",angulo,"\nSeno: ", seno,"\nCo-seno:", cosseno,"\nTangente: ", tang,"\nSecante: ", secante,"\nCo-Secante: ", coSecante,"\nCo-Tangente: ", cotangente)
