import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_json('Alura/G8 ONE - Especialização Data Science/Encare o Challenge Alura Store/Challenge Telecom X - Análise de Evasão de Clientes/TelecomX_Data.json')


print(df.info()) # Verificar estrutura básica
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

print("\nNúmero de linhas duplicadas:", df.duplicated().sum()) # Verificar valores duplicados
print("\nValores únicos em 'Churn':", df['Churn'].unique()) # Verificar valores únicos nas colunas categóricas



# Tratando as Inconsistências
df['Churn'] = df['Churn'].replace('', np.nan)
print("Valores ausentes em 'Churn' após tratamento:", df['Churn'].isnull().sum())

df = df.dropna(subset=['Churn'])

customer_df = pd.json_normalize(df['customer'])
phone_df = pd.json_normalize(df['phone'])
internet_df = pd.json_normalize(df['internet'])
account_df = pd.json_normalize(df['account'])

df_clean = pd.concat([
    df[['customerID', 'Churn']],
    customer_df,
    phone_df,
    internet_df,
    account_df
], axis=1)

print("\nInformações após limpeza:")
print(df_clean.info())



# Coluna de Contas Diárias
if df_clean['Charges.Total'].dtype == 'object':
    df_clean['Charges.Total'] = pd.to_numeric(df_clean['Charges.Total'], errors='coerce')

df_clean['Contas_Diarias'] = df_clean['Charges.Total'] / df_clean['tenure']



# Padronização e Transformação de Dados
binary_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
for col in binary_cols:
    df_clean[col] = df_clean[col].map({'Yes': 1, 'No': 0})

df_clean['MultipleLines'] = df_clean['MultipleLines'].replace({'No phone service': 0, 'No': 0, 'Yes': 1})

internet_services = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
                    'TechSupport', 'StreamingTV', 'StreamingMovies']

for col in internet_services:
    df_clean[col] = df_clean[col].replace({'No internet service': 0, 'No': 0, 'Yes': 1})

df_clean = df_clean.rename(columns={
    'gender': 'Genero',
    'SeniorCitizen': 'Idoso',
    'tenure': 'Tempo_Contrato',
    'InternetService': 'Servico_Internet',
    'Contract': 'Tipo_Contrato',
    'PaymentMethod': 'Metodo_Pagamento',
    'Charges.Monthly': 'Faturamento_Mensal',
    'Charges.Total': 'Faturamento_Total'
})



# Análise Descritiva
print(df_clean.describe())
print("\nDistribuição de categorias:")
print(df_clean['Genero'].value_counts())
print(df_clean['Servico_Internet'].value_counts())
print(df_clean['Tipo_Contrato'].value_counts())
print(df_clean['Metodo_Pagamento'].value_counts())



# Distribuição da Evasão
plt.figure(figsize=(6,4))
sns.countplot(x='Churn', data=df_clean)
plt.title('Distribuição de Churn')
plt.show()

churn_rate = df_clean['Churn'].value_counts(normalize=True) * 100
print("\nTaxa de Churn:")
print(churn_rate)



# Contagem de Evasão por Variáveis Categóricas
def plot_churn_by_category(column):
    plt.figure(figsize=(10,5))
    sns.countplot(x=column, hue='Churn', data=df_clean)
    plt.title(f'Churn por {column}')
    plt.xticks(rotation=45)
    plt.show()
    
    ct = pd.crosstab(df_clean[column], df_clean['Churn'], normalize='index') * 100
    print(f"\nTaxa de Churn por {column}:")
    print(ct)

plot_churn_by_category('Genero')
plot_churn_by_category('Servico_Internet')
plot_churn_by_category('Tipo_Contrato')
plot_churn_by_category('Metodo_Pagamento')




# Contagem de Evasão por Variáveis Numéricas
def compare_numeric_distribution(column):
    plt.figure(figsize=(10,5))
    sns.boxplot(x='Churn', y=column, data=df_clean)
    plt.title(f'Distribuição de {column} por Churn')
    plt.show()
    
    print(f"\nEstatísticas de {column} por Churn:")
    print(df_clean.groupby('Churn')[column].describe())

compare_numeric_distribution('Tempo_Contrato')
compare_numeric_distribution('Faturamento_Mensal')
compare_numeric_distribution('Faturamento_Total')
compare_numeric_distribution('Contas_Diarias')




# Extra: Análise de Correlação entre Variáveis
df_corr = df_clean.copy()
df_corr['Churn'] = df_corr['Churn'].map({'Yes': 1, 'No': 0})

df_corr['Genero'] = df_corr['Genero'].map({'Male': 1, 'Female': 0})
df_corr['Tipo_Contrato'] = df_corr['Tipo_Contrato'].map({
    'Month-to-month': 0,
    'One year': 1,
    'Two year': 2
})

corr = df_corr.corr()

plt.figure(figsize=(12,8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlação')
plt.show()

print("\nCorrelação com Churn:")
print(corr['Churn'].sort_values(ascending=False))