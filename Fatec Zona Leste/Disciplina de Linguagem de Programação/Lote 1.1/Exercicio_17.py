import os
os.system('cls')

'''
Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. 
Receber o tempo de percurso e a velocidade média.
'''

percurso = float(input("Informe o percurso: "))
velocidadeMedia = float(input("Informe a velocidade média: "))

distancia = percurso * velocidadeMedia

litros = distancia / 12

print(f"A quantidade de litros gastos é de {litros:.2f} litros")
