import os

os.system('cls')
'''
    Criar um algoritmo que verifique a(s) letra(s) central(is) de uma palavra Se o numero de caracteres for ímpar, 
    ele verifica se a letra central é uma vogal; caso contrario verifica se e um dos digrafos rr ou ss 
    (só precisa, testar letras minusculas) 
'''

p = input("Informe uma palavra para análise: ").lower()

qLetras = len(p)

c = round(qLetras / 2)

if qLetras % 2 == 0:
    if p[c] == "ss" and p[c-1] == "ss" or p[c] == "rr" and p[c-1] == "rr":
        print("No centro da palavra tem rr ou ss.")
    else:
        print("No centro da palavra não tem rr ou ss.")
else:
    if p[c] == "a" or p[c] == "e" or p[c] == "i" or p[c] == "o" or p[c] == "u":
        print("No centro da palavra tem uma vogal.")
    else:
        print("No centro da palavra não tem um vogal.")

input("\n\nPressione o \"enter\" para encerrar...")
