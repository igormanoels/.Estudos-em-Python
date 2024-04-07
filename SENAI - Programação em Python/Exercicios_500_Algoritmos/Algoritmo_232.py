import os

os.system('cls')
'''
    Soma os número das entradas enquanto o número não for zero, 
    quando for zero encerre as entradas
'''
res = 0
c = 1

print("Digite zero para encerrar!")
while True:
    num = int(input(f"Informe o {c}º número: "))
    if num == 0:
        break
    else:
        res += num
    c += 1

print("Somatória: ", res)

input("\n\nPressione o \"enter\" para encerrar...")
