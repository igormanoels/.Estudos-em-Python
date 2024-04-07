import os

os.system('cls')
'''
    Entrar com nome e salário bruto de 10 pessoas. Imprimir nome 
    e o valor da aliquota do imposto de renda:
        salário menor que R$ 600,00                 isento
        salário >= R$ 600,00 e < R$ 1500,00         10% de desconto
        salário >= R$ 1500,00                       15% de desconto
'''

funcionario = []
salarios = []
salLiquido = []

for i in range(10):
    nome = input("Informe o nome do funcionário: ")
    funcionario.append(nome)
    
    salario = float(input("Informe o salário bruto: "))
    salarios.append(salario)
    
    if salario < 600:
        salLiquido.append(salario)
    elif salario < 1500:
        salario = salario * 0.9
        salLiquido.append(salario)
    else:
        salario = salario * 0.85
        salLiquido = salario
    print("\n")
    
for i in range(len(funcionario)):
    print(f"Funcionário: R$ {funcionario[i]} | Salário Bruto: R$ {salarios[i]} | Salário Líquido: R$ {salLiquido[i]}")

input("\n\nPressione o \"enter\" para encerrar...")
