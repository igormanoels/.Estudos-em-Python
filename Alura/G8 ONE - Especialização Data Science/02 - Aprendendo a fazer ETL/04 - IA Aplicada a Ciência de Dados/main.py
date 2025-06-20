import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

clientes = pd.read_csv('D:/GitHub/.Estudos-em-Python/Alura/G8 ONE - Especialização Data Science/02 - Aprendendo a fazer ETL/04 - IA Aplicada a Ciência de Dados/dados/zoop_clientes.csv')
vendas = pd.read_csv('D:/GitHub/.Estudos-em-Python/Alura/G8 ONE - Especialização Data Science/02 - Aprendendo a fazer ETL/04 - IA Aplicada a Ciência de Dados/dados/zoop_vendas.csv')
cadastro = pd.read_csv('D:/GitHub/.Estudos-em-Python/Alura/G8 ONE - Especialização Data Science/02 - Aprendendo a fazer ETL/04 - IA Aplicada a Ciência de Dados/dados/cadastro_zoop_pay.csv')

'''
PROMPT 1
Vamos atuar como analista de dados de um e-commerce. Recebemos duas bases de dados com os dados dos clientes e das vendas em 2023, respectivamente.

Neste primeiro momento, vamos explorar a base clientes no formato de um DataFrame, chamado "clientes". Ela contém dados dos clientes que realizaram comprar na loja virtual, sendo eles: ID da compra, ID do cliente, a cidade, estado e região da compra, idade, sexo biológico, se participam do programa de cashback e avaliação da compra.

Queremos fazer uma breve exploração dos dados para compreender um pouco sobre eles. Lembrando que os dados desta base já estão limpos e tratados. Construa um código para executar esta etapa usando o Python.

Não é necessário utilizar "print()" para mostrar o resultado das consultas.
'''
# Visualizando as primeiras linhas para entender a estrutura
print(clientes.head(),'\n')

# Verificando informações gerais sobre o DataFrame
print(clientes.info(),'\n')

# Estatísticas descritivas para variáveis numéricas
print(clientes.describe(),'\n')

# Verificando a distribuição por sexo biológico
print(clientes['sexo_biologico'].value_counts(),'\n')
print(clientes['regiao'].value_counts(),'\n') # Análise por região

# Verificando participação no programa de cashback
print(clientes['cashback'].value_counts(normalize=True),'\n')

# Análise da distribuição de idade
print('Média de idade: ', clientes['idade'].mean(),'\n')


# Verificando avaliação média por região
print(clientes.groupby('regiao')['avaliacao_compra'].mean(),'\n')

# Verificando a distribuição de estados
print(clientes['cidade'].value_counts(),'\n')

# Correlação entre idade e avaliação da compra
print(clientes[['idade', 'avaliacao_compra']].corr(),'\n')





####################################################################################################################################################################
'''
PROMPT 2
Agora vamos explorar a base de vendas no formato de um DataFrame, chamado "vendas". Ela contém dados das vendas do e-commerce, sendo eles: 
ID da compra, data da compra, horário da compra, categoria do produto, preco unitário do produto, quantidade vendida, frete e o método do pagamento.

Queremos fazer uma breve exploração dos dados para compreender um pouco sobre eles. Lembrando que os dados desta base também já estão limpos e tratados. 
Construa um código para executar esta etapa usando o Python.
'''
# Visualizando as primeiras linhas
print(vendas.head(), '\n')

# Informações gerais sobre a estrutura do DataFrame
print(vendas.info(), '\n')

# Estatísticas descritivas das variáveis numéricas
print(vendas.describe(), '\n')

# Verificando a distribuição por categoria de produto
print(vendas['categoria'].value_counts(), '\n')

# Análise dos métodos de pagamento mais utilizados
print(vendas['metodo_pagamento'].value_counts(normalize=True), '\n')

# Criando uma coluna de valor total (preço unitário * quantidade + frete)
vendas['valor_total'] = (vendas['preco_unitario'] * vendas['quantidade']) + vendas['frete']
print('Valor total: ', vendas['valor_total'], '\n')

# Estatísticas do valor total das vendas
print(vendas['valor_total'].describe(), '\n')

# Distribuição das vendas por horário
print(vendas['horario'].value_counts().sort_index(), '\n')

