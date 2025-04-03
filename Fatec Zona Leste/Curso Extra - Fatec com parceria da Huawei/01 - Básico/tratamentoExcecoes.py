import os
os.system('cls')

try:
  valorA = int(input("Informe o valor A: "))
  valorB = int(input("Informe o valor B: "))
  res = valorA / valorB
  print(res)
except ZeroDivisionError:
  print("Não é possível realizar divisões por zero")
except ValueError:
  print("Apenas valores numéricos são aceitos.")
except:
  print("Não é possivel realizar a divisão.")  