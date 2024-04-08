import os

os.system('cls')
'''
    Num campeonato europeu de volleyball, se inscreveram 30 países. Sabendo-se que na lista 
    oficial de cada país consta, além de outros dados, peso e idade de 12 jogadores criar um
    algoritmo que apresente as seguintes informações 
        - o peso médio e a idade média de cada um dos times; 
        - o peso medio e a idade media de todos os participantes 
'''
paises = []
pesos = []
idades = []

for l in range(30):
    pais = input("Informe a qual país pertence a delegação a ser inserida: ")
    paises.append(pais)
    peso_time = []
    idade_time = []
    for c in range(12):
        peso = int(input("Informe o peso do atleta: "))
        peso_time.append(peso)
        idade = int(input("Informe a idade do atleta: "))
        idade_time.append(idade)
    pesos.append(peso_time)
    idades.append(idade_time)
    print("\n")

mediaPgeral = 0
mediaIdgeral = 0
for i in range(30):
    mediaP = sum(pesos[i]) / 12
    mediaId = sum(idades[i]) / 12
    print(f"{paises[i]} --> Média idade: {mediaId} --> Média peso: {mediaP}")
    mediaPgeral += mediaP
    mediaIdgeral += mediaId

mediaIdgeral /= 30
mediaPgeral /= 30

print(f"Peso médio dos participantes: {mediaPgeral}\nIdade média dos participantes: {mediaIdgeral}")

input("\n\nPressione o \"enter\" para encerrar...")    
