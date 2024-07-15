# Aula 01 - Conhecendo a Linguagem de Programação Python

import os
os.system('cls')

# As funções são blocos de código


def exibir_msg():
    print("Essa é uma função")

exibir_msg()


###################################################################################################################################
print("\n")
def funcao_retornando(a, b):
    return a + b

res = funcao_retornando(7, 8)
print("Função com retorno:",res)


###################################################################################################################################
print("\n")
def antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero +1
    return antecessor, sucessor

print(antecessor_sucessor(8))       # Retorna uma tupla


###################################################################################################################################
print("\n")
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/ {modelo}/ {ano}/ {placa}")


salvar_carro("palio", "Fiat", 1999, "abc-1235")             # envia o parametro por posição
salvar_carro(marca="palio", modelo="Fiat", ano=1999, placa="abc-1235")  # Envia o parametro por chave


###################################################################################################################################
print("\n")
def salvar_carro(marca, modelo, /, ano, placa):
    print(marca, modelo, ano, placa)

salvar_carro("palio", "Fiat", ano=1999, placa="abc-1235")   # Também pode ser passado junto, posição e chave


###################################################################################################################################
print("\n")
def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 5, somar)  # passa valor e função por parametro


###################################################################################################################################
print("\n")
pontuacao = 220

def calcular_pontos(tempo, pontos):
    multiplo = tempo * pontos
    return pontuacao + multiplo

res = calcular_pontos(12, 50)
print(res)
