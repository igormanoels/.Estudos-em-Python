import os

os.system('cls')

# Os vatores em python são conhecidos como listas
listas = [100, "A", 2 , "texto", 3.5, "Bom dia! Seja bem vindo"]
carros = ["BMW", "Mazda", "VW", "Volvo"]
dados = listas+carros

print(listas, end="\n\n")

listas.append("Carro") # Inclui um dado na lista
listas[1] = "Cachorro" # Altera um item da lista
listas.remove("texto")
for i in listas:
    print(i, end=" ")

print("\n")

for i in dados:
    print(i, end=" ")
    
print("\n\n")

