import numpy as np
import matplotlib.pyplot as plt

caminho = 'Alura//G8 - ONE - TECH FOUNDATION - Especialização Data Science//02 - Aprendendo a fazer ETL//01 - NumPy - Análise numérica eficiente//Aula 01//numpy-dados//apples_ts.csv'

'''
    Através da biblioteca numpy os dados são carregados usando 3 condições
        - é usado um caminho relativo
        - um delimitador ',' para esse caso
        - para carregados os dados é necessário um array e a função usecols cria um vetor segundo os parametros abaixo:
            - Queremos pegar apenas os valores, ou seja, vamos pular a coluna 0. Logo o valos 1 será o parametro
            - São linha são 88 colunas ao todo. Logo o 88 será nosso ponto de parada
            - 1 é o valor de contagem, vamos de uma em uma. Mas poderia ser a cada duas colunas usando 2.
'''
dados = np.loadtxt(caminho, delimiter=',', usecols=np.arange(1, 88, 1))

''' Teste de visualização dos valores de criação do array
array =  np.arange(1, 88, 1) # coluna inicial, coluna final, contador
print(dados)
'''

#print('\nqtd: ', dados.size)
#print('\nLinhas e colunas: ',dados.shape)

dados_transposto = dados.T # é o conjunto de dados levando em consideração o indice do MES e ANO a qual ele se refere
#print(dados_transposto, "\n")

datas = dados_transposto[:,0] # ':'indica que quer todos os dados. Em seguida o outro parametro é da coluna referencia
#print(datas, '\n')

precos = dados_transposto[:,1:] # Aqui o primeiro pamametro é o mesmo de datas, já o segundo indica que quer fazer a busca da coluna 1 em diante
# precos = dados_transposto[:,1:6] # outra forma
#print(precos)


qtd_meses = np.arange(1, 88, 1) # como o datas cria uma coleção, vamos criar um array com a quantidade de meses
#print(qtd_meses)





# Usando matplotlib para gerar os gráficos do
plt.plot(qtd_meses, precos[:,0]) # Coloca no eixo 'x' as datas, e precos no eixo 'y'
plt.show()

Moscow = precos[:,0]
Kalin = precos[:,1]
Peter = precos[:,2]
Kras = precos[:,3]
Ekater = precos[:,4]
#print(Moscow)

plt.plot(qtd_meses, Moscow, Kras)
plt.title('Dados de vendas de maças em Moscow e Kras')
plt.show()



# Caso fosse necessário buscar apenas os meses para gerar ano a ano
Moscow_ano1 = Moscow[0:12] 
Moscow_ano2 = Moscow[13:25]
Moscow_ano3 = Moscow[25:37]
Moscow_ano4 = Moscow[37:49]

qtd_meses_ano = np.arange(1,13,1) 

# Ao gerar gráficos com mais de dois dados, é necessário separar, do contrário as informações não ficaram sobrepostas
plt.plot(qtd_meses_ano, Moscow_ano1)
plt.plot(qtd_meses_ano, Moscow_ano2)
plt.plot(qtd_meses_ano, Moscow_ano3)
plt.plot(qtd_meses_ano, Moscow_ano4)
plt.legend(['Ano1', 'Ano2', 'Ano3', 'Ano4'])
plt.title('Andamento do preço das maças em Moscow')
plt.show()


resp = np.array_equal(Moscow_ano1, Moscow_ano2) # retorna um boolean

resp = np.allclose(Moscow_ano1, Moscow_ano2, 10) # Verifica se a distancia entre os valores vai até 10, retorna um boolean



# Lidando com valores NaN
plt.plot(qtd_meses, Kalin)
print(Kalin,'\n')
plt.show()


print(np.isnan(Kalin),'\n' )  # a função is NaN, retorna um boolean para cada posição do array criando um array de verificação
print(sum(np.isnan(Kalin))) # com o uso da função sum, o retorno é uma soma das quantidade true, ou seja o total de NaNs contidos


#Para tratar os valores NaNs por conveniencia se aplica a media entre o valor anterior e o posterios a posição com valor NaN
Kalin[4] = np.mean([Kalin[3],Kalin[5]]) # Por ser um array é preciso passar um colchete dentro da função
print('\n\n',Kalin,'\n\n')



# Comparando a média de preços
media_preco_moscow = np.mean([Moscow])
media_preco_kalin = np.mean([Kalin])

print(media_preco_moscow,'\t',media_preco_kalin)