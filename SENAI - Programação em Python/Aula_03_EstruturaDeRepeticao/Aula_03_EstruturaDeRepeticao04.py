import os
import random

os.system('cls')

num_da_sorte = random.randint(1, 10)
palpite = 0
jogadas = 1

while palpite != num_da_sorte:
    palpite = int(input(f"{jogadas} jogadas. Informe qual o seu palpite: "))
    if palpite > num_da_sorte:
        print("O número informado é maior que o número da sorte.\n")
    elif palpite < num_da_sorte:
        print("O número informado é menor que o número da sorte.\n")
    jogadas += 1

print(f"Parabéns, você acertou! O número da sorte {palpite}\n\n")
