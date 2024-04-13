import os 

os.system('cls')

lista = []

num = int(input("Informe um número: "))
while num != 0:
    lista.append(num)
    num = int(input("Digite outro número, ou zero para encerrar: "))
    
print("Lista Final: ", lista)
