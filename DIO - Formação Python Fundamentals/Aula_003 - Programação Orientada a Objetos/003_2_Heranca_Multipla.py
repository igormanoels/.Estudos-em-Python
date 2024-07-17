import os 
os.system('cls')

class Animal:
    def __init__(self, patas):
        self.patas = patas

    def __str__(self):
        return self.patas
        

# KW usa o conceito de key args, ou seja posso passar mais de um parametro, que seja do pai
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): 
        super().__init__(**kw) # Super deve enviar o Key args pro pai 
        self.cor_pelo = cor_pelo # Só recebe atribuindo, o que for apenas dessa classe

        
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico
    
    def __str__(self):
        return self.cor_bico
        

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass




# Pela classe usar o conceito de Key args (chave/valor), se faz necessário indicar a chave do parametro que está sendo enviado
gato = Gato(patas=4, cor_pelo="Preto") 
print("O gato tem", gato.patas, "patas")

orn = Ornitorrinco(patas=4, cor_pelo="vermelho", cor_bico="laranja")
print("O ornitorrinco tem", orn.patas, "patas e bico ", orn.cor_bico)