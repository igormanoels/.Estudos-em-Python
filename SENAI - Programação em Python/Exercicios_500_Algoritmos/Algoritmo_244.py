import os

os.system('cls')
'''
    Entrar com uma mensagem e criptogra fá-Ia da seguinte maneira: 
        A-X ;   E-Y     ;   I-W     ;   O-K     ;   U-Z 

'''

msg = input("Informe sua mensagem: ").lower()
quant = len(msg)
newMsg = []

for i in range(quant):
    if msg[i] == "a":
        newMsg.append("x")
    elif msg[i] == "e":
        newMsg.append("y")
    elif msg[i] == "i":
        newMsg.append("w")
    elif msg[i] == "o":
        newMsg.append("k")
    elif msg[i] == "u":
        newMsg.append("z")
    else:
        newMsg.append(msg[i])
        
cript = "".join(newMsg) # Converte um vetor em uma string

print("Mensagem incripitada: ", cript)

input("\n\nPressione o \"enter\" para encerrar...")
