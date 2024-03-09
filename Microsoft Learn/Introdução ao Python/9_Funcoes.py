# TRABALHANDO COM FUNÇÕES

x = 10              # Variável Global

def primeiraFuncao():
    print('Essa mensagem vem da minha primeira função')

primeiraFuncao()                    # Realiza a chamada da Função
  


def segundaFuncao(nome):
    print(f'Olá, {nome}!')

segundaFuncao("Igor")               # Realiza a chamada da Função com passagem de parametro



def terceiraFuncao(a, b):           # Realiza a chamada da Função com passagem de parametro e retorno
    res = a + b
    return res

print(f'Soma: {terceiraFuncao(4, 5)}')



def quartaFuncao(a, b):           # Realiza a chamada da Função com passagem de parametro e retorno
    return a + b

print(f'Soma: {quartaFuncao(4, 5)}')



def quintaFuncao(y):
    return x * y

print(f'O produto de x e y = {quintaFuncao(5)}')