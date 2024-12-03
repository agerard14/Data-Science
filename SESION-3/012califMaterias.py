import pandas as pd
import matplotlib.pyplot as plt

archivo_csv='calificaciones.csv'
datos=pd.read_csv('calificaciones.csv', encoding='UTF-8')#excel latin

print(datos)
#crear el grafico de barras
plt.figure(figsize=(8,5))
plt.bar(datos['Materia'],datos['Promedio'],color='lightgreen')
#añadir titulos y etiquetas
plt.title('Promedio de Calificacion por Materia')
plt.xlabel('Materia')
plt.ylabel('Promedio')
#guardaremos el grafico
plt.savefig('PromediosCalificaciones.jpg')
plt.show()