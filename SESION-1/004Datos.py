import pandas as pd
#cargaremos datos desde un archivo csv
df=pd.read_csv('AExpDatVentas.csv')
#limpiar datos
df['Fecha de Venta']=pd.to_datetime(df['Fecha de Venta'])
#descripción estadística básica
descripcion=df.describe()
print('Descripción estadística básica:')
print(descripcion)
#Calcular la cantidad total de productos vendidos
total_cantidad=df['Cantidad'].sum()
print('La cantidad total de productos vendidos es:',total_cantidad)
#calcular el total de ingresos por productos
df['Ingreso']=df['Precio']*df['Cantidad']
ingreso_total=df['Ingreso'].sum()
print('Ingreso total:',ingreso_total,'Dolares')