import os 
import math

os.system('cls')
'''
    Criar um algoritmo que leia o valor de N imprima a sequência a seguire o resultado 
    (N! / 0^2!) - ((N-1)! / (2^2)!) + ((N-2)! / (4^2)!) - ((N-3)! / (6^2)!) + ((0!) / (n^2)!)
'''
# Função cálcula fatorial
def fatorial (f):
    if f == 0 or f == 1:
        return 1
    else: 
        return f * fatorial(f-1)

# Falta válidar, erro na linha 29 passagem do parametro
def serie (n, c, r):
    if n == 0:
        return fatorial(n)
    else:
        if c % 2 == 0:
            return r + serie((fatorial(n-1)) / fatorial(math(c,2)))
        else: 
            return r - serie((fatorial(n-1)) / fatorial(math(c+2,2)))
        
c = 0
r = 0       
n = int(input("Informe o N dá serie: "))
resSerie = serie(n, c, r)
print(f"Resultado da Série: {resSerie}")

