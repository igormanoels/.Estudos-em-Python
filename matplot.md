# Tabela de Funções do matplotlib.pyplot com Exemplos

| Função                  | Descrição                                  | Exemplo de Uso                                       |
|------------------------|---------------------------------------------|------------------------------------------------------|
| `plt.plot()`           | Gráfico de linha                            | `plt.plot(x, y)`                                     |
| `plt.scatter()`        | Gráfico de dispersão                        | `plt.scatter(x, y)`                                  |
| `plt.bar()`            | Gráfico de barras verticais                 | `plt.bar(categorias, valores)`                      |
| `plt.barh()`           | Gráfico de barras horizontais               | `plt.barh(categorias, valores)`                     |
| `plt.hist()`           | Histograma                                  | `plt.hist(dados, bins=10)`                          |
| `plt.pie()`            | Gráfico de pizza                            | `plt.pie(valores, labels=rotulos)`                 |
| `plt.boxplot()`        | Diagrama de caixa                           | `plt.boxplot(dados)`                                |
| `plt.violinplot()`     | Gráfico de violino                          | `plt.violinplot(dados)`                             |
| `plt.errorbar()`       | Linha com barras de erro                    | `plt.errorbar(x, y, yerr=erro)`                     |
| `plt.stackplot()`      | Área empilhada                              | `plt.stackplot(x, [y1, y2])`                        |
| `plt.fill_between()`   | Área entre curvas                           | `plt.fill_between(x, y1, y2)`                       |
| `plt.step()`           | Gráfico em degraus                          | `plt.step(x, y)`                                    |
| `plt.stem()`           | Gráfico de hastes                           | `plt.stem(x, y)`                                    |
| `plt.hexbin()`         | Gráfico de densidade com hexágonos          | `plt.hexbin(x, y, gridsize=30)`                     |

### Personalização

| Função                  | Descrição                                  | Exemplo de Uso                                       |
|------------------------|---------------------------------------------|------------------------------------------------------|
| `plt.title()`          | Define o título                             | `plt.title("Meu Gráfico")`                          |
| `plt.xlabel()`         | Rótulo do eixo X                            | `plt.xlabel("Eixo X")`                              |
| `plt.ylabel()`         | Rótulo do eixo Y                            | `plt.ylabel("Eixo Y")`                              |
| `plt.legend()`         | Adiciona legenda                            | `plt.legend(["Série 1"])`                           |
| `plt.grid()`           | Adiciona grade                              | `plt.grid(True)`                                    |
| `plt.xticks()`         | Define rótulos do eixo X                    | `plt.xticks([1,2,3], ['A','B','C'])`                |
| `plt.yticks()`         | Define rótulos do eixo Y                    | `plt.yticks(range(0,10,2))`                         |
| `plt.xlim()`           | Limites do eixo X                           | `plt.xlim(0, 100)`                                  |
| `plt.ylim()`           | Limites do eixo Y                           | `plt.ylim(0, 100)`                                  |
| `plt.text()`           | Adiciona texto no gráfico                   | `plt.text(2, 5, "Ponto importante")`                |
| `plt.annotate()`       | Anota com seta                              | `plt.annotate("Máximo", xy=(3,8), xytext=(4,10))`   |

### Layout e figuras

| Função                  | Descrição                                  | Exemplo de Uso                                       |
|------------------------|---------------------------------------------|------------------------------------------------------|
| `plt.figure()`         | Cria uma nova figura                        | `plt.figure(figsize=(10,6))`                        |
| `plt.subplots()`       | Cria múltiplos gráficos                     | `fig, ax = plt.subplots(2, 2)`                      |
| `plt.subplot()`        | Subgráfico manual                           | `plt.subplot(2, 1, 1)`                              |
| `plt.tight_layout()`   | Ajusta automaticamente                      | `plt.tight_layout()`                                |
| `plt.subplots_adjust()`| Ajusta espaçamentos                         | `plt.subplots_adjust(hspace=0.5)`                   |

### Estilo e aparência

| Função                  | Descrição                                  | Exemplo de Uso                                       |
|------------------------|---------------------------------------------|------------------------------------------------------|
| `plt.style.use()`      | Define estilo global                        | `plt.style.use("ggplot")`                           |
| `plt.colormaps()`      | Lista colormaps                             | `plt.colormaps()`                                   |
| `plt.set_cmap()`       | Define colormap                             | `plt.set_cmap("viridis")`                           |

### Exportação e exibição

| Função                  | Descrição                                  | Exemplo de Uso                                       |
|------------------------|---------------------------------------------|------------------------------------------------------|
| `plt.savefig()`        | Salva o gráfico                             | `plt.savefig("grafico.png")`                        |
| `plt.show()`           | Exibe o gráfico                             | `plt.show()`                                        |
| `plt.close()`          | Fecha o gráfico atual                       | `plt.close()`                                       |
