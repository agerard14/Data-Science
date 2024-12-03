import pandas as pd
import matplotlib.pyplot as plt
archivo_csv='ventas_televisores.csv'
datos=pd.read_csv(archivo_csv)
print(datos)
plt.figure(figsize=(10,6))
#crearemos las barras para cada mes y marca
bar_width=0.25
meses=datos['Mes']
indices=range(len(meses))
#print(indices)
#creamos las barras para la marca samsung
plt.bar(indices,datos['Samsung'],width=bar_width,label='Samsung',color='g')
#barras para la marca LG
plt.bar([i-bar_width for i in indices], datos['LG'],width=bar_width,label='LG',color='b')
#barras de sony
plt.bar([i+bar_width for i in indices],datos['Sony'],width=bar_width,label='Sony',color='#cc0000')
#añadir titulos y etiquetas
plt.title('ventas de televisores por Marcas')
plt.xlabel('Mes')
plt.ylabel('ventas')
plt.xticks(indices,meses)
#añadir leyenda
plt.legend()
#cuadricula
plt.grid(True,axis='y')
plt.show()