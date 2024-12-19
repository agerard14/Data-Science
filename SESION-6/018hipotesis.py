#generaremos muestras aleatorias usando una dist normal donde:
#Producto A tiene una media de 30 y una desv estandar de 5
#Producto B tiene una media de 35 y una desv estandar de 7
import numpy as np
from scipy.stats import ttest_ind
#creamos las muestras de datos
np.random.seed(42) #el valor de la semilla es 42
#media=30 desv=5
sample1=np.random.normal(loc=30, scale=5, size=100)
#media=35 desv=7
sample2=np.random.normal(loc=35,scale=7,size=100)
#realizar la prueba t para determinar si hay una diferencia significativa
#entre las medias, se compararn 2 grupos para determinar si hay una dif
#estadisticamente significativa entre ellas
stat,p=ttest_ind(sample1,sample2)
#el resultado es una tupla que contiene dos elementos, el primer valor(stat)
#es el estadistico t. y el segundo (p) es el valor de p
print('Estadistico t:',stat)
print('Valor de p:',p)
#interpretar los resultados
alpha=0.05 #nivel de significancia
#si el valor de p es <0.05 (nivel de significancia de 95%)
#rechazamos la hipotesis nula y concluimos que hay una diferencia significativa
#entre las medias de los productos
#si el valor de p es >0.05 no tenemos suficiente evidencia para rechazar
#la hipotesis nula y concluimos que las medias no son significativamente 
# diferentes
if p<alpha:
    print('Rechazamos la hipótesis nula, las medias son diferentes')
else:
    print('No rechazamos la hipótesis nula, no hay suficiente evidencia'
          'para afirmar que las medias son diferentes')