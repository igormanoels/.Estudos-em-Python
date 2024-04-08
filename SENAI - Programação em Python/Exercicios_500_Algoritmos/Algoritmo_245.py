import os

os.system('cls')
'''
    Criar um algoritmo que receba a idade e o peso de 20 pessoas. Calcular e 
    imprimir as médias dos pesos das pessoas da mesma faixa etária. As faixas 
    etárias são: de 1 a 10 anos, de 11 a 20 anos, de 21 a 30 anos e maiores de
    30 anos. 
'''

faixa1 = 0
c1 = 0
faixa2 = 0
c2 = 0
faixa3 = 0
c3 = 0
faixa4 = 0
c4 = 0

for i in range(20):
    idade = int(input("\nInforme a idade: "))
    peso = float(input("Informe o peso: "))
    if idade <= 10:
        faixa1 += peso
        c1 += 1 
    elif idade <= 20:
        faixa2 += peso
        c2 += 1
    elif idade <= 30:
        faixa3 += peso
        c3 += 1
    else:
        faixa4 += peso
        c4 += 1

if c1 != 0:
    faixa1 = faixa1 / c1
if c2 != 0:
    faixa2 = faixa2 / c2
if c3 != 0:
    faixa3 = faixa3 / c3
if c4 != 0:
    faixa4 = faixa4 / c4    
        

print("\nMédia de peso da faixa 1 = ", faixa1, "\nMédia de peso da faixa 2 = ", faixa2,
      "\nMédia de peso da faixa 3 = ", faixa3, "\nMédia de peso da faixa 4 = ", faixa4)

input("\n\nPressione o \"enter\" para encerrar...")
