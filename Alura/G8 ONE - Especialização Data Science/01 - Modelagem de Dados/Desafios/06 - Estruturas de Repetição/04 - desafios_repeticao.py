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

