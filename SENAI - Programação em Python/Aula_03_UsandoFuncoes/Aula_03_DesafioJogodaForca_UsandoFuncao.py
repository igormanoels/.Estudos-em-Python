import os
import random
os.system('cls')

print("Seja bem vindo ao meu jogo da forca 2.0"
      "\nVocê tera 6 erros no máximo, boa sorte e bom jogo!")

def SortearPalavra(): # Método para gerar uma palavra chave para o jogo
    vetPalavras = ["Casa", "Gato", "Cachorro", "Rato", "Amigo", "Livro", "Mesa", "Porta", "Cadeira", "Pato", "Banana",
                   "Rua", "Computador", "Caneta", "Teclado", "Janela", "Caderno", "Camisa", "Sapato", "Lanche", "Praia",
                   "Sol", "Lua", "Noite", "Dia", "Torre", "Quadro", "Escola", "Professor", "Estudante", "Parque",
                   "Bola", "Brinquedo", "Carro", "Asa", "Trem", "Pneu", "Navio", "Bicicleta", "Corrida", "Piscina",
                   "Nadar", "Correr", "Jogar", "Ler", "Escrever", "Desenhar", "Pintar", "Cozinhar", "Comer"]
    n = random.randint(0, 49)
    return vetPalavras[n]

def JogoDaForca(forca):
    erros = 0
    acertos = 0
    posicao = 0
    letras = len(forca)
    palavra = []
    jogada = 1

    while (erros < 6 or acertos != letras):
        print(f"\nAcertos: {acertos} \nErros: {erros}")
        palpite = input(f"\nFaça sua {jogada}º jogada, digite uma letra: ").upper()
        if palpite == forca[posicao]:
            print("Acertou!")
            palavra.append(palpite)
            acertos += 1
            posicao += 1
        else:
            print("Errou!")
            erros += 1
        jogada += 1


PalavraDaSorte = SortearPalavra().upper()
print("\nPalavra Sorteada: ", end="")
for i in PalavraDaSorte:
    print(end="_ ") # Força que o print seja executado na mesma linha

JogoDaForca(PalavraDaSorte)


input("\n\nPressione o \"enter\" para encerrar...")
