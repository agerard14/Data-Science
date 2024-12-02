import matplotlib.pyplot as plt #pip install matplotlib

#Datos de ejemplo
meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio']
ventas_Juan=[1500,1300,1600,1300,1750,1550]
ventas_Ana=[1200,1700,1250,1850,1400,1800]
ventas_Luis=[800,1500,850,950,1920,1500]

plt.figure(figsize=(10,6))
#establece el tamaño de 10 de ancho por 6 de alto pulgadas
plt.plot(meses,ventas_Juan,marker='o',linestyle='-',color='b',label='Juan')
plt.plot(meses,ventas_Ana,marker='o',linestyle='-',color='g',label='Ana')
plt.plot(meses,ventas_Luis,marker='o',linestyle='-',color='r',label='Luis')
plt.title('Ventas Mensuales de Productos')
plt.xlabel('Meses')
plt.ylabel('Ventas ($)')
plt.legend()#muestra la leyenda del grafico
plt.grid(True)
plt.show()