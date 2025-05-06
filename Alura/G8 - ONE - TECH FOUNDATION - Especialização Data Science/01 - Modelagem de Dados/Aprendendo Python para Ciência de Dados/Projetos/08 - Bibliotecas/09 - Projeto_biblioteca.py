'''
9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando 
quais resultaram em um número inteiro. A lista é a seguinte:

No final, informe quais números possuem raízes inteiras e seus respectivos valores.

1.5 é inteiro? : False
2 é inteiro? : True
'''
from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]

raiz_numeros = []

for n in numeros:
    n = round(sqrt(n), 2)
    print(f'{n} é inteiro? :', n // 1 == n)


