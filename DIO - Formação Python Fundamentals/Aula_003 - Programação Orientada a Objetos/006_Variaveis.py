import os
os.system('cls')


class Estudante:
    escola = "DIO" # Variáveis de classe

    def __init__ (self, nome, numero):
        self. nome = nome # Variáveis de instancia
        self. numero = numero

    def __str__ (self):
        return f"{self.nome} ({self.numero}) - {self.escola}"


igor = Estudante ("Igor", 56451)
alice = Estudante("Alice", 17323)

print(igor)
print(alice)