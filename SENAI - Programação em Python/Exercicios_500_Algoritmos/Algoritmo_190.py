import os

os.system('cls')
'''
    Entrar com um nome, idade e sexo de 20 pessoas. Imprimir o nome 
    se a pessoa for do sexo masculino e tiver mais de 21 anos. 
'''

for i in range(20):
    nome = input("\nInforme seu nome: ")
    sexo = input("Informe seu sexo: ").lower()
    idade = int(input("Informe sua idade: "))
    if idade > 21 and sexo[0].__contains__("m"):
        print(f"Parabéns {nome}, você foi escolhido!\n")
        
input("\n\nPressione o \"enter\" para encerrar...") 
