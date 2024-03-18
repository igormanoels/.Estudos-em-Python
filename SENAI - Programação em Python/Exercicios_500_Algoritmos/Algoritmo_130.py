import os

os.system('cls')
'''
    Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; 
    caso contrário, o lucro será de 30%. Entrar com o valor do produto e imprimir o valor da venda. 
'''
preco = float(input("Informe o preço do produto: "))

if preco < 20:
    nPreco = round((preco * 1.2), 2)
else:
    nPreco = round((preco * 1.3), 2)

print(f"\nNovo preço: R${nPreco}")

input("\n\nPressione o \"enter\" para encerrar...")
