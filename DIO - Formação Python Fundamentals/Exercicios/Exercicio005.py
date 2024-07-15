#   Descrição
# Desenvolva uma função que receba duas listas de números inteiros separados por espaço e retorne uma lista contendo 
# apenas os elementos que são comuns a ambas as listas, sem duplicatas.
# 
# Detalhamento:
# Função elementos_comuns:
# 1. Crie a função que converte cada elemento das listas lista1 e lista2 para inteiro usando map(int, lista) 
# antes de convertê-los em conjuntos (set) e encontrar a interseção entre eles. Isso garante que tratemos os 
# elementos corretamente como números inteiros e não como strings.


def elementos_comuns(set1, set2):
    return list(set1.intersection(set2))

lista1 = input().split()
lista2 = input().split()

if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    comuns = elementos_comuns(set1, set2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")