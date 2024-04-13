import os 

os.system('cls')
'''
    Uma escola tem 5 turmas e cada turma tem n alunos. Criar um algoritmo que imprima, 
    por turma, total de alunos com média superiora 7 e a média geral da escola. 
'''
turmas = []
notas = []
totalM7 = []

i = 0
while (i < 5): 
    acimaDe7 = 0
    t = input("Informe a turma: ")
    turmas.append(t)
    while (True):
        nota = int(input("Digite uma nota do aluno, ou 99 para encerrar: "))
        if(nota == 99):
            break
        acimaDe7 += 1
        notas.append(nota)
    totalM7.append(acimaDe7)
    print("\n")
    i += 1        
        

mediaGeral = (sum(notas) / int(len(notas)))

i = 0
print(f"Media geral das notas dos alunos da Escola: {mediaGeral}")
while i < 5:
    print(f"Turma: {turmas[i]}\t|\tTotal de Notas acima de 7: {totalM7[i]}")
    i +=1
    
input("\n\nPressione o \"enter\" para encerrar...")
