import pandas as pd
'''
Mais uma etapa de desafio se inicia! Aproveite a oportunidade proposta e mergulhe nas possibilidades. Na aula anterior, você teve 
o desafio de criar uma figura com subplots que apresentam a variação no número de vendas em quatro diferentes lojas ao longo de um 
ano. Agora é o momento de elevar essa figura a um novo patamar! É a hora de personalizá-la! Nesta segunda parte do desafio, você 
deve explorar as opções de customização dos subplots para deixar a figura mais clara e atraente para a gerência da empresa.

Algumas ideias de customização que você pode explorar são:

Alterar a posição dos títulos dos subplots para esquerda.
Aumentar o tamanho da fonte do título geral da figura para destacá-lo.
Aumentar o tamanho dos títulos e rótulos dos eixos dos subplots.
Deixar as linhas com a espessura maior.
Alterar a cor das linhas de cada loja para diferenciá-las ainda mais.
Fique à vontade para testar mais customizações!

E mais uma dica: você pode reduzir o tamanho do código utilizando o comando for i, ax in enumerate(axs.flat): que permite um loop 
iterando sobre todos os subplots da figura. Dentro desse loop você pode passar as funções plot, set_title, set_xlabel, set_ylabel e etc…

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

# Criando DataFrame
df = pd.DataFrame(vendas_2022, index=lojas)