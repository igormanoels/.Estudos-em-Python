import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def limpar_terminal2():
    os.system('cls')


print(os.name)

# Exemplo de uso:
print("Mensagem antes de limpar...")
input("Pressione Enter para limpar a tela...")
limpar_terminal2()

