
import pandas as pd


url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

lojas = [pd.read_csv(url), pd.read_csv(url2), pd.read_csv(url3), pd.read_csv(url4)]

faturamento_total = {}
avaliacao_media_lojas = {}
valor_medio_frete = {}

categorias = []
faturamento_categoria = {}

produtos = []
qtd_produtos = {}


# CÁLCULA O FATURAMENTO POR LOJA
def verificarFaturamento():
    #print(sum(lojas[0]['Preço'])) # Forma sem graça de fazer
    for i, loja in enumerate(lojas, start=1): 
        num_loja = 'loja'
        faturamento = 0.0
        for preco in loja['Preço']:
            faturamento += preco
        num_loja = num_loja + str(i)
        faturamento_total[num_loja] = round(faturamento, 2)



# CÁLCULA A NOTA POR LOJA
def avaliacaoMedia():
    for i, loja in enumerate(lojas, start=1):
        num_loja = 'loja'
        media = 0.0
        for avaliacao in loja['Avaliação da compra']:
            media += avaliacao
        media = (media / (len(loja) - 1))
        num_loja = num_loja + str(i)
        avaliacao_media_lojas[num_loja] = round(media, 1)



# CÁLCULA O CUSTO COM O FRETE POR LOJA
def verificarCustoFrete():
    for i, loja in enumerate(lojas, start=1): 
        num_loja = 'loja'
        frete_total = 0.0
        for frete in loja['Frete']:
            frete_total += frete
        num_loja = num_loja + str(i)
        valor_medio_frete[num_loja] = round((frete_total / (len(loja) - 1)), 2)



# LISTAR CATEGORIAS E CONTAR VENDAS
def listarCategorias():
    for i, loja in enumerate(lojas, start=1):
        for categoria in loja['Categoria do Produto']:
            if  categoria not in categorias:
                categorias.append(categoria)



def vendasPorCategoria():
    listarCategorias()
    for categoria in categorias:
        total_categoria = 0.0 
        for i, loja in enumerate(lojas, start=1):
            for cat, pr in zip(loja['Categoria do Produto'], loja['Preço']):
                if categoria == cat:
                    total_categoria += pr
        faturamento_categoria[categoria] = round(total_categoria, 2)



# LISTAR PRODUTOS E CONTAR QUANTIDADE
def listarProdutos():
    for i, loja in enumerate(lojas, start=1):
        for produto in loja['Produto']:
            if produto not in produtos:
                produtos.append(produto)


def ordenarProdutosMaior():
    ordenado = dict(sorted(qtd_produtos.items(), key=lambda item: item[1], reverse=True))    
    return ordenado


def ordenarProdutosMenor():
    ordenado = dict(sorted(qtd_produtos.items(), key=lambda item: item[1], reverse=False))    
    return ordenado


def contarQtdProdutos():
    listarProdutos()
    for produto in produtos:
        qtd = 0
        for i, loja in enumerate(lojas, start=1):
            for pdt in loja['Produto']:
                if produto == pdt:
                    qtd +=1
        qtd_produtos[produto] = qtd

    



'''
    TESTES DAS FUNÇÕES
loja.head()        # Mostra as 5 primeiras linhas
loja.tail(3)       # Últimas 3 linhas
loja.info()        # Informações gerais (tipos, colunas)
loja.describe()    # Estatísticas descritivas

print('\n\nTipo da loja: ',type(loja),'\n\n' , loja.head())


#print(lojas[2]['Produto'])
verificarFaturamento()
print('\nFaturamento por loja: ',faturamento_total)

avaliacaoMedia()
print('\nAvaliação média por loja', avaliacao_media_lojas)

verificarCustoFrete()
print('\nCusto médio com frete', valor_medio_frete)

listarCategorias()
print('\nLista de categorias', categorias)

vendasPorCategoria()
print('\nReceita total por categoria', faturamento_categoria)

listarProdutos()
print('\nLista de produtos: ', produtos)

contarQtdProdutos()
print('\nLista qtd produtos: ', qtd_produtos)


print('Maior', ordenarProdutosMaior())
print('inverso:', ordenarProdutosMenor())

'''