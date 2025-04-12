'''
9) Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve 
pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao 
gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.

Gabarito da prova:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B
'''
gabarito = {1:'D', 2:'A', 3:'C', 4:'B', 5:'A', 6:'D', 7:'C', 8:'C', 9:'A', 10:'B'}
respostas = {}
nota = 0

questao = 1

while (questao <= 10):
    respostas[questao] = input('Informe sua resposta: ').upper()
    questao +=1

for g, r in zip(gabarito.values(), respostas.values()): # A função zip junta os elementos em pares
    if g == r:
        nota +=1


print(f'O aluno tirou {nota}')


