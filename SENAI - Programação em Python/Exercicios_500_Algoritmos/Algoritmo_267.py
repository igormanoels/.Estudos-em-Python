import os
os.system('cls')
'''
    Entrar com profissão de várias pessoas e imprimir quantos são dentistas 
    (considerar DENTISTA, dentista e Dentista). 
'''

quant = 0
print("Algoritmo que conta quantos dentistas estão listados")

while True:
    prof = input("Informe uma profissão, ou digite \"fim\" para encerrar: ").upper()
    if prof.__contains__("FIM"):
        print(f"A quantidade de Dentistas é de {quant}")
        print("Programa encerrado!")
        break
    else:
        if prof.__contains__("DENTISTA"):
            quant += 1

input("\n\nPressione o \"enter\" para encerrar...")
