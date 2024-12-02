#CVS es un archivo con datos separadas por comas u otro caracter similar
#y se puede vizualizar con Excel, bloc de notas y otros editores
import csv #pip install csv
#datos para el archivo csv
datos=[
    ['Leche',5,28],
    ['Azucar',35,32],
    ['Arroz',23,30],
    ['Queso',14,140],
    ['Jamon',25,50]
]

with open('productos.csv','w',newline='') as file:
    #estructura para crear archivos
    writer=csv.writer(file)
    writer.writerow(['Productos','Cantidades','Precios'])
    writer.writerow(datos)
    
print('El archivo se creo el nombre: productos.csv')