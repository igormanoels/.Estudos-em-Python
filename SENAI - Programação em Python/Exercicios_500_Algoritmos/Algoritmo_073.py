import os

os.system('cls')
'''
    Criar um algoritmo que receba um número real, calcular e imprimir: 
    - A parte inteira do número 
    - A parte fracionária do número 
    - O número arredondado
'''

num = input("Favor informar um número fracionado: ")

pInteira, pFracionada = num.split('.')
pRedondo = round(float(num))

print("\nParte Inteira: ", pInteira,
      "\nParte Fracionária: ", pFracionada,
      "\nNúmero Arredondado: ", pRedondo)

input("\n\nPressione o \"enter\" para encerrar...")
