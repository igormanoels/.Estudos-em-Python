# TRABALHANDO COM ESTRUTURAS DE REPETIÇÃO

idade = int(input('Favor informar sua idade: '))
while idade <= 17 :
    print('Idade inválida!')
    idade = int(input('Favor informar sua idade: '))

contador = 0
while contador <= 5:
    print(contador)                 # Exibe cada valor de 0
    contador += 1                   # Operação de incremento

for i in range(5):
    print('contando' , i)

planets = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter']
for planeta in planets:
    print(planeta)                  # Exibe cada item do vetor 

for letra in 'Python':              # Exibe cada letra 
    print(letra)

capitais = {'Brasil': 'Brasília', 'EUA': 'Washington', 'França': 'Paris'}
for pais, capital in capitais.items():              
    print(f'A capital de {pais} é {capital}')       # Exibe todos os valores do dicinário

alunos = ''                                 # Variavél de entrada
lista = []                                  # Cria a lista que vai receber os nomes
while alunos != '0':                        # Condição para executar o loop enquanto alunos for diferente de 0
    if alunos:                              
        lista.append(alunos)                # Garante que houve um valor atribuido na variável para incluir na lista
    alunos = input('Informe o nome do aluno ou aperte 0 para encerrar: ')
print(lista)                                # Exibe a lista
print(lista[2])                             # Exibe apenas o indice desejado da lista

from time import sleep

countdown = [4, 3, 2, 1, 0]                 # variavel com uma lista de valores
for number in countdown:                    # repetição para cada numero dentro da varivel lista
    print(number)                           # exibe o valor da lista
    sleep(1)                                # insere uma interrupção de 1 segundo para cada repetição do looping

