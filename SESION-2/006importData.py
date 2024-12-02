#Extraeremos  los datos de un archivo csv llamado ventas
#para este ejemplo el archivo debe estar en la misma carpeta que este programa 
import numpy as np #pip install numpy

datos=np.genfromtxt('ventas.csv',delimiter=',',skip_header=1, dtype=None,encoding=None)

print('Datos importados:\n',datos)
#separar los datos diferentes arreglos (arrays)
productos=np.array([row[0] for row in datos])
cantidades=np.array([row(1) for row in datos]).astype(int)
precios=np.array([row[2] for row in datos]).astype(float)
#mostraremos la informacion
print('Productos:\n',productos)
print('Cantidades:\n',cantidades)
print('Precios:\n',precios)