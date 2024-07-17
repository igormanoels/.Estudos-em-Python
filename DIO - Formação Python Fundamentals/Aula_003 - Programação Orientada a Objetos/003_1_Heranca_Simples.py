import os
os.system('cls')

class Veiculo:      # Todos os métodos e argumentos são herdados pelos filhos
    def __init__(self, cor, placa, rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = rodas
    
    def ligarMotor(self):
        print("Ligando motor!")

    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, rodas, carregado):
        super().__init__(cor, placa, rodas) # Implemente os métodos da classe pai, sem sobre-escrever
        self.carregado = carregado
     
    def carregar(self, carregado):
        if carregado == True:
            print("O caminhão está carregado!")
        else:
            print("O caminhão não está carregado!")


moto = Motocicleta("preta", "abc-1234", 2)
moto.ligarMotor()

caminhao = Caminhao("azul", "abc-1235", 10, False)
caminhao.carregar(True)
print(f"A cor do caminhão é {caminhao.cor}")