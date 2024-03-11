import math
import os

os.system('cls')
# Entrar com o número e a base em que se deseja calcular o logaritmo desse número e imprimi-lo.

log = int(input("Favor informar o número para cálcular o logaritmo: "))
base = int(input("Favor informar a base do cálculo: "))

logNbase = math.log(log, base)
print("Log ", log, " na base ", logNbase)
