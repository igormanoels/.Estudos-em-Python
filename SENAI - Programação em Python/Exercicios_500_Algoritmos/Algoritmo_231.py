import os

os.system('cls')
'''
    colete quantas palavras, depois as palavras e depois exiba o vetor
'''

palavras = []
quant = int(input("Informe a quantidade de palavras que deseja inserir: "))

for i in range(quant):
    palavra = input(f"Informe a {i+1}º palavra: ")
    palavras.append(palavra)
    print("\n")
    
print(palavras)

input("\n\nPressione o \"enter\" para encerrar...")
    