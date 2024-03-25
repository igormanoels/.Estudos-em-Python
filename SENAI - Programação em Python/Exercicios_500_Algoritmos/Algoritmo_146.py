import os

os.system('cls')
'''
    Fazer um algoritmo que leia o percurso em quilômetros, o tipo do carro e informe 
    o consumo estimado de combustível, sabendo-se que um carro tipo C faz 12 km 
    com um litro de gasolina, um tipo B faz 9 km e o tipo A, 8 km por litro. 
'''

modelo = input("Informe o modelo do seu carro A - 4x4 | B - Sedam | C - Hatch: ").upper()
dist = float(input("Informe o percurso em KM: "))

if modelo == "A":
    litros = round((dist / 8), 2)
elif modelo == "B":
    litros = round((dist / 9), 2)
elif modelo == "C":
    litros = round((dist / 12), 2)
else:
    litros = 0

if litros == 0:
    print("\nOpção inválida!")
else: 
    print(f"\nQuantidade de litros utilizada {litros} lts.")    




input("\n\nPressione o \"enter\" para encerrar...")
