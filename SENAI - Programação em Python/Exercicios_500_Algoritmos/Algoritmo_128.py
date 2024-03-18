import os

os.system('cls')
'''
    Entrar com um verbo no infinitivo e imprimir uma das mensagens: 
        - verbo não está no infinitivo 
        - verbo da 1 conjugação
        - verbo da 2 conjugação 
        - verbo da 3 conjugação 
'''

palavra = input("Informe a palavra desejada: ").lower()
ultLetra = palavra[-1]
pntLetra = palavra[-2]

if ultLetra == "r":
    print("\nA palavra informada é um verbo no infinitivo.")
    
    if pntLetra == "a":
        print("E está na primeira conjugação.")
    elif pntLetra == "i":
        print("E está na segunda conjugação.")
    elif pntLetra == "o":
        print("E está na terceira conjugação.")
    else:
        print("Não existe verbo com terminação \"ur\".")
else:
    print("É um verbo no infinitivo.")
    
input("\n\nPressione o \"enter\" para encerrar...")
