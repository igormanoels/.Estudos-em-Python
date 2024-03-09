"""
TRABALHANDO COM TIPOS DE VARIÁVEIS
O Python possui uma tipagem dinâmina, ou seja as variáveis serão tipadas de acordo 
com o valor que ela carrega naquele momento.
"""

# VARIAVEIS PRIMITIVAS
idade = 25              # idade recebe um valor inteiro
altura = 1.75           # altura recebe um valor float
nome = "João"           # nome recebe uma string 
esta_chovendo = True    # e aqui o valor é um boolean

# LISTAS: São coleções de dados mutáveis, podem ser acessados e alterados conforme necessário
numeros = [1, 2, 3, 4, 5]

# TUPLAS: São coleções de dados imutáveis, ele podem ser acessados porém não alterados 
coordenadas = (10, 20)

# DICIONÁRIOS: São coleções de dados não ordenadas, ou seja você atribiu uma variável e um valor em seguida
pessoa = {"nome": "Maria", "idade": 30}

# CONJUNTOS: São coleções de dados não ordenadas e sem elementos duplicados, nele você pode adcionar e remover elementos
conjunto_numeros = {1, 2, 3, 4, 5}

# NONETYPE: É um tipo especial, representa a falta de valor. Por exemplo a variável vazia ou com uma função sem retorno
valor_nulo = None



print(type(altura))  # Isso vai imprimir a classe a qual o valor da variavél pertence