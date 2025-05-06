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