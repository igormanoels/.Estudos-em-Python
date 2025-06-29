#import numpy as np
from scipy.stats import norm

'''
Um concurso tem notas normalmente distribuídas, com média 70 e desvio padrão 5.
Queremos calcular a probabilidade de um aluno selecionado aleatoriamente ter nota menor que 85.
Usaremos a Distribuição Normal, que modela fenômenos contínuos e simétricos em torno da média.
'''


# Parâmetros da distribuição
media = 70
desvio_padrao = 5

# Nota desejada
x = 85

# Cálculo do Z-score (padronização)
z = (x - media) / desvio_padrao
print(f'Z-score: {z:.2f}')  # Saída: Z-score: 3.00

# Cálculo da probabilidade P(X < 85) usando a função norm.cdf (cumulativa)
probabilidade = norm.cdf(x, loc=media, scale=desvio_padrao)
# Alternativamente: norm.cdf(z)  # Usando o Z-score diretamente

print(f'Probabilidade (P(X < 85)): {probabilidade:.6f}')  # 6 casas decimais




############################################################################################################
'''
O faturamento diário de um motorista de aplicativo segue uma distribuição normal
com média R$ 300 e desvio padrão R$ 50. Calcularemos as probabilidades para os intervalos:
1) Entre R$ 250 e R$ 350
2) Entre R$ 400 e R$ 500
'''
# Parâmetros da distribuição
media = 300
desvio_padrao = 50

# Intervalo 1: 250 < X < 350
prob_250_350 = norm.cdf(350, media, desvio_padrao) - norm.cdf(250, media, desvio_padrao)

# Intervalo 2: 400 < X < 500
prob_400_500 = norm.cdf(500, media, desvio_padrao) - norm.cdf(400, media, desvio_padrao)

print(f'1) Probabilidade entre R$ 250 e R$ 350: {prob_250_350:.4f} ({prob_250_350*100:.2f}%)')
print(f'2) Probabilidade entre R$ 400 e R$ 500: {prob_400_500:.6f} ({prob_400_500*100:.4f}%)')



############################################################################################################
'''
O Inmetro verificou que as lâmpadas incandescentes da fabricante XPTO têm vida útil
normalmente distribuída, com média 720 dias e desvio padrão 30 dias. Calcularemos:
1) Probabilidade de durar entre 650 e 750 dias
2) Probabilidade de durar mais que 800 dias
3) Probabilidade de durar menos que 700 dias
'''
media = 720
desvio_padrao = 30

# Item A
Z_inferior = (650 - media) / desvio_padrao
Z_superior = (750 - media) / desvio_padrao

probabilidade = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
print("{0:.2%}".format(probabilidade))

# Item B
Z = (800 - media) / desvio_padrao

probabilidade = 1 - norm.cdf(Z)
print("{0:.2%}".format(probabilidade))

# Item C
Z = (700 - media) / desvio_padrao

probabilidade = norm.cdf(Z)
print("{0:.2%}".format(probabilidade))



######################################################################################
'''
Utilizando a tabela padronizada, ou o ferramental disponibilizado pelo Python, encontre a área sob a curva normal para os valores de Z abaixo:

1) Z < 1,96

2) Z > 2,15

3) Z < -0,78

4) Z > 0,59
'''
# Item A
probabilidade = norm.cdf(1.96)
print("{0:0.4f}".format(probabilidade))

# Item B
probabilidade = 1 - norm.cdf(2.15)
# ou -> probabilidade = norm.sf(2.15)
print("{0:0.4f}".format(probabilidade))

# Item C
probabilidade = norm.cdf(-0.78)
print("{0:0.4f}".format(probabilidade))

# Item D
probabilidade = 1 - norm.cdf(0.59)
# ou -> probabilidade = norm.sf(0.59)
print("{0:0.4f}".format(probabilidade))



