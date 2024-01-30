# OPERAÇÕES ARITIMÉTICAS

adicao = 30 + 20
print(adicao)

difenca = 30-20
print(difenca)

produto = 30*20
print(produto)

divisao = 30 / 20
print(divisao)

segundos = 1042
Displ_minutos = segundos // 60          # Realiza a divisão com arredondamento
Displ_segundos = segundos % 60          # Retorna apenas o resto da divisão
print("Tempo:" , Displ_minutos, "min:" , Displ_segundos,"seg")

print(abs(39 - 16)) # converte o valor para absoluto, quando a resposta independe da posicao, como por exemplo a distancia entre lugares
print(abs(16 - 39))

print(round(1.4)) 
print(round(1.5))       # Sobre o arredondamento o valor é arredondado conforme o número par mais proximo, isso 
print(round(2.5))       # quando o valor for .5
print(round(2.6))

from math import ceil, floor        # com o uso dessa biblioteca o arredondamento pode ser direcionado para cima ou baixo

round_up = ceil(12.5)       # Arredondamento para cima
print(round_up)

round_down = floor(12.5)    # Arredondamento para baixo
print(round_down)

# ENTRADA DE DADOSNA MESMA LINHA DA PERGUNTA
num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
res = num1 * num2
print('Produto = ' , res)

# OPERADOR MAIOR E MENOR DE UM VETOR
idades = [18, 25, 13, 12, 45, 60]
maisJovem = min(idades)
maisVelho = max(idades)
print('Mais velho: ', maisVelho, "e Mais Jovem: ", maisJovem)

