
import os
import lojas


def limpar_tela():
    os.system('cls')


limpar_tela()
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
        '5 - Listar produtos vendidos\n' \
        '0 - Encerrar programa\n')
        op = int(input('Digite a opção desejada: '))
        
        match op:
            case 1:
                lojas.verificarFaturamento()
                limpar_tela()
            case 2:
                lojas.avaliacaoMedia()
                limpar_tela()
            case 3:
                lojas.verificarCustoFrete()
                limpar_tela()
            case 4:
                lojas.vendasPorCategoria()
                limpar_tela()
            case 5:
                print('\nEscolha a forma:\n' \
                '6 - Produtos Mais vendidos\n' \
                '7 - Produtos Menos vendidos\n')
                op = int(input('Digite a opção desejada: '))
                lojas.contarQtdProdutos(op)
                limpar_tela()
            case 0:
                limpar_tela()
                input('Obrigado por testar meu algoritmo!!!\n' \
                'Pressione \'Enter\' para Encerrar... ')
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


