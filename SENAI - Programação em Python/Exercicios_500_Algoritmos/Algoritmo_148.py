import os

os.system('cls')
'''
    Criar um algoritmo que leia o destino do passageiro, se a viagem inclui retorno 
    (ida e volta) e informar o preço da passagem conforme atabela a seguir. 
    DESTINO                         IDA                         IDA E VOLTA 
    Região Norte                    R$500,00                    R$900,00 
    Região Nordeste                 R$350,00                    R$650,00 
    Região Centro-Oeste             R$350,00                    R$600,00 
    Região Sul                      R$300,00                    R$550,00 
'''

destino = int(input("Destinos:",
"\n\t1-Região Norte\n\t2-Região Nordeste\n\t3-Região Centro-Oeste\n\t4-Região Sul\nDigite a opção desejada: "))
tipo = int(input("Digite 1-Para viagem de Ida e 2-Para viagem de Ida e Volta: "))

if destino == 1:
    if tipo == 1:
        preco = 500.00
    else:
        preco = 900.00
elif destino == 2:
    if tipo == 1:
        preco = 350.00
    else:
        preco = 650.00
elif destino == 3:
    if tipo == 1:
        preco = 350.00
    else:
        preco = 600.00
elif destino == 4:
    if tipo == 1:
        preco = 350.00
    else:
        preco = 550.00

print(f"\nO valor para o destino desejado é {preco}")

input("\n\nPressione o \"enter\" para encerrar...")
