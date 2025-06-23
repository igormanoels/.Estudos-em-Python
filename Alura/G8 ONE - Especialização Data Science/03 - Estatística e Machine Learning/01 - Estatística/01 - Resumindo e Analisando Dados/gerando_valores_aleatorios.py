import numpy as  np

# Gerando dados simulados de consumo de energia (kWh)
np.random.seed(42)
consumo = 2 * np.round(100 * np.random.beta(10, 4, size=10000), 0)

# Calculando a média
media_consumo = np.mean(consumo)

# Calculando a variância
variancia = np.var(consumo)

# Calculando o desvio padrão
desvio_padrao = np.std(consumo)

# Calculando o Desvio Médio Absoluto (MAD)
mad = np.mean(np.abs(consumo - media_consumo))

# Exibindo os resultados
print(f"Média do Consumo: {round(media_consumo, 2)} kWh")
print(f"Variância: {round(variancia, 2)} kWh^2")
print(f"Desvio Padrão: {round(desvio_padrao, 2)} kWh")
print(f"Desvio Médio Absoluto: {round(mad, 2)} kWh")

'''
saída esperada

'Média do Consumo: 142.68 kWh'
'Variância: 538.39 kWh^2'
'Desvio Padrão: 23.22 kWh'
'Desvio Médio Absoluto: 18.74 kWh'
'''

