import pandas as pd
import numpy as np
from collections import Counter
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler  # type: ignore
from sklearn.pipeline import Pipeline  # type: ignore
from sklearn.model_selection import train_test_split, GridSearchCV  # type: ignore
from sklearn.inspection import permutation_importance  # type: ignore
from sklearn.linear_model import LogisticRegression  # type: ignore
from sklearn.neighbors import KNeighborsClassifier  # type: ignore
from sklearn.svm import SVC  # type: ignore
from sklearn.ensemble import RandomForestClassifier  # type: ignore
from sklearn.metrics import ( # pyright: ignore[reportMissingModuleSource]
    classification_report, 
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score, 
    confusion_matrix,
    roc_auc_score,
    RocCurveDisplay
)  # type: ignore
from imblearn.under_sampling import RandomUnderSampler  # type: ignore
from imblearn.over_sampling import RandomOverSampler, SMOTE  # type: ignore
from xgboost import XGBClassifier # type: ignore

# Carregar os dados
dados = pd.read_json('Alura/G8 ONE - Especialização Data Science/Encare o Challenge Alura Store/Challenge Telecom X - Análise de Evasão de Clientes v2/TelecomX_Data.json')

# 1. Remover coluna customerID (como feito anteriormente)
dados.drop(columns=['customerID'], inplace=True)

# 2. Desaninhar as colunas JSON
# Criar DataFrames separados para cada grupo aninhado
customer_df = pd.json_normalize(dados['customer'])
phone_df = pd.json_normalize(dados['phone'])
internet_df = pd.json_normalize(dados['internet'])
account_df = pd.json_normalize(dados['account'])
charges_df = pd.json_normalize(dados['account'].apply(lambda x: x['Charges']))

# Juntar tudo em um único DataFrame
dados_flat = pd.concat([
    dados[['Churn']],
    customer_df,
    phone_df,
    internet_df,
    account_df.drop(columns=['Charges']),
    charges_df
], axis=1)

# 3. Identificar colunas categóricas
categorical_cols = dados_flat.select_dtypes(include=['object', 'bool']).columns.tolist()

# Remover 'Churn' pois será nossa variável target (vamos tratá-la separadamente)
categorical_cols.remove('Churn')

# 4. Aplicar One-Hot Encoding
encoder = OneHotEncoder(drop='first', sparse_output=False)  # drop='first' para evitar multicolinearidade
encoded_data = encoder.fit_transform(dados_flat[categorical_cols])

# Criar DataFrame com as colunas codificadas
encoded_df = pd.DataFrame(
    encoded_data,
    columns=encoder.get_feature_names_out(categorical_cols)
)

# 5. Juntar com as colunas numéricas e a variável target
numerical_cols = dados_flat.select_dtypes(exclude=['object', 'bool']).columns.tolist()
final_df = pd.concat([
    dados_flat[numerical_cols],
    encoded_df,
    dados_flat['Churn']  # variável target
], axis=1)

# 6. Converter a variável target para numérica (0 para 'No', 1 para 'Yes')
final_df['Churn'] = final_df['Churn'].map({'No': 0, 'Yes': 1})

# Verificar o resultado
print(final_df.head())
print("\nColunas após one-hot encoding:")
print(final_df.columns.tolist())





'''
Análise de Desequilíbrio de Classes (Churn)
'''
# Supondo que 'final_df' seja o DataFrame após o pré-processamento anterior
# Se não tiver carregado ainda, carregue os dados conforme mostrado anteriormente

# 1. Calcular a distribuição da variável target
distribuicao_churn = final_df['Churn'].value_counts()

# 2. Calcular proporções
proporcao_churn = final_df['Churn'].value_counts(normalize=True) * 100

# 3. Exibir resultados
print("Distribuição absoluta de Churn:")
print(distribuicao_churn)
print("\nDistribuição percentual de Churn:")
print(proporcao_churn)

