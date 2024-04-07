import os

os.system('cls')
'''
    Entrar com o número de vezes que se deseja imprimira palavra SOL e imprimir.
'''

nome = input("Informe a palavra desejada: ")
quant = int(input("Informe a quantidade de vezes que você quer ver essa palavra: "))

for i in range(quant):
    print(f"{i+1}º <--- {nome}.")
    
input("\n\nPressione o \"enter\" para encerrar...")
