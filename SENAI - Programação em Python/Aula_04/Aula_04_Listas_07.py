import os 

os.system('cls')

meuDicionario = {}

meuDicionario["Nome"] = "Igor"
meuDicionario["Endereco"] = "Rua de casa"
meuDicionario["Telefone"] = 123434564
meuDicionario["Email"] = "h@gmail.com"

nome = meuDicionario["Nome"]
print(f"Nome: {nome}\n")

print(meuDicionario, "\n")

if "cep" in meuDicionario:
    cep = meuDicionario["cep"]
    print(f"Cep: {cep}")
else: 
    print("A chave 'CEP' não está nesse dicionário.")

try:
    cep = meuDicionario["cep"]
    print(f"Cep: {cep}")
except:
    print("A chave 'CEP' não foi encontrada no dicionário.")

