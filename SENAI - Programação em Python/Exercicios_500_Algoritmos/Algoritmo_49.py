import os

os.system('cls')
''' Entrar com um nome e imprimir: 
        - Todo o nome: 
        - Primeiro caractere: 
        - Último caractere: 
        - Do primeiro ate o terceiro: 
        - Quarto caractere: 
        - Todos menos o primeiro: 
        - Os dois últimos:
'''

nomeCompleto = input("Favor informar seu Nome Completo: ")
primLetra = nomeCompleto[0]
ultLetra = nomeCompleto[-1]
umAoTerc = nomeCompleto[0:2]
quartaLetra = nomeCompleto[3]
tdMenosUm = nomeCompleto[1:]  # Não colocando um valor na posição ele retorna até a última letra
doisUlt = nomeCompleto[-2:]

print("\nNome Informado: ", nomeCompleto,
      "\nPrimeiro Letra: ", primLetra,
      "\nÚltimo Letra: ", ultLetra,
      "\nDo primeiro ate o terceiro: ", umAoTerc,
      "\nQuarto Letra: ", quartaLetra,
      "\nTodos menos o primeiro: ", tdMenosUm,
      "\nOs dois últimos: ", doisUlt)
