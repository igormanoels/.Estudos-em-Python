# Importando as visualizações
import matplotlib.pyplot as plt

# Importando as visualizações import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
# importando o r2 score from sklearn.metrics import r2_score

# import train_test_split
from sklearn.model_selection import train_test_split

#import ols
from statsmodels.formula.api import ols

# importando a api do statsmodels
import statsmodels.api as sm

dados = pd.read_csv("D:/GitHub/.Estudos-em-Python/Alura/G8 ONE - Especialização Data Science/03 - Estatística e Machine Learning/02 - Regressão Linear/Preços_de_casas.csv")


# Como é a relação entre área construída e o preço do imóvel?
plt.scatter(dados['area_primeiro_andar'], dados['preco_de_venda'])



# Aparentemente, quanto maior a área do primeiro andar, maior o preço da casa.
# E se quisermos traçar uma linha que melhor representa esse comportamento?
plt.scatter(dados['area_primeiro_andar'], dados['preco_de_venda'])
plt.title("Relação entre Preço e Area")
plt.xlabel("Area do primeiro andar")
plt.ylabel("Preço de venda")



# Aparentemente, quanto maior a área do primeiro andar, maior o preço da casa.
# E se quisermos traçar uma linha que melhor representa esse comportamento?
plt.scatter(dados['area_primeiro_andar'], dados['preco_de_venda'])
plt.axline(xy1 = (66, 250000),xy2 = (190, 1800000), color = "red" )
plt.title("Relação entre Preço e Area")
plt.xlabel("Area do primeiro andar")
plt.ylabel("Preço de venda")




# Qual a reta que melhor se adequa a relação?
px.scatter(dados, x = 'area_primeiro_andar', y = 'preco_de_venda', trendline_color_override="red", trendline = 'ols' )



#Definindo y eX
y = dados['preco_de_venda']
X = dados.drop(columns = 'preco_de_venda')


#Aplicando o split do y e x
train_test_split(X, y, test_size = 0.3, random_state= 230)
#Aplicando o split do y e x
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.3, random_state= 230)
#Dados de treino para usar a fórmula
df_train = pd.DataFrame(data= X_train) 
df_train['preco_de_venda'] = Y_train


# ajustando o primeiro modelo
modelo_0 = ols('preco_de_venda ~ area_primeiro_andar', data = df_train).fit()


# visualizando os parametros
modelo_0.params


# o resumo do nosso modelo
print(modelo_0.summary())


# observando o R²
modelo_0.rsquared


# Quais são os resíduos
modelo_0.resid


# Como eles estão distribuídos
modelo_0.resid.hist()
plt.title("Distribuição dos resíduos")
plt.show()


# definindo o y previsto
y_predict = modelo_0.predict(X_test)


'''
#printando o R² 
print("R²: ", r2_score(y_test,y_predict))

'''


sns.displot(dados['preco_de_venda'], kde=True, color='green')
plt.title('Distribuição do preço de venda')
plt.show()



# quais outras características poderiam explicar o preço dos imóveis?
sns.pairplot(dados)


dados.columns


'''
Index(['area_primeiro_andar', 'existe_segundo_andar', 'area_segundo_andar',
       'quantidade_banheiros', 'capacidade_carros_garagem',
       'qualidade_da_cozinha_Excelente', 'preco_de_venda'],
      dtype='object')

'''


#Vamos olhar apenas com y_vars='preco_de_venda'
sns.pairplot(dados, y_vars = 'preco_de_venda', x_vars = 'quantidade_banheiros')



#Vamos olhar apenas com y_vars='preco_de_venda'
sns.pairplot(dados, y_vars = 'preco_de_venda', x_vars = ['quantidade_banheiros','area_segundo_andar','capacidade_carros_garagem'])




# adicionando o constante
X_train = sm.add_constant(X_train)

X_train.head()
y_train = 0 # precisa buscar esse valor

# Criando o modelo de regressão (sem fómula): saturado
modelo_1 = sm.OLS(y_train,
                  X_train[['const','area_primeiro_andar','existe_segundo_andar',
                          'area_segundo_andar','quantidade_banheiros','capacidade_carros_garagem',
                           'qualidade_da_cozinha_Excelente']]).fit()



# Modelo sem a área do segundo andar
modelo_2 = sm.OLS(y_train,
                  X_train[['const','area_primeiro_andar','existe_segundo_andar',
                          'quantidade_banheiros','capacidade_carros_garagem',
                           'qualidade_da_cozinha_Excelente']]).fit()


'''
'''
# Modelo sem informações sobre garagem
modelo_3 = sm.OLS(y_train,
                  X_train[['const','area_primeiro_andar','existe_segundo_andar',
                          'quantidade_banheiros',
                           'qualidade_da_cozinha_Excelente']]).fit()



# Resumo do modelo 1
print(modelo_1.summary())
# Resumo do modelo 2
print(modelo_2.summary())
# Resumo do modelo 3
print(modelo_3.summary())


print("R²")
print("Modelo 0: ", modelo_0.rsquared)
print("Modelo 1: ", modelo_1.rsquared)
print("Modelo 2: ", modelo_2.rsquared)
print("Modelo 3: ", modelo_3.rsquared)


#Quantos parametros estão no modelo?
print(len(modelo_0.params))
print(len(modelo_1.params))
print(len(modelo_2.params))
print(len(modelo_3.params))