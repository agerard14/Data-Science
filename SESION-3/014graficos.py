import pandas as pd
import matplotlib.pyplot as plt

print(plt.style.available)
#creamos un dataframe
data={
    'Año':[2016,2017,2018,2019,2020,2021],
    'Ventas':[250,300,400,350,500,450],
    'Ganancias':[50,80,100,90,120,110]
}
#convertimos el diccionario en un dataframe
df=pd.DataFrame(data)
#cambiamos el estilo del grafico
plt.style.use('ggplot')
plt.figure(figsize=(10,6))
#grafico de lineas
#divide la figura en 3 filas y una columna y selecciona la primer grafica
plt.subplot(3,1,1)
plt.plot(df['Año'],df['Ventas'],marker='o',linestyle=':',color='b',label='ventas')
plt.title('Evolucion de las ventas con los años')
plt.xlabel('Año')
plt.ylabel('Ventas')
plt.legend()
plt.grid(True)
#grafico de barras
plt.subplot(3,1,2)
plt.bar(df['Año'],df['Ganancias'],color='green',label='Ganancias')
plt.xlabel('Año')
plt.ylabel('Ganancias')
plt.legend()

#grafico de histograma
plt.subplot(3,1,3)
plt.hist(df['Ganancias'],bins=5,color='purple',edgecolor='black',alpha=0.7)
#plt.hist crea un grafico de histograma
#bins=5 divide los datos en 5 intervalos
#color=purple pone colores purpuras a las barras
#edgecolor=black pone bordes negros en las barras
#alpha=0.7 transparencia de las barras para mejorar su visualizacion
plt.title('Distribucion de las Ganancias')
plt.xlabel('Ganancias')
plt.ylabel('Frecuencia')
plt.tight_layout()



plt.show()
