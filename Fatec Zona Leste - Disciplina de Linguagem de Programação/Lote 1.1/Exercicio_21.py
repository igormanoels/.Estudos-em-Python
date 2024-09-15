import os
import math
os.system('cls')

'''
Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
a. Se a média for >= 6,0 exibir “APROVADO”;
b. Se a média for >= 3,0 ou < 6,0 exibir “EXAME”;
c. Se a média for < 3,0 exibir “RETIDO”.
'''

n1 = float(input("Informe o valor da primeira nota: "))
n2 = float(input("Informe o valor da segunda nota: "))
n3 = float(input("Informe o valor da terceira nota: "))
n4 = float(input("Informe o valor da quarta nota: "))

media = ((n1 + n2 + n3 + n4) / 4)

res = "Aprovado" if media >= 6 else ("Exame" if media >= 3 else "Retido")

print(f"Média: {media:.2f}", end=", situação: ")
print(res)
