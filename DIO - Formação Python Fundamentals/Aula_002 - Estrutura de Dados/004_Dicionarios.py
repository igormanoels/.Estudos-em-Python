# Aula 01 - Conhecendo a Linguagem de Programação Python

import os
os.system('cls')

# Composto por um conjunto não ordenado de chave:valor

pessoa = {"nome": "Igor", "idade": 28}

pessoa2 = dict(nome="Igor", idade=25)   # Cria o dicionário passando pelo construtor

print(pessoa)
print(pessoa2)

pessoa["Telefone"] = "1212-5548"    # Realiza a inclusão de uma chave e valor para um dicionário existente
print(pessoa)

print(pessoa["nome"])               # Retorna o valor da chave

# Dicionário aninhado, e pode criar vários níveis
contatos = {
    "contato1": {"nome": "Igor", "idade": 28, "telefone": "1212-5548"},
    "contato2": {"nome": "Maria", "idade": 18, "telefone": "1912-4448"},
    "contato3": {"nome": "Mateu", "idade": 98, "telefone": "89212-5548"},
    } # Sempre manter o último com uma vírgula

print(contatos["contato1"])             # Retorna o dicionário interno 
print(contatos["contato2"]["idade"])    # Retorna o valor da chave do dicionário, como se fosse manipulação de matriz

# MÉTODOS
print("\n")
for chave, valor in pessoa.items():     # Retorna as chaves e contúdos 
    print(chave,":" ,valor)

pessoa.clear()      # Apaga os dados
pessoa.copy()       # Copia os dados
pessoa.fromkeys(["rua", "numero","estado"])             # Cria chaves vazias
pessoa.fromkeys(["rua", "numero","estado"], "vazio")    # Cria as chaves com um valor padrão
pessoa.get("nome")          # Busca uma chave, se ele não encontra retorna 'None'
pessoa.get("nome", "Vazio")          # Busca uma chave e retorna um valor padrão
pessoa.keys()               # Retorna as chaves
pessoa.pop("nome")          # Remove a chave escolhida
pessoa.pop("piratas", "chave inexistente")      # Remove a chave, se não encontrar retorna um valor padrão
pessoa.popitem()        # Remove na sequencia, ou retorna um erro se estiver vazio
pessoa.setdefault()
pessoa.setdefault("time", "Tricolor")       # Adiciona uma nova chave caso não haja, mas ele respeita o valor caso a chave exista
pessoa.update("nome","Manoel")          # Atualiza a chave
pessoa.values()         # Retorna todos os valores
verifica = "nome" in pessoa     # verifica se a chave existe no dicionário
del contatos["contato1"]["telefone"]    # Remove chaves e valor
del contatos    # apaga o dicionário inteiro
