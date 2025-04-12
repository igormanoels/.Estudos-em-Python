'''
8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números 
inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código 
que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.
'''

doces = 0
amargos = 0
lista_id = []

for i in range(0,10):
    id = int(input('Informe o id do produto desejado: '))
    lista_id.append(id)
    if id % 2 == 0:
        doces+=1
    else:
        amargos+=1

print(f'\nQuantidade de doces: {doces}\nQuantidade de amargos: {amargos}')


