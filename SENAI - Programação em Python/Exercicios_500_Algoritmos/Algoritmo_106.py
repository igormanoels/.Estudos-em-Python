import os

os.system('cls')
# Entrar com um nome e imprimi-lo se o primeiro caractere for a letra A (considerar letra minúscula ou maiúscula).

nome = input("Informe seu nome: ").lower()

if nome[0].count("a"):
    print("O nome informado contém a \"letra A\" no início.")
else:
    print("O nome informado não contem a \"letra A\" no inicio.")

input("\n\nPressione o \"enter\" para encerrar...")
