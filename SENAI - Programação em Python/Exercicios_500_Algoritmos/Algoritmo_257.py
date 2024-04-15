import os 
import math

os.system('cls')
'''
    Criar um algoritmo que leia o valor de N imprima a sequência a seguire o resultado 
    Exemplo N - 4 
        4!/0! - 3!/4! + 2!/16! - 1!/36! + 0!/64! 
        SOMA 23.75
'''
# Função cálcula fatorial
def fatorial (f):
    if f == 0 or f == 1:
        return 1
    else: 
        return f * fatorial(f-1)

def divisor (c):
        return fatorial(math.pow(c, 2)) 
    
def serie (n):
    c = 0
    res = 0
    for i in range(n):
        if i % 2 == 0:
            res += (fatorial(n-i) / (divisor(c)))
        else:
            res -= (fatorial(n-i) / (divisor(c)))
        c += 2
    return res

n = int(input("Informe o N dá serie: "))
resSerie = serie(n)
print(f"Resultado da Série: {resSerie}")

input("\n\nPressione o \"enter\" para encerrar...")
