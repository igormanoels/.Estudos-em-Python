import os

os.system('cls')
'''
    A série de RICCI difere da série de FIBONACCI porque os dois primeiros 
    termos são fornecidos pelo usuário. Os demais termos são gerados da mesma 
    forma que a série de FIBONACCI. Criar um algoritmo que imprima os n 
    primeiros termos da série de RICCI e a soma dos termos impressos, sabendo-se
    que para existir esta série serão necessários pelo menos três termos. 
'''

ricci = []

termo1 = int(input("Informe o primeiro termo: "))
termo2 = int(input("Informe o segundo termo: "))
quant = int(input("Informe quantos termos gostaria de ver: "))

ricci.append(termo1)
ricci.append(termo2)

for i in range(2, quant):
    ricci.append((ricci[i-2])+(ricci[i-1]))

print(f"Sequência de Ricci: ", end="")
for i in ricci:
    print(f"{i}", end=" ")
    
input("\n\nPressione o \"enter\" para encerrar...")
