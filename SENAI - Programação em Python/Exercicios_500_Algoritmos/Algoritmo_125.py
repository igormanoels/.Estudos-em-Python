import os

os.system('cls')
''' 
    Entrar com a idade de uma pessoa e informar: 
        - Se é maior de idade 
        - Se é menor de idade 
        - Se é maior de 65 anos 
'''

idade = int(input("Informe sua idade: "))

if idade <= 17:
    print("\nMenor de Idade.")
else:
    if idade <= 64:
        print("Maior de Idade.")
    else: 
        print("Terceira idade.")
        
input("\n\nPressione o \"enter\" para encerrar...")
