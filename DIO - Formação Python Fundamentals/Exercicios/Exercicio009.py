import os
os.system('cls')

''' Descrição
    Implemente uma classe ConversorTemperatura que converte temperaturas de Celsius para Fahrenheit. 
    A classe deve incluir um método chamado celsius_para_fahrenheit que realiza o cálculo de conversão. 
    
    A fórmula para converter de Celsius para Fahrenheit é:
    Fahrenheit=((Celsius*9)/5)+32
    
    Você também deverá criar uma instância do conversor e utilizar essa instância para realizar a conversão.
'''


class Converter_temperatura():

    def conversor(celsius):
        return (((celsius * 9) / 5) + 32)



celsius = float(input())

temperatura = Converter_temperatura

fahrenheit = temperatura.conversor(celsius)
print(fahrenheit)