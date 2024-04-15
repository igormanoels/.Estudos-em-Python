import os
os.system('cls')

def est_aninhada(listaPrincipal, listaAninhada):
    if len(listaPrincipal) != len(listaAninhada):
        raise ValueError("As listas fornecidas devem ter o mesmo comprimento.")
    
    est_aninhada = []
    for nome, idade in zip(listaPrincipal, listaAninhada):
        est_aninhada.append((nome, idade))
    return est_aninhada

nomes = ["José", "João", "Maria", "Carlos"]
idade = [21, 34, 68, 4]

EstruturaAninhada = est_aninhada(nomes, idade)
for nome, idade in EstruturaAninhada:
    print(f"{nome} {idade},", end=" ")
print("\n")
