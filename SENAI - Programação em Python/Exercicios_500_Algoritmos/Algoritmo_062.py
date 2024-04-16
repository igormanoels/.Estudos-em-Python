import os

os.system('cls')
# Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto.
# Faça um algoritmo que possa entrar com o valor de um produto e imprima o novo valor tendo em vista que o desconto foi de 9%.

preco = float(input("Informe o valor do produto: R$ "))
nPreco = preco * 0.91
nPreco = round(nPreco, 2)

print("\nPreço Ajustado: R$ ", nPreco)
input("\n\nPressione o \"enter\" para encerrar...")
