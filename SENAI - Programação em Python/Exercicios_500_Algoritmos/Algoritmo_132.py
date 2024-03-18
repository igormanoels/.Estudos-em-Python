import os

os.system('cls')
'''
    Fazer um algoritmo que possa converter uma determinada quantia dada em reais para uma das seguintes moedas: 
        f - franco suíço 
        l - libra  
        d - dólar 
        e - euro 
'''

print("Informe a letra da moeda para conversão.",
              "\nf - franco suíço", "\nm - libra esterlina", "\nd - dólar", "\nm - marco alemão")
moeda = input("\nDigite a opção desejada: ").lower()
valor = float(input("Agora informe o valor a ser convertido: R$"))

match moeda:
    case "f":
        conversao = round((valor * 5.65), 2)
    case "l":
        conversao = round((valor * 6.35), 2)
    case "d":
        conversao = round((valor * 4.99), 2)
    case "e":
        conversao = round((valor * 5.43), 2)
    case _:
        conversao = 00.00
        print("\nOpção inválida!")
        
        
print(f"\nValor informado após conversão: R${conversao}")

input("\n\nPressione o \"enter\" para encerrar...")
