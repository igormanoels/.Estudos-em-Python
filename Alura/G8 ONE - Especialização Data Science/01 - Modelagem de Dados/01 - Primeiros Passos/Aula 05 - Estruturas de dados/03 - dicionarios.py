loja = {'nomes': ['televisão', 'celular', 'notebook', 'geladeira', 'fogão'],
        'precos': [2000, 1500, 3500, 4000, 1500]}


for chave, elementos in loja.items():
  print(f'Chave: {chave}\nElementos:')
  for dado in elementos:
    print(dado)