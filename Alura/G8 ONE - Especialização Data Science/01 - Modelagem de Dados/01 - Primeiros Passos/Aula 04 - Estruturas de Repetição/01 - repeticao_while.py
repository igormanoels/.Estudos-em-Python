########################################################
# Entendendo o while

i = 1
while i <= 10:
    print(i)
    i+=1


########################################################
# Utilizando com operações
i = 0

while i < 3:
    nota_1 = float(input('Digite a 1° nota: '))
    nota_2 = float(input('Digite a 2° nota: '))

    print(f'Média: {(nota_1+nota_2)/2}')
    i+=1

