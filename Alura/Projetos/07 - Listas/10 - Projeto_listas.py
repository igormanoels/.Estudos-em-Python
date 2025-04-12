'''
10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. 
Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. 
Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e 
em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
'''

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

temperaturas = []
media = 0

for i in range(1, len(meses)):
    temperaturas.append(int(input('Informe o valor da temperatura: ')))


media = round (sum(temperaturas) / len(temperaturas))

print('\nLista de temperaturas acima da média')
for m, t in zip(meses, temperaturas):
    if t > media:
        print(f'Mês: {m} - Temperatura: {t}º')



