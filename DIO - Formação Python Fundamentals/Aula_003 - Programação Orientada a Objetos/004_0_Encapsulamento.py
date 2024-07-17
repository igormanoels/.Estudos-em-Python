import os
os.system('cls')

''' 
    Em python tudo é público, porém, por convensão, compreende que um atributo ou método é privado quando
    seu nome se iniciar com underline. Portando o mesmo não deve ser manupulado diretamente fora de sua classe.
'''
class Conta():
    def __init__(self, saldo):
        self._saldo = saldo

    def Depositar(self, valor):
        self._saldo += valor

    def Sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print("Saque realizado, valor R$", valor, "\nSaldo atual: R$",self._saldo)
        else:
            print("Saldo insufuciente!")
    
    def Saldo(self):
        return self._saldo
   
    def __str__(self):
        return self._saldo




conta = Conta(100)

print(conta._saldo)
conta.Depositar(500)
conta.Sacar(450)
print(conta.Saldo())