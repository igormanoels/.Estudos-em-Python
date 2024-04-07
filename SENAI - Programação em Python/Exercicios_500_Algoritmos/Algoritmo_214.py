import os

os.system('cls')
'''
    Entrar com nome, nota da PR1 e nota da PR2 de 15 alunos. Imprimir uma 
    listagem, contendo: nome, nota da PR1, nota da PR2 e média arredondada
    de cada aluno Ao final calcule a media geral da turma.
'''

lista = []
prova1 = []
prova2 = []
media = []

for i in range(15):
    nome = input("Informe o nome do aluno: ")
    lista.append(nome)
    n1 = int(input("Informe a nota da p1: "))
    prova1.append(n1)
    n2 = int(input("Informe a nota da p2: "))
    prova2.append(n2)
    media.append((prova1[i] + prova2[i]) / 2)
    print("\n")
    
print("Aluno:\t  1º prova:\t  2º prova:\t\tMédia:")
for i in range(15):
    print(f"{lista[i]}\t\t{prova1[i]}\t\t{prova2[i]}\t\t{media[i]}")
    
input("\n\nPressione o \"enter\" para encerrar...")
