import pandas as pd

# 1 - Atribuição direta de valores a uma nova coluna:
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = [7, 8, 9]
df


# 2 - Criação de uma coluna a partir de operações entre outras colunas:
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = df['A'] + df['B']
df


# 3 - Utilização do método assign() para criar uma nova coluna:
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = df['A'].apply(lambda x: x * 2)
df


# 4 - Utilização do método apply() para aplicar uma função a uma coluna existente e criar uma nova coluna:
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = df['A'].apply(lambda x: x * 2)
df
