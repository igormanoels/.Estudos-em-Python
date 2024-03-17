import os

os.system('cls')
# Entrar comum número e informar se ele é divisível por 10, por 5, por 2 ou se não é divisível por nenhum destes.

num = int(input("Informe o número desejado: "))

if (num % 10 == 0):
    print("\nO número informado é divisível por 10")
elif (num % 5 == 0):
    print("\nO número informado é divisível por 5")
elif (num % 2 == 0):
    print("\nO número informado é divisível por 2")
else: 
    print("O número informado não é divisível por nenhum dos números 2, 5 ou 10.")


input("\n\nPressione o \"enter\" para encerrar...")
 