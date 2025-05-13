| Categoria                         | Função/Classe       | Descrição                                 | Como usar                                                                 |
|----------------------------------|---------------------|-------------------------------------------|---------------------------------------------------------------------------|
| Estruturas de Dados              | `Series`            | Cria uma série unidimensional             | `s = pd.Series([1, 2, 3])`                                                |
|                                  | `DataFrame`         | Cria uma tabela bidimensional             | `df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})`                           |
| Leitura de Arquivos              | `read_csv()`        | Lê um arquivo CSV                         | `df = pd.read_csv('dados.csv')`                                          |
|                                  | `read_excel()`      | Lê um arquivo Excel                       | `df = pd.read_excel('arquivo.xlsx')`                                     |
|                                  | `read_json()`       | Lê um arquivo JSON                        | `df = pd.read_json('dados.json')`                                        |
| Escrita de Arquivos              | `to_csv()`          | Salva em arquivo CSV                      | `df.to_csv('saida.csv', index=False)`                                    |
|                                  | `to_excel()`        | Salva em Excel                            | `df.to_excel('saida.xlsx')`                                              |
| Seleção de Dados                 | `loc[]`             | Seleção por rótulo                        | `df.loc[0, 'A']`                                                          |
|                                  | `iloc[]`            | Seleção por posição                       | `df.iloc[0, 1]`                                                           |
|                                  | `at[]`, `iat[]`     | Seleção rápida por rótulo/posição         | `df.at[0, 'A']`, `df.iat[0, 1]`                                           |
| Manipulação de Colunas e Linhas | `drop()`            | Remove colunas ou linhas                  | `df.drop('A', axis=1)`                                                   |
|                                  | `rename()`          | Renomeia colunas ou índices               | `df.rename(columns={'A': 'Coluna_A'})`                                   |
|                                  | `append()`          | Adiciona linhas                           | `df.append(outra_linha, ignore_index=True)`                              |
|                                  | `merge()`           | Junta DataFrames (tipo JOIN)              | `pd.merge(df1, df2, on='id')`                                            |
|                                  | `concat()`          | Concatena DataFrames                      | `pd.concat([df1, df2], axis=0)`                                          |
| Estatísticas Descritivas         | `mean()`            | Média                                     | `df['A'].mean()`                                                         |
|                                  | `median()`          | Mediana                                   | `df['A'].median()`                                                       |
|                                  | `std()`             | Desvio padrão                             | `df['A'].std()`                                                           |
|                                  | `describe()`        | Estatísticas resumidas                    | `df.describe()`                                                           |
| Filtros e Máscaras               | Condicional         | Filtragem de dados                        | `df[df['A'] > 10]`                                                        |
| Datas e Tempos                   | `to_datetime()`     | Converte string para datetime             | `df['data'] = pd.to_datetime(df['data'])`                                |
|                                  | `.dt` accessor      | Acessa partes da data                     | `df['data'].dt.year`, `df['data'].dt.month`                              |
| Agrupamento e Agregação         | `groupby()`         | Agrupa por colunas                        | `df.groupby('categoria')['valor'].sum()`                                 |
|                                  | `agg()`             | Múltiplas agregações                      | `df.groupby('cat').agg({'v1':'mean','v2':'sum'})`                        |
| Ordenação                        | `sort_values()`     | Ordena por valores                        | `df.sort_values(by='A')`                                                 |
|                                  | `sort_index()`      | Ordena pelo índice                        | `df.sort_index()`                                                        |
| Tratamento de Nulos              | `isnull()`          | Verifica valores nulos                    | `df.isnull()`                                                             |
|                                  | `fillna()`          | Preenche valores nulos                    | `df.fillna(0)`                                                            |
|                                  | `dropna()`          | Remove linhas com nulos                   | `df.dropna()`                                                             |
| Aplicação de Funções             | `apply()`           | Aplica função linha/coluna                | `df['A'].apply(lambda x: x * 2)`                                         |
|                                  | `map()`             | Aplica função a Series                    | `df['A'].map({'Sim': 1, 'Não': 0})`                                      |
|                                  | `applymap()`        | Aplica função a todos os elementos        | `df.applymap(lambda x: x * 2)`                                           |



[Documentação: API reference](https://pandas.pydata.org/docs/reference/index.html)