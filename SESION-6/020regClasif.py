import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
#pip install scikit-learn
from sklearn.datasets import fetch_california_housing

#cargamos el dataset
california_housing=fetch_california_housing(as_frame=True)
#as_frame=True es para que los datasets cargados se presenten como dataset de
#pandas en lugar de un array de numpy

#Exploramos el dataset
print('Dataset California Housing (Regresión):')
print(f'Características: {california_housing.feature_names}')
print(f'Forma de los datos: {california_housing.data.shape}')
print(f'Descripción breve: {california_housing.DESCR}\n')
input('Presione enter para continuar...')
#creamos un dataframe para facilitar la exploración
df_california=california_housing.data
print(df_california.head())
input('Presione enter para continuar...')
#convierte el dataframe California_Housing en uno llamado df_california
#y añade la variable objetivo
df_california['MedHouseVal']=california_housing.target
print(df_california.head())
input('Presiona enter para continuar')
#visualizar relaciones entre características
plt.figure(figsize=(10,6))
sns.scatterplot(data=df_california,x='MedInc',y='MedHouseVal',alpha=0.6)
plt.title('Relación entre ingreso medio (MedInc) y valor medio de la '
          'vivienda (MedHouseVal)')
plt.xlabel('Ingreso medio (MedInc)')
plt.ylabel('Valor medio de la vivienda (MedHouseVal)')
plt.show()
