import os
import random

os.system('cls')
'''
    ar um algoritmo para imprimir uma tabela para DEZ times num torneio de rodada simples. 
'''

times = ["Brasil", "Estados", "Unidos", "Rússia", "Itália", 
         "Argentina", "França", "Polônia", "Sérvia", "Irã", "Canadá"]

sorteados = []

for i in range(5):
    while True:
        num = random.randint(0,9)
        if num not in sorteados:
            sorteados.append(num)
            break
    while True:
        num = random.randint(0,9)
        if num not in sorteados:
            sorteados.append(num)
            break    

c = 0
i = 1
while c <= 8:
    print(f"Partida: {sorteados[c]} x {sorteados[i]}")
    c += 2
    i += 2
    print("\n")

input("\n\nPressione o \"enter\" para encerrar...")
    