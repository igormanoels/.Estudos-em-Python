import os 
os.system('cls')

# Geradores são tipos especiais de iteradores, ao contrário das listas ou outro iteráveis, não armazenam todos os seus valores na memória.
def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros = [1,2,3,4,5,6,7,8,9,10]):
    print(i)
