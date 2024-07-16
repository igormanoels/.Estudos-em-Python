import os
os.system('cls')

'''
    João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. 
    Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. 
    Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!
'''

class Bicicleta:
    # pass # define que é uma classe vazia

    # Construtor da classe, o self/ this são referencias para apontamento
    def __init__(self, cor, modelo, ano, valor): 
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print("Buzinou!")

    def parar(self):
        print("Bicicleta parada!")
    
    def correr(self):
        print("Correndo!")
    
    def trocar_marcha(self, num_marcha):
        if num_marcha > self.marcha:
            print("Marcha trocada!")
        else: 
            print("Não trocou a marcha.")
    
    def __str__(self): # método similiar ao toString
        return f"Dados: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}."
    
        

# Instancia de um objeto
bike1 = Bicicleta("Vermelha", "caloi", 2022, 600.00)

# Executando funções
bike1.buzinar()
bike1.correr()
bike1.trocar_marcha(4)
bike1.parar()
# Bicicleta.buzinar(bike1) outra forma de fazer a chamada dos métodos

# Acessando Métodos
print("Cor da bicicleta: ", bike1.cor)

# Chamando o Objeto
print(bike1)