# Análise da frequência de fretes gratuitos
print(vendas['frete'].apply(lambda x: 'Grátis' if x == 0 else 'Pago').value_counts(), '\n')

# Média de valor total por categoria de produto
print(vendas.groupby('categoria')['valor_total'].mean().sort_values(ascending=False), '\n')

# Relação entre método de pagamento e valor total médio
print(vendas.groupby('metodo_pagamento')['valor_total'].mean(), '\n')

# Verificando a distribuição temporal das vendas (se a coluna de data estiver no formato datetime)
if 'data_compra' in vendas.columns:
    vendas['data_compra'] = pd.to_datetime(vendas['data_compra'])
    vendas['mes_compra'] = vendas['data_compra'].dt.month
    vendas['mes_compra'].value_counts().sort_index()
    print(vendas['mes_compra'], '\n')





####################################################################################################################################################################
'''
PROMPT 3
Vamos agora unir as duas bases do nosso projeto em uma só utilizando como chave a coluna "ID_compra". Além disso, vamos organizar as colunas na seguinte sequência:

- ID_compra
- data
- horario
- categoria
- preco_unitario
- quantidade
- frete
- metodo_pagamento
- ID_cliente
- idade
- sexo_biologico
- cidade
- uf
- regiao
- cashback
- avaliacao_compra

Construa um código para executar esta etapa usando o Python e a biblioteca Pandas.
'''
# Realizando o merge das bases
dados_completos = pd.merge(
    vendas,
    clientes,
    on='ID_compra',
    how='inner'  # Usando inner join para manter apenas compras presentes em ambas as bases
)

# Renomeando colunas para padronização (se necessário)
dados_completos = dados_completos.rename(columns={
    'data_compra': 'data',
    'horario_compra': 'horario',
    'categoria_produto': 'categoria',
    'metodo_pagamento': 'metodo_pagamento',
    'cashback': 'cashback'
})

# Definindo a ordem das colunas conforme solicitado
ordem_colunas = [
    'ID_compra',
    'data',
    'horario',
    'categoria',
    'preco_unitario',
    'quantidade',
    'frete',
    'metodo_pagamento',
    'ID_cliente',
    'idade',
    'sexo_biologico',
    'cidade',
    'uf',
    'regiao',
    'cashback',
    'avaliacao_compra'
]

# Reorganizando o DataFrame
dados_completos = dados_completos[ordem_colunas]

# Verificando o resultado
dados_completos.head()





####################################################################################################################################################################
'''
PROMPT 4
Agora com o nosso "df" já construído por meio das duas bases do projeto, vamos iniciar um novo processo. Queremos iniciar a etapa da 
geração dos visuais que possam auxiliar na análise do faturamento ao longo do ano, perfil do cliente e outros dados que possam ser 
relevantes à análise e construção do nosso storytelling.

As colunas de "df" são:

- ID_compra: número único atribuído a compra realizada, no formato int
- data: data da compra, no formato datetime
- horario: horário da compra no formato object
- categoria: categoria do produto, no formato object
- preco_unitario: preço de uma unidade do produto, no formato float
- quantidade: quantidade vendida do produto, no formato int
- frete: frete a ser pago no total da compra, no formato float
- metodo_pagamento: método de pagamento da compra, no formato object
- ID_cliente: número único atribuído ao cliente, no formato int
- idade: idade do cliente, no formato int
- sexo_biologico: sexo biológico do cliente, no formato object
- cidade: cidade do cliente, no formato object
- uf: unidade federativa do cliente, no formato object
- regiao: região do cliente, no formato object
- cashback: se o cliente participa ou não do programa de cashback da loja, no formato object
- avaliacao_compra: avaliação do cliente pela compra, no formato int

O objetivo é abstrair e buscar relações para construir visuais interessantes para a análise dos dados dos clientes e vendas da Zoop.

Com base nas informações fornecidas, quais tipos de visualizações seriam úteis para atingir o objetivo de analisar os dados?
'''

