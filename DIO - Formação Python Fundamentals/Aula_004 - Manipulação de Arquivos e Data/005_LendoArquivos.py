import os
os.system('cls')
''' 
    Modo de abertura deve ser escolhido conforme a operação
    - 'r' leitura
    - 'w' gravação
    - 'a' anexar
'''

file = open('C:\\temp\\documentos.txt', 'r', encoding='utf-8') # encoding é o formato do tipo de escrita do arquivo
print(file.read()) # Lê todo conteudo como string única. 

file.close()

print("##############################################\n")
"""# Caso o arquivo esteja na pasta raiz do projeto, basta charmar o nome do arquivo
file = open('documentos.txt', 'r', encoding='utf-8')

print(file.read())

file.close()"""

############################################################################################################################

file = open('C:\\temp\\documentos.txt', 'r', encoding='utf-8')

print(file.readline()) # Lendo por linha
file.close()

print("##############################################\n")

############################################################################################################################


file = open('C:\\temp\\documentos.txt', 'r', encoding='utf-8')
for linha in file:
    print(linha, end="")  # Lendo por linha

file.close()

print("\n\n##############################################\n")

############################################################################################################################
# readlines() Lê retorna uma lista, onde cada elemento é uma linha do arquivo

file = open('C:\\temp\\documentos.txt', 'r', encoding='utf-8')
for linha in file.readlines():
    print(linha, end="")  # Lendo por linhas

file.close()

print("\n\n##############################################\n")

############################################################################################################################

file = open('C:\\temp\\documentos.txt', 'r', encoding='utf-8')
arquivo = file.readlines() # Lendo por linhas, com retorno em lista de elementos
print(arquivo)

file.close()

print("\n\n##############################################\n")

############################################################################################################################

file = open('C:\\temp\\documentos.txt', 'r', encoding='utf-8')
while len(linha := file.readline()): # Lendo por linhas, verifica a quantidade de linhas, e vai lendo uma a uma
    print(linha)

file.close()

print("\n\n##############################################\n")


