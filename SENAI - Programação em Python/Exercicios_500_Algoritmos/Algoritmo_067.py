import os

os.system('cls')
# Efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula:
# prestação = valor + (valor*(taxa/100)*tempo).

parcela = float(input("Informe o valor da parcela em atraso: R$ "))
taxa = float(input("Informe o valor da taxa: "))
tempo = int(input("Informe agora o tempo de atraso: "))

prest = round((parcela + (parcela * (taxa/100) * tempo)), 2)

print("\nPrestação: R$", prest)
input("\n\nPressione o \"enter\" para encerrar...")