# 4. Visualização gráfica
plt.figure(figsize=(8, 5))
plt.bar(['Não Evadiram (0)', 'Evadiram (1)'], distribuicao_churn, color=['blue', 'red'])
plt.title('Distribuição de Churn')
plt.ylabel('Número de Clientes')
plt.text(0, distribuicao_churn[0], f'{proporcao_churn[0]:.1f}%', ha='center', va='bottom')
plt.text(1, distribuicao_churn[1], f'{proporcao_churn[1]:.1f}%', ha='center', va='bottom')
plt.show()

# 5. Avaliação do desequilíbrio
desequilibrio = distribuicao_churn[0] / distribuicao_churn[1]
print(f"\nRazão de desequilíbrio: {desequilibrio:.1f}:1 (Não Evadiram:Evadiram)")

# 6. Interpretação
if desequilibrio > 4:
    print("\nALERTA: Desequilíbrio significativo entre as classes detectado!")
    print("Recomendações:")
    print("- Considerar técnicas de balanceamento (oversampling, undersampling)")
    print("- Usar métricas de avaliação adequadas (precision, recall, F1, AUC-ROC)")
    print("- Considerar class_weight nos modelos para penalizar mais erros na classe minoritária")
elif desequilibrio > 2:
    print("\nDesequilíbrio moderado detectado. Algum cuidado pode ser necessário.")
else:
    print("\nAs classes estão relativamente balanceadas.")





'''
Aplicação de Técnicas de Balanceamento para o Problema de Churn
'''
## Preparação dos dados
# Supondo que 'final_df' já contém os dados pré-processados
X = final_df.drop('Churn', axis=1)
y = final_df['Churn']

# Dividir em treino e teste (manter o teste desbalanceado para avaliação realista)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verificar distribuição original
print("Distribuição original:", Counter(y_train))

## 1. Random Undersampling (reduz a classe majoritária)
under_sampler = RandomUnderSampler(random_state=42)
X_under, y_under = under_sampler.fit_resample(X_train, y_train)
print("\nDistribuição após undersampling:", Counter(y_under))

## 2. Random Oversampling (replica a classe minoritária)
over_sampler = RandomOverSampler(random_state=42)
X_over, y_over = over_sampler.fit_resample(X_train, y_train)
print("\nDistribuição após oversampling:", Counter(y_over))

## 3. SMOTE (cria amostras sintéticas da classe minoritária)
smote = SMOTE(random_state=42)
X_smote, y_smote = smote.fit_resample(X_train, y_train)
print("\nDistribuição após SMOTE:", Counter(y_smote))

## Visualização comparativa
plt.figure(figsize=(15, 5))

# Original
plt.subplot(1, 4, 1)
plt.bar(['0', '1'], [Counter(y_train)[0], Counter(y_train)[1]], color=['blue', 'red'])
plt.title('Original\n(%.1f%% Evasão)' % (Counter(y_train)[1]/len(y_train)*100))

# Undersampling
plt.subplot(1, 4, 2)
plt.bar(['0', '1'], [Counter(y_under)[0], Counter(y_under)[1]], color=['blue', 'red'])
plt.title('Undersampling\n(50% Evasão)')

# Oversampling
plt.subplot(1, 4, 3)
plt.bar(['0', '1'], [Counter(y_over)[0], Counter(y_over)[1]], color=['blue', 'red'])
plt.title('Oversampling\n(50% Evasão)')

# SMOTE
plt.subplot(1, 4, 4)
plt.bar(['0', '1'], [Counter(y_smote)[0], Counter(y_smote)[1]], color=['blue', 'red'])
plt.title('SMOTE\n(50% Evasão)')

plt.tight_layout()
plt.show()

## Exemplo de aplicação em um modelo (Random Forest)


def evaluate_model(X_train, y_train, X_test, y_test, technique_name):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    print(f"\nAvaliação do modelo com {technique_name}:")
    print(classification_report(y_test, y_pred))

