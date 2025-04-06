########################################################
# Entendendo o for, ele ser para iterar sobre uma lista

conjunto = 'abcdefgh'

for elemento in conjunto:
    print(elemento)


# Outra forma de utilizar o for é como contador, porém sempre colocar um valor a mais sobre a iteração, pois ele vai até -1
for contador in range(1, 11, 1):
  print(contador)


for contador in range(1, 11, 2):
  print(contador)


# Aplicando o último exercicio
for contador in range(0, 3):
    nota_1 = float(input('Digite a 1° nota: '))
    nota_2 = float(input('Digite a 2° nota: '))

    print(f'Média: {(nota_1+nota_2)/2}')


# O continue pode ser utilizado para pular valores
for i in range(1,6):
    if i == 4:
        continue
    print(i)


# O break encerra a iteração
for i in range(1,6):
    if i == 4:
        break
    print(i)