import os 

os.system('cls')
'''
    Criar um algoritmo que entre com dez mensagens, e, para cada mensagem, 
    imprimir quantas letras A tem (considerar maiúsculas e minúsculas). 
'''

for i in range(10):
    c = 0
    msg = input("Digite o texto desejado: ")
    quant = len(msg)
    for j in range(quant):
        if msg[j] == "a" or msg[j] == "A":
            c += 1
    print(f"{msg}\nQuant. Letras 'A': {c}\n")

input("\n\nPressione o \"enter\" para encerrar...")
