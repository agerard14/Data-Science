import pandas as pd #pip install pandas
#creamos una serie de pandas
datos=[10,20,30,40,50]
indices=['Lunes','Martes','Miercoles','Jueves','Viernes']
#creamos las series que representan los valores asociados a los dias
serie=pd.Series(datos,index=indices)
print('La serie de datos:\n',serie)
#convertir la serie en un DataFrame
#convierte la serie en un formato tabular, con una columna llamada valores
df=serie.to_frame(name='Ventas')
print('El dataframe es:\n',df)
#añadiremos una nueva columna llamada 'porcentaje'
#porcentaje calcula la proporcion de cada valor respecto al total
df['Porcentaje']=(df['Ventas']/df['Ventas'].sum())*100
print('Dataframe con porcentaje:\n',df)