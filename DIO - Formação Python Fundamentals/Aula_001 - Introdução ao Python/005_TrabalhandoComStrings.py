# Aula 01 - Conhecendo a Linguagem de Programação Python

import os
os.system('cls')

print("MÉTODOS DA CLASSE STRING")
curso = input("Digite uma palavra: ")
print(curso.upper())    # Transforma o texto em caixa alta
print(curso.lower())    # Tranforma o texto em caixa baixa
print(curso.title())    # Apenas a priemria letra em caixa alta
print(curso.strip())    # Remove os espaços
print(curso.lstrip())   # Remove os espaço da esquerda
print(curso.rstrip())   # Remove os espaços da direita
print(curso[0])         # Seleciona apenas a posição desejada
print(curso[:3])        # Seleciona a quantidade de posições desejada
print(curso[2:])        # A partir de um valor, até o final
print(curso[0:-1:2])    # Retorna de 2 em dois
print(curso[-1])        # Seleciona a última posição
print(curso[::-1], "\n\n")      # Inverte as strings

palavra = "Python"
print(palavra.center(100,"#"))      # Coloca o texto centralizado entre os caracteres que você desejar
print(".".join(palavra))            # Separa as letras da palavra com um simbolo ou espaços 
print(" ".join(palavra))

print("\n\nINTERPOLAÇÃO DE VARIÁVEIS")
# USANDO %
nome = "Igor"
idade = 28
# Usa %s para apontar para strings e %d para decimais e %f para valores de ponto flutuante, colocar em ordem!
print("Olá me chamo %s e tenho %d anos." % (nome, idade)) 

# USANDO FORMAT
nome = "Igor"
idade = 28
# Indica as posições onde as variaveis vão ficar com chaves, e substitui segundo a ordem 
print("Olá me chamo {} e tenho {} anos.".format(nome, idade)) 

# Também é possivel indicar usando o indice das palavras
ESTADO = "São Paulo" 
print("Olá tenho {1} anos e me chamo {0}.".format(nome, idade))     
print("Olá tenho {1} anos e me chamo {0}.".format(nome, idade))     # É LEGAL PARA REAPROVEITAR A VARIAVEL 
print("Olá eu moro em {2}, tenho {1} anos e me chamo {0}. Aqui em {2} tudo é muito corrido.".format(nome, idade, ESTADO))

print(f"Olá me chamo {nome} e tenho {idade} anos.")

saldo = 2451.457789
print(f"Saldo: {saldo:.2f}")        # Formata a quantidade de casas decimais
print(f"Saldo: {saldo:10.2f}")      # Coloca espaços em branco antes da variavel

# IMPRIMINDO DADOS DA LISTA, basta passar o valor da chaves da lista dentro do print
dados = {"nome": "Igor Manoel", "idade": 28}
print("Nome: {nome} - Idade: {idade}".format(**dados))


mensagem = f"""
 Olá eu me chamo {nome}, 
e estou estudando estudando Python.
    Essa opção é boa para criar um menu já formatado
"""
print(mensagem)



