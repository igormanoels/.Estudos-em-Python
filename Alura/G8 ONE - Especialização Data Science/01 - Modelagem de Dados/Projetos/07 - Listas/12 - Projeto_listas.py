'''
12) Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. 
A pesquisa foi feita e o votos computados podem ser observados abaixo:

Tabela de votos da marca

Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a 
porcentagem de votos recebidos.
'''

dicionario = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}

total_votos = 0
percentual_votos = 0.0
vencedor = ''
votos_vencedor = 0

for chave, valor in dicionario.items():
    total_votos += valor

    if valor > votos_vencedor:
        votos_vencedor = valor
        vencedor = chave

percentual_votos = round(((votos_vencedor / total_votos) * 100),2)

print(f'\nVencedor: {vencedor}\nTotal votos: {votos_vencedor}\nPorcentagem de votos: {percentual_votos}%')








