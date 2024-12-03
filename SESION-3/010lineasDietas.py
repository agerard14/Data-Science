import pandas as pd
import matplotlib.pyplot as plt
#leer el archivo csv
archivo_csv='reto_dieta.csv'
datos=pd.read_csv(archivo_csv)
#mostrar el contenido del archivo csv
print(datos)
#crear gráfico de líneas
plt.figure(figsize=(10,6))
#graficaremos los datos de Ana
plt.plot(datos['Mes'],datos['Ana'],marker='o',label='Ana')
#graficaremos los datos de Mario
plt.plot(datos['Mes'],datos['Mario'],marker='o',label='Mario')
#graficarmeos los datos de Luis
plt.plot(datos['Mes'],datos['Luis'],marker='o',label='Luis')
#Añadir titulos y etiquetas
plt.title('Evolución del Peso Durante la Dieta')
plt.xlabel('Mes')
plt.ylabel('Peso (kg)')
#añadimos la leyenda
plt.legend()
#añadimos la cuadricula
plt.grid(True)
#guardaremos el gráfico como un archivo de imagen
plt.savefig('EvolucionDieta.png')
#mostramos la gráfica en pantalla
plt.show()