cadastro = ("Júlia", 23, "São Paulo", "SP", "Python para DS 1")


print(cadastro[0]) # imprime Júlia
print(cadastro[-1]) # imprime Python para DS 1


'''
    Além disso, por também ser um iterável, podemos desempacotar os dados de 
    uma tupla passando cada valor para uma variável. Por exemplo:
'''
nome, idade, cidade, estado, turma = cadastro


print(f'A estudante {nome} tem {idade} anos e mora em {cidade}-{estado}. Ela está matriculada na turma de {turma}.')


