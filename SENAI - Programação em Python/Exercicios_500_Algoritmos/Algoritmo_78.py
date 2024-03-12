import os

os.system('cls')
'''
    Dado um polígono convexo de n lados, podemos calcular o número de diagonais diferentes (nd) desse polígono 
    pela fórmula : nd = n (n —3)/ 2. Fazer um algoritmo que leia quantos lados tem o polígono. 
    Calcule e escreva o número de diagonais diferentes (nd) do mesmo.
'''

n = int(input("Informe quantos lados tem o poligono em questão: "))

nd = n * (n - 3) / 2

print(f"O número de \"Diagonais Diferente do Poligono\" é {nd}")
input("\n\nPressione o \"enter\" para encerrar...")
