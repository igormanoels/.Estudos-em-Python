import pandas as pd
import numpy as np

hospedagem = pd.read_json('D:/GitHub/.Estudos-em-Python/Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/Transformação e Manipulação de Dados/01 - Manipulando dados com pandas/dados/dados_hospedagem.json')
# Normalizando dados de hospedagem
hospedagem = pd.json_normalize(hospedagem['info_moveis'])

print(hospedagem.head())


# Desagrupando Dados
colunas = list(hospedagem.columns) # Pega apenas os valores dos indices das colunas
print(colunas) 

hospedagem = hospedagem.explode(colunas[3:]) # cria a separação dos dados a partir do indice 3
print(hospedagem) 

hospedagem.reset_index(inplace=True, drop=True) # Subistitui os parametros e apaga os indices antigos
print(hospedagem) 


# Verificando os dados se todos possuem o mesmo tipo, e os tipos são representados como object porque os dados estão misturados
print(hospedagem.info()) 


# Convertendo os dados 
hospedagem['max_hospedes'] = hospedagem['max_hospedes'].astype('Int64') # Converte os dados para inteiro
hospedagem['quantidade_banheiros'] = hospedagem['quantidade_banheiros'].astype('Int64')
hospedagem['quantidade_quartos'] = hospedagem['quantidade_quartos'].astype('Int64')
hospedagem['quantidade_camas'] = hospedagem['quantidade_camas'].astype('Int64')

# Outra forma
cols_int = ['quantidade_banheiros', 'quantidade_quartos', 'quantidade_camas'] # Crio um Array com os dados que precisam ser tratatods
hospedagem[cols_int] = hospedagem[cols_int].astype('Int64') # chamo o array como parametro para a conversão

hospedagem['avaliacao_geral'] = hospedagem['avaliacao_geral'].astype('float64')

# Substitui os valores do Crifrão e virgula por vazio, e depois apaga os valores vazios
hospedagem['preco'] = hospedagem['preco'].apply(lambda x: x.replace('$','').replace(',','').strip()) 
hospedagem['preco'] = hospedagem['preco'].astype(np.float64)

cols_float = ['taxa_deposito', 'taxa_limpeza']
hospedagem[cols_float] = hospedagem[cols_float].applymap(lambda x: x.replace('$','').replace(',','').strip())
hospedagem[cols_float] = hospedagem[cols_float].astype(np.float64)

print(hospedagem.info()) 



# Tratando os Textos, para criar tokens
print('\n', hospedagem.head())
hospedagem['descricao_local'] = hospedagem['descricao_local'].str.lower() # Tranforma em string e colocar em caixa baixa
print('\n', hospedagem['descricao_local'] )

print('\nAvaliação do usuário 3156\n',hospedagem['descricao_local'][3156]) # Visualizando um dado

# Coluna descricao_local
hospedagem['descricao_local'] = hospedagem['descricao_local'].str.replace('[^a-zA-Z0-9\-\']',' ', regex=True) # Remove todos os caracteres distintos do código regex
hospedagem['descricao_local'] = hospedagem['descricao_local'].str.replace('(?<!\w)-(?!\w)','', regex=True) # Remove os hífens que estiverem soltos

hospedagem['descricao_local'] = hospedagem['descricao_local'].str.split(' ') # Transforma os textos em uma lista de palavras substituindo os espaços

#Coluna comodidades
hospedagem['comodidades'] = hospedagem['comodidades'].str.replace('\{|}|\"','', regex=True) # Remove os {,} e "
hospedagem['comodidades'] = hospedagem['comodidades'].str.split(',') # Transforma os textos em uma lista de palavras substituindo as virgulas



# Tratando os dados com datetime
#moveis = pd.read_json('D:/GitHub/.Estudos-em-Python/Alura/G8 - ONE - TECH FOUNDATION - Especialização Data Science/02 - Aprendendo a fazer ETL/02 - Pandas - Manipulação e análise de dados/Transformação e Manipulação de Dados/01 - Manipulando dados com pandas/dados/moveis_disponiveis.json')
#print('\n', moveis.head())




