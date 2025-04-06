''' 
13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais 
para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda 
durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação,
deve ser enviada às seguintes sugestões:

Para variação acima de 20%: bonificação para o time de vendas.
Para variação entre 2% e 20%: pequena bonificação para time de vendas.
Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
Para bonificações abaixo de -10%: corte de gastos.'
'''


quantidade_vendas22 = int(input('Informe a quantidade de vendas em 2022: '))
quantidade_vendas23 = int(input('Informe a quantidade de vendas em 2023: '))

variacao = (quantidade_vendas22 / quantidade_vendas23) * 100

if variacao > 20:
    print('Bonificação para o time de vendas')
elif variacao > 2 and variacao <= 20:
    print('Pequena bonificação para time de vendas')
elif variacao > (-10) and variacao <=2:
    print('Planejamento de políticas de incentivo às vendas')
else: 
    print('Corte de gastos')

