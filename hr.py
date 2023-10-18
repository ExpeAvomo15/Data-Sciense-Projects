import streamlit as st
import pandas as pd
from sklearn.ensemble import VotingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler

# Configurar la página de Streamlit
st.title('Predicción de la estancia del trabajador')

# Cargar el archivo CSV como un DataFrame de Pandas
data = pd.read_csv('df2.csv')

#Eliminamos la columna 'EducationField'
#data = data.drop('EducationField', axis=1)

# Dividir el DataFrame en características y etiquetas
X = data.drop('Attrition', axis=1)


#Normalizamos los valores de X
scaler = MinMaxScaler()
X.columns = X.columns.astype(str) # En las versiones actuales es necesario para que todas las columnas sean tipo String
X = scaler.fit_transform(X)

y=data['Attrition']

# Crear una lista de modelos
models = [
    ('decision_tree', DecisionTreeRegressor()),
    ('linear_regression', LinearRegression()),
    ('k_neighbors', KNeighborsRegressor(n_neighbors=5))
]

# Crear un modelo de ensamble con los modelos anteriores
model = VotingRegressor(models)

# Entrenar el modelo con los datos
model.fit(X, y)

# Crear widgets para ingresar los valores de entrada
# Crear widgets para ingresar los parámetros de entrada
age = st.sidebar.slider('Edad', 19, 65, 30)
education = st.sidebar.slider('Nivel de Educación', 1, 5, 2)
educationFiled =  st.sidebar.slider('Campo educativo', 0, 5, 2)
jobSatisfaction = st.sidebar.slider('Satisfacción en el Trabajo', 1, 5, 3)
relationshipSatisfaction = st.sidebar.slider('Satisfacción en las Relaciones', 1, 5, 3)
workLifeBalance = st.sidebar.slider('Balance entre Trabajo y Vida Personal', 1, 5, 3)
performanceRating = st.sidebar.slider('Calificación del Rendimiento', 1, 5, 3)

# Hacer una predicción con el modelo
predict = model.predict([[age,education, educationFiled, jobSatisfaction,
                relationshipSatisfaction,  workLifeBalance,  performanceRating ]])

# Mostrar el resultado

predict_abs = abs(predict)
st.write(predict_abs)
if predict_abs <2.7:
    st.write('The worker LEAVES')
else:
    st.write('The worker STAYS')
