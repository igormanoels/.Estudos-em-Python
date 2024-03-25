import os

os.system('cls')
'''
IMC 	                Classificação 	          Obesidade (grau)
Menor que 18,5 	        Magreza 	                    0
Entre 18,5 e 24,9 	    Normal 	                        0
Entre 25,0 e 29,9 	    Sobrepeso 	                    I
Entre 30,0 e 39,9 	    Obesidade 	                    II
Maior que 40,0 	        Obesidade Grave 	            III

IMC = peso/(altura x altura)
'''

peso = float(input("Informe o peso do paciente: "))
altura = float(input("Informe a altura do paciente: "))

imc = (peso / (altura * altura))

if imc <= 18.5:
    print("\nClassificação: Magreza.")
elif imc <= 24.9:
    print("\nClassificação: Normal.")
elif imc <= 29.9:
    print("\nClassificação: Sobrepeso.")
elif imc <= 39.9:
    print("\nClassificação: Obesidade Grave I.")
else: 
    print("\nClassificação: Obesidade Grave II.")
