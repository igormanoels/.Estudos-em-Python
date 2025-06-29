from scipy.stats import norm
import math

'''
Cálculo do tamanho da amostra para estimar a média populacional dos gastos,
com desvio padrão conhecido (σ = R$ 15,00), nível de significância de 10%,
e erro máximo de 10% da média (R$ 4,55).
'''

# Dados do problema
sigma = 15.0
media = 45.50
erro_percentual = 0.10  # 10%
E = media * erro_percentual  # R$ 4,55
confianca = 0.90  # 1 - alpha (alpha = 0.10)

# 1. Encontrar o valor crítico z para 90% de confiança
alpha = 1 - confianca
z_critico = norm.ppf(1 - alpha/2)  # Para dois lados

# 2. Calcular o tamanho da amostra (arredondar para cima)
n = ( (z_critico * sigma) / E ) ** 2
n_arredondado = math.ceil(n)  # Arredonda para o próximo inteiro

print(f'Valor crítico (z): {z_critico:.4f}')
print(f'Tamanho da amostra calculado: {n:.2f}')
print(f'Tamanho da amostra arredondado: {n_arredondado}')


########################################################################################
'''
Um fabricante de farinha verificou que, em uma amostra aleatória formada por 200 sacos de 25 kg de um lote formado por 2.000 sacos, 
apresentou um desvio padrão amostral do peso igual a 480 g.

Considerando um erro máximo associado à média populacional igual a 0,3 kg e um nível de confiança igual a 95%, qual tamanho de amostra 
deveria ser selecionado para obtermos uma estimativa confiável do parâmetro populacional?
'''
N = 2000
z = norm.ppf(0.5 + (0.95 / 2))
s = 480
e = 0.3 * 1000   # Convertendo kg para g

n = ((z**2) * (s**2) * (N)) / (((z**2) * (s**2)) + ((e**2) * (N - 1)))

print(int(n.round()))