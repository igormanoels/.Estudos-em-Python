import os
os.system('cls')

#Dicionarios com dicionários
estoque = {
    "FRUTAS":{
        "Maca": 5,
        "Laranja": 10,
        "Banana": 20
    },
    "LEGUMES":{
        "Batata": 30,
        "Berinjela": 15,
        "Cebola": 8
    }
}

# Acessando
secao = input("Informe a seção, Frutas / Legumes: ").upper() # toda entrada em caixa baixa
produto = input("Informe o produto: ").capitalize() # substitiu os caracteres os espaços em branco

if secao in estoque and produto in estoque[secao]:
    quant = estoque[secao][produto]
    print(f"{quant} x {produto} na seção {secao}")
else: 
    print("Produto não localizado.")

print("")
