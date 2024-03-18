import os

os.system('cls')
# fetuara leitura de cinco números inteiros diferentes e identificar o maior e o menor valor.

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))
num4 = int(input("Informe o primeiro número: "))
num5 = int(input("Informe o segundo número: "))

if (num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5):
    max = num1
elif (num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5):
    max = num2
elif (num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5):
    max = num3
elif (num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5):
    max = num4
else: 
    max = num5
if (num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5):
    min = num1
elif (num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5):
    min = num2
elif (num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5):
    min = num3
elif (num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5):
    min = num4
else: 
    min = num5

print(f"O maior número é {max} e o menor número é {min}")
input("\n\nPressione o \"enter\" para encerrar...") 
