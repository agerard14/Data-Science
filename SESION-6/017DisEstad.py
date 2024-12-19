import numpy as np
import matplotlib.pyplot as plt
#scipy(abreviatura de scientific python) calcula métricas estadísticas como
# media, mediana, moda, desviación estandar y percentiles
from scipy import stats 

#loc define la media de la distribución normal
#scale define la  desviación estandar
#size cuantos números se generarán
data=np.random.normal(loc=50, scale=10, size=1000)
#calcularemos datos estadísticos básicos
media=np.mean(data)# media
mediana=np.median(data)# mediana
#en versiones antiguas de scipy la moda se calcula asi:
#moda = stats.mode(data)[0][0]
moda=stats.mode(data,keepdims=True).mode[0]
#stats es una función de la librería scipy que calcula la moda
#keepdims=True indica que se deben conservar las dimensiones originales
#del arreglo al que se le calculará la moda
desviacion_estandar=np.std(data)
#imprimiremos la información
print(f'Media: {media:.2f}')
print(f'Mediana: {mediana:.2f}')
print(f'Moda: {moda:.2f}')
print(f'Desviación Estándar: {desviacion_estandar:.2f}')
#visualizaremos el histograma de la distribución normal
plt.figure(figsize=(10,6))
plt.hist(data,bins=30,color='skyblue',alpha=0.7,label='Distribución normal')
#bins =controla la cantidad de intervalos en los que se agrupan los datos
plt.axvline(media,color='red',linestyle='--',linewidth=2,label=f'media: {media:.2f}')
plt.axvline(mediana,color='green',linestyle='--', linewidth=2,label=f'mediana: {mediana:.2f}')
plt.axvline(moda,color='purple',linestyle='--',linewidth=2,label=f'moda: {moda:.2f}')
plt.axvline(desviacion_estandar,color='blue',linestyle='--',linewidth=2,
            label=f'desv. Est.{desviacion_estandar:.2f}')
plt.title('Histograma de la distribución normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True,alpha=0.5,linestyle='--')
plt.tight_layout()
plt.show()