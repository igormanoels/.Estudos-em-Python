import math
import os

os.system('cls')
'''
    Uma pessoa resolveu fazer uma aplicação em uma poupança programada. 
    Para calcular seu rendimento, ela deverá fornecer o valor constante da aplicação mensal, a taxa e o número de meses. 
    Sabendo-se que a fórmula usada para este cálculo é:
'''

aplicacao = float(input("Informe o valor da Aplicação: "))
taxa = float(input("Informe o valor da Taxa: "))
tempo = int(input("Informe o tempo da Aplicação: "))

montante = round((aplicacao * (((math.pow(1+(taxa/100), tempo))-1) / (taxa/100))), 2)

print("Montante: R$ ", montante)
input("\n\nPressione o \"enter\" para encerrar...")
