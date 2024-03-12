import os

os.system('cls')
'''
    Criar um algoritmo que leia o peso de uma pessoa, só a parte inteira, calcular e imprimir: 
    - O peso da pessoa em gramas 
    - Novo peso em gramas se a pessoa engordar 12% 
'''

peso = float(input("Informe seu peso: "))
pEmGramas = round(peso * 1000)
casoEngorde = round((peso * 1.12), 2)

print("\nPeso em Gramas: ", pEmGramas,
      "\nCaso Engorde: ", casoEngorde)
input("\n\nPressione o \"enter\" para encerrar...")
