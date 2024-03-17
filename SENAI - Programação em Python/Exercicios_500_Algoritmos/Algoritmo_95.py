import os

os.system('cls')
# Entrar com um número e informar se ele é ou não divisível por 5.

num = int(input("Informe um número: "))

if (num % 5 == 0):
    print(f"\n{num} é múltiplo de 5.")
else:
    print(f"\n{num} não é múltiplo de 5.")
    
input("\n\nPressione o \"enter\" para encerrar...")
