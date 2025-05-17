from random import randint


estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]


def gera_codigo():
  return str(randint(0,999)) # Retorna um valor entre os parametros, inclusive os próprios valores

codigo_estudantes = []

# Criando uma lista de túplas
for i in range(len(estudantes)):
    ''' 
        Uma string tbm é iteravel, portando esturantes[i][0] busca o estudante na posição do indice 
        e a letra daquela palavra tbm pelo indice
    '''
    codigo_estudantes.append((estudantes[i],estudantes[i][0] + gera_codigo()))

print(codigo_estudantes)