# Avaliar cada abordagem
print("\n=== COMPARAÇÃO DE TÉCNICAS ===")
evaluate_model(X_train, y_train, X_test, y_test, "dados originais")
evaluate_model(X_under, y_under, X_test, y_test, "undersampling")
evaluate_model(X_over, y_over, X_test, y_test, "oversampling")
evaluate_model(X_smote, y_smote, X_test, y_test, "SMOTE")





'''
Avaliação da Necessidade de Normalização/Padronização dos Dados
'''
# Identificar colunas numéricas (excluindo as já codificadas)
numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns

# Padronização (StandardScaler - recomendado para maioria dos casos)
scaler = StandardScaler()
X_scaled = X.copy()
X_scaled[numeric_cols] = scaler.fit_transform(X[numeric_cols])

# Normalização (MinMaxScaler - para casos específicos)
normalizer = MinMaxScaler()
X_normalized = X.copy()
X_normalized[numeric_cols] = normalizer.fit_transform(X[numeric_cols])



# Pipeline para modelos sensíveis à escala
pipeline_lr = Pipeline([
    ('scaler', StandardScaler()),  # Padronização
    ('model', LogisticRegression())
])

pipeline_knn = Pipeline([
    ('scaler', StandardScaler()),
    ('model', KNeighborsClassifier())
])

pipeline_svm = Pipeline([
    ('scaler', StandardScaler()),
    ('model', SVC())
])

# Pipeline para modelos não sensíveis (exemplo)
pipeline_rf = Pipeline([
    ('model', RandomForestClassifier())
])

# Teste comparativo com e sem scaling para um modelo sensível

# Sem scaling
knn = KNeighborsClassifier()
knn.fit(X_train[numeric_cols], y_train)
y_pred = knn.predict(X_test[numeric_cols])
print("Acurácia KNN sem scaling:", accuracy_score(y_test, y_pred))

# Com scaling
knn_scaled = Pipeline([('scaler', StandardScaler()), ('knn', KNeighborsClassifier())])
knn_scaled.fit(X_train[numeric_cols], y_train)
y_pred_scaled = knn_scaled.predict(X_test[numeric_cols])
print("Acurácia KNN com scaling:", accuracy_score(y_test, y_pred_scaled))

# Divida primeiro em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Aplique o scaling APENAS nos dados de treino
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train[numeric_cols])
X_test_scaled = scaler.transform(X_test[numeric_cols])  # Note: só transform, não fit

# Para modelos que não precisam de scaling, use os dados originais





'''
Análise de Correlação para Identificação de Relações entre Variáveis
'''
# 1. Preparar os dados (considerando final_df já pré-processado)
# Selecionar apenas variáveis numéricas (incluindo as codificadas)
numeric_df = final_df.select_dtypes(include=[np.number])

# 2. Calcular a matriz de correlação
corr_matrix = numeric_df.corr()

# 3. Focar na correlação com a variável target (Churn)
churn_corr = corr_matrix['Churn'].sort_values(ascending=False)

# 4. Visualização da correlação com Churn
plt.figure(figsize=(8, 12))
sns.barplot(x=churn_corr.values, y=churn_corr.index, palette='coolwarm')
plt.title('Correlação das Variáveis com Churn')
plt.xlabel('Coeficiente de Correlação')
plt.ylabel('Variáveis')
plt.axvline(0, color='black', linestyle='--')
plt.show()

# 5. Matriz de correlação completa (heatmap)
plt.figure(figsize=(16, 12))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', 
            center=0, linewidths=0.5, annot_kws={"size": 8})
plt.title('Matriz de Correlação Completa', pad=20)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# 6. Identificar as variáveis mais relevantes
print("\nTop 10 variáveis com maior correlação positiva com Churn:")
print(churn_corr.head(10))

print("\nTop 10 variáveis com maior correlação negativa com Churn:")
print(churn_corr.tail(10))

# Identificar pares de variáveis altamente correlacionadas entre si
high_corr_pairs = corr_matrix.abs().stack().sort_values(ascending=False)
high_corr_pairs = high_corr_pairs[high_corr_pairs.between(0.7, 1, inclusive='neither')]
print("\nPares de variáveis com alta correlação entre si:")
print(high_corr_pairs)

