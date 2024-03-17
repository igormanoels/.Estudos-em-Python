import os

os.system('cls')
# Entrar com um número e imprimir uma das mensagens: maior do que 20, igual a 20 ou menor do que 20.

num = int(input("Informe um número: "))

if num == 20:
    print(f"\nO {num} é igual a 20.")
else: 
    if num > 20:
        print(f"\nO {num} é maior que 20.")
    else:
        print(f"\nO {num} é menor que 20.")

input("\n\nPressione o \"enter\" para encerrar...")
