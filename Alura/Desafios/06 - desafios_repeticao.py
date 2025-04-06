# 1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num1 +=1
for cont in range(num1, num2):
    print(cont, end=' ')



'''
2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar 
ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. 
Considere que a colônia A inicia com 4 elementos e a B com 10.
'''
colonia_a = 4
colonia_b = 10
dias = 0

while(colonia_a <= colonia_b):
    colonia_a *= 1.03
    colonia_b *= 1.015
    dias += 1

print(f'Levou {dias} dias para que a \'colonia A\' supera-se a \'colonia B\'')



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



'''
4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média
delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.
'''
temperaturas = []
temp = 0

while(temp != -273):
    temp = float(input('Informe a temperatura desejada: '))
    temperaturas.append(temp)

qtd = 0
media = 0

for i in temperaturas:
    media += i
    qtd += 1

media /= qtd
print('Média de temperatura: ', media)



'''
5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando 
que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o 
número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.'
'''

fat = int(input('Informe um número para cálcular seu fatorial: '))
res = 1

while(fat != 0):
    res *= fat 
    fat -= 1

print('O fatorial é', res)

