import matplotlib.pyplot as plt

# Dados
lojas = ['Loja A', 'Loja B', 'Loja C', 'Loja D']
faturamento = [12500, 17300, 9800, 20100]

# Criação do gráfico
fig, ax = plt.subplots()
barras = ax.bar(lojas, faturamento, color='skyblue')

# Título e rótulos
ax.set_title('Faturamento por Loja')
ax.set_xlabel('Lojas')
ax.set_ylabel('Faturamento (R$)')

# Adicionando os valores no topo das barras
ax.bar_label(barras, padding=3)

plt.tight_layout()
plt.show()
