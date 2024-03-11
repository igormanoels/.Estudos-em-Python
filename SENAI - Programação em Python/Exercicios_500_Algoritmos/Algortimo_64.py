import os

os.system('cls')
# Ler uma temperatura em graus centígrados e apresentá-la convertida em graus Fahrenheit

temp = float(input("Informe a temperatura: "))
fahr = ((9 * temp + 160) / 5)

print("Fahrenheit: ", fahr)
input("\n\nPressione o \"enter\" para encerrar...")
