import os

os.system('cls')
'''
    Criar um algoritmo que leia a quantidade de fitas que uma locadora de vídeo possui e o valor que ela cobra por cada 
    aluguel, mostrando as informações pedidas a seguir: 
    - Sabendo que um terço das fitas são alugadas por mês, exiba o Faturamento anual da locadora; 
    
    - Quando o cliente atrasa a entrega, é cobrada uma multa de 10% sobre o valor do aluguel. Sabendo que um décimo das 
    fitas alugadas no mês são devolvidas com atraso, calcule o valor ganho com multas por mês; 
    
    - Sabendo ainda que 2% de fitas se estragam ao longo do ano, e um décimo do total é comprado para reposição, exiba 
    a quantidade de fitas que a locadora terá no final do ano. 
'''
fitas = int(input("Informe a quantiadade de Fitas disponíveis: "))
pAluguel = float(input("Informe o valor unitário do aluguel: R$ "))

arrecMensal = round(((fitas * pAluguel) / 3), 2)
arrecAnual = round((arrecMensal * 12), 2)
recAtrasosMensal = round(((arrecMensal / 10) * 1.1), 2)
recAtrasosAnual = round((recAtrasosMensal * 12), 2)
descFitas = round(fitas * 0.02)
repoFitas = round(fitas * 0.1)
saldoFitas = ((fitas + repoFitas) - descFitas)

print(f"\n...................Locadora XYZ..................."
      f"\nQuantidade de Fitas............................{fitas} qtd"
      f"\nReceita Média Mensal.........................R$ {arrecMensal}"
      f"\nReceita Média Anual..........................R$ {arrecAnual}"
      f"\nReceita Média Mensal c/ Atrasos..............R$ {recAtrasosMensal}"
      f"\nReceita Média Anual c/ Atrasos...............R$ {recAtrasosAnual}"
      f"\nFitas Descartadas..............................{descFitas} qtd"
      f"\nFitas Repostas.................................{repoFitas} qtd"
      f"\nSaldo Final das Fitas..........................{saldoFitas} qtd")

input("\n\nPressione o \"enter\" para encerrar...")