####################################################################################################################################################################
'''
RESPOSTA
# Visualizações para Análise de Dados do E-commerce

Com base nas colunas disponíveis, sugiro as seguintes visualizações para uma análise abrangente do faturamento, perfil do cliente e padrões de compra:

## 1. Análise Temporal de Vendas
- **Série temporal mensal de faturamento**: Gráfico de linha mostrando a evolução do faturamento (preco_unitario * quantidade + frete) ao longo dos meses
- **Vendas por dia da semana**: Gráfico de barras mostrando em quais dias ocorrem mais vendas
- **Heatmap de vendas**: Combinação de dia da semana vs horário para identificar picos de compra

## 2. Análise por Categoria de Produto
- **Faturamento por categoria**: Gráfico de barras horizontais ou treemap mostrando as categorias que mais geram receita
- **Quantidade vendida por categoria**: Gráfico de pizza ou barras mostrando participação de cada categoria no volume total
- **Ticket médio por categoria**: Gráfico de barras comparando o valor médio gasto em cada categoria

## 3. Perfil Demográfico dos Clientes
- **Distribuição por faixa etária**: Histograma ou gráfico de densidade mostrando a distribuição de idades
- **Proporção por gênero**: Gráfico de pizza ou barras mostrando divisão por sexo biológico
- **Mapa de calor por região/UF**: Mapa coroplético mostrando concentração de clientes ou vendas por região

## 4. Métodos de Pagamento e Frete
- **Métodos de pagamento mais usados**: Gráfico de barras ou pizza mostrando a preferência dos clientes
- **Relação entre método de pagamento e valor gasto**: Boxplot comparando os valores por método
- **Proporção de fretes gratuitos vs pagos**: Gráfico de donut mostrando esta divisão

## 5. Análise de Avaliação e Fidelização
- **Distribuição das avaliações**: Gráfico de barras mostrando a frequência de cada nota
- **Avaliação média por categoria**: Gráfico de barras comparando satisfação por tipo de produto
- **Participação no cashback**: Gráfico de pizza mostrando proporção de clientes no programa

## 6. Relações Cruzadas
- **Faturamento por região e categoria**: Gráfico de barras agrupadas
- **Idade vs valor gasto**: Gráfico de dispersão com linha de tendência
- **Método de pagamento preferido por faixa etária**: Gráfico de barras empilhadas

## Visualizações Avançadas (Storytelling)
- **Painel de métricas-chave**: Mostrando faturamento total, ticket médio, clientes únicos, etc.
- **Customer Journey**: Fluxograma mostrando o caminho típico do cliente (categoria → método pagamento → avaliação)
- **Análise de cohort**: Retenção de clientes ao longo do tempo

Cada uma dessas visualizações pode ser implementada usando bibliotecas como Matplotlib, Seaborn ou Plotly, dependendo do nível de interatividade desejado. 
A escolha específica dependerá dos insights mais relevantes para o negócio da Zoop.

'''





####################################################################################################################################################################
'''
PROMPT 5
Temos um DataFrame chamado "df" e queremos construir um visual que apresente quais métodos de pagamentos foram os mais utilizados.

Em "df", temos a coluna "metodo_pagamento" com os 4 tipos de pagamento utilizado na compra.

Inicialmente, queremos construir uma tabela chamada "metodos_de_pagamento" que resuma os dados dessa coluna e, na sequência, desejamos criar uma visualização que apresente a quantidade desses métodos de pagamento presentes na tabela "metodo_pagamento".

Utilize as bibliotecas de visualização de dados do Python para criar essa visualização.
'''

# 1. Criando a tabela resumo "metodos_de_pagamento"
metodos_de_pagamento = dados_completos['metodo_pagamento'].value_counts().reset_index()
metodos_de_pagamento.columns = ['metodo_pagamento', 'quantidade']
metodos_de_pagamento['percentual'] = (metodos_de_pagamento['quantidade'] / metodos_de_pagamento['quantidade'].sum()) * 100

# 2. Visualização dos métodos de pagamento
plt.figure(figsize=(10, 6))

# Gráfico de barras
ax = sns.barplot(
    x='metodo_pagamento', 
    y='quantidade', 
    data=metodos_de_pagamento,
    palette='viridis',
    order=metodos_de_pagamento.sort_values('quantidade', ascending=False)['metodo_pagamento']
)

# Adicionando rótulos e título
plt.title('Métodos de Pagamento Mais Utilizados', fontsize=16, pad=20)
plt.xlabel('Método de Pagamento', fontsize=12)
plt.ylabel('Quantidade de Transações', fontsize=12)

