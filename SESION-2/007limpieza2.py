#limpiaremos los datos, si encontramos campos corruptos
#o no validos
import numpy as np
#importaremos los datos de un archivo csv
datos=np.genfromtxt('ventas2.csv ',delimiter=',',skip_header=1, dtype=str, encoding=None)

print('\ndatos importados:\n',datos)
#reemplazaremos los valores faltantes (nan) con ceros
datos[datos=='nan']='0' #asi la posicion tiene nan reemplaza por cero
print('\nDatos con valores faltantes reemplazados por ceros\n',datos)
#convertimos las columnas cantidad y precios a tipo numerico
cantidades=datos[:,1].astype(int)
precios=datos[:,2].astype(float)
#calcular el total de ventas por producto
total_ventas=cantidades*precios
print('Total de ventas por producto:\n',total_ventas)
#filtrar productos con cantidad mayor a 15
filtro_cantidad=cantidades>15
productos_filtrados=datos[filtro_cantidad,0]
print('\nProductos con cantidad mayor a 15\n',productos_filtrados)