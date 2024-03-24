import os

os.system('cls')

c = 0
res = 0
tab = int(input("Informe um número para receber o valor da tabuada: "))

while c <= 10:
    res = tab * c
    print(f"{tab} x {c} = {res}")
    c+=1