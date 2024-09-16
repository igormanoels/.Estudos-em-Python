import os
os.system('cls')

'''
Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. 
Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. 
Demais tipos não serão considerados.
'''

op = int(input("Menu de investimento \n1-Poupança \n2-Renda fixa \nDigite a opção desejada: "))
investimento = float(input("Informe agora o valor a ser investido: R$"))
match op:
    case 1:
        print(f"Montante após investimento R${(investimento*1.03):.2f}")
    case 2:
        print(f"Montante após investimento R${(investimento * 1.05):.2f}")
    case _:
        print("Opção inválida!")
