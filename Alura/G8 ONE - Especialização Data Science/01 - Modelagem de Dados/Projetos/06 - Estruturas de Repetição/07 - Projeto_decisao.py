'''
7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, 
por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um 
programa que peça um número inteiro e determine se ele é ou não um número primo.
'''

num = int(input('Informe um número inteiro: '))

if (num == 2 or num == 3 or num == 5 or num == 7):
    print('O número informado é primo')
elif num > 10:
    if (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0):
        print('O número informado não é primo')
    else:
        print('O número informado é primo')
else: 
    print('O número informado não é primo')