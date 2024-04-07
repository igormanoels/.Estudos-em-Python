import os

os.system('cls')
'''
    Criar um algoritmo que leia a quantidade de números que se deseja digitar para 
    que possa ser impresso o maior e o menor numero digitados Não suponha que todos 
    os números lidos serão positivos 
'''

quant = int(input("Informe a quantidade de números que você vai digitar: "))
nums = [quant]

for i in range(quant):
    num = int(input("Informe o números desejado: "))
    nums.insert(i, num) # forma para inserir dados em uma lista

maior = max(nums)
menor = min(nums)

print(f"O maior número é {maior} e o menor número é {menor}")

input("\n\nPressione o \"enter\" para encerrar...")
