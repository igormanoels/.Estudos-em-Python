import os
os.system('cls')

''' Descrição
    Neste desafio, temos a classe Pessoa com seus atributos que armazenam o nome e a idade de uma pessoa. 
    Implemente um método para retornar uma representação formatada dos dados da pessoa, crie uma instância 
    da pessoa e, por fim, chame o método para retornar as informações formatadas e imprimir o resultado. 
    O objetivo é utilizarmos formas para criar e manipular objetos com POO, usando atributos e métodos para 
    encapsular dados e comportamentos.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
    

nome = input()
idade = int(input())

pessoa = Pessoa(nome, idade)
print(pessoa)
