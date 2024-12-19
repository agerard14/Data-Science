import pandas as pd
import numpy as np
#fijamos la semilla
np.random.seed(42)
#generamos el dataset simulado
n_samples=500
data={
    #generamos las horas en las que viaja la gente en la ciudad
    'Hora_del_dia':np.random.randint(6,22,size=n_samples),
    #la velocidad en km/h
    'Velocidad_media':np.random.uniform(10,80,size=n_samples),
    #distancia en km
    'Distancia':np.random.uniform(1,50,size=n_samples)
}
df=pd.DataFrame(data)
#calcularemos el tiempo de viaje
df['Tiempo_de_viaje']=np.round(df['Distancia']/df['Velocidad_media']*60,2)
#mostramos las primeras filas
print('Los datos son:\n',df.head())
input('Presiona enter para continuar...')
####################################
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt

#separar las características y el objetivo
X=df[['Hora_del_dia','Velocidad_media','Distancia']]
y=df['Tiempo_de_viaje']
#dividir en conjuntos de entrenamiento y prueba
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,
                                               random_state=42)
#crear el modelo de regresion lineal
model=LinearRegression()
#entramos el modelo
model.fit(X_train,y_train)
#Realizaremos predicciones en el conjunto de prueba
y_pred=model.predict(X_test)
#evaluaremos el modelo
#con el coeficiente de determinacion R2
r2=r2_score(y_test,y_pred)
#un valor cercano a 1 significa un modelo muy bueno
#un valor cercano a 0 significa un modelo muy pobre
print(f'Coeficiente de determinación R2: {r2:.2f}')
input('Presiona enter para continuar...')
#visualizaremos los datos de los valores reales vs ls predichos
plt.figure(figsize=(8,6))
plt.scatter(y_test,y_pred,alpha=0.7,color='blue')
plt.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],
         color='red',linestyle='--')
plt.xlabel('Valor real de tiempo de viaje (minutos)')
plt.ylabel('Valor predicho de tiempo de viaje (minutos)')
plt.title('Valores Reales VS Predichos')
plt.show()
#los circulos azules presenta los valores predichos
#la línea roja punteada es la linea de identidad que representa
#la relación perfecta entre los valores reales y los predichos