import os

os.system('cls')
'''
    Criar um algoritmo que permita ao aluno responder qual a capital do Brasil. 
    Todas as possibilidades deverão ser pensadas.
'''

capital = input("Qual a capital do Brasil?\n Resposta: ")

if capital.__contains__("Brasília") or capital.__contains__("BRASÍLIA"):
    print("Resposta Correta!")
elif capital.__contains__("brasília"):
    print("Resposta Correta! Mas preste atenção a grafía correta, \"Brasília\" ou \"BRASÍLIA\"")
else:
    print("Resposta Incorreta!")

input("\n\nPressione o \"enter\" para encerrar...")
