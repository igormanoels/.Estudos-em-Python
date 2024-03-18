import os

os.system('cls')
'''
    Entrar com nome, nota da PR1 e nota da PR2 de um aluno. 
    Imprimir nome, nota da PR1, nota da PR2, média e uma das mensagens: 
        - Aprovado: A média é 7
        - Reprovado: Menor que 3  
        - Prova Final: Maior que 3 e menor que 7 
'''

nome = input("Digite o nome do aluno: ")
n1 = float(input("Informe o valor da primeira nota: "))
n2 = float(input("Informe o valor da segunda nota: "))

media = ((n1 + n2) / 2)

if media < 3:
    print(f"\nO {nome} está Reprovado. Média é igual a {media}.") 
else:
    if media < 7:
        print(f"\nO {nome} está de Exame. Média é igual a {media}.")
    else:
        print(f"\nO {nome} está Aprovado. Média é igual a {media}.")

input("\n\nPressione o \"enter\" para encerrar...")
