import os 

os.system('cls')
'''
        ESTRUTURAS CONDICIONAIS
        
'''

dinheiro = 100

# Eu posso ou não fazer o uso do parentes na atribuição da sentença comparativa
if (dinheiro == 100):
    print("Comprar")
else: 
    print("Não comprar")

# Estrutura Condicional Escolha...Caso
op = 1

match op:
    case 1:
        print("Opção 1")
    case 2:
        print("Opção 2")
