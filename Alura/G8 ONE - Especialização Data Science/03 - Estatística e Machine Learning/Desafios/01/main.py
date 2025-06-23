'''
Análise da Pesquisa Nacional por Amostra de Domicílios - 2015
Utilizando os conhecimentos adquiridos ao longo do curso, você precisará realizar uma análise descritiva básica de um conjunto de dados 
retirados da Pesquisa Nacional por Amostra de Domicílios - 2015 do IBGE. Vamos dividir esse processo aula a aula de acordo com o que 
aprendemos no momento, respondendo às perguntas levantadas e interpretando os dados. Dentro do notebook você conseguirá entender sobre 
a base, quais dados foram levantados e o que eles representam.

Case Aula 01:
Neste primeiro momento, você está treinando para ser uma pessoa cientista de dados e recebeu a demanda de investigar os dados da PNAD 
de 2015. A fim de testar as suas habilidades de análise de dados e os conceitos da estatística descritiva, siga as seguintes instruções:

- Importe o dataset e armazene o conteúdo em um data.frame: no documento já consta a url, mas você precisa passar o arquivo .csv que 
está nela para uma variável.

- Visualize o conteúdo do data.frame e leia as infos sobre os dados (linhas, colunas, tipos): Observe brevemente os dados usando as 
funções de leitura dos dados e visualize os tipos de dados.

- Explore brevemente a variável UF e investigue quantos dados possuímos para cada estado: observe quantos valores distintos temos na 
variável, conte as ocorrências em cada caso e crie um gráfico de barras horizontal com esses dados.

- Transforme as variáveis Sexo, Cor e Anos.de.Estudo em categorical e observe o resultado: crie colunas que tratam as variáveis categóricas 
nominais e ordinais de dados numéricos. Siga as instruções e dados trazidos no documento. Leia no final a nova tabela com os dados transformados.

- Apresente em texto a menor e maior Renda da base de dados: Utilize a função print juntamente a formatação de dados f-string como explicada 
no documento para exibir estes dados.

https://cdn3.gnarususercontent.com.br/4217%20-%20Estat%C3%ADstica%20com%20Python%20frequ%C3%AAncias%20e%20medidas/Projeto/estatistica-python-frequencias-medidas/Aula%2001/Desafios.ipynb

'''

link = 'https://www.ibge.gov.br/estatisticas/sociais/populacao/9127-pesquisa-nacional-por-amostra-de-domicilios.html?edicao=9128'
