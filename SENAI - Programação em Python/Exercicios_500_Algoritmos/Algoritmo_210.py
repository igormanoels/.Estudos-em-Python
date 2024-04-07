import os

os.system('cls')
'''
    A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos
    são fornecidos pelo usuário; a partir dai., os termos são gerados com a 
    soma ou subtração dos dois termos anteriores, ou seja:
        A1 = A i-1 + i-2 para / ímpar
        A1 = A i-1 - i..2 para /par
    Criar um algoritmo que imprima os 10 primeiros termos da série de FETUCCINE.
'''

termo1 = int(input("Informe o primeiro termo: "))
termo2 = int(input("Informe o segundo termo: "))

fetu = []

fetu.append(termo1)
fetu.append(termo2)

for i in range(2, 10):
    if i % 2 == 0:
        fetu.append((fetu[i-1])-(fetu[i-2]))
    else:
        fetu.append((fetu[i-1])+(fetu[i-2]))
        
print("\nSequência de Fetuccini: ", end="")
for i in fetu:
    print(f"{i}", end=" ")
        
input("\n\nPressione o \"enter\" para encerrar...")