# Filtrar apenas correlações relevantes com Churn
significant_corr = churn_corr[abs(churn_corr) > 0.1]
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df[significant_corr.index].corr(), 
            annot=True, cmap='coolwarm', center=0)
plt.title('Correlações Significativas com Churn (|corr| > 0.1)')
plt.show()



'''
Análise de Relação entre Variáveis Específicas e Evasão (Churn)
'''
# 1. Tempo de Contrato (tenure) × Evasão
plt.figure(figsize=(12, 6))

# Boxplot
plt.subplot(1, 2, 1)
sns.boxplot(x='Churn', y='tenure', data=final_df, palette=['#1f77b4', '#ff7f0e'])
plt.title('Distribuição do Tempo como Cliente\npor Status de Evasão')
plt.xlabel('Evasão (0=Não, 1=Sim)')
plt.ylabel('Meses como Cliente')

# Densidade
plt.subplot(1, 2, 2)
sns.kdeplot(data=final_df, x='tenure', hue='Churn', 
            palette=['#1f77b4', '#ff7f0e'], fill=True, common_norm=False)
plt.title('Densidade do Tempo como Cliente')
plt.xlabel('Meses como Cliente')
plt.ylabel('Densidade')
plt.legend(['Não Evadiram', 'Evadiram'])

plt.tight_layout()
plt.show()

# Análise estatística descritiva
print("\nEstatísticas descritivas do tempo como cliente:")
print(final_df.groupby('Churn')['tenure'].describe())



# 2. Total Gasto (TotalCharges) × Evasão
plt.figure(figsize=(12, 6))

# Boxplot
plt.subplot(1, 2, 1)
sns.boxplot(x='Churn', y='TotalCharges', data=final_df, palette=['#1f77b4', '#ff7f0e'])
plt.title('Distribuição do Total Gasto\npor Status de Evasão')
plt.xlabel('Evasão (0=Não, 1=Sim)')
plt.ylabel('Total Gasto ($)')

# Dispersão com linha de tendência
plt.subplot(1, 2, 2)
sns.scatterplot(data=final_df, x='tenure', y='TotalCharges', hue='Churn',
                palette=['#1f77b4', '#ff7f0e'], alpha=0.6)
plt.title('Relação entre Tempo como Cliente e Total Gasto')
plt.xlabel('Meses como Cliente')
plt.ylabel('Total Gasto ($)')
plt.legend(title='Evasão')

plt.tight_layout()
plt.show()

# Análise estatística
print("\nEstatísticas descritivas do total gasto:")
print(final_df.groupby('Churn')['TotalCharges'].describe())



# 3. Análise Conjunta: Tipo de Contrato × Evasão
# Criar uma coluna combinando tenure e contract type
final_df['Contract_Type'] = final_df[['Contract_Month-to-month', 
                                     'Contract_One year', 
                                     'Contract_Two year']].idxmax(axis=1)
final_df['Contract_Type'] = final_df['Contract_Type'].str.replace('Contract_', '')

plt.figure(figsize=(14, 6))

# Violin plot
plt.subplot(1, 2, 1)
sns.violinplot(data=final_df, x='Contract_Type', y='tenure', hue='Churn',
               split=True, palette=['#1f77b4', '#ff7f0e'])
plt.title('Distribuição de Tempo por Tipo de Contrato')
plt.xlabel('Tipo de Contrato')
plt.ylabel('Meses como Cliente')

# Gráfico de barras da taxa de evasão por tipo de contrato
plt.subplot(1, 2, 2)
contract_churn = final_df.groupby('Contract_Type')['Churn'].mean().sort_values()
contract_churn.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title('Taxa de Evasão por Tipo de Contrato')
plt.xlabel('Tipo de Contrato')
plt.ylabel('Taxa de Evasão (%)')
plt.ylim(0, 1)
plt.gca().yaxis.set_major_formatter('{:.0%}'.format)

