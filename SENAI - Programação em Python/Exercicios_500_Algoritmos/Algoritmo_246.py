import os

os.system('cls')
'''
    No dia da estréia do filme "Senhor dos Anéis" uma grande emissora de TV realizou uma 
    pesquisa logo após o encerramento do filme. Cada espectador respondeu a um questionário 
    no qual constava sua idade e a sua opinião em relação ao filme: 
    excelente -3; bom -2; regular- 1. 
    Criar um algoritmo que receba a idade e a opinião de 20 espectadores, calcule e imprima: 
        - A média das idades das pessoas que responderam excelente; 
        - A quantidade de pessoas que responderam regular; 
        - A percentagem de pessoas que responderam bom entre todos os expectadores analisados. 
'''
iexe = 0
exe = 0
ce = 0

ibom = 0
bom = 0
cb = 0

ireg = 0
reg = 0
cr = 0

for i in range(20):
    idade = int(input("Informe sua idade: "))
    voto = int(input("1-Excelente | 2-Bom | 3-Regular --- Vote: "))
    if voto == 1:
        iexe = idade
        exe += 1
        ce += 1
    elif voto == 2:
        ibom = idade
        bom += 1
        cb += 1
    elif voto == 3:
        ireg = idade
        reg += 1
        cr += 1
    print("\n")

if ce != 0:
    miExe = iexe / ce
if cb != 0:
    miBom = ibom / cb
if cr != 0:
    miReg = ireg / cr

print(f"Votos Exelente: {exe} - Média idade: {miExe}")
print(f"Votos Bom: {bom} - Média idade: {miBom}")
print(f"Votos Regular: {reg} - Média idade: {miReg}")

input("\n\nPressione o \"enter\" para encerrar...")
