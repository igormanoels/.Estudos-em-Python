import os

os.system('cls')
'''
    Criar um algoritmo que leia os limites inferior e superior de um intervalo e o 
    número cujos múltiplos se deseja que sejam impressos no intervalo aberto. Suponha 
    que os dados digitados sãopara um intervalo crescente. Exemplo: 
        Limite inferior: 3      Saída: 6 9 
        Limite superior: 12 
        Número: 3
'''

limInf = int(input("Informe o limite inferior: "))
limSup = int(input("Informe o limite superior: "))
mult = int(input("Informe o múltiplo: "))

print("Sequência: ", end="")
while limInf <= limSup:
    if limInf % mult == 0:
        print(f"{limInf}", end=" ")
    limInf += 1

input("\n\nPressione o \"enter\" para encerrar...")
        