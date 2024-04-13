import os
os.system('cls')

lista_01 = [1, 2, 3]
lista_02 = [4, 5, 6]
listaIntercalada = []

# CONCATENANDO OS DADOS EM UM OUTRO VETOR
i = 0
j = 0
while i < len(lista_01) and j < len(lista_02):
    listaIntercalada.append(lista_01[i])
    listaIntercalada.append(lista_02[j])
    i += 1
    j += 1

print("Lista Intercalada 01:", end=" ")
for i in listaIntercalada:
    print(i, end=" ")


print("\n")


# MÉTODO SORT PARA O ORDENAMENTO DE DADOS
listaIntercalada2 = []
listaIntercalada2 = listaIntercalada
listaIntercalada2.sort()
print("Lista intercalada 02:", end=" ")
for i in listaIntercalada2:
    print(i, end=" ")
    
    
print("\n")