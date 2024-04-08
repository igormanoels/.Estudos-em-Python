import os
import random

os.system('cls')
'''
    Criar um algoritmo para imprimir uma tabela para DEZ times num torneio de rodada dupla.
'''

times = ["Brasil", "Estados", "Unidos", "Rússia", "Itália", 
         "Argentina", "França", "Polônia", "Sérvia", "Irã", "Canadá"]

sorteados = []

for i in range(5):
    while True:
        num = random.randint(0,9)
# verifica se o valor sorteado não está dentro do vetor         
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
    print(f"Jogo de Ida: {sorteados[c]} x {sorteados[i]}")
    print(f"Jogo de Volta: {sorteados[i]} x {sorteados[c]}")
    c += 2
    i += 2
    print("\n")

input("\n\nPressione o \"enter\" para encerrar...")
    