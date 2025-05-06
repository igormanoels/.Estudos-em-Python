# 5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.

numeros_primos = [1, 2, 3, 5]

numero_limite = int(input('Informe um número: '))

for i in range(5, numero_limite):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        numeros_primos.append(i)


print(numeros_primos)

