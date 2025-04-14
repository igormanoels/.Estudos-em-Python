# A 'LIST COMPREHENSION' É UMA FORMA SIMPLES PARA CRIAÇÃO DE UMA LISTA
# MODO DE USAR ---> [expressão for item in lista]

notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

''' Função para calcular a média de notas passadas por uma lista

  lista: list, default [0]
    Lista com as notas para calcular a média
  return = calculo: float
    Média calculada
'''
def media(lista: list=[0]) -> float:
    calculo = sum(lista) / len(lista)
    return calculo


medias = [round(media(nota),1) for nota in notas]
print('Médias', medias)

#####################################################################################################################
# OUTRA SITUAÇÃO
# MODO DE USAR ---> [expressão for item in lista if condição]

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]


# Gerando a lista de nomes extraídos da túpla, cada nome está na posição 0 das túplas
nomes = [nome[0] for nome in nomes]
print(nomes)


# Usando o zip e list para converter esse objeto zip para uma lista
estudantes = list(zip(nomes, medias))
print(estudantes)


# Gerando a lista de pessoas candidatas a bolsa
candidatos = [estudante[0] for estudante in estudantes if estudante[1]>=8]
candidatos

#####################################################################################################################
# Agora usando if-else
nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]


situacao = ["Aprovado" if media >= 6 else "Reprovado" for media in medias]
print(situacao)

cadastro = [x for x in [nomes, notas, medias, situacao]]
print(cadastro)

# Outra forma
lista_completa = [nomes, notas, medias, situacao]
print(lista_completa)
