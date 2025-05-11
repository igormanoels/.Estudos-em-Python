id = [1, 2, 3, 4, 5]
regiao = ["Norte", "Nordeste", "Sudeste", "Centro-Oeste", "Sul"]

'''
    A zip() é uma função embutida do Python que recebe um ou mais iteráveis (lista, string, dict, etc.) e retorna-os como 
    um iterador de tuplas onde cada elemento dos iteráveis são pareados. Ela é útil para fazer iterações simultâneas em várias listas.
'''
mapa = list(zip(id, regiao))
print(mapa)


####################################################################################################
codigos = ["1000", "1001", "1002", "1003", "1004", "1005"]
frutas = ["maçã", "uva", "banana", "laranja"]

mercadorias = list(zip(codigos, frutas)) # Retorna uma lista de túplas
print('\nMercadorias: ', mercadorias)

# Acessando a túpla da lista
print(f'Mercadoria: {mercadorias[0][1]} - Quantidade: {mercadorias[0][0]}')



####################################################################################################
# Processo inverso
tupla_iteravel = [('J392', 'João'), ('M890', 'Maria'), ('J681', 'José'), ('C325', 'Claúdia'), ('A49', 'Ana')]
ids, nomes  = zip(*tupla_iteravel)

ids = list(ids)
nomes = list(nomes)

print("\nIDs = ", ids)
print("Nomes = ", nomes)



####################################################################################################
# Aplicando uma fórmula ao percorrer valores de duas listas com o uso do ZIP para percorrer os valores
alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
pesos = [65, 80, 58, 70, 95]

imc = [round((peso / altura**2), 1) for altura, peso in zip(alturas, pesos)]
print('\n',imc)

