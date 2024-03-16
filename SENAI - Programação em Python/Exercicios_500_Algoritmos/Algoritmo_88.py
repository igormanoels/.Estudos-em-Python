import os

os.system('cls')
# Algoritmo Calculadora

calc = input("****************************************\n"
             " ***********  CALCULADORA  **************"
             "\n\t\t\t + para somar"
             "\n\t\t\t - para subtrair"
             "\n\t\t\t * para multip1icar"
             "\n\t\t\t / para dividir"
             "\nDigite opção: ")

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if calc.__contains__("+"):
    res = num1 + num2
elif calc.__contains__("-"):
    res = num1 - num2
elif calc.__contains__("*"):
    res = num1 * num2
elif calc.__contains__("/"):
    res = num1 / num2

print(f"\n{num1} {calc} {num2} = {res}")

input("\n\nPressione o \"enter\" para encerrar...")
