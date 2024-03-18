import os

os.system('cls')
'''
Entrar com o salário de uma pessoa e imprimir o desconto do INSS segundo a tabela a seguir: 
    - menor ou igual a R$ 600,00                            -       isento 
    - maior que R$ 600,00 e menor ou igual a R$ 1200,00     -         20% 
    - maior que R$ 1200,00 e menor ou igual a R$2000,00     -         25% 
    - maior que R$ 2000,00                                  -         30%
'''

salario = float(input("Informe o salário do colaborador: "))

if salario <= 600:
    desconto = 0.00
else:    
    if salario <= 1200:
        desconto = round((salario * 0.8), 2)
    else:
        if salario <= 2000:
            desconto = round((salario * 0.75), 2)
        else:
            desconto = round((salario * 0.7), 2)
    
print(f"\nDe acordo com o salário: R${salario}, e o desconto R${desconto}")

input("\n\nPressione o \"enter\" para encerrar...")
