import os
os.system('cls')

# Tipos de entrada de dados
numero = int(input("Informe o número desejado: "))
fracao = float(input("Informe a nota do aluno: "))       
letra = ""
condicao = True

res = numero + fracao
print(res, "\t", type(res))     # \n realiza um pulo de linha e \t da espaço entre a linha
'''
Operadores Aritiméticos
+ Soma      - Subtração     * Multiplicação     
/ Divisão   % Resto da Divisão 
// Divisão absoluta  
'''

divisao = 10 / 6   #Retorna o valor da divisão
divAbsoluta = 10//6    #Retorna o valor absoluto
print(divisao, "\t", divAbsoluta)
