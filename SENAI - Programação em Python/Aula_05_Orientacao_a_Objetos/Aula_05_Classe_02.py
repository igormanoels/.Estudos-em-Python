import os
os.system('cls')

class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, novoNome):
        if not novoNome:
            raise ValueError("O campo nome não está preenchido")
        self.nome = novoNome

    @property
    def idade(self):
        return self.idade

    @idade.setter
    def idade(self, novaIdade):
        if not isinstance(novaIdade, int) or novaIdade < 0:
            raise ValueError("O campo idade não está preenchida")
        self.idade = novaIdade

    @property
    def sexo(self):
        return self.sexo

    @nome.setter
    def sexo(self, novoSexo):
        if not novoSexo:
            raise ValueError("O campo nome não está preenchido")
        self.sexo = novoSexo
