import os
os.system('cls')

# Entrar com dois numeros inteiros e imprimir a seguinte saída:
div = int(input("Informe o dividendo: "))
divsr = int(input("Informe o divisor: "))

quociente = div // divsr
resto = div % divsr

print("Quociente: ", quociente, "\t Resto: ",resto)