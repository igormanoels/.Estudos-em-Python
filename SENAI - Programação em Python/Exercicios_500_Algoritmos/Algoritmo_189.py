import os

os.system('cls')
'''
    Criar um algoritmo que imprima a tabela de conversão de graus Celsius-Fahrenheit 
    para o intervalo desejado pelo usuário. O algoritmo deve solicitar ao usuário o 
    limite superior, o limite inferior do intervalo e o decremento. 
        Fórmula de conversão: C = 5 * (F - 32) / 9
'''
print("Vamos gerar uma tabela com as temperaturas?\nAqui você irá infomar o intervalo(Ex.: 10 a 25).")
limInf = int(input("Informe a partir de qual temperatura você deseja saber: "))
limSup = int(input("Informe até qual temperatura você deseja saber: "))

while limInf <= limSup:
    c = (5 * (limInf - 32) / 9)
    print(f"Para {limInf} Fahrenheit temos ---> {c} Celsius.")
    limInf += 1

input("\n\nPressione o \"enter\" para encerrar...")
