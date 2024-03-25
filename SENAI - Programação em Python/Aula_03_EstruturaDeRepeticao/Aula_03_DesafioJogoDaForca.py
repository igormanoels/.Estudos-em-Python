import os
import random

os.system('cls')

lista_palavras = ["BANANA", "CASA", "PANDEIRO", "JARDIM", "SENAI", "LOJA", 
                  "GARRAFA", "TORRE", "XADREZ", "PROGRAMA"]# lista
num = random.randint(1, 9)
palavra_secreta = lista_palavras[num]
quantLetras = len(palavra_secreta)
#Teste da palavra -----> print(palavra_secreta, "\t", quantLetras)
palavra = [quantLetras] # Vetor vazio
acertos = 0
erros = 0
posicao = 0
print("Seja bem vindo ao meu jogo da forca!\nVocê tem no máximo 6 erros, bom jogo e boa sorte!")
while erros < 6: # or acerto < quantLetras:
    print(f"Erros: {erros} \nAcertos: {acertos} \nPalavra: {palavra}")
    letra = input("Digite a Letra desejada: ").upper()
    pLetra = palavra_secreta[posicao]
    if letra == pLetra:
        print(f"Parabéns você já acertou a letra {letra}\n")
        posicao += 1
        acertos += 1
        palavra.append(letra)
    else:
        erros += 1
        print(f"{palavra[posicao]} ---> Letra errada.\n")
    if acertos == quantLetras:
        break

if acertos == quantLetras:
    print(f"Parabéns você venceu! Palavra: {palavra_secreta}")
else:
    print(f"Infelizmente você perdeu, a palavra era {palavra_secreta}")
