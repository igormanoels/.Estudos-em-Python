import os

os.system('cls')
# Entrar com um número no formato CDU e imprimir invertido: UDC. (Exemplo: 123, sairá 321.)
# O número deverá ser armazenado em outra variável antes de ser impresso.

num = int(input("Favor informar o número desejado: "))
cent = num // 100
deze = (num // 10) % 10
unit = num % 10

print("Centena: ", cent, "\tDezena: ", deze, " \tUnidade: ", unit)
