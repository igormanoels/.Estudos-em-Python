import os, shutil
os.system('cls')

from pathlib import Path


#print(__path__)

ROOT_PATH = Path(__file__) # Retorna a parte onde o conteúdo executável está, com o nome do arquivo
print(ROOT_PATH)

ROOT_PATH = Path(__file__).parent # retorna a pasta rais do conteudo está, apenas a pasta
print(ROOT_PATH)


os.mkdir(ROOT_PATH / 'Nova Pasta') # Gera no caminho do arquivo, uma nova pasta com do conteúdo

#os.mkdir("C:\\temp\\Nova Pasta") # Criando uma pasta em um lugar desejado

arquivo = open(ROOT_PATH /'Nova Pasta'/ 'novoarquivo.txt', 'w') # Criando um arquivo na pasta do projeto
arquivo.close()

'''
Para renomear o arquivo basta usar barras invertidas, o interpretador python faz a busca do caminho baseado no sistema, 
esse tipo de barra permite que ele interprete livremetne
'''
# os.rename("D:/GitHub/.Estudos-em-Python/DIO - Formação Python Fundamentals/Aula_004 - Manipulação de Arquivos e Data/Nova Pasta/novoarquivo.txt", 
#          "D:/GitHub/.Estudos-em-Python/DIO - Formação Python Fundamentals/Aula_004 - Manipulação de Arquivos e Data/Nova Pasta/Dados_Usuario.txt")


# Remove o arquivo
#os.remove("D:/GitHub/.Estudos-em-Python/DIO - Formação Python Fundamentals/Aula_004 - Manipulação de Arquivos e Data/Nova Pasta/Dados_Usuario.txt")

# Ou simplemente a pasta
#os.rmdir("D:/GitHub/.Estudos-em-Python/DIO - Formação Python Fundamentals/Aula_004 - Manipulação de Arquivos e Data/Nova Pasta")

# Mover pasta
#shutil.move("diretório/nome.txt", "novodiretório"/"arquivo.txt")