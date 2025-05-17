import datetime

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
