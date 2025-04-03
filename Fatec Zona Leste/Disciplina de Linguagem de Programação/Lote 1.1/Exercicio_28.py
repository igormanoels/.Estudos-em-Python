import os
os.system('cls')

'''
Receba o preço atual e a média mensal de um produto. Calcule e mostre o
novo preço sabendo que:
Venda Mensal        Preço Atual     Preço Novo
< 500               < 30              + 10%
>= 500 e < 1000    >= 30 e < 80       + 15%
>= 1000             >= 80             - 5%
Obs.: para outras condições, preço novo será igual ao preço atual.
'''

precoAtual = float(input("Informe o preço atual do produto: "))
mediaMensal = int(input("Informe a média mensal de vendas: "))

if precoAtual < 30 and mediaMensal < 500:
    novoPreco = precoAtual * 1.1
elif precoAtual < 80 and mediaMensal < 1000:
    novoPreco = precoAtual * 1.15
else:
    novoPreco = precoAtual * 0.95

print(f"O novo preço será R${novoPreco:.2f}")
