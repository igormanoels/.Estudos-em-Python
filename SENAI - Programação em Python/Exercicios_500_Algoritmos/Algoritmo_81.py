import os

os.system('cls')
'''
    Criar um algoritmo que, dado um número de conta corrente com três dígitos, retorne o seu dígito verificador, o qual é calculado da seguinte maneira: 
    Exemplo: número da conta: 235 
    Somar o número da conta com o seu inverso: 235+ 532 = 767 
    multiplicar cada dígito pela sua ordem posicional e somar estes resultados: 767 
    o último dígito desse resultado é o dígito verificador da conta (40 -> 0). 
'''
nConta = int(input("Favor informar o número da conta: "))

cent = (nConta // 100)
dez = (nConta // 10) % 10
uni = (nConta % 10)

x1 = ((cent + uni) * 1)
x2 = ((dez + dez) * 2)
x3 = ((uni + cent) * 3)

digito = (x1 + x2 + x3)

print("\nDigito Verificador: ", digito)
input("\n\nPressione o \"enter\" para encerrar...")
