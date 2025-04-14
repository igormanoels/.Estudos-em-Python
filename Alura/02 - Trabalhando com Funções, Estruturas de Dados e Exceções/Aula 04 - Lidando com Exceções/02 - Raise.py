'''
Uma outra forma de trabalhar com as exceções em seu código, é criar as suas próprias exceções para determinados comportamentos que deseja em seu código.

Para isso, utilizamos a palavra-chave raise junto ao tipo de exceção que deseja lançar e uma mensagem a ser exibida.

raise NomeDoErro("mensagem_desejada")
'''


def media(lista: list=[0]) -> float:
  ''' Função para calcular a média de notas passadas por uma lista

  lista: list, default [0]
    Lista com as notas para calcular a média
  return = calculo: float
    Média calculada
  '''

  calculo = sum(lista) / len(lista)

  if len(lista) > 4 : 
    raise ValueError("A lista não pode possuir mais que 4 notas.")

  return calculo


notas = [1, 5, 6, 7]
resultado = media(notas)
print(resultado)


# Com a lista maior um erro será lançado
notas = [1, 5, 6, 7, 5]
resultado = media(notas)

'''
    Os erros ocorrem segundo uma hierarquia, não importa quantos possam existir, o que acontecer primeiro aparecerá
    nesse caso, antes da quantidade é realizado o cálculo pela função.
'''
notas = [1, 5, 6, 7, '4']
resultado = media(notas)



#####################################################################################################################
# Executando o código com a proteção dos erros 
try: 
  notas = [1, 5, 6, 7]
  resultado = media(notas)
except ValueError as e:
  print(e)
except TypeError:
  print('Não foi possível calcular a média do estudante')
else: 
  print(resultado)
finally:
  print('Consulta encerrada')



# Testando os erros - 1 erro
try: 
  notas = [1, 5, 6, 7, 5]
  resultado = media(notas)
except ValueError as e:
  print(e)
except TypeError:
  print('Não foi possível calcular a média do estudante')
else: 
  print(resultado)
finally:
  print('Consulta encerrada')


# Testando os erros - 2 erro
try: 
  notas = [1, 5, 6, 7, 'a']
  resultado = media(notas)
except ValueError as e:
  print(e)
except TypeError:
  print('Não foi possível calcular a média do estudante')
else: 
  print(resultado)
finally:
  print('Consulta encerrada')


