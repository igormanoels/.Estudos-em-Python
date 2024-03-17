import os

os.system('cls')
'''
    Entrar com o ano de nascimento de uma pessoa e o ano atual. Imprimira idade da pessoa. 
    Não se esqueça de verificar se o ano de nascimento é um ano válido.
'''

anoNasc = int(input("Informe seu ano de Nascimento: "))
anoAtual = int(input("Informe o ano atual: "))

if anoNasc > anoAtual:
    print("O ano de Nascimento é inválido.")
else:
    idade = anoAtual - anoNasc
    print(f"Idade = {idade}")

input("\n\nPressione o \"enter\" para encerrar...")
