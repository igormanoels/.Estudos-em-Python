# Aula 01 - Conhecendo a Linguagem de Programação Python

# COMANDOS
# Para acessar o modo interativo do Python pelo terminal basta chamar o comando "python"
# Para para sair do moto interativo basta usar o comando "exit()"
# Para executar um programa via terminar usar o comando "python -i nomeDoPrograma.py"
# O comando "dir()" mostra o escopo local, retornando a listra de métodos, podendo ser possivel fazer imports de bibliotecas como math
# O comando "dir(100)" mostra todo o conteúdo
# O comando "help()" faz a busca das informações sobre o os métodos que podem ser implementados
# O comando "help(100)" mostra todo o conteúdo


import os
os.system('cls')

# Variável, pode mudar. E não há palavras reservadas para que a variável seja constante
idade = 45 

# Por convensão, variáveis que devem ser consideradas constantes, devem ser escritas em caps
ESTADO = ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Rio Grande do Sul", "Pernambuco"]

print(ESTADO[0])

print(type(idade)) # Mostra a qual tipo de classe essa variável pertence

nome = "Igor"
sobrenome = "Manoel"

# Tipos de Print
print(nome, sobrenome)
print(nome, sobrenome, end=", Você é incrivél!\n")      # Mantém o resto do print na mesma linha
print(nome, sobrenome, sep="***")                       # Entre os espaços, inclui o separador de sua preferencia
print(f"Nome: {nome} {sobrenome}, seja bem vindo!")
      
print(float("a"))

