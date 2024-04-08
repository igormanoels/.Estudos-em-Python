import os

os.system('cls')
'''
    Imprimir todas as tabuadas de multiplicar de 1 até 10. 
'''

for i in range(1,11):
    print(f"Tabuada do {i}.")
    for j in range(1,11):
        res = i * j
        print(f"{i} x {j} = {res}")
    print("\n")    
        
input("\n\nPressione o \"enter\" para encerrar...")
