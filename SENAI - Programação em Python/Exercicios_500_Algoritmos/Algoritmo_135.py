import os

os.system('cls')
'''
    Criar um algoritmo que leia a idade de uma pessoa e informara sua classe eleitoral: 
        - Não-eleitor (abaixo de 16 anos) 
        - Eleitor obrigatório (entre 18 e 65 anos) 
        - Eleitor facultativo (entre 16 e 18 anos e maior de 65 anos) 
'''

idade = int(input("Informe a idade do eleitor: "))

if idade <= 16:
    categoria = "Voto não obrigatório."
elif idade <= 65:    
    categoria = "Voto obrigatório."
else:
    categoria = "Voto não Obrigatório."
    
print(f"\nCategoria: {categoria}")

input("\n\nPressione o \"enter\" para encerrar...")
