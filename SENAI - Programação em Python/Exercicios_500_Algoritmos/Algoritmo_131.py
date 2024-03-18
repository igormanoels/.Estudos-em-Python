import os

os.system('cls')
'''
    A turma de Programação 1, por ter muitos alunos, será dividida em dias de provas. Após um estudo feito pelo coordenador, 
    decidiu-se dividi-la em três grupos. Fazer um algoritmo que leia o nome do aluno e indicar a sala em que ele deverá fazer 
    as provas, tendo em vista a tabela a seguir e sabendo-se que todas as salas. se encontram no bloco F: 
            A - K:  sala 101 
            L - N:  sala 102 
            O - Z:  sala 103
'''
aluno = input("Informe o seu primeiro nome: ").lower()
letra = aluno[0]

if  letra < "k":
    print("\nBloco F: Sala 101.")
else:
    if  letra < "n":
        print("\nBloco F: Sala 102.")
    else:
        print("\nBloco F: Sala 103.")
        
input("\n\nPressione o \"enter\" para encerrar...")