plt.tight_layout()
plt.show()





'''
Divisão do Conjunto de Dados em Treino e Teste
'''
# 1. Definir variáveis preditoras (X) e variável target (y)
X = final_df.drop('Churn', axis=1)  # Todas as colunas exceto a target
y = final_df['Churn']  # Apenas a coluna target

# 2. Divisão estratificada (mantém proporção de classes em ambos conjuntos)
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.3,  # 30% para teste, 70% para treino
    random_state=42,  # Semente para reprodutibilidade
    stratify=y  # Mantém proporção de classes
)

# 3. Verificar as proporções
print(f"Proporção original: {round(y.value_counts(normalize=True)[1]*100, 1)}% de evasão")
print(f"Proporção no treino: {round(y_train.value_counts(normalize=True)[1]*100, 1)}% de evasão")
print(f"Proporção no teste: {round(y_test.value_counts(normalize=True)[1]*100, 1)}% de evasão")

# 4. Verificar tamanhos dos conjuntos
print(f"\nTotal de amostras: {len(X)}")
print(f"Treino: {len(X_train)} amostras ({len(X_train)/len(X)*100:.1f}%)")
print(f"Teste: {len(X_test)} amostras ({len(X_test)/len(X)*100:.1f}%)")

# 5. Opcional: Salvar os conjuntos para uso futuro

with open('train_test_split.pkl', 'wb') as f:
    pickle.dump((X_train, X_test, y_train, y_test), f)


# Gráfico de proporções
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.pie([len(X_train), len(X_test)], 
        labels=['Treino', 'Teste'], 
        colors=['#1f77b4', '#ff7f0e'],
        autopct='%1.1f%%')
plt.title('Divisão Treino-Teste')

plt.subplot(1, 2, 2)
sns.countplot(x=y_train, palette=['#1f77b4', '#ff7f0e'])
plt.title('Distribuição de Classes no Treino')
plt.xlabel('Churn')
plt.ylabel('Contagem')
plt.xticks([0, 1], ['Não', 'Sim'])

plt.tight_layout()
plt.show()


# Verificar se as estatísticas básicas são similares
print("\nMédias nas variáveis numéricas:")
print("Original:", X.select_dtypes(include='number').mean().head(3))
print("Treino:", X_train.select_dtypes(include='number').mean().head(3))
print("Teste:", X_test.select_dtypes(include='number').mean().head(3))






'''
Implementação de Modelos Preditivos para Evasão de Clientes
'''
# Pipeline com normalização
lr_pipe = Pipeline([
    ('scaler', StandardScaler()),  # Normalização dos dados
    ('model', LogisticRegression(
        class_weight='balanced',  # Ajuste para classes desbalanceadas
        random_state=42,
        max_iter=1000
    ))
])

# Treinamento
lr_pipe.fit(X_train, y_train)

# Avaliação
y_pred_lr = lr_pipe.predict(X_test)
y_proba_lr = lr_pipe.predict_proba(X_test)[:, 1]

print("=== Regressão Logística ===")
print(classification_report(y_test, y_pred_lr))
print(f"AUC-ROC: {roc_auc_score(y_test, y_proba_lr):.4f}")



# Modelo sem necessidade de normalização
rf_model = RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced_subsample',  # Tratamento do desbalanceamento
    random_state=42,
    max_depth=5,  # Evitar overfitting
    n_jobs=-1  # Usar todos os cores do processador
)

# Treinamento
rf_model.fit(X_train, y_train)

# Avaliação
y_pred_rf = rf_model.predict(X_test)
y_proba_rf = rf_model.predict_proba(X_test)[:, 1]

print("\n=== Random Forest ===")
print(classification_report(y_test, y_pred_rf))
print(f"AUC-ROC: {roc_auc_score(y_test, y_proba_rf):.4f}")


plt.figure(figsize=(10, 6))

# Curva ROC Regressão Logística
RocCurveDisplay.from_estimator(lr_pipe, X_test, y_test, name='Regressão Logística')

# Curva ROC Random Forest
RocCurveDisplay.from_estimator(rf_model, X_test, y_test, name='Random Forest')

plt.plot([0, 1], [0, 1], 'k--', label='Aleatório')
plt.title('Comparação de Desempenho - Curva ROC')
plt.xlabel('Taxa de Falso Positivo')
plt.ylabel('Taxa de Verdadeiro Positivo')
plt.legend()
plt.show()

# Extrair importância das features
importances = rf_model.feature_importances_
features = X_train.columns
indices = np.argsort(importances)[-10:]  # Top 10 features

# Visualização
plt.figure(figsize=(10, 6))
plt.title('Top 10 Features Mais Importantes - Random Forest')
plt.barh(range(len(indices)), importances[indices], color='#1f77b4')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Importância Relativa')
plt.tight_layout()
plt.show()


# Exemplo para Random Forest
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(rf_model, param_grid, cv=5, scoring='roc_auc')
grid_search.fit(X_train, y_train)



'''
Avaliação Comparativa de Modelos Preditivos para Churn
'''
# 1. Implementação da Avaliação
# Modelos a serem avaliados
models = {
    "Regressão Logística": LogisticRegression(max_iter=1000, random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "KNN": KNeighborsClassifier()
}

# Dicionário para armazenar resultados
results = {}

# Avaliação de cada modelo
for name, model in models.items():
    # Treinar o modelo
    model.fit(X_train, y_train)
    
    # Previsões
    y_pred = model.predict(X_test)
    y_pred_train = model.predict(X_train)
    
    # Métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    # Armazenar resultados
    results[name] = {
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1': f1,
        'Confusion Matrix': cm,
        'Train Accuracy': accuracy_score(y_train, y_pred_train)
    }

# Exibir resultados
for model_name, metrics in results.items():
    print(f"\n=== {model_name} ===")
    print(f"Acurácia (Treino): {metrics['Train Accuracy']:.4f}")
    print(f"Acurácia (Teste): {metrics['Accuracy']:.4f}")
    print(f"Precisão: {metrics['Precision']:.4f}")
    print(f"Recall: {metrics['Recall']:.4f}")
    print(f"F1-Score: {metrics['F1']:.4f}")
    print("Matriz de Confusão:")
    print(metrics['Confusion Matrix'])


# 2. Visualização Comparativa
# Preparar dados para visualização
metrics_df = pd.DataFrame.from_dict({(i,j): results[i][j] 
                                   for i in results.keys() 
                                   for j in results[i].keys() 
                                   if j not in ['Confusion Matrix', 'Train Accuracy']},
                                  orient='index')

metrics_df = metrics_df.reset_index()
metrics_df.columns = ['Model', 'Metric', 'Value']

# Gráfico comparativo
plt.figure(figsize=(12, 6))
sns.barplot(data=metrics_df, x='Model', y='Value', hue='Metric')
plt.title('Comparação de Métricas por Modelo')
plt.ylim(0, 1)
plt.legend(loc='upper right')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Matrizes de confusão lado a lado
plt.figure(figsize=(18, 12))
for i, (name, metrics) in enumerate(results.items(), 1):
    plt.subplot(2, 3, i)
    sns.heatmap(metrics['Confusion Matrix'], annot=True, fmt='d', cmap='Blues')
    plt.title(f'{name}\nAcurácia: {metrics["Accuracy"]:.2f}')
    plt.xlabel('Previsto')
    plt.ylabel('Real')
plt.tight_layout()
plt.show()





'''
Análise das Variáveis Mais Relevantes para Previsão de Evasão
'''
# 1. Regressão Logística - Análise de Coeficientes
# Pipeline com padronização
lr_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(random_state=42, class_weight='balanced'))
])

# Treinar modelo
lr_pipe.fit(X_train, y_train)

# Extrair coeficientes
coefs = lr_pipe.named_steps['model'].coef_[0]
features = X_train.columns

