
import pandas as pd


url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)
lojas = [pd.read_csv(url), pd.read_csv(url2), pd.read_csv(url3), pd.read_csv(url4)]

faturamento_total = {}
avaliacao_media_lojas = {}
valor_medio_frete = {}
vendas_categoria = {}
produtos_mais_vendidos = {}


'''
    for i, loja in enumerate(lojas, start=1):
        print(i)
        for lj in loja['Preço']:
            print(lj)
'''
def verificarFaturamento():
    #print(sum(lojas[0]['Preço'])) # Forma sem graça de fazer
    for i, loja in enumerate(lojas, start=1): 
        num_loja = 'loja'
        faturamento = 0.0
        for preco in loja['Preço']:
            faturamento += preco
        num_loja = num_loja + str(i)
        faturamento_total[num_loja] = round(faturamento, 2)



def avaliacaoMedia():
    for i, loja in enumerate(lojas, start=1):
        num_loja = 'loja'
        media = 0.0
        for avaliacao in loja['Avaliação da compra']:
            media += avaliacao
        media = (media / (len(loja) - 1))
        num_loja = num_loja + str(i)
        avaliacao_media_lojas[num_loja] = round(media, 1)



def verificarCustoFrete():
    for i, loja in enumerate(lojas, start=1): 
        num_loja = 'loja'
        frete_total = 0.0
        for frete in loja['Frete']:
            frete_total += frete
        num_loja = num_loja + str(i)
        valor_medio_frete[num_loja] = round((frete_total / (len(loja) - 1)), 2)


def vendasPorCategoria():
    pass


def listarProdutosPorVendas():
    pass


#print('\n\nTipo da loja: ',type(loja),'\n\n' , loja.head())

'''
loja.head()        # Mostra as 5 primeiras linhas
loja.tail(3)       # Últimas 3 linhas
loja.info()        # Informações gerais (tipos, colunas)
loja.describe()    # Estatísticas descritivas
'''

#print(lojas[2]['Produto'])
verificarFaturamento()
print(faturamento_total)

avaliacaoMedia()
print(avaliacao_media_lojas)

verificarCustoFrete()
print(valor_medio_frete)



