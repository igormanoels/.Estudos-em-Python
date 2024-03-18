import os

os.system('cls')
'''
    A confederação brasileira de natação irá promover eliminatórias para o próximo mundial Fazer um algoritmo 
    que receba a idade de um nadador e imprimir a sua categoria segundo a tabela a seguir: 
        Categoria               Idade 
        Infantil A              5 - 7 anos
        Infantil B              8 - 10 anos 
        Juvenil A               11 - 13 anos 
        Juvenil B               14 - 17 anos 
        Sênior                  Maiores de 18 anos 
'''

idade = int(input("Informe a idade do participante: "))

if idade <= 4:
    categoria = "Não há categoria para esse participante."
elif idade <= 7:    
    categoria = "Infantil A."
elif idade <= 10:    
    categoria = "Infantil B."
elif idade <= 13:    
    categoria = "Juvenil A."
elif idade <= 17:    
    categoria = "Juvenil B."
else:
    categoria = "Sênior."
    
print(f"\nCategoria: {categoria}")

input("\n\nPressione o \"enter\" para encerrar...")
