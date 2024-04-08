import os

os.system('cls')
'''
    Entrar com uma mensagem e imprimir quantas letras A E / O e U tem esta 
    mensagem (considerar minúscula e maiúscula). 
'''

palavra = input("Informe a palavra desejada: ").lower()
quant = len(palavra)

la = 0
le = 0
li = 0
lo = 0
lu = 0

for i in range(quant):
    if palavra[i] == "a":
        la += 1
    elif palavra[i] == "e":
        le += 1
    elif palavra[i] == "i":
        li += 1
    elif palavra[i] == "o":
        lo += 1
    elif palavra[i] == "u":
        lu += 1

print(f"\nQuantidade de Letras A = {la}\nQuantidade de Letras E = {le}",
      f"\nQuantidade de Letras I = {li}\nQuantidade de Letras O = {lo}",
      f"\nQuantidade de Letras U = {lu}",)

input("\n\nPressione o \"enter\" para encerrar...")
