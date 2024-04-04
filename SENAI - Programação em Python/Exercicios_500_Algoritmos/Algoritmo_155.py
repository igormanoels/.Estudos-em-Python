import os

os.system('cls')
'''
    Ler uma palavra e, se ela começar pela letra L ou D 
    (também deve ser considerado 1 ou d), formar uma nova 
    palavra que terá os dois primeiros caracteres e o último, 
    caso contrário a nova palavra será formada por todos os 
    caracteres menos o primeiro. 
'''

palavra = input("Informe a palavra desejada: ").lower()

if palavra[0] == "l" or palavra[0] == "d":
    palavra2 = palavra[0] + palavra[1] + palavra[-1]
    print(f"Nova palavra: {palavra2} ")
else: 
    palavra2 = palavra[1:]
    print(f"Nova palavra: {palavra2}")
    
input("\n\nPressione o \"enter\" para encerrar...")
