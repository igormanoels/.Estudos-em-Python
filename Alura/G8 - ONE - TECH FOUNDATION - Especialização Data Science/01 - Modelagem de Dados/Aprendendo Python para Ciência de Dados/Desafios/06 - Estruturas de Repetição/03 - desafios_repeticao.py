'''
3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, 
precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 
de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, 
repita até que a pessoa usuária insira um valor válido.
'''
i = 0
notas = []

while(i < 15):
    nota = float(input('Informe a nota desejada: '))
    if nota >= 0 and nota <= 5:
        notas.append(nota)
        i+=1

print(notas)


