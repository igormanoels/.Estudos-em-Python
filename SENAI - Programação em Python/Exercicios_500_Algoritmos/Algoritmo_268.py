import os
os.system('cls')
'''
    Entrar com sexo de várias pessoas e imprimir quantas pessoas são do sexo masculino (considerar m ou M).
'''

quant = 0
print("Algoritmo que conta quantos homens foram entrevistados.")

while True:
    gen = input("Informe com qual genero você se identifica, ou fim para encerrar: ").upper()
    if gen.__contains__("FIM"):
        print(f"Quantidade de pessoas do genero masculino é {quant}")
        print("Programa encerrado")
        break
    else:
        if gen[0].__contains__("M"):
            quant += 1

input("\n\nPressione o \"enter\" para encerrar...")
