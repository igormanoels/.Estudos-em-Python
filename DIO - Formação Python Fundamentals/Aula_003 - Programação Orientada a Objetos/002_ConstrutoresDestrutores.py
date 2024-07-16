import os
os.system('cls')

class Cachorro: # Nome da classe
    '''
        O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o 
        estado do nosso objeto. Para declarar o método construtor da classe, criamos um método com o nome init
    '''
    def __init__ (self, nome, cor, acordado = True): # Construtor com os atributos
        print("Iniciando instância")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    '''
    O método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores em Python não são 
    tão necessários quanto em C++ porque o Pyton tem um coletor de lixo que lida com o gerenciamento de memória
    automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome del
    '''
    def __del__ (self): # Finaliza o objeto para elimitar o uso dele na memória
        print("Destruindo a instância")
        
    def latir(self):
        print("O cachorro está latindo!")



c = Cachorro("Sisi", "preto")
c.latir()
c.latir()

del c # É como utilizar o close.scanner(); a qualquer momento você pode encerrar o uso de um objeto

