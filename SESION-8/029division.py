import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
#cargar los datos desde un archivo csv
df=pd.read_csv('ventas_productos.csv')
#creamos una nueva columna para guardar los ingresos
df['Ingresos']=df['Precio']*df['Cantidad_Vendida']
print(df)
input()
#separaremos las características y el objetivo
X=df.drop(columns=['Ingresos'])
#este es el objetivo
y=df['Ingresos']
print('Los datos de X son:\n',X)
print('Los datos de y son:\n',y)
input('Presiona enter para continuar...')
#dividimos los datos en conjuntos de entrenamiento y prueba
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,
                                               random_state=42)
#definimos una función para graficar distribuciones
def plot_distributions(df_train,df_test,column):
    plt.figure(figsize=(10,6))
    sns.kdeplot(df_train[column],label='Entrenamiento',fill=True,alpha=0.5)
    sns.kdeplot(df_test[column],label='Prueba',fill=True,alpha=0.5)
    plt.title(f'Distribucion de {column} (Conjuntos de entrenamiento y Prueba)')
    plt.legend()
    plt.show()
#Graficar las distribuciones de las columnas numéricas
numerical_columns=['Precio','Cantidad_Vendida']
for col in numerical_columns:
    plot_distributions(X_train,X_test,col)