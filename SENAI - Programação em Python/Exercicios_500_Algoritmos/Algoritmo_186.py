import os 
import math

os.system('cls')
'''
    Entrar com quatro números e imprimir o cubo e a raiz cúbica de cada número. 
'''

for i in range(4):
    num = int(input("Informe o número desejado: "))
    aoCubo = math.pow(num, 3)
    raizCubica = math.pow(num, 1/3)
    print(f"{num} ao cubo ---> {aoCubo} \n{num} raiz cúbica ---> {raizCubica}\n")
    
input("\n\nPressione o \"enter\" para encerrar...")
