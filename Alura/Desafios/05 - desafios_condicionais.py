# 1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe um número inteiro: '))

if num1 > num2:
    print(f'O maior número é {num1}')
else:
    print(f'O maior número é {num2}')


''' 
2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve 
um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
'''
porcentagem = int(input('Informe a porcentagem de produção: '))

if porcentagem == 0:
    print('Não houve crescimento!')
elif porcentagem > 0:
    print(f'Houve um crescimento de {porcentagem}%')
else:
    print(f'Houve um decrescimento de {porcentagem}%')


# 3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
letra = input('Informe a letra desejada: ')
vogais = 'a, e, i, o, u'

if letra in vogais:
    print('A letra informada é uma vogal')
else:
    print('A letra informada não é uma vogal')


'''
4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba
o valor mais alto e mais baixo entre esses três anos.
'''
preco1 = float(input('Informe o primeiro valor do carro: '))
preco2 = float(input('Informe o segundo valor do carro: '))
preco3 = float(input('Informe o terceiro valor do carro: '))

lista = preco1, preco2, preco3
menor_valor = min(lista)
maior_valor = max(lista)

print(f'O menor valor é {menor_valor} e o maior valor é {maior_valor}')


# 5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
produto1 = float(input('Informe o primeiro valor do produto: '))
produto2 = float(input('Informe o segundo valor do produto: '))
produto3 = float(input('Informe o terceiro valor do produto: '))

lista = produto1, produto2, produto3

print(f'O menor valor é {min(lista)}')


# 6) Escreva um programa que leia três números e os exiba em ordem decrescente.
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

lista = num1, num2, num3

print(f'Lista ordenada: {sorted(lista)}')


'''
# 7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem 
# "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
'''
turno = input('Informe em qual turno você estuda: ')

if turno == 'manhã' or turno == 'Manhã' or turno == 'manha' or turno == 'Manha' or turno == 'diurno' or turno == 'diurno':
    print('Bom dia!')
elif turno == 'tarde' or turno == 'Tarde' or turno == 'vespertino' or turno == 'Vespertino':
    print('Boa tarde!')
elif turno == 'noite' or turno == 'Noite' or turno == 'Noturno' or turno == 'noturno':
    print('Boa noite!')
else: 
    print('Valor inválido')

'''
8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. 
Dica: Você pode utilizar o operador módulo %.
'''
numero = float(input('Informe o númerom desejado: '))

if numero % 2 != 0:
    print('O número é impar')
else:
    print('O número é par')

    
# 9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
numero = float(input('Informe o númerom desejado: '))

if numero % 1 != 0:
    print('O número é decimal')
else:
    print('O número é inteiro')


