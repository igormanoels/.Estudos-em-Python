# 1. Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado.
import math

print("Algoritmo: Cálcula área do quadrado.")

lado = int(input("Favor informar o valor do lado: "))
#quadrado = lado * lado
quadrado = (int) (math.pow(lado, 2))
# usando a classe math a variável vira double, mas também é possível fazer o casting da mesma forma que em java

print("Área do quadrado: ", quadrado)
