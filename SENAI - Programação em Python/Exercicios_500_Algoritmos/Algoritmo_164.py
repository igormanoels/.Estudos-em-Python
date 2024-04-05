import os

os.system('cls')
'''
    Você já pensou em fazer várias tabu/ações usando a estrutura do para? 
'''
c = 1

for i in range(3):
    for j in range(3):
        if c == 1 or c == 9:
            print(f"{c}º zona", end="\t")
        else:
            print("\t", end="")
        c += 1           
    print("\n")
    
input("\n\nPressione o \"enter\" para encerrar...")
