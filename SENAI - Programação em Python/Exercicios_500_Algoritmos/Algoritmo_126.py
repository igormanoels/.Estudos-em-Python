import os

os.system('cls')
# Ler um número e imprimir se ele é igual a 5, a 200, a 400, se está no intervalo entre 500 e 1000, 
# inclusive, ou se ele está fora dos escopos anteriores.

num = int(input("Informe o número desejado: "))

if num >= 500 and num <= 100:
    print("\nO número informado está dentro do intervalo.")
else:
    print("\nO número informado está fora do intervalo.")

if num == 5 or num == 200 or num == 400:
    print(f"E o número informado é igual a o número {num} do sistema.")
else:
    print("E o número informado mão é igual a nenhum dos números do sistema.")
    
input("\n\nPressione o \"enter\" para encerrar...")
