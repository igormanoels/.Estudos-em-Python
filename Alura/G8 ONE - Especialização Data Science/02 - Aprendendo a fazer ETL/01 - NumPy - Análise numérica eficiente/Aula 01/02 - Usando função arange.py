import numpy as np
import time

# CRIANDO UM ARRAY COM PARAMETROS DE INICIO E FIM
ano_inicial = 2000
ano_final = 2102

anos_copas = np.arange(ano_inicial, ano_final + 1, 4)
print('Array com os anos das copas: ',anos_copas,'\n')




# CONVERTE UMA LISTA EM ARRAY
lista = [1, 2, 3, 4, 5]
array = np.array(lista) # transforma a lista em um array Numpy

print("Lista: ", lista)
print("Array: ", array,'\n')




# TESTE DE VELOCIDADE DE PROCESSAMENTO

lista = list(range(1000000)) # cria uma lista com 1000000 elementos

array = np.array(lista) # transforma a lista em um array Numpy

start_time = time.time() # começa a cronometrar o tempo para a operação com a lista
lista_quadrado = [i**2 for i in lista] # realiza a operação de elevar ao quadrado cada elemento da lista
list_time = time.time() - start_time # para o cronômetro

start_time = time.time() # começa a cronometrar o tempo para a operação com o array
array_quadrado = array**2 # realiza a operação de elevar ao quadrado cada elemento do array
array_time = time.time() - start_time # para o cronômetro

print("Tempo da operação com a lista: ", list_time)
print("Tempo da operação com o array: ", array_time)



# Copiando um array
preco_imoveis = np.array([10000,120000,11000,200000])
preco_imoveis_sao_paulo = preco_imoveis
preco_imoveis[0] = 120000
preco_imoveis_sao_paulo = np.copy(preco_imoveis)




# Gerando número aleatórios
num_int = np.random.randint(low=40, high=100, size=100)
num_float = np.random.uniform(low=0.4, high=0.9, size=100)


print('\n\n',num_int,'\n\n',num_float,'\n\n')


array_vazio = np.array([]) # Cria um array vazio
array_vazio = np.append(array_vazio,2) # Adciona valores, é preciso passar o próprio array como argumento
array_vazio = np.append(array_vazio,3)
array_vazio = np.append(array_vazio,5)
array_vazio = np.append(array_vazio,7)


print(array_vazio)
print(array_vazio[1]) # Pega o valor da posição



# Gerando a msm sequencia de numeros aleatórios
np.random.seed(16)
num_int2 = np.random.randint(low=40, high=100, size=100)
print('\n\n',num_int2)

num_int3 = np.random.randint(low=40, high=100, size=100)
print('\n',num_int3)

np.random.seed(14)
num_int4 = np.random.randint(low=40, high=100, size=100)
print('\n',num_int4)


# Traduzindo cálculo para NumPy
x = [0,1,2,3,4,5,6,7,8,9,10]
y = []

for i in x:
    y.append(i + 3 / 2)
print(y)


# depois de converter
x = np.array(x)
y = x + 3/2
print(y)



# Agregando arrays
dados = np.column_stack([x,y])
print(dados.shape) # Ao agregar, o shape mostrará que são 11 colunas e 2 linhas
np.savetxt('dados.csv', dados, delimiter=',') # Serve salvar os dados 