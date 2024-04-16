import os
import math

os.system('cls')
# Entrar com os valores dos catetos de um triângulo retângulo e imprimira hipotenusa

cat1 = float(input("Informe o valor do primeiro cateto: "))
cat2 = float(input("Informe o valor do segundo cateto: "))

hipo = math.sqrt((math.pow(cat1, 2)) + (math.pow(cat2,2)))
hipo = round(hipo, 2)
print("\nHitotenusa = ", hipo)

input("\n\nPressione o \"enter\" para encerrar...")
