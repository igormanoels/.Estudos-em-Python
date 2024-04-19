import os
import math

os.system('cls')  # Este comando pode não funcionar em todos os sistemas operacionais, dependendo do sistema, você pode querer considerar alternativas.

'''
    MENU - um pouco de tudo 
        A - Armazena na variavel menor e imprime o nome que tiver o menor 
        numero de caracteres entre tres 
        B - Gera e imprime uma nova palavra 
        C - Calcula e imprime a raiz a quarta de um numero 
        F - Finalizar 
'''

def palavras():
    global menorPalavra
    palavra1 = input("Informe a primeira palavra: ")
    palavra2 = input("Informe a segunda palavra: ")
    palavra3 = input("Informe a terceira palavra: ")
    
    if len(palavra1) < len(palavra2) and len(palavra1) < len(palavra3):
        palavra = palavra1    
    elif len(palavra2) < len(palavra3):
        palavra = palavra2
    else: 
        palavra = palavra3
    
    menorPalavra = palavra

def menu():
    print("MENU - Um pouco de tudo",
           "\nA - Armazena na variavel menor e imprime o nome que tiver o menor numero de caracteres entre tres",
           "\nB - Imprime a palavra", 
           "\nC - Calcula e imprime a raiz a quarta do tamanho da palavra", 
           "\nF - Finalizar")
    op = input("\nDigite a opção desejada: ").upper()   
    
    if op == "A":
        palavras()
        menu()
    elif op == "B":
        print(menorPalavra)
        menu()
    elif op == "C":
        print(math.pow(len(menorPalavra), 4))
        menu()
    elif op == "F":
        print("Até logo!")
    else:
        print("Opção inválida!")
        menu()

menu()

input("\n\nPressione o \"enter\" para encerrar...")
