import os

os.system('cls')
'''
    Imagine você dando uma volta na Lagoa Rodrigo de Freitas (Rio de Janeiro): 
    passa uma vez pelo Corte do Cantagalo, uma vez pelo Clube do Flamengo, uma 
    vez pelo Clube Pira quê, uma vez pelos fundos do Clube Militar; esse trajeto 
    representa seus algoritmos feitos até agora com os comandos aprendidos.Imagine 
    que seu preparo físico melhorou e agora você consegue dar três ou cinco voltas 
    ou, quem sabe, até dez voltas na Lagoa; isso significa que você passará dez 
    vezes pelos mesmos lugares. Esse exemplo representa a estrutura do Para. Imagine 
    agora que você, orientado por um profissional especializado, passou a dar três 
    voltas na Lagoa mas, em frente ao Clube do Flamengo, você fará cinco abdominais. 
    Se, em cada volta você faz cinco abdominais, ao final, você terá feito 15 abdominais
    e terá dado três voltas na Lagoa. Isso representa um Para dentro de um PARA. Acompanhe:
'''

for i in range(3):
    print(f"{i+1}º volta na lagoa.")
    for j in range(5):
        print(f"\t{j+1}º abdominal.")
else: 
    print("Fim do exercício")
    
input("\n\nPressione o \"enter\" para encerrar...")
