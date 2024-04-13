import os

os.system('cls')
'''
    Palíndromos são palavras (frases também) que são iguais quando lidas de frente 
    para trás e de trás para frente, ignorando os espaços. 
    AME O POEMA AMORA ROMA ATEOPOETA LUZAZUL
'''

frase = input("Informe a frase desejada: ")
quant = len(frase)

if quant % 2 != 0:
    print("Essa frase é um palindromo. Ao contrário fica:")
    i = quant-1
    while i >= 0:
        print(f"{frase[i]}", end="")
        i -= 1
else:
    print("Essa frase não é um palindromo.")

input("\n\nPressione o \"enter\" para encerrar...")
