import matplotlib.pyplot as plt

# Exemplo de dados
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [2, 5, 10, 17]
y3 = [3, 6, 11, 18]
y4 = [4, 7, 12, 19]

# Lista com as legendas
legendas = ['Série A', 'Série B', 'Série C', 'Série D']

# Plota as séries
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)

# Adiciona a legenda
plt.legend(legendas)

# Exibe o gráfico
plt.show()