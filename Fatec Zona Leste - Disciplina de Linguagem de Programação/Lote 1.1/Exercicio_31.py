import os
import math
os.system('cls')

# Calcule e mostre o quadrado dos números entre 10 e 150.

n = 10
while n <= 150:
    print(f"O quadrado de {n} é {(math.pow(n, 2)):.0f}")
    n+=1
