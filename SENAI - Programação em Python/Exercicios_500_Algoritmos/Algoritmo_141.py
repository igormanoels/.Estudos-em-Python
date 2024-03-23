import os

os.system('cls')
'''
    Criar um algoritmo que leia o nome e o total de pontos de três finalistas de um campeonato de pingue-pongue 
    e exibir a colocação da seguinte forma: 
        - Vencedor:_______ XXXX ptos 
        - Segundo colocado: XXXX ptos 
        - Terceiro colocado: XXXX ptos
'''
p1 = input("Informe o nome do primeiro participante: ")
pt1 = int(input("Informe agora quantos pontos o primero participante fez: "))
p2 = input("Informe o nome do segundo participante: ")
pt2 = int(input("Informe agora quantos pontos o segundo participante fez: "))
p3 = input("Informe o nome do terceiro participante: ")
pt3 = int(input("Informe agora quantos pontos o terceiro participante fez: "))

if pt1 > pt2 and pt1 > pt3:
    print(f"\nVencedor: {p1} ---> pontos: {pt1}")
    if pt2 > pt3:
        print(f"Segundo Lugar: {p2} ---> pontos: {pt2} \nTerceiro Lugar: {p3} ---> pontos: {pt3}")
    else:
        print(f"Segundo Lugar: {p3} ---> pontos: {pt3} \nTerceiro Lugar: {p2} ---> pontos: {pt2}")
else:
    if pt2 > pt1 and pt2 > pt3:
        print(f"\nVencedor: {p2} ---> pontos: {pt2}")
        if pt1 > pt3:
            print(f"Segundo Lugar: {p1} ---> pontos: {pt1} \nTerceiro Lugar: {p3} ---> pontos: {pt3}")
        else:
            print(f"Segundo Lugar: {p3} ---> pontos: {pt3} \nTerceiro Lugar: {p1} ---> pontos: {pt1}")
    else:
        print(f"\nVencedor: {p3} ---> pontos: {pt3}")
        if pt1 > pt3:
            print(f"Segundo Lugar: {p1} ---> pontos: {pt1} \nTerceiro Lugar: {p2} ---> pontos: {pt2}")
        else:
            print(f"Segundo Lugar: {p2} ---> pontos: {pt2} \nTerceiro Lugar: {p1} ---> pontos: {pt1}")


input("\n\nPressione o \"enter\" para encerrar...")
