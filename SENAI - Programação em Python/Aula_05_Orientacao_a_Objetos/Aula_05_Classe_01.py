import os
os.system('cls')

class Pessoa:
    def __init__(self, nome, idade, genero, cor):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.cor = cor

    def apresentar(self):
        print(f"Olá meu nome é: {self.nome}! Tenho {self.idade} anos")

menino = Pessoa(nome="Igor", idade=29, genero="Masculino",cor="Branco")
menino.apresentar()

usuario = Pessoa()
usuario.nome = input("Informe seu nome: ")
usuario.idade = int(input("Informe sua idade: "))
usuario.apresentar()

#SENAI@126