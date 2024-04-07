import os

os.system('cls')
'''
    Criar um algoritmo que leia os limites inferior e superior de um intervalo e 
    imprima todos os números pares no intervalo aberto e seu somatório. Suponha que os 
    dados digitados são para um intervalo crescente. Exemplo: 
        Limite inferior: 3          Saída: 4 6 8 10 
        Limite superior: 12         Soma: 28 
        Número: 3 
'''

limInf = int(input("Informe qual o limite inferior: "))
limSub = int(input("Informe qual o limite superior: "))

soma = 0

print("Sequência: ", end="")
while limInf <= limSub:
    if limInf % 2 == 0:
        print(f"{limInf}", end=" ")
        soma += limInf
    limInf += 1
    
print(f"Somatória: {soma}")

input("\n\nPressione o \"enter\" para encerrar...")
