'''
2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais 
e calcule a porcentagem quanto ao total de compras.
'''

lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

total_compras = 0
acima_estimado = 0

for valor in lista:
    total_compras += valor

    if valor >= 3000:
        acima_estimado += valor


porcentagem = round(((acima_estimado / total_compras) * 100), 2)


print(f'Total em compras R$ {total_compras}\nGastos acima de 3k - R$ {acima_estimado}\nPercentual acima de 3k - {porcentagem}%')


