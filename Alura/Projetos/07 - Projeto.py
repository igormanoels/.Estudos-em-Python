'''
8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa 
que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], 
[26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.
'''
faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0

entrada = 0

while(entrada >= 0):
    entrada = int(input('Informe a idade do pensionista: '))

    if(entrada <= 25):
        faixa1 += 1
    elif(entrada <= 50):
        faixa2 += 1
    elif(entrada <= 75):
        faixa3 += 1
    else:
        faixa4 += 1

print(f'Faixa1 = {faixa1}\nFaixa2 = {faixa2}\nFaixa3 = {faixa3}\nFaixa4 = {faixa4}')

