import os

os.system('cls')
'''
    Criar um algoritmo que informe a quantidade total de calorias de uma refeição a 
    partir da escolha do usuário 'que deverá informar o prato, a sobremesa e bebida 
        PRATO                       SOBREMESA                       BEBIDA 
        Vegetariano 180cal          Abacaxi 75cal                   Chá 20caI 
        Peixe 230cal                Sorvete diet 11Oca!             Suco de laranja 70cal 
        Frango 250ca!               Mousse diet 17Oca!              Suco de melão 1OOca! 
        Carne 350ca!                Mousse chocolate 200cal         Refrigerante diet 65cal
'''
cal = 0

op = int(input("Opções de Prato: 1-Vegetáriano | 2-Peixe | 3-Frango | 4-Carne", 
               "\nInforme o prato desejado: "))
if op == 1:
    cal += 180
elif op == 2:
    cal += 230
elif op == 3:
    cal += 250
elif op == 4:
    cal += 350

op = int(input("\nOpções de Sobremesa: 1-Abacaxi | 2-Sorvete diet | 3-Mousse diet | 4-Mousse chocolate", 
               "\nInforme a sobremesa desejada: "))
if op == 1:
    cal += 75
elif op == 2:
    cal += 110
elif op == 3:
    cal += 170
elif op == 4:
    cal += 200
    
op = int(input("\nOpções de Bebida: 1-Chá | 2-Suco de laranja | 3-Suco de melão | 4-Refrigerante diet", 
               "\nInforme a bebida desejada: "))
if op == 1:
    cal += 20
elif op == 2:
    cal += 70
elif op == 3:
    cal += 100
elif op == 4:
    cal += 65

print(f"\nO total de calorias para essa refeição é de {cal}cal.")

input("\n\nPressione o \"enter\" para encerrar...")