# Adicionando os valores nas barras
for p in ax.patches:
    ax.annotate(
        f'{int(p.get_height())}\n({p.get_height()/metodos_de_pagamento["quantidade"].sum()*100:.1f}%)', 
        (p.get_x() + p.get_width() / 2., p.get_height()), 
        ha='center', 
        va='center', 
        xytext=(0, 10), 
        textcoords='offset points',
        fontsize=10
    )

# Ajustando layout
plt.tight_layout()
plt.show()

# Retornando a tabela resumo para possível uso posterior
metodos_de_pagamento





####################################################################################################################################################################
'''
PROMPT 6
Temos um DataFrame chamado "df" e queremos construir um visual de gráfico de barras horizontais que apresente o faturamento por categoria da Zoop.

Em "df", temos as colunas:

categoria: categorias dos produtos

preco_unitario: preço de uma unidade do produto

quantidade: quantidade vendida do produto

frete: frete a ser pago no total da compra.

Desejamos criar uma visualização que apresente o faturamento de cada categoria, em que o faturamento é dado pelo produto entre o preço unitário e a quantidade somadas ao frete.

Utilize as bibliotecas de visualização de dados do Python para criar essa visualização.
'''
# 1. Calcular o faturamento por categoria
dados_completos['faturamento'] = (dados_completos['preco_unitario'] * dados_completos['quantidade']) + dados_completos['frete']
faturamento_por_categoria = dados_completos.groupby('categoria')['faturamento'].sum().sort_values(ascending=True)

# 2. Configurações do gráfico
plt.figure(figsize=(12, 8))
sns.set_style("whitegrid")
colors = sns.color_palette("viridis", len(faturamento_por_categoria))

# 3. Criar o gráfico de barras horizontais
ax = faturamento_por_categoria.plot(
    kind='barh',
    color=colors,
    edgecolor='black',
    linewidth=0.5
)

# 4. Adicionar rótulos e formatação
plt.title('Faturamento Total por Categoria', fontsize=16, pad=20)
plt.xlabel('Faturamento (R$)', fontsize=12)
plt.ylabel('Categoria', fontsize=12)

# Formatar valores no eixo X para exibir em milhares/milhões
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Adicionar os valores nas barras
for i, v in enumerate(faturamento_por_categoria):
    ax.text(v + faturamento_por_categoria.max()*0.01, 
            i, 
            f'R$ {v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'), 
            color='black',
            va='center',
            fontsize=10)

# 5. Ajustar layout e mostrar
plt.tight_layout()
plt.show()





####################################################################################################################################################################
'''
PROMPT 7
Temos um DataFrame chamado "df" e queremos construir um visual de gráfico de linha que apresente as vendas totais mensais da Zoop.

Em "df", temos as colunas:

data: com as datas das compras no formato datetime (aaaa-mm-dd)
faturamento: dado pelo produto entre o preço unitário e a quantidade somadas ao frete de cada venda.
Desejamos criar uma visualização que apresente as vendas por mês. Prmeiro, agrupe os dados por mês e depois crie uma nova coluna chamada "mes" 
que receba o nome de cada mês, traduzindo os meses do índice por meio do dicionário abaixo. Utilize a coluna "data" para o agrupamento dos dados 
e construção do gráfico. A coluna "mes" só deve ser utilizada para alterar os rótulos do eixo x.

meses = { 'January': 'Jan', 'February': 'Fev', 'March': 'Mar', 'April': 'Abr', 'May': 'Mai', 'June': 'Jun', 'July': 'Jul', 'August': 'Ago', 
'September': 'Set', 'October': 'Out', 'November': 'Nov', 'December': 'Dez' }

Utilize as bibliotecas de visualização de dados do Python para criar essa visualização.
'''
# Dicionário para tradução dos meses
meses = {
    'January': 'Jan', 'February': 'Fev', 'March': 'Mar', 
    'April': 'Abr', 'May': 'Mai', 'June': 'Jun',
    'July': 'Jul', 'August': 'Ago', 'September': 'Set',
    'October': 'Out', 'November': 'Nov', 'December': 'Dez'
}

# 1. Converter a coluna 'data' para datetime (caso ainda não esteja)
dados_completos['data'] = pd.to_datetime(dados_completos['data'])

