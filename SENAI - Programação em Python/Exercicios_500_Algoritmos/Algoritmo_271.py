import os
os.system('cls')
'''
    Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% 
    ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% 
    ao ano calcular e imprimir o tempo necessario para que a população do pais A 
    ultrapasse a população do pais B
'''
paisA = 5000000
paisB = 7000000
anos = 0

while True: 
    anos += 1
    paisA *= 1.03
    paisB *= 1.02
    if paisA > paisB: break


print(f"Levou {anos} anos, para a população do pais A passar a população do pais B.")

input("\n\nPressione o \"enter\" para encerrar...")
