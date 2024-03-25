import os

os.system('cls')
'''
    O prefeito do Rio de Janeiro contratou uma firma especializada para manter os níveis de poluição considerados
    ideiais para um país do 1 2mundo. As indústrias, maiores responsáveis pela poluição, foram classificadas em 
    três grupos. Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição aceitável até 0, 25, 
    fazer um algoritmo que possa imprimir intimações de acordo com o índice e a tabela a seguir: 
    
    índice indústrias que receberão intimação 
        0,3     1º grupo 
        0,4     1º e 2º grupos 
        0,5     1º e 2º e 3º grupos 
'''

indice = float(input("\ndigite indice de poluicao: "))

if (indice >= 0.5):
    print("\nsuspender atividades as industrias dos grupos 1, 2 e 3")
else:
    if(indice >= 0.4):
        print("\nsuspender atividades as industrias dos grupos 1 e 2 ") 
    else: 
        if(indice >= 0.3):
            print("\nsuspender atividades as industrias dos grupos 1 ")
        else:
            print("\nindice de poluicao aceitavel para todos os grupos ")


input("\n\nPressione o \"enter\" para encerrar...")
