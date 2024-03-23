import os

os.system('cls')
'''
    Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores para cada estado. Sabendo-se que os 
    arqueiros de uma equipe não obtiveram o mesmo número de pontos, criar um algoritmo que informe se uma equipe foi 
    classificada, de acordo com a seguinte especificação: 
        - ler os pontos obtidos por cada jogador da equipe; 
        - mostrar esses valores em ordem decrescente; 
        - se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles; senão, imprimir a 
        mensagem "Equipe desclassificada.
'''

estado = input("A qual estado essa equipe pertence: ")
jgd1 = int(input("Informe a quantidade de pontos o primeiro competidor fez: "))
jgd2 = int(input("Informe a quantidade de pontos o segundo competidor fez: "))
jgd3 = int(input("Informe a quantidade de pontos o terceiro competidor fez: "))

if jgd1 > jgd2 and jgd1 > jgd3:
    if jgd2 > jgd3:
        print(f"Ordem: {jgd1}, {jgd2} e {jgd3}.")
    else:
        print(f"Ordem: {jgd1}, {jgd3} e {jgd2}.")
elif jgd2 > jgd1 and jgd2 > jgd3:
    if jgd1 > jgd3:
        print(f"Ordem: {jgd2}, {jgd1} e {jgd3}.")
    else:
        print(f"Ordem: {jgd2}, {jgd3} e {jgd1}.")
elif jgd3 > jgd1 and jgd3 > jgd2:
    if jgd1 > jgd2:
        print(f"Ordem: {jgd3}, {jgd1} e {jgd2}.")
    else:
        print(f"Ordem: {jgd3}, {jgd2} e {jgd3}.")

totalEquipe = (jgd1 + jgd2 + jgd3)

if totalEquipe > 100:
    totalEquipe = totalEquipe / 3
    print(f"Equipe Classificada ---> média de pontos: {totalEquipe}.")
else:
    print(f"Equipe Desclassificada.")

input("\n\nPressione o \"enter\" para encerrar...")
