import os

os.system
'''
    Sabendo-se que a UAL calcula o produto através de somas sucessivas, 
    criar um algoritmo que calcule o produto de dois números inteiros 
    lidos. Suponha que os números lidos sejam positivos e que o 
    multiplicando seja menor do que o multiplicador. 
'''

num = int(input("Informe o número desejado: "))
multp = int(input("Informe por quanto você quer múltiplicar: "))
res = 0 

for i in range(multp):
    res += num

print(f"{num} x {multp} = {res}")

input("\n\nPressione o \"enter\" para encerrar...")
