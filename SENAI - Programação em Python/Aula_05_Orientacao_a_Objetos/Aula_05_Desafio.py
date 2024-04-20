import os
import time

os.system('cls')
'''
    1 - Faça uma classe que simule o funcionamento de uma bomba d'água. A bomba
    possui um atributo booleano chamado “status” e os métodos “ligar” e “desligar” 
    (ambos sem retorno). O método “ligar” coloca true em “status” e o método 
    “desligar” coloca false em status. A bomba deve ficar ligada durante um certo 
    intervalo de tempo (em segundos). O tempo em segundos deve ser recebido pelo 
    método ligar. A cada segundo, apresente em tela quantos segundos faltam para 
    a bomba ser desligada. Decorrido o tempo, o método desligar é acionado e a 
    bomba é desligada.
    
    2. Crie uma classe chamada UsaBomba que utilize a classe do exercício anterior.
    instanciar uma bomba (bomba1); 
        ligar o objeto bomba1 durante 5 segundos;
    
    3. Crie uma classe chamada GPS contendo os seguintes atributos do tipo String:
    “idioma” e “rota”. Defina dois métodos construtores: o default e outro para 
    ligar o GPS com o idioma português e uma rota qualquer. Elabore métodos para
    realizar as seguintes funções:
        Definir idioma;
        Definir rota;
    Um método chamado “mostrar” para apresentar todos os valores atuais dos 
    atributos do GPS. Elabore também uma outra classe (UsaGPS) para testar essas
    funcionalidades
'''

class Bomba:
    def __init__(self, status, tempo):
        self.status = status
        self.tempo = tempo
    
    def ligar(self):
        print("Bomba d'água ligada.")
        for i in range(30):
            print(f"Tempo {self.tempo-i} segundos.")
            time.sleep(1)
        acao.desligar()

    def desligar(self):
        print("Bomba d'água desligada.")


op = int(input("0 - Desligar Bomba \n1 - 1Ligar Bomba \nEscolha a opção desejada: "))
acao = Bomba(status=True, tempo=30)
if op == 1:
    acao.ligar()
elif op == 0:
    acao.desligar()
else:
    print("Opção inválida.")
