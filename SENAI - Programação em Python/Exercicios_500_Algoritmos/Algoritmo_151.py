import os

os.system('cls')
'''
    Um endocrinologista deseja controlar a saúde de seus pacientes e, para isso, se 
    utiliza do Índice de Massa Corporal (IMC). Sabendo-se que o lMCé calculado através 
    da seguinte fórmula:    IMC = peso / altura x altura 
    
    Onde: 
        - peso é dado em Kg 
        - altura é dada em metros 

    Criar um algoritmo que apresente o nome do paciente e sua faixa de risco, baseando-se na seguinte tabela: 
            IMC                                     FAIXA DE RISCO 
            abaixo de 20                            abaixo do peso 
            a partir de 20 até 25                   normal 
            acima de 25 até 30                      excesso de peso 
            acima de 30 até 35                      obesidade 
            acime de 35                             obesidade mórbida
'''

peso = float(input("Informe o peso do paciente: "))
altura = float(input("Informe a altura do paciente: "))

imc = (peso / (altura * altura))

if imc <= 20:
    print("\nClassificação: Abaixo do Peso.")
elif imc <= 25:
    print("\nClassificação: Normal.")
elif imc <= 30:
    print("\nClassificação: Excesso de Peso.")
elif imc <= 35:
    print("\nClassificação: Obesidade.")
else: 
    print("\nClassificação: Obesidade Mórbida.")

input("\n\nPressione o \"enter\" para encerrar...")
