import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo
categorias = ['A', 'B', 'C', 'D']
valores1 = [10, 15, 7, 12]
valores2 = [5, 12, 9, 14]

# Posição das barras
x = np.arange(len(categorias))
largura = 0.35

# Cria as barras lado a lado
fig, ax = plt.subplots()
barras1 = ax.bar(x - largura/2, valores1, largura, label='2023')
barras2 = ax.bar(x + largura/2, valores2, largura, label='2024')

# Adiciona os rótulos e título
ax.set_xlabel('Categorias')
ax.set_ylabel('Valores')
ax.set_title('Comparação por categoria')
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend()

# Adiciona os valores no topo das barras
ax.bar_label(barras1, padding=3)
ax.bar_label(barras2, padding=3)

# Exibe o gráfico
plt.tight_layout()
plt.show()
