# Os dicionários possuem uma estrutura de chave e valor
dicionario = {'chave': 'valor'}

dicionario = {'chave_1':1, 'chave_2':2, 'chave_3':3}
print(dicionario)



# Dicionário com chaves múltiplas
cadastro = {'matricula': 2000168933,
    'dia_cadastro': 25,
    'mes_cadastro': 10,
    'turma': '2E'}
print(cadastro,'\n')

print(cadastro['matricula'],'\n')    # Como acessar os valores do dicionario



# Manipulando os valores das chaves
cadastro['turma'] = '2G'
print(cadastro['turma'],'\n')



# Adcionando uma nova chave
cadastro['modalidade'] = 'EAD'
print(cadastro,'\n')



# Removendo uma chave do dicionario
cadastro.pop('turma') # além de remover, ele tbm retorna o valor da chave q foi removida
print(cadastro,'\n')



# Exibindo apenas os itens, em pares de chaves e valor
print(cadastro.items(),'\n')



# Retornando apenas as chaves
print(cadastro.keys(),'\n')



# Retornando apenas os valores
print(cadastro.values(),'\n')



# Iterando sobre os elemento do dicionários
for chave in cadastro.keys(): # lendo os valores do dicionário
    print(cadastro[chave])

print('\n')

for valor in cadastro.values(): # outra forma
    print(valor)

print('\n')

for chaves, valores in cadastro.items(): # Utilizando o itens
  print(f'Chave:{chaves}: valor: {valores}')


print('\n')


