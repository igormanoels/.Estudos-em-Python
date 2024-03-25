import os
import math

os.system('cls')
'''
Criar um algoritmo que leia um ângulo em graus e apresente: 
    - o seno do ângulo, se o ângulo pertencer a um quadrante par; 
    - o co-seno do ângulo, se o ângulo pertencer a um quadrante ímpar. 
'''

angulo = float(input("Informe o valor do angulo: "))
rang = angulo * math.pi / 180
pi = math.pi

if (rang > pi / 2 and rang <= pi) or (rang < 3 * pi / 2 and rang <= 2*pi):
    print(f"\nSeno: {math.sin(rang)}")
else:
    print(f"\nCo-Seno: {math.cos(rang)}")

input("\n\nPressione o \"enter\" para encerrar...")
