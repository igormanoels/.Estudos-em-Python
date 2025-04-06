'''
12) Um estabelecimento está vendendo combustíveis com descontos variados. 

Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. 

Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. 

O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. 

Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. 

Tenha em mente algumas dicas:
O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
'''
preco_diesel = 2.00
preco_etanol = 1.70
res = 0.0

combustivel = input('Informe o tipo de combustivel: ')
quantidade_lts = float(input('Informe a quantidade de litros: '))


if combustivel == 'd' or combustivel == 'D':
    if quantidade_lts <= 15:
        res = (quantidade_lts * preco_diesel) * 0.97
    else:
        res = (quantidade_lts * preco_diesel) * 0.95
elif combustivel == 'e' or combustivel == 'E':
    if quantidade_lts <= 15:
        res = (quantidade_lts * preco_etanol) * 0.98
    else:
        res = (quantidade_lts * preco_etanol) * 0.96


print('O valor para pagamento deverá ser de R$ %.2f' %(res))

