import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
from sklearn.datasets import load_iris

iris=load_iris(as_frame=True)
print('Dataset Iris (Clasificación):')
print(f'Características: {iris.feature_names}')
print(f'Forma de los datos: {iris.data.shape}')
print(f'Descripción breve: \n{iris.DESCR}\n')
input('presiona enter para continuar...')

df_iris=iris.data
print(df_iris.head())
input('Presiona enter para continuar...')

#agregamos la columna Species al DF que contiene etiquetas numéricas de las
#especies (0,1,2)
df_iris['Species']=iris.target #agregamos la variable objetivo

df_iris['Species']=df_iris['Species'].map(
    {i: name for i, name in enumerate(iris.target_names)})
#convertimos las etiquetas numéricas de las especies en nombres como:
#setosa, versicolor, virginica
#.map() reemplaza los valores numéricos de la columna Species por sus 
#nombres correspondientes
print('Primeras filas del dataset Iris:')
print(df_iris.head())
#creamos un gráfico de pares (pairplot)
sns.pairplot(df_iris,hue='Species',markers=['o','s','D'])
#hue colorea los puntos segun las especies de flores
#markers asigan formas específicas a los puntos para diferenciar las especies
plt.suptitle('Relaciones entre las características del dataSet Iris',
             y=1.02)
#y=1.02 ajusta la posición vertical del titulo para que quede encima
plt.show()