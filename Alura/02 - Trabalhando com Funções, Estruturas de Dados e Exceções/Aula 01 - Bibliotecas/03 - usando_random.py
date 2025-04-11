# Importando uma função específica de uma biblioteca
from random import choice # choice é o método que será utilizado da biblioteca random

estudantes_2 = ["João", "Maria", "José", "Ana"]


estudante = choice(estudantes_2)
print(estudante)

help(choice) # Explica o método
help(print)

