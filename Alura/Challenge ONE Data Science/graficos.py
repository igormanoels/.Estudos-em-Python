
import matplotlib.pyplot as plt




def graficoFaturamento(faturamentoLojas):
    lojas = []
    faturamentos = []
    
    for loja, faturamento in faturamentoLojas.items():
        lojas.append(loja)
        faturamentos.append(faturamento)

    plt.bar(lojas, faturamentos, color='green')
    plt.title('Gráfico de Faturamento por Loja')
    plt.xlabel('Lojas')
    plt.ylabel('Faturamento')
    plt.show()



def graficoAvaliacao(avaliacaoLojas):
    lojas = []
    avaliacoes = []

    for loja, avaliacao in avaliacaoLojas.items():
        lojas.append(loja)
        avaliacoes.append(avaliacao)
    
    fig, grafico = plt.subplots()
    barras = grafico.bar(lojas, avaliacoes, color='green')

    grafico.set_title('Gráfico de avaliações média por Loja')
    grafico.set_xlabel('Lojas')
    grafico.set_ylabel('Avaliações dos Clientes')
    
    grafico.bar_label(barras, padding=3)
    
    plt.tight_layout()
    plt.show()



def graficoFretes(freteLojas):
    lojas = []
    fretes = []

    for loja, frete in freteLojas.items():
        lojas.append(loja)
        fretes.append(frete)

    barra = plt.bar(lojas, fretes, color='blue')
    plt.title('Gráfico de Custo médio dos fretes por Loja')
    plt.bar_label(barra, padding=0)
    plt.xlabel('Lojas')
    plt.ylabel('Gasto Médio com Fretes')
    plt.show()    



def graficoCategorias(categoriaLojas):
    categorias = []
    vendas = []

    for cat, venda in categoriaLojas.items():
        categorias.append(cat)
        vendas.append(venda)

    plt.pie(vendas, labels=categorias, autopct='%1.2f%%')
    plt.title('Gráfico de Custo médio dos fretes por Loja')
    plt.show()



def graficoQuantidade(quantidadesProdutos, listarPor):
    produtos = []
    quantidades = []

    for produto, quant in quantidadesProdutos.items():
        if len(produtos) < 10:
            produtos.append(produto)
            quantidades.append(quant)
        else:
            break

    barra = plt.barh(produtos, quantidades, color='orange')
    if listarPor == 6:
        plt.title('Gráfico Produtos mais vendidos')
    else:
        plt.title('Gráfico Produtos menos vendidos')
        
    plt.xlim(0, 300)
    plt.bar_label(barra)
    plt.xlabel('Quantidades')
    plt.ylabel('Produtos')

    plt.show()    
