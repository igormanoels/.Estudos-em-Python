import os
os.system('cls')

numeros = [ 1,2,3,4,5,6,7,8,9,10]
total = 0

for i in numeros:
    total+=i

media = total / len(numeros)
print(f"Total: {total}\nMédia: {media}\n")
