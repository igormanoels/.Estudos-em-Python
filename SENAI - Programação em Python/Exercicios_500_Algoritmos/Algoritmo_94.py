import os

os.system('cls')
# Entrar com um número e imprimir uma das mensagens: é multiplo de 3 ou não é multiplo de 3.

num = int(input("Informe um número: "))

if (num % 3 == 0):
    print(f"\n{num} é múltiplo de 3.")
else:
    print(f"\n{num} não é múltiplo de 3.")
    
input("\n\nPressione o \"enter\" para encerrar...")
