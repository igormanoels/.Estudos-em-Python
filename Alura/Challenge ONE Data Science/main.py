
import os
import lojas


def limpar_tela():
    os.system('cls')


print('Seja bem vindo ao meu código')
input('Pressione \"enter\" para prosseguir...')
limpar_tela()


while(True):
    try:
        print('Sistema de avaliação varejista\n' \
        '1 - Faturamento Total por loja\n' \
        '2 - Avaliação Média por loja\n' \
        '3 - Gasto medio com frete por loja\n' \
        '4 - Total de vendas por categoria\n' \
        '5 - Produtos mais vendidos\n' \
        '0 - Encerrar programa\n')
        op = int(input('Digite a opção desejada: '))
        
        match op:
            case 1:
                lojas.faturamento_total()
                limpar_tela()
            case 2:
                limpar_tela()
            case 3:
                limpar_tela()
            case 4:
                limpar_tela()
            case 5:
                limpar_tela()
            case 0:
                limpar_tela()
                break
            case _:
                print('\nOpção inválida! \nEscolha uma das opções do menu para consultar os dados ou digite 0 para encerrar')
                input('Pressione \'Enter\' para tentar novamente... ')
                limpar_tela()
    except Exception as e:
        print(e)
    else:
        pass
    finally:
        pass


