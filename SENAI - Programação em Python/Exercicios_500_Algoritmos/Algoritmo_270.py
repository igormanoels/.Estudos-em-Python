import os
os.system('cls')
'''
    Ler vários numeros ate entrar o numero -999. Para cada numero imprimir seus divisores. 
'''

while True: 
    i = 1
    num = int(input("Informe o número desejado ou -999 para encerrar: "))
    if num == -999: break
    while i <= 10:
        if num % i == 0:
            print(f"{num} é divisivel por {i}")
        i += 1
        
input("\n\nPressione o \"enter\" para encerrar...")
     