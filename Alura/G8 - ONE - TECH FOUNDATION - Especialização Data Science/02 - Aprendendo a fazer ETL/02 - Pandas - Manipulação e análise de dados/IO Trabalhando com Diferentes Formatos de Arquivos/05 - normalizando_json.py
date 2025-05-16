import pandas as pd

# Normalizando um objeto com atributos em chave e valor
dados = {'Pesquisa': 'Principais Indicadores de Doenca Cardiaca', 'Ano': 2020, 'Numero_Pacientes':3}
print('\n', pd.json_normalize(dados))


# Normalizando uma lista com objetos em chave e valor
json_lista = [
    { 'ID': '01', 'Faixa_etaria': '55-59', 'Sexo_biologico': 'feminino'},
    { 'ID': '02', 'Faixa_etaria': '80 ou +', 'Sexo_biologico': 'feminino'}
]
print('\n', pd.json_normalize(json_lista))


# Normalizando uma lista aninhada
json_obj = {
    'ID': '01',
    'Faixa_etaria': '55-59',
    'Sexo_biologico': 'Feminino',
    'Saude': {'Dificuldade_caminhar': 'Nao',
              'Atividade_fisica': 'Sim',
              'IMC': 16.6,
              'Doenca_cardiaca': 'Nao',
          }
      }
print('\n', pd.json_normalize(json_obj))


# Normalizando uma lista aninhada de dicionários
json_list = [
    {
    'ID': '01',
    'Faixa_etaria': '55-59',
    'Sexo_biologico': 'Feminino',
    'Saude': {'Dificuldade_caminhar': 'Nao',
              'Atividade_fisica': 'Sim',
              'IMC': 16.6,
              'Doenca_cardiaca': 'Nao',
          }
      },
      {
          'ID': '02',
          'Faixa_etaria': '80 ou +',
          'Sexo_biologico': 'Feminino',
          'Saude': {'Dificuldade_caminhar': 'Nao',
                    'Atividade_fisica': 'Sim',
                    'IMC': 20.34,
                    'Doenca_cardiaca': 'Sim'}
       }
       ]
print('\n', pd.json_normalize(json_list))


# Normalizando dados de Pacientes do docionário
dados_dict = {
  "Pesquisa": "Principais Indicadores de Doenca Cardiaca",
  "Ano": 2020,
  "Pacientes": [
    {
      "ID": "01",
      "Faixa_etaria": "55-59",
      "Sexo_biologico": "Feminino",
      "Raça": "Branca",
      "IMC": 16.6,
      "Fumante": "Sim",
      "Consumo_alcool": "Nao",
      "Saude_fisica": 3,
      "Saude_mental": 30,
      "Dificuldade_caminhar": "Nao",
      "Atividade_fisica": "Sim",
      "Saude_geral": "Muito boa",
      "Horas_sono": 5,
      "Problemas_saude": [
        "Diabetes",
        "Asma",
        "Cancer_pele"
      ]
    },
    {
      "ID": "02",
      "Faixa_etaria": "80 ou +",
      "Sexo_biologico": "Feminino",
      "Raça": "Branca",
      "IMC": 20.34,
      "Fumante": "Nao",
      "Consumo_alcool": "Nao",
      "Saude_fisica": 0,
      "Saude_mental": 0,
      "Dificuldade_caminhar": "Nao",
      "Atividade_fisica": "Sim",
      "Saude_geral": "Muito boa",
      "Horas_sono": 7,
      "Problemas_saude": [
        "AVC"
      ]
    },
    {
      "ID": "03",
      "Faixa_etaria": "65-69",
      "Sexo_biologico": "Masculino",
      "Raça": "Branca",
      "IMC": 26.58,
      "Fumante": "Sim",
      "Consumo_alcool": "Nao",
      "Saude_fisica": 20,
      "Saude_mental": 30,
      "Dificuldade_caminhar": "Nao",
      "Atividade_fisica": "Sim",
      "Saude_geral": "Muito boa",
      "Horas_sono": 8,
      "Problemas_saude": [
        "diabetes",
        "Asma"
      ]
    }
  ]
}
print('\n', pd.json_normalize(dados_dict['Pacientes']))



''' 
    Utilizando parametros para normalizar
    record_path: especifica o caminho para os registros que devem ser normalizados em um DataFrame separado
    meta: especifica outras colunas que queremos no DataFrame
'''
print('\n', pd.json_normalize(dados_dict, record_path =['Pacientes'], meta=['Pesquisa', 'Ano']))