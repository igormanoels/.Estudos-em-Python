import os

os.system('cls')
''' Antes de o racionamento de energia ser decretado, quase ninguém falava em quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário.
    Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo, fazer um algoritmo que receba o valor do salário mínimo e a
    quantidade de quilowatts gasta por uma residência e calcule. Imprima:
        - o valor em reais de cada quilowatt
        - o valor em reais a ser pago
        - o novo valor a ser pago por essa residência com um desconto de 10%.
'''

#Valor do saláriol mínimo 2014 - R% 1412,00
salMin = float(input("Favor informar o valor do Salário Mínimo: "))
qwt = (salMin / 7) / 100
quantQwt = float(input("Favor informar a quantidade de Quilowatts foi gasta no mês: "))

valorPg = qwt * quantQwt
valorPgDesc = valorPg * 0.9

pgmtFormat = "{:.2f}".format(valorPg)
pgmtDescFormat = "{:.2f}".format(valorPgDesc)

print("\nValor a pagar: R$", pgmtFormat, "\nValor a pagar com Desconto: R$", pgmtDescFormat)
