import pandas as pd
from sklearn.ensemble import VotingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
# Carga el archivo CSV como un DataFrame de Pandas
data = pd.read_csv(‘niños.csv’)
# Divide el DataFrame en características y etiquetas
X = data[[‘peso’, ‘sexo’, ‘altura’]]
y = data[‘talla’]
# Crea una lista de modelos
models = [
    (‘decision_tree’, DecisionTreeRegressor()),
    (‘linear_regression’, LinearRegression()),
    (‘k_neighbors’, KNeighborsRegressor(n_neighbors=5))
]
# Crea un modelo de ensamble con los modelos anteriores
model = VotingRegressor(models)
# Entrena el modelo con los datos
model.fit(X, y)
# Hace una predicción con el modelo
peso = 50
sexo = 0 # 1 representa chico
altura = 158
talla_predicha = model.predict([[peso, sexo, altura]])
print(f’Para un peso de {peso} kg, una altura de {altura} cm y un sexo masculino, se predice una talla de {talla_predicha[0]}’)