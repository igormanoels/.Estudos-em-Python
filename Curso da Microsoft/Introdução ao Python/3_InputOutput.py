# TRABALHANDO COM ENTRADAS E SAÍDAS

nome = input('Favor informar seu nome: ')
print('Seja bem vindo' , nome)

# OUTRA FORMA
# Toda entrada é uma string, e é necessário fazer o casting, para que os dados não sejam concatenados

#Entrada com quebra de linha
print('Informe o primeiro valor: ')
num1 = int(input()) 

print('Informe o segundo valor: ')
num2 = int(input())

res = num1 + num2
print('Soma: ', res)

num1_emString = str(num1) # Converte o numero em uma string
print(type(num1_emString)) # Exibe o tipo da variável para confirmar que virou uma string


x = 2           # o valor de x é 2
x += 2          # realiza o incremento de 2 para o valor de x
x -= 1          # realiza o decremento de 1 para o valor de x
x /= 2          # realiza a divisão de x por 2
x *= 5          # realiza a multiplicação de x por 5

from datetime import date           # importa do sistema a data atual

date.today()                        # chama a data

print(date.today())                 # imprime a data

data = str(date.today)              # converte a data em string
print(type(data))                   # exibe a conversão

# Entrada sem quebra de linha
num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
res = num1 * num2
print('Produto = ' , res)