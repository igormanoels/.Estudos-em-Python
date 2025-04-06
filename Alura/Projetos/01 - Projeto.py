'''
10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual 
operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número 
- se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
'''

res = 0.0

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o primeiro número: '))

operacao = input('Informe a operação desejada, soma, subtracao, multiplicao e divisao: ')

if operacao == 'soma':
    res = num1 + num2
elif operacao == 'subtracao':
    res = num1 - num2
elif operacao == 'multiplicao':
    res = num1 * num2
elif operacao == 'divisao':
    res = num1 / num2
else:
    print('Opção inválida, aplicação finalizada')


if res % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')

if res > 0:
    print('O número é positivo')
else:
    print('O número é negativo')

if res % 1 != 0:
    print('O número é decimal')
else:
    print('O número é inteiro')

