import os

os.system('cls')
'''
    Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir: 
    VALOR DA COMPRA                             VALOR DA VENDA 
    Valor < R$ 10,00                            lucro de 70% 
    R$10,00 <= valor < R$ 30,00                 lucro de 50% 
    R$30,00 <= valor < R$ 50,00                 lucro de 40% 
    Valor > R$50,00                             lucro de 30%
'''

pCompra = float(input("Informe o valor do preço de compra: R$ "))

if pCompra < 10:
    nPreco = round((pCompra * 1.7), 2)
elif pCompra < 30:
    nPreco = round((pCompra * 1.5), 2)
elif pCompra < 50:
    nPreco = round((pCompra * 1.4), 2)
else:
    nPreco = round((pCompra * 1.3), 2)

print(f"\nO novo preço deverá ser R$ {nPreco}")

input("\n\nPressione o \"enter\" para encerrar...")
