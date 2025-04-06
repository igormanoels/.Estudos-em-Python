'''
9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um 
programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

- Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
- Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
'''

from sqlalchemy import Case


candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
brancos = 0
nulos = 0

for i in range(1, 21):
    voto = int(input('Escolha seu candidato: \n'
    '1 para candidato1\n'
    '2 para candidato2\n'
    '3 para candidato3\n'
    '4 para candidato4\n'
    '5 para anular\n'
    '6 votar em branco\n'
    'Digite o voto desejado: '))

    match voto:
        case 1:
            candidato1+=1
        case 2: 
            candidato2+=1
        case 3: 
            candidato3+=1
        case 4: 
            candidato4+=1
        case 5:
            brancos+=1
        case 6:
            nulos+=1

print(f'Apuração dos votos\nCandidato 1: {candidato1}\nCandidato 2: {candidato2}\nCandidato 3: {candidato3}\nCandidato 4: {candidato4}\nNulos: {nulos}\nBrancos: {brancos}\n')