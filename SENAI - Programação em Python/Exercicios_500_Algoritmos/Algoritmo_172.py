import os

os.system('cls')
'''
    Matriz: 0 a 9
'''

print("Matriz 10 x 10: ")

for i in range(10):
    for j in range(10):
        print(f"{i}-{j}", end="\t")
    print("\n", end="")
    
input("\n\nPressione o \"enter\" para encerrar...")
