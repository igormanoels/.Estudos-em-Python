import os 

os.system('cls')
'''
    Entrar com um nome e imprimi-lo se o primeiro caractere for a letra A (considerar
    letra minúscula ou maiúscula).
'''

nome = input("Digite seu nome: ")
preNome = nome.split(" ") [0]
print(f"Seu primeiro nome é {preNome}")

input("\n\nPressione o \"enter\" para encerrar...")
