import os

os.system('cls')
'''
    Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens:
    - Carioca
    - Paulista
    - Mineiro
    - Outros estados
'''
uf = input("Informe a sigla de seu estado: ").lower()

if uf.count("sp"):
    print("\nPaulista!")
elif uf.count("rj"):
    print("\nCarioca!")
elif uf.count("mg"):
    print("\nMineiro!")
else: 
    print("\nOutro Estado.")

input("\n\nPressione o \"enter\" para encerrar...")