# Criar DataFrame com coeficientes
lr_feature_importance = pd.DataFrame({
    'Feature': features,
    'Coefficient': coefs,
    'Absolute_Coeff': np.abs(coefs)
}).sort_values('Absolute_Coeff', ascending=False)

# Visualizar top 10
plt.figure(figsize=(10, 6))
sns.barplot(x='Coefficient', y='Feature', 
            data=lr_feature_importance.head(10), palette='coolwarm')
plt.title('Top 10 Variáveis Mais Importantes - Regressão Logística')
plt.xlabel('Coeficiente Padronizado')
plt.ylabel('Variável')
plt.axvline(0, color='black', linestyle='--')
plt.show() 


# 2. KNN - Análise Baseada em Distâncias
# Treinar KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# Calcular importância por permutação
knn_importance = permutation_importance(
    knn, X_test_scaled, y_test, n_repeats=10, random_state=42
)

# Organizar resultados
knn_feature_importance = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': knn_importance.importances_mean,
    'Std': knn_importance.importances_std
}).sort_values('Importance', ascending=False)

# Visualizar top 10
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', 
            data=knn_feature_importance.head(10), palette='viridis')
plt.title('Top 10 Variáveis Mais Importantes - KNN')
plt.xlabel('Redução na Acurácia por Permutação')
plt.ylabel('Variável')
plt.show()

# 3. Random Forest - Importância de Variáveis Nativa
# Treinar Random Forest
rf = RandomForestClassifier(random_state=42, class_weight='balanced')
rf.fit(X_train, y_train)

# Extrair importância
rf_feature_importance = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': rf.feature_importances_
}).sort_values('Importance', ascending=False)

# Visualizar top 10
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', 
            data=rf_feature_importance.head(10), palette='Greens_r')
plt.title('Top 10 Variáveis Mais Importantes - Random Forest')
plt.xlabel('Importância (Redução Média na Impureza)')
plt.ylabel('Variável')
plt.show()


# 4. SVM - Análise de Coeficientes
# Pipeline com padronização para SVM
svm_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', SVC(kernel='linear', random_state=42, class_weight='balanced'))
])

# Treinar SVM linear
svm_pipe.fit(X_train, y_train)

# Extrair coeficientes
svm_coefs = svm_pipe.named_steps['model'].coef_[0]
svm_feature_importance = pd.DataFrame({
    'Feature': X_train.columns,
    'Coefficient': svm_coefs,
    'Absolute_Coeff': np.abs(svm_coefs)
}).sort_values('Absolute_Coeff', ascending=False)

# Visualizar top 10
plt.figure(figsize=(10, 6))
sns.barplot(x='Coefficient', y='Feature', 
            data=svm_feature_importance.head(10), palette='coolwarm')
plt.title('Top 10 Variáveis Mais Importantes - SVM Linear')
plt.xlabel('Coeficiente do Vetor de Suporte')
plt.ylabel('Variável')
plt.axvline(0, color='black', linestyle='--')
plt.show()


# 5. Análise Comparativa entre Modelos
# Juntar todas as importâncias
comparison = pd.DataFrame({
    'LogisticRegression': lr_feature_importance.set_index('Feature')['Absolute_Coeff'],
    'RandomForest': rf_feature_importance.set_index('Feature')['Importance'],
    'SVM': svm_feature_importance.set_index('Feature')['Absolute_Coeff'],
    'KNN': knn_feature_importance.set_index('Feature')['Importance']
}).fillna(0)

# Normalizar cada coluna entre 0 e 1
comparison = comparison.apply(lambda x: x/x.max(), axis=0)

# Visualizar concordância entre modelos
plt.figure(figsize=(12, 8))
sns.heatmap(comparison.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlação entre Importâncias de Variáveis por Modelo')
plt.show()

# Top 5 variáveis em cada modelo
print("\nTop 5 variáveis por modelo:")
for model in comparison.columns:
    top_vars = comparison[model].sort_values(ascending=False).head(5).index.tolist()
    print(f"{model}: {', '.join(top_vars)}")

