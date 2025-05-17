'''
13) As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% 
do salário devido ao ótimo desempenho do time. 

O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar
nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: 

O abono de cada colaborador(a) não pode ser inferior a 200. 

Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. 

Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o 
maior valor de abono fornecido.
'''

lista_salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
dicionario_abono = {}

abono = 0
qtd_abono_min = 0
maior_abono = 0

for salario in lista_salarios:
    abono = round((salario * 0.1),2)

    if abono < 200:
        dicionario_abono[salario] = 200    
    else:
        dicionario_abono[salario] = abono

     
for chave, valor in dicionario_abono.items():

    if valor == 200:
        qtd_abono_min +=1
    
    if valor > maior_abono:
        maior_abono = valor


print(f'{dicionario_abono}\nQuant. Mínima de abono: {qtd_abono_min}\nMaior valor de abono R$ {maior_abono}')


