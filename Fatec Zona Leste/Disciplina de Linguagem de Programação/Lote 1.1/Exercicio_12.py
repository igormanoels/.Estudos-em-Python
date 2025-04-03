import os
os.system('cls')

# Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.

anoAtual = int(input("Informe o ano atual: "))
anoNascimento = int(input("Informe o seu ano de nascimento: "))

idade = anoAtual - anoNascimento

print(f"Sua idade provavél é {idade}, em 17 anos vc terá {idade+17}")
