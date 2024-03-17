import os

os.system('cls')
# Entrar com um número e informar se ele é divisível por 3 e por 7.

num = int(input("Informe um número: "))

if (num % 3 == 0 and num % 7 == 0):
    print(f"\n{num} é múltiplo de 3 e 7.")
else:
    print(f"\n{num} não é múltiplo de 3 e 7.")
    
input("\n\nPressione o \"enter\" para encerrar...")
