# 3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
letra = input('Informe a letra desejada: ')
vogais = 'a, e, i, o, u'

if letra in vogais:
    print('A letra informada é uma vogal')
else:
    print('A letra informada não é uma vogal')


