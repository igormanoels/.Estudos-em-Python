import os
os.system('cls')

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

pares = lista[0::2] # Separa o vetor por posição, 
impares = lista[1::2]

for i in pares:
    print(i, end=" ")

print("\n")

for i in impares:
    print(i, end=" ")

print("\n")

tresUltimos = lista[-3:]
for i in tresUltimos:
    print(i, end=" ")

print("\n")

PrimeirosEUltimos = lista[:2] + lista[-2:]
for i in PrimeirosEUltimos:
    print(i, end=" ")
    
print("\n")

