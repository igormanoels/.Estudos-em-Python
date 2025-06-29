import numpy as np
from scipy.stats import norm

'''
Cálculo da margem de erro para a estimativa da média populacional,
com desvio padrão conhecido (σ = R$ 6,00), amostra de 50 clientes,
e nível de confiança de 95%.
'''

# Dados do problema
n = 50
desvio_padrao = 6.0
confianca = 0.95

# 1. Encontrar o valor crítico z para 95% de confiança
# Nível de significância (α) = 1 - confiança
alpha = 1 - confianca
z_critico = norm.ppf(1 - alpha/2)  # ppf é a função percentil (inversa da CDF)

# 2. Calcular a margem de erro
margem_erro = z_critico * (desvio_padrao / np.sqrt(n))

print(f'Valor crítico (z): {z_critico:.4f}')
print(f'Margem de erro (E): R$ {margem_erro:.2f}')


