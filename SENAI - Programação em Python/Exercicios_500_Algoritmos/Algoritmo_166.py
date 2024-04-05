import os

os.system('cls')
'''
    Matriz: ACIMA DA DIAGONAL PRINCIPAL 
'''

print("Matriz 10 x 10: ")
for i in range(10):
    for j in range(10):
        if i < j:
            print(f"{i+1}-{j+1}", end="\t")
        else:
            print("\t", end="")
    print("\n")

input("\n\nPressione o \"enter\" para encerrar...")
