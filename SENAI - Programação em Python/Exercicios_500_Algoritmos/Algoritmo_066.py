import os

os.system('cls')
'''
Efetuar o cálculo da quantidade de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12 km com um litro. 
Deverão ser fornecidos o tempo gasto na viagem e a velocidade média.
 
Utilizar as seguintes fórmulas:     distância = tempo x velocidade. 
                                    litros usados = distância / 12. 
                                    
O algoritmo deverá apresentar os valores da velocidade média, tempo gasto na viagem, distância percorrida e a quantidade de litros utilizados na viagem. 
'''

tempo = float(input("Informe o tempo gasto na viagem: "))
velo = int(input("Informe a velocidade média: "))

distancia = tempo * velo
litros = round((distancia / 12) , 2)

print("Distância = ", distancia, "km \t Litros: ", litros, "lts")
input("\n\nPressione o \"enter\" para encerrar...")
