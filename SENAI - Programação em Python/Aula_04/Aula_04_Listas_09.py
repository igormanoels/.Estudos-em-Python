import os
os.system('cls')

agenda = {
    "Docinho":["2992-1923", "docinho@gmail.com"],
    "Florzinha":["2994-1245", "florzinha@gmail.com"]
}

nome = input("Informe o nome: ")

if nome in agenda:
    numero,email = agenda[nome]
    print(f"Telefone: {numero} e E-mail{email}")
else:
    print(f"O nome '{nome}' informado não está presente na lista.")

print("")