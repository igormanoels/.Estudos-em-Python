'''
2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a 
escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

Tabuada do 7:
7 x 0 = 0
7 x 1 = 7
[...]
7 x 10 = 70

'''

def tabuada(num):
    print('Tabuada do ', num)
    for i in range(0,11,1):
        print(num, ' x ', i , ' = ', num*i)


n_tabuada = int(input('Informe o número da tabuada desejada: '))
tabuada(n_tabuada)


