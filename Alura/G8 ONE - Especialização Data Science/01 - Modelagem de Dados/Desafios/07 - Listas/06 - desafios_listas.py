# 6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.

data = input('Informe a data desejada: ')

data = data.split('/')

dia = int(data[0])
mes = int(data[1])
ano = int(data[2])


if dia >= 1 and dia <= 31:
    if mes >= 1 and mes <= 12:
        if ano >= 1500 and ano <= 2050:
            print('Data válida')
        else:
            print('Data inválida')
    else:
        print('Data inválida')
else:
    print('Data inválida')


