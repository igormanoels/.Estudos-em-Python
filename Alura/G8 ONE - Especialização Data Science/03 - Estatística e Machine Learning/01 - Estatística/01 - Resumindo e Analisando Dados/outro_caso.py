import pandas as pd

# Dados das preferências de transporte
transporte = [
    "Carro", "Ônibus", "Bicicleta", "Carro", "Metrô", "Ônibus", 
    "Bicicleta", "Carro", "Metrô", "Bicicleta", "Carro", "Ônibus", 
    "Bicicleta", "Carro", "Metrô", "Carro", "Ônibus", "Bicicleta", 
    "Carro", "Metrô", "Ônibus", "Bicicleta", "Metrô", "Carro",
    "Bicicleta", "Carro", "Metrô", "Ônibus", "Carro", "Bicicleta",
    "Metrô", "Ônibus", "Carro", "Bicicleta", "Ônibus", "Metrô",
    "Carro", "Ônibus", "Metrô", "Bicicleta", "Carro", "Metrô",
    "Bicicleta", "Ônibus", "Carro", "Metrô", "Ônibus", "Bicicleta"
]

# Transformando em um DataFrame
dados = pd.DataFrame(transporte, columns=['Meio_Transporte'])

# Calculando a distribuição de frequência e ordenando por frequência absoluta
tabela_freq = (
    dados.groupby('Meio_Transporte')
    .size()
    .reset_index(name='Fi')  # Frequência absoluta
)

# Calculando a frequência relativa
tabela_freq['Fri'] = round(tabela_freq['Fi'] / tabela_freq['Fi'].sum(),2)

# Calculando a frequência acumulada
tabela_freq['F'] = tabela_freq['Fi'].cumsum()

# Calculando a frequência relativa acumulada
tabela_freq['Fri_acum'] = tabela_freq['Fri'].cumsum()

# Ordenando pela frequência absoluta
tabela_freq = tabela_freq.sort_values(by='Fi', ascending=False)

print(tabela_freq)