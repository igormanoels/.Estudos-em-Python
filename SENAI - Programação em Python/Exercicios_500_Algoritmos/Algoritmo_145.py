import os

os.system('cls')
'''
    A biblioteca de uma universidade deseja fazer um algoritmo que leia o nome 
    do livro que será emprestado, o tipo de usuário (professor ou aluno) e possa 
    imprimir um recibo conforme mostrado a seguir. Considerar que o professor tem
    dez dias para devolver o livro e o aluno só três dias. 
        - Nome do livro:
        - Tipo de usuário: 
        - Total de Dias: 
'''
NomeLivro = input("Informe o nome do livro: ")
usuario = input("Informe o usuário: ").lower()

if usuario == "aluno":
    print(f"\nO livro: {NomeLivro}, deverá ser emprestado por 3 dias.")
elif usuario == "professor":
    print(f"\nO livro: {NomeLivro}, deverá ser emprestado por 10 dias.")
else:
    print("\nUsuário inválido.")
    
input("\n\nPressione o \"enter\" para encerrar...")
