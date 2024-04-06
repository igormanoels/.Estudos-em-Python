import os

os.system('cls')
'''
    Criar um algoritmo que leia um número que será o limite superior de um intervalo e 
    o incremento (incr) Imprimir todos os numeros naturais no intervalo de O ate esse 
    numero Suponha que os dois numeros lidos são maiores do que zero Exemplo 
        Limite superior 20              Saída. O 5 10 15,20, 
        Incremento: 5
'''

limSup = int(input("Informe o limite superior: "))
inc = int(input("Informe o intervalo de incremento: "))
num = 0

print("\nSequencia: ", end="")
while num < limSup:
    print(f"{num}", end="\t")
    num += inc
    

input("\n\nPressione o \"enter\" para encerrar...")
