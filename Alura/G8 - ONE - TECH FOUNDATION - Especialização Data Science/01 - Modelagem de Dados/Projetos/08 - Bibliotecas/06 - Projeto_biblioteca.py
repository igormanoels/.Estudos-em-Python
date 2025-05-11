'''
6. Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. 
A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade 
de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para 
ela o número sorteado.

'''
from random import choice

numeros_sorteio = []


while(True):
    num = int(input('Informe um número para o sorteio, ou zero para encerrar: '))
    if(num != 0):
        numeros_sorteio.append(num)
    else:
        print('Inscrições para sorteio encerradas.')
        break

numero_vencedor = choice(numeros_sorteio)
print(f'O número vencedor é {numero_vencedor}')


