import os
os.system('cls')

class A:
    pass # Indicador de que nada ainda foi feito, usado antes de implementar os métodos da classe


# para declarar que a classe B extends A, basta declarar A entre parenteses
class B (A):
    pass

# classe C extends de A e B
class C (A, B):
    pass
