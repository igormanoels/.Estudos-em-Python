import os

os.system('cls')
'''
    Um restaurante faz uma promoção semanal de descontos para clientes de acordo com as iniciais do nome da pessoa. 
    Criar um algoritmo que leia o primeiro nome do cliente, o valor de sua conta e se o nome iniciar com as letras 
    A, D, M ou 5, dar um desconto de 30%. Para o cliente cujo nome não se inicia por nenhuma dessas letras, exibir a 
    mensagem "Que pena. Nesta semana o desconto não é para seu nome; mas continue nos prestigiando que sua vez chegara". 
'''
cliente = input("Informe o nome do cliente: ").upper()
letra = cliente[0]
conta = float(input("Informe o valor da conta: R$ "))

if letra == "A" or letra == "D" or letra == "M" or letra == "S":
    conta = round((conta * 0.7), 2)
    print(f"\nO cliente ganhou 30% de desconto. Valor a pagar R$ {conta}")
else:
    print(f"\nO cliente não ganhou o desconto. Valor a pagar R$ {conta}")

input("\n\nPressione o \"enter\" para encerrar...")
