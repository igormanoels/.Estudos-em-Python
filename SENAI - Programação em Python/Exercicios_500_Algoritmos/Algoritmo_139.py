import os

os.system('cls')
'''
    Sabendo que somente os municípios que possuem mais de 20.000 eleitores aptos têm segundo turno nas eleições 
    para prefeito caso o primeiro colocado não tenha mais do que 50% dos votos, fazer um algoritmo que leia o nome 
    do município, a quantidade de eleitores aptos, o número de votos do candidato mais votado e informar se ele 
    terá ou não segundo turno em sua eleição municipal. 
'''

municipio = input("Informe o nome do município: ")
eleitores = int(input("Informe o quantidade de eleitores: "))
votos = int(input("Informe a quantidade de votos do candidato mais votado: "))

if eleitores > 20000 and votos <= eleitores / 2:
    print(f"\nEm {municipio} terá segundo turno.")
else:
    print(f"\nEm {municipio} não terá segundo turno")

input("\n\nPressione o \"enter\" para encerrar...")
