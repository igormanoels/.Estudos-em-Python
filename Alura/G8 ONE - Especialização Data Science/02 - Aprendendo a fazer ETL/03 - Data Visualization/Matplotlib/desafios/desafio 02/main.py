'''
Você trabalha como Analista de Dados em uma empresa de varejo e recebeu a tarefa de criar uma figura com subplots que 
apresente a variação no número de vendas em quatro diferentes lojas ao longo de um ano. A gerência da empresa precisa 
visualizar de forma clara as tendências de vendas em cada loja, para que possam tomar decisões estratégicas sobre os 
estoques e ações de marketing. Para isso, você deve criar quatro subplots dispostos em duas linhas e duas colunas, 
onde cada subplot representa uma loja diferente. Nesse desafio, cada subplot deve apresentar um gráfico de linhas que 
mostre a variação do número de vendas ao longo dos meses do ano.

Agora, chegou a hora de mostrar suas habilidades em análise de dados e visualização! Para criar o DataFrame com o número 
de vendas das lojas e criar a figura, utilize as informações abaixo:

Dica: Para facilitar a criação dos subplots, você pode definir a coluna "Lojas" como índice do DataFrame e utilizar a 
propriedade loc da biblioteca Pandas para plotar cada uma das lojas.
'''

lojas = ['A', 'B', 'C', 'D']

vendas_2022 = {'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}