import os
os.system('cls')



# FileNotFoundError: Lançada quando o arquivo que está sendo aberto não pode ser encontrado no diretório especificado.
try:
    file = open('C:/temp/novapasta/andorinha.txt')
except FileNotFoundError as erro: # as erro captura a mensagem da excessão
    print(f"Arquivo não encontrado. \n{erro}")

'''
    OUTROS MODOS DE ERRO
    - PermissionError: Lançada quando ocorre uma tentativa de abrir um arquivo sem as permissões adequadas para leitura ou gravação.
    - IOError: Lançada quando ocorre um erro geral de E/S (entrada/saída) ao trabalhar com o arquivo, como problemas de permissão, falta de 
    espaço em disco, entre outros.
    - UnicodeDecodeError: Lançada quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada.
'''


#############################################################
# BOAS PRÁTICAS

try: # tratar a manupulação dentro de um try...except para otimizar o tempo de execução quando erros existirem
    # Faça operações de leitura/gravação no arquivo
    with open('arquivo.txt' ,'r', encoding='utf-8') as arquivo: # Sempre incluir o encoding nas operações de leitura e escrita
        1 / 0
        # isso ganrante que o arquivo será fechado
except IOError as erro:
    print(f"Alguma mensagem, {erro}")