import os
os.system('cls')


file = open('C:\\temp\\Escrevendo.txt', 'w', encoding='utf-8')

file.write("Tabuada do 2\n")

for i in range (1,11):
    file.write(f"2 x {i} = {2 * i}\n")

file.close()

print("\n\n##############################################\n")
