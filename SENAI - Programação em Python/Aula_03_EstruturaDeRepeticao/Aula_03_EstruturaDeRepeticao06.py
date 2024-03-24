import os
import random

os.system('cls')
lista_palavras = ["BANANA", "CASA", "PANDEIRO", "JARDIM", "SENAI", "LOJA", 
                  "GARRAFA", "TORRE", "XADREZ", "PROGRAMA"] # lista
num = random.randint(1, 9)
palavra_secreta = lista_palavras[num]
quantLetras = len(palavra_secreta)
#Teste da palavra -----> 
print(palavra_secreta, "\t" ,quantLetras)
palavra = [quantLetras] # Vetor vazio
acerto = 0
erros = 0
posicao = 0

while erros < 6 or acerto == quantLetras:
    posicao+=1
    print(palavra_secreta[posicao])
    palavra[posicao] = input("Digite a Letra desejada: ").upper()
    if palavra[posicao] == palavra_secreta[posicao]:
        print(f"Parabéns você acertou a letra {palavra[posicao]}\n")
        acerto +=1
        
    else:
        erros+=1
        print(f"{palavra[posicao]} ---> Letra errada.\n")

if palavra == palavra_secreta:     
    print(f"Parabéns você venceu! Palavra: {palavra}")
else:
    print(f"Infelizmente você perdeu, a palavra era {palavra_secreta}") 
