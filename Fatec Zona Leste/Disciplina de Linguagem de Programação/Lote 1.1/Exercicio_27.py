import os
os.system('cls')

'''
Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). 
Calcule e mostre a velocidade média em km/h.
'''

circuito = float(input("Informe a distancia em metros: "))
tempo = int(input("Informe o tempo em minutos: "))

velocidade = (circuito / 1000) / (tempo / 60)
print(f"Velocidade média {velocidade:.2f} km/h")
