import os
os.system('cls')

''' Descrição
    O desafio consiste em implementar uma classe Calculadora que utilize os princípios da Programação Orientada a Objetos (POO). 
    A classe deve conter um método para realizar a operação de soma entre dois números inteiros, encapsulando assim a lógica matemática da adição.
'''
class Calculadora:

    def somar(self, valorA, valorB):
        return valorA + valorB
    

num1 = int(input())
num2 = int(input())

calc = Calculadora()

resultado = calc.somar(num1, num2)
print(resultado)