notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

nomes = []
notas_juntas = []
for i in range(len(notas_turma)):
  if i % 4 == 0:
    nomes.append(notas_turma[i])
  else:
    notas_juntas.append(notas_turma[i])

print(nomes)
print(notas_juntas)


notas = []
for i in range(0, len(notas_juntas), 3):
  notas.append([notas_juntas[i], notas_juntas[i+1], notas_juntas[i+2]])


print('\nNotas em um conjunto de listas de listas: ',notas)


print('Acessando uma lista das listaas: ',notas[0])

print('Acessando um item da lista de listas: ',notas[0][2])













