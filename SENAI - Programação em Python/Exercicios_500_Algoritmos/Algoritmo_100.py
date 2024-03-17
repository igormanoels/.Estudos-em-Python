import os

os.system('cls')
# Ler um número inteiro de 4 casas e imprimir se é ou não múltiplo de quatro o número formado pelos 
# algarismos que estão nas casas das unidades de milhar e das centenas.

num = int(input("Informe um número que seja maior ou igual a 1000: "))

casasMC = num // 100

if casasMC % 4 == 0: 
    print("\nA casa de \"milhar e centena\" é divisível por 4.")
else: 
    print("\nA casa de \"milhar e centena\" não é divisível por 4.")


input("\n\nPressione o \"enter\" para encerrar...")
