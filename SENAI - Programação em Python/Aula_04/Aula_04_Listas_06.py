import os
os.system('cls')
# falta validar o código

def est_aninhada(listaPrincipal, listaAninhada):
    est_aninhada = []
    for elementoPrincipal in listaPrincipal:
        subLista = [elementoPrincipal]
        for elementoAninhado in listaAninhada:
            subLista.append(elementoAninhado)
        est_aninhada.append(subLista)
    return est_aninhada

nomes = ["José", "João", "Maria", "Carlos"]
idade = [21, 34, 68, 4]

EstruturaAninhada = est_aninhada(nomes, idade)

for i in EstruturaAninhada:
    print(i, end=" ")
    
print("\n")