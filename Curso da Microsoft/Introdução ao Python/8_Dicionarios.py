# TRABALHANDO COM DICIONÁRIOS

aluno = { 'nome': 'Julia', 'media': 7}
print(aluno)                                    # Acessa todos os elementos do dicionário
print(aluno.get('nome'))                        # Acessa o elemento nome que está contido no dicionário

aluno.update({'nome': 'Ricardo', 'media': 8})   # Altera os valores presentes dentro do Dicionário                                
print("Aluno: " , aluno.get('nome') , " | Média: " , aluno.get('media'))

aluno['serie'] = '4ªB'                          # Inclui elementos-chave dentro do dicionário
print("Aluno: " , aluno.get('nome') , " | Média: " , aluno.get('media') , " | Sala: " , aluno.get('serie') )


# Também é possivel aninhar dicionários
planet = {
    'name': 'Jupiter',
    'moons': 79
}

planet['orbital period'] = 4333

planet['diameter'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(planet)
print(f'{planet["name"]} polar diameter: {planet["diameter"]["polar"]}')       # Forma de acessar

# REPRESENTAÇÃO DE COMO É POSICIONADO QUANDO É ANINHADO
# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }


# Método de acesso utilizando FOR
produtos = {
    'arroz': 9.99,
    'feijao': 5.49,
    'macarrao': 3.99,
    'leite': 2.99,
    'biscoito': 1.99
}

for i in produtos.keys():                       # O laço percorre a estrutura do dicionário item a item
    print(f'{i}: {produtos[i]}')                # trazendo a chave e o conteúdo

if 'cebola' in produtos:                        # Verifica SE a chave cebola está contida
    produtos['cebola'] = 1.25                   # CASO esteja altera o valor para 1,25
else:
    produtos['cebola'] = 1.25                   # CASO-CONTRÁRIO inclui a chave e seu valor
print(produtos)

# SOMANDO OS VALORES DE UM DICIONÁRIO
AliceNotas = {
    'primSem': 4.9,
    'segSem': 9.12,
    'terSem': 4.45,
    'quartSem': 5.24
}
media = 0
quant = 0
for i in AliceNotas.values():                   # Percorre as chaves do dicionário AliceNotas
    media = media + i                           # Cada item percorrido da chave fica contido em 'i', que é somado a media
    quant += 1                                  # Realiza a contagem de itens dentro do dicionário
media /= quant                                  # Divide a média por 4
print('Média Final: ' , round(media,2))         # Exibe a nota com o arredondamento de duas casas



aluno = {'nome': 'Ana', 'idade': 20, 'nota': 8.5} 
print(aluno)
idade = aluno.pop('idade')      # Usando pop para remover a chave 'idade' e obter o valor associado
print(f"Idade removida: {idade}")
print(f"Dicionário atualizado: {aluno}")

