import os

os.system('cls')
'''
    Segundo uma tabela medica o peso ideal esta relacionado com a altura e o sexo. Fazer um algoritmo que 
    receba a altura e o sexo de uma pessoa, calcular e imprimir o seu peso ideal utilizando as seguintes 
    formulas:
        - Para homens: (72.7 * H) - 58 
        - Para mulheres (62 1 * H) - 44.7
'''

sexo = input("Informe o sexo do paciente: ").lower()
altura = float(input("Informe a altura do paciente: "))

if altura > 2.5:
    altura = altura / 100
    if sexo.count("f"):
        peso = round(((62.1 * altura) - 44.7), 2)
        pronome = "dela"
    else:
        peso = round(((72.7 * altura) - 58), 2)
        pronome = "dele"
    
print(f"\nO peso ideal {pronome} deverá ser {peso}")

input("\n\nPressione o \"enter\" para encerrar...")
