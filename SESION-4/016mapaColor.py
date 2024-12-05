import seaborn as sns 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
gapminder=pd.read_csv('gapminder.csv')
print(gapminder)
input()
#generación de datos ficticios para PIB si no está en gapminder
if 'PIB' not in gapminder.columns:
    #fijamos la semilla para generar números aleatorios
    np.random.seed(42)
    #generaremos números entre 1000 y 50000
    #cuantas filas haya en la lista de datos gapminder
    gapminder['PIB']=np.random.randint(1000,50000,size=len(gapminder))
print(gapminder)
input()
#calcular la matriz de correlación
corr_matrix=gapminder[['lifeExp','pop','PIB']].corr()
#mide la relación lineal entre las variables seleccionadas
#valores cercanos a 1: fuerte correlación positiva
#valores cercanos a -1: fuerte correlación negativa
#valores cercanos a 0: sin correlación significativaplt.figure(figsize=(8,6))
sns.heatmap(corr_matrix,annot=True,fmt='.2f',cmap='coolwarm',cbar=True)
#la matriz se crea basandose en corr_matrix
#annot= True muestra los números de las correlaciones en cada celda
#fmt especifica el formato de los números
#cmap='coolwarm' aplica el esquema de colores coolwarm (azul y rojo 
# para correlaciones) positivas y negativas
#cbar=True muestra una barra lateral con la escala de colores 
plt.title('Correlación entre Esperanza de vida, Población y PIB'
          ,fontsize=14)
plt.tight_layout()
plt.show()