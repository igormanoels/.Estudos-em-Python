import os

os.system('cls')
'''
    Escrever um algoritmo que leia um peso na Terra e o numero de um planeta e 
    imprima o valor do seu peso nesteplaneta A relação de planetas é dada a seguir 
    juntamente com o valor das gravidades relativas a Terra
        #   Gravidade Relativa  Planeta
        1   0,37                Mercúrio
        2   0,88                Vênus
        3   0,38                Marte
        4   2,64                Júpiter
        5   1,15                Saturno
        6   1,17                Urano
    
    Para calcular o peso no planeta use a fórmula:
    Pplaneta =  ((Pterra / 10) * gravidade)
'''
print("\nCálcula a sua massa em outro Planeta: ", 
      "\n#   Gravidade Relativa  Planeta",
       "\n1   0,37                Mercúrio",
       "\n2   0,88                Vênus",
       "\n3   0,38                Marte",
       "\n4   2,64                Júpiter",
       "\n5   1,15                Saturno",
       "\n6   1,17                Urano")

op = int(input("\nInforme a Opção desejada: "))

pTerra = float(input("\nInforme seu peso na terra: "))

match op:
    case 1:
        planeta = "Mercúrio"
        peso = ((pTerra / 10) * 0.37)
    case 2:
        planeta = "Vênus"
        peso = ((pTerra / 10) * 0.88)
    case 3: 
        planeta = "Marte"
        peso = ((pTerra / 10) * 0.38)
    case 4: 
        planeta = "Júpiter"
        peso = ((pTerra / 10) * 2.64)
    case 5: 
        planeta = "Saturno"
        peso = ((pTerra / 10) * 1.15)
    case 6:
        planeta = "Urano"
        peso = ((pTerra / 10) * 1.15)
    case _:
        print("\n\nOpção Inválida!")

print(f"\n\nO seu peso em {planeta} é {peso}")

input("\n\nPressione o \"enter\" para encerrar...")
