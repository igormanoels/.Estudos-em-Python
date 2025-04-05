if 2 < 7:
    print('é menor')


####################################################


if 2 > 7:
    print('é menor')
else:
    print('não é menor')


####################################################


media = float(input('Digite a média: '))
if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')


####################################################


media = float(input('Digite a média: '))
if media >= 6.0:
  print('Aprovado')
else:
  if media >= 4.0:
    print('Exame')
  else:
    print('Reprovado')


####################################################


media = float(input('Digite a média: '))
if media >= 6.0:
  print('Aprovado')
elif media >= 4.0:
  print('Exame')
else:
  print('Reprovado')


####################################################
''' OPERADORES LÓGICOS 
    AND     -   ambas condições precisam ser verdadeiras
    OR      -   apenas um condição precisa ser verdadeira
    NOT     -   inverte a condição
'''
t1 = t2 = True
f1 = f2 = False

if t1 and t2:
  print('expressão verdadeira')
else:
  print('expressão falsa')

if t1 and f1:
  print('expressão verdadeira')
else:
  print('expressão falsa')


if t1 or f1:
  print('expressão verdadeira')
else:
  print('expressão falsa')

if f1 or f2:
  print('expressão verdadeira')
else:
  print('expressão falsa')


if not f1:
  print('expressão verdadeira')
else:
  print('expressão falsa')


####################################################
'''
    IN  -   Verifica se um valor está presente e retorna um valor boleano
'''
lista = 'José da Silva, Maria Oliveira, Pedro Martins, Ana Souza, Carlos Rodrigues, Juliana Santos, Bruno Gomes, Beatriz Costa, Felipe Almeida, Mariana Fernandes, João Pinto, Luísa Nascimento, Gabriel Souza, Manuela Santos, Thiago Oliveira, Sofia Ferreira, Rafael Albuquerque, Isabella Gomes, Bruno Costa, Maria Martins, Rafaela Souza, Matheus Fernandes, Luísa Almeida, Beatriz Pinto, Mariana Rodrigues, Gabriel Nascimento, João Ferreira, Maria Albuquerque, Felipe Oliveira'

nome_1 = 'Mariana Rodrigues'
nome_2 = 'Marcelo Nogueira'

if nome_1 in lista:
  print(f'O nome {nome_1} está presente na lista')
else:
  print(f'O nome {nome_1} não está presente na lista')

if nome_2 in lista:
  print(f'O nome {nome_2} está presente na lista')
else:
  print(f'O nome {nome_2} não está presente na lista')


  