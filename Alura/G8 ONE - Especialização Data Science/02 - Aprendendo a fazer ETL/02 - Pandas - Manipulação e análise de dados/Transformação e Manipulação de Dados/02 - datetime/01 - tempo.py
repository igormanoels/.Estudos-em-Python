import datetime
import pandas

# criando um objeto datetime com a data e hora atual
agora = datetime.datetime.now()
print("Data e hora atual:", agora)


# criando um objeto date com a data de hoje
hoje = datetime.date.today()
print("Data de hoje:", hoje)


# criando dois objetos date com datas diferentes
data_1 = datetime.date(2022, 1, 1)
data_2 = datetime.date(2023, 1, 1)

# calculando a diferença entre as duas datas
diferenca = data_2 - data_1
print("Diferença entre as duas datas:", diferenca)




# Criando o DataFrame com as informações
dados = pandas.DataFrame({
    'Data de venda': ['01/01/2022', '05/02/2022', '10/03/2022', '15/04/2022','18/04/2022','20/04/2022'],
    'Valor': [100, 150, 200, 250,80,180]
})

dados['Data de venda'] = dados['Data de venda'] = pandas.to_datetime(dados['Data de venda'], format='%d/%m/%Y')

# Exibindo o DataFrame
print(dados)
print(dados.info())
