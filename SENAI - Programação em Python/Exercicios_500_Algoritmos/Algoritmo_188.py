import os

os.system('cls')
'''
    Criar um algoritmo que imprima uma tabela de conversão de polegadas para 
    centímetros. Deseja-se que na tabela conste valores desde 1 polegada até 
    20 polegadas inteiras. 
'''

pol = 1

while pol <= 20:
    cm = pol * 2.54
    print(f"{pol}' equivalem a {cm}cm(s)")
    pol += 1

input("\n\nPressione o \"enter\" para encerrar...")