# 2. Agrupar dados por mês usando a nova frequência 'ME' (Mensal)
vendas_mensais = dados_completos.groupby(pd.Grouper(key='data', freq='ME'))['faturamento'].sum().reset_index()

# 3. Criar coluna com nome do mês em português
vendas_mensais['mes_nome'] = vendas_mensais['data'].dt.strftime('%B').map(meses)
vendas_mensais['ano_mes'] = vendas_mensais['data'].dt.strftime('%Y-%m')  # Para ordenação

# 4. Ordenar por data cronológica
vendas_mensais = vendas_mensais.sort_values('ano_mes')

# 5. Configurar o gráfico
plt.figure(figsize=(14, 7))
sns.set_style("whitegrid")

# 6. Criar gráfico de linha (corrigindo o warning da paleta)
ax = sns.lineplot(
    data=vendas_mensais,
    x='mes_nome',
    y='faturamento',
    hue='mes_nome',  
    palette='viridis',
    marker='o',          # Formato dos pontos (pode ser 'o', 's', 'D', etc.)
    markersize=8,        # Tamanho dos pontos
    linewidth=2.5,       # Espessura da linha
    linestyle='-',       # Estilo da linha (sólida, tracejada, etc.)
    legend=False         # Remove a legenda redundante
)

# 7. Personalizar o gráfico
plt.title('Vendas Mensais da Zoop', fontsize=16, pad=20)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Faturamento Total (R$)', fontsize=12)

# Formatar eixos
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"R$ {x/1000:,.0f}K"))
plt.xticks(rotation=45)

# Adicionar valores nos pontos
for x, y in zip(vendas_mensais['mes_nome'], vendas_mensais['faturamento']):
    ax.text(
        x, 
        y + vendas_mensais['faturamento'].max()*0.02, 
        f'R$ {y/1000:,.1f}K'.replace('.', ','), 
        ha='center',
        fontsize=10
    )

# 8. Ajustar layout e mostrar
plt.tight_layout()
plt.show()





####################################################################################################################################################################
'''
PROMPT 8
Temos um DataFrame chamado "df" e queremos construir um visual de gráfico de barras empilhadas que apresente as vendas por trimestre em relação ao método de pagamento da Zoop.

Em "df", temos as colunas:

data: com as datas das compras no formato datetime (aaaa-mm-dd)

faturamento: com os valores das vendas

metodo_pagamento: com o método de pagamento escolhido na compra

Desejamos criar uma visualização que apresente as vendas por trimestre, agrupando os métodos de pagamento de cada trimestre correspondente a cada compra.

Utilize as bibliotecas de visualização de dados do Python para criar essa visualização.
'''
# 1. Converter a coluna 'data' para datetime (caso ainda não esteja)
dados_completos['data'] = pd.to_datetime(dados_completos['data'])

# 2. Extrair trimestre e ano da data
dados_completos['trimestre'] = dados_completos['data'].dt.to_period('Q').astype(str)
dados_completos['ano'] = dados_completos['data'].dt.year

# 3. Criar uma coluna combinada de ano-trimestre para melhor visualização
dados_completos['ano_trimestre'] = dados_completos['ano'].astype(str) + ' - T' + dados_completos['trimestre'].str[-1]

# 4. Agrupar por trimestre e método de pagamento
vendas_trimestre = dados_completos.groupby(['ano_trimestre', 'metodo_pagamento'])['faturamento'].sum().unstack()

# 5. Configurar o gráfico
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")

# 6. Criar gráfico de barras empilhadas
vendas_trimestre.plot(
    kind='bar',
    stacked=True,
    colormap='viridis',
    edgecolor='black',
    linewidth=0.5,
    figsize=(14, 8)
)

# 7. Personalizar o gráfico
plt.title('Vendas por Trimestre e Método de Pagamento', fontsize=16, pad=20)
plt.xlabel('Trimestre', fontsize=12)
plt.ylabel('Faturamento Total (R$)', fontsize=12)

# Formatar eixo Y em valores monetários
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"R$ {x/1000:,.0f}K"))

# Adicionar legenda
plt.legend(title='Método de Pagamento', bbox_to_anchor=(1.05, 1), loc='upper left')

# Rotacionar labels do eixo X para melhor visualização
plt.xticks(rotation=45, ha='right')

# 8. Ajustar layout e mostrar
plt.tight_layout()
plt.show()