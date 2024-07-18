import os
os.system('cls')

class Passaro:
    def locomover(self): pass # Classe abstrada

class Pardal (Passaro):
    def locomover(self):
        print("Voando")

class Avestruz (Passaro):
    def locomover(self):
        print("Correndo")


# Sempre instanciar a classe que faz o implemento do método
pardal = Pardal()
pardal.locomover()

avestruz = Avestruz()
avestruz.locomover()
