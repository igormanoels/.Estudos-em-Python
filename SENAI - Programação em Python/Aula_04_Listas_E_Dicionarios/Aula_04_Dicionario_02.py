import os
os.system('cls')

meuDicionario = {"nome": "Igor", "Idade": 29, "cidade": "São Paulo"}

meuDicionario["cidade"] = "Guarulhos"

cidadeAtualizada = meuDicionario["cidade"]
print(cidadeAtualizada, "\n")

for chave, valor in meuDicionario.items():
    print(f"{chave}: {valor}")
print("")
