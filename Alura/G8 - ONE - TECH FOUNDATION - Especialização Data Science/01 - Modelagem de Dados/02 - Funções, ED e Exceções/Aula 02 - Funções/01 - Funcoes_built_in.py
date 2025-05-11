# Built-in function - Funções embutidas

# Notas do(a) estudante em dicionário
notas = {'1º Trimestre': 8.5, '2º Trimestre': 7.5, '3º Trimestre': 9}
print(notas)


# Calculando a soma normalmente
soma = 0

for nota in notas.values(): # Transforma a lista em iteravel
  soma+=nota

print(soma)


# Usando built-in function
somatorio = sum(notas.values())
print(somatorio)

# Usando a função embutida len()
qtd = len(notas.values())


# calculando média com round
media = round((somatorio / qtd), 2)
print(media)