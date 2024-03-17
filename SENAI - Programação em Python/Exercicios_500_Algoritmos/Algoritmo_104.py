import os

os.system('cls')
'''
Entrar com nome, sexo e idade de uma pessoa. Se a pessoa for do sexo feminino e tiver menos que 25 anos, 
imprimir nome e a mensagem: ACEITA. Caso contrário, imprimir nome e a mensagem: NÃO ACEITA. (Considerar f ou F.)
'''

nome = input("Informe seu nome: ")
sexo = input("Informe seu sexo: ").lower()
idade = int(input("Digite sua idade: "))

if (sexo.count("f") and idade < 25):
    print("\nACEITA.")
else:
    print("\nNÃO ACEITA.")

input("\n\nPressione o \"enter\" para encerrar...")