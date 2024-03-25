import os

os.system('cls')
'''
    Criar um algoritmo que a partir da idade e peso do paciente calcule a dosagem de determinado medicamento
    e imprima a receita informando quantas gotas do medicamento o paciente deve tomar por dose Considere que
    o medicamento em questão possui 500 mg por ml e que cada ml corresponde a 20 gotas.
    
    -   Adultos ou adolescentes desde 12 anos, inclusive, se tiverem peso igual ou acima de 60 quilos devem 
        tomar 1000 mg; com peso abaixo de 60 quilos devem tomar 875 mg. 

    -   Para crianças e adolescentes abaixo de 12 anos é dosagem é calculada pelo peso corpóreo conforme a 
    tabela a seguir: 
        5 kg a 9 kg = 125 mg 
        9.1 kg a 16 kg = 250 mg
        16.1 kg a 24 kg = 375 mg
        24.1 kg a 30 kg = 500 mg 
        acima de 30 kg = 750 mg 
'''

idade = int(input("Informe a idade do paciente: "))
peso = float(input("Informe o peso do paciente: "))
dose = (20/500)

if(idade >= 12):
    if(peso >= 60):
        dose *= 1000  
    else:
        dose *= 875
else:
    if(peso <= 9):
        dose *= 125
    elif(peso <= 16):
        dose *= 250
    elif(peso <= 24):
        dose *= 375
    elif(peso <= 30):
        dose *= 500
    else:
        dose *= 750

dose = int(dose)
        
print(f"\nA dose do paciente deverá ser de {dose} gotas.")

input("\n\nPressione o \"enter\" para encerrar...")
