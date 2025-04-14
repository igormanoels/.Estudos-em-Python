'''
try:
    # código a ser executado. Caso uma exceção seja lançada, pare imediatamente
except:
    # Se uma exceção for lançada no try, rode esse código, senão pule esta etapa
else:
    # Se não houver uma exeção lançada pelo try, rode essa parte
finally:
    # Rode essa parte (com ou sem exceção)
'''



notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0],
         'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}


# Funcionando
nome = input('Digite o nome do aluno: ')
res = notas[nome] # Colocando um nome que não existe retorna um erro
print(res)



# Aplicando um tratamento para caso haja uma exceção pela classe mãe de erro
try:
  nome = input('Digite o nome do aluno: ')
  res = notas[nome]
except Exception as e:
  print(e, ': ', nome, 'é um nome inesistente' )


# Outra forma, tratando o erro diretamente
try:
  nome = input('Digite o nome do aluno: ')
  res = notas[nome]
except KeyError:
  print('Estudante não matriculado' )


# ADCIONAMOS O ELSE, PARA CASO NÃO HAJA EXCEÇÃO O FLUXO DO ALGORITMO CONTINUE
try:
  nome = input('Digite o nome do aluno: ')
  res = notas[nome]
except KeyError:
  print('Estudante não matriculado' )
else:
  print(res)


# ADCIONAMOS O FINALLY PARA RETORNAR ALGO INDEPENDENTE DO RESULTADO DA OPERAÇÃO
try:
  nome = input('Digite o nome do aluno: ')
  res = notas[nome]
except KeyError:
  print('Estudante não matriculado' )
else:
  print(res)
finally:
  print('Consulta encerrada')


