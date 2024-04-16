import os

os.system('cls')
# ar um algoritmo que efetue o cálculo do salário líquido de um professor.
# Os dados fornecidos serão: valor da hora aula, número de aulas dadas no mês e percentual de desconto do INSS.

vhAula = float(input("Informe o valor da \"Hora da Aula\": "))
nAulas = int(input("Informe o \"Número de Aulas\" realizadas: "))
inss = float(input("Informe o valor de \"Desconto do INSS\": "))

salLiq = round(((vhAula * nAulas) * (1 - (inss/100))),2)

print("\nSalário Líquido: R$", salLiq)
input("\n\nPressione o \"enter\" para encerrar...")
