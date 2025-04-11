# Função 
nota = 5

def qualitativo(x):
  return x+0.5

qualitativo(nota)



# Transformando a função em uma expressão lambda
nota = 5

qualitativo = lambda x: x+0.5  # noqa: E731

qualitativo(nota)



##################################################################################################################
# UTILIZANDO A EXPRESSÃO LAMBDA
N1 = float(input("Digite a 1ª nota do(a) estudante: "))
N2 = float(input("Digite a 2ª nota do(a) estudante: "))
N3 = float(input("Digite a 3ª nota do(a) estudante: "))

media_ponderada = lambda x, y, z: (((x*3) + (y*2) + (z*5)) / 10)  # noqa: E731
media_estudante = media_ponderada(N1, N2, N3)


print(f'O(a) estudante atingiu uma média de {media_estudante}')



##################################################################################################################
# UTILIZANDO A FUNÇÃO MAP
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5

# Faz o mapeamento de notas para x, iterando sobre cada elemento para realizar a alteração, criando na memória um objeto tipo map
notas_atualizadas = map(lambda x: x+qualitativo, notas) 

# Tranforma o objeto map, em uma lista
notas_atualizadas = list(notas_atualizadas)
print(notas_atualizadas) 