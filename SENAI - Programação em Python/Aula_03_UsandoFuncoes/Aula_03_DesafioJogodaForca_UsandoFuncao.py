import os
import random

os.system('cls')

print("Seja bem vindo ao meu jogo da forca 2.0"
      "\nVocê terá 6 erros no máximo, boa sorte e bom jogo!")

def SortearPalavra():
    vetPalavras = ["Casa", "Gato", "Cachorro", "Rato", "Amigo", "Livro", "Mesa", "Porta", "Cadeira", "Pato", "Banana",
                   "Rua", "Computador", "Caneta", "Teclado", "Janela", "Caderno", "Camisa", "Sapato", "Lanche", "Praia",
                   "Sol", "Lua", "Noite", "Dia", "Torre", "Quadro", "Escola", "Professor", "Estudante", "Parque",
                   "Bola", "Brinquedo", "Carro", "Asa", "Trem", "Pneu", "Navio", "Bicicleta", "Corrida", "Piscina",
                   "Nadar", "Correr", "Jogar", "Ler", "Escrever", "Desenhar", "Pintar", "Cozinhar", "Comer"]
    n = random.randint(0, 49)
    return vetPalavras[n].upper()

def JogoDaForca(forca):
    erros = 0
    acertos = 0
    posicao = 0
    letras = len(forca)
    letras_Usadas = []
    palavra = list(forca)  # Converte a palavra para uma lista para manipulação
    jogada = 1

    while (erros < 6 and acertos < letras):
        print(f"\nAcertos: {acertos} \nErros: {erros}")
        print("Palavra: ", end="")
        for letra in palavra:
            if letra in letras_Usadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print("\n")
        palpite = input(f"\nFaça sua {jogada}ª jogada, digite uma letra: ").upper()

        if palpite in letras_Usadas:
            print("Essa letra já foi usada.")
            jogada += 1
            continue
        elif palpite in forca:
            cont = 0
            while cont < letras:
                if forca[cont] == palpite:
                    palavra[cont] = palpite  # Atualiza a palavra com a letra correta
                    acertos += 1
                cont += 1
        else:
            print("Errou!")
            erros += 1
        jogada += 1

        letras_Usadas.append(palpite)

    if (acertos == letras):
        print(f"\nParabéns! Você venceu, a palavra era {forca}")
    else:
        print(f"\nInfelizmente você perdeu! A palavra era {forca}")


PalavraDaSorte = SortearPalavra()
print("\nPalavra Sorteada: ", end="")
for i in PalavraDaSorte:
    print(end="_ ") # Força que o print seja executado na mesma linha

JogoDaForca(PalavraDaSorte)

input("\n\nPressione o \"enter\" para encerrar...")
