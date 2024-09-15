import os
os.system('cls')

''' 
Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará 
esse alimento sabendo que a pessoa consome 50g ao dia.
'''

quantKg = float(input("Informe a quantidade de quilos de alimento: "))

dias = int((quantKg * 1000) / 50)

print("A quantidade de dias é de", dias)
