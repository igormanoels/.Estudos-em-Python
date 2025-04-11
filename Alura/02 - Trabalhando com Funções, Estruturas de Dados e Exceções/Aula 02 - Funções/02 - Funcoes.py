# FUNÇÕES SEM PARAMETROS
a = 1
b = 2

def somar():
    print(a+b)

somar()



##################################################################################################################
# FUNÇÕES COM PARAMETROS
def media(n1, n2, n3): # argumentos
  res = ((n1+n2+n3)/3)
  print(res)

media(2,3,6.5) # parametros

#outra forma
nt1 = 1
nt2 = 5
nt3 = 6

media(nt1,nt2,nt3) # parametros



##################################################################################################################
# APLICANDO A UM COLEÇÃO DE DADOS COM RETURNO DE VALORES
notas = [8.5, 9.0, 6.0, 10.0] # Notas do(a) estudante

def media(lista):
    res = sum(lista) / len(lista)
    return res

resultado = media(notas)
print(resultado)


##################################################################################################################
notas = [6.0, 7.0, 9.0, 5.0] # Notas do(a) estudante

def boletim(lista):
    media = sum(lista) / len(lista)
    if media >= 6:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
    
    return (media, situacao) # O valor aqui é retornado como uma túpla


media_estudante, situacao_estudante = boletim(notas) # É possivel receber os valores de uma túpla, retornando e separando entre duas variáveis

print(f'O(a) estudante atingiu uma média de {media_estudante} e foi {situacao_estudante}.')



##################################################################################################################
# a nossa função recebe uma lista do tipo list e retorna uma variável do tipo float
def media(lista: list) -> float:
  calculo = sum(lista) / len(lista)
  return calculo


# a nossa função recebe uma lista do tipo list e retorna uma variável do tipo float
# caso não recebe nenhum valor de parâmetro será passada uma lista com um único
# elemento sendo ele zero
def media(lista: list=[0]) -> float:
  calculo = sum(lista) / len(lista)
  return calculo