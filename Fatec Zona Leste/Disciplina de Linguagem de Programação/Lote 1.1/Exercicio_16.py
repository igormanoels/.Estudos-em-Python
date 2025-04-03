import os
os.system('cls')

'''
Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de descendentes. 
Calcule o salário que serão as horas trabalhadas x o valor por hora. 
Calcule o salário líquido (= SalárioBruto – desconto). 
A cada dependente será acrescido R$ 100 no Salário Líquido. 
Exiba o salário a receber.
'''

horasTrabalhadas = float(input("Informe o valor das horas trabalhadas: "))
valorHora = float(input("Informe o valor da hora: "))
desc = float(input("Informe o percentual de desconto: "))
filhos = float(input("Informe a quantidade de decendentes: "))

salarioBruto = horasTrabalhadas * valorHora

desc = (desc * salarioBruto) / 100

salarioLiquido = salarioBruto - desc + (filhos * 100)

print(f"Salário Líquido: R$ {salarioLiquido:.2f}")
