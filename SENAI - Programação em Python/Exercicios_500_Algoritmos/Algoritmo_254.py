import os

os.system('cls')
'''
    Criar um algoritmo que entre com dez notas de cada aluno de uma 
    turma de 20 alunos e imprima: 
        - A média de cada aluno 
        - A média da turma 
        - O percentual de alunos que tiveram medias maiores ou iguais a 5.0.
'''
nomes = []
medias = []
med = 0
medTurma = 0
acimaDe5 = 0

for i in range(20):
    nome = input("Informe o nome do aluno: ")
    nomes.append(nome)
    for i in range(10):
        nota = float(input(f"Informe a {i+1}º nota: "))
        med += nota 
    med /= 10
    medTurma += med
    medias.append(med)
    if med >= 5:
        acimaDe5 += 1
    print("\n")

percAcima5 = acimaDe5 / 20 * 100

print(f"Percentual de alunos que tiraram nota a partir de 5: {percAcima5}%")

i = 0
while i < 20:
    print(f"Nome: {nomes[i]} | Média: {medias[i]}")
    i += 1

input("\n\nPressione o \"enter\" para encerrar...")
