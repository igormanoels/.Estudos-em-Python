# Listas vazia
minha_lista = []



# Lista de dados variados
lista_alunos = ['Igor', 2.4, 6.7, 4.8, False]
print(f'Nome: {lista_alunos[0]}\n')



# Percorrendo a lista
for i in lista_alunos:
    print(i)



# Alterando um valor da lista
lista_alunos[2] = 10
print('\n',lista_alunos,'\n')



# Quantidade de elementos em uma lista
print(len(lista_alunos),'\n')



# Método split para separa elementos
duvida = 'Quem veio antes? O ovo? Ou foi a serpente?'
lista_palavras = duvida.split('?')
print(lista_palavras,'\n')

duvida = 'Quem veio antes? O ovo? Ou foi a serpente?'
lista_palavras = duvida.split()
print(lista_palavras)



# Método join para unir elementos
misturas = ['Tintas: vermelho, azul e amarelo',
            'Verde: mistura de azul e amarelo',
            'Laranja: mistura de vermelho e amarelo',
            'Roxo: mistura de vermelho e azul']
unificador = '. '
string_misturas = unificador.join(misturas)
print(string_misturas,'\n')



# Separando elementos
dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(dados[3:7])   # informando o intervalo, sempre será -1, ou seja pegará até o 6
print(dados[2:])    # até o final da lista
print(dados[:4])    # até o último elemento informado -1
print(dados[:])     # todos os dados da lista



# Manipulando a lista
dados.append(11)    # Adciona um elemento ao final da lista

continuacao_dados = [12,13,14,15]   # Adciona uma coleção a outra
dados.extend(continuacao_dados)
print(dados)

dados.remove(5)     # Remove um elemento da lista
print(dados)



# Outras formas de manipular as listas
raca_caes = ['Labrador Retriever',
             'Bulldog Francês',
             'Pastor Alemão',
             'Poodle']

raca_caes.insert(1, 'Golden Retriever') # Insere o elemento na posição

raca_caes.pop(1)    # Remove o elemento da posição informada

raca_caes.index('Pastor Alemão')    # Retorna a posição do elemento informado

raca_caes.sort()    # Ordena os valores da lista


