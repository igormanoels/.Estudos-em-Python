import os

os.system('cls')
# Criar um algoritmo que leia o valor de um depósito e o valor da taxa de juros.
# Calcular e imprimir o valor do rendimento e o valor total depois do rendimento.

depost = float(input("informe o valor do depósito: "))
taxa = float(input("Informe o valor da taxa: "))

rend = round((depost * (taxa / 100)), 2)
mont = round((depost + rend), 2)

print("\nRendimento.................R$ ", rend,
      "\nMontante...................R$ ", mont)
input("\n\nPressione o \"enter\" para encerrar...")
