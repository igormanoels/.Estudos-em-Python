import os

os.system('cls')
# Entrar com a razão de uma PA e o valor do primeiro termo. Calcular imprimiro 10 termo da serie

razao = float(input("Favor informar qual a razão: "))
termo = float(input("Favor informar qual é o primeiro termo: "))
decTermo = (termo + (9 * razao))

print("O décimo termo é ", decTermo)

input("\n\nPressione o \"enter\" para encerrar...")
