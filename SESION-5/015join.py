#el programa muestra como se unen los conjuntos de datos usando
#diferentes criterios, como se harían con tablas de una base de datos
import pandas as pd

df1=pd.DataFrame({
    'ID':[1,2,3],
    'Nombre':['Ana','Luis','Mario']
})

df2=pd.DataFrame({
    'ID':[2,3,4],
    'Puntos':[90,80,70]
})

print('Data frame 1 original:\n',df1)
print('Data frame 2 original:\n',df2)
input('presiona enter para continuar...')

merge_df=pd.merge(df1,df2, on='ID',how='inner')
#inner: mezcla solo filas coincidentes
print('La mezcla usando inner es:\n',merge_df)
input('presiona enter para continuar...')

merge_df=pd.merge(df1,df2,on='ID',how='outer')
#outer: todas las filas, llenando con NaN cuando no hay coincidencias
print('La mezcla usando outer es:\n',merge_df)
input('presiona enter para continuar...')

merge_df=pd.merge(df1,df2,on='ID',how='left')
#left muestra todas las filas de df1 con NaN si no hay coincidencias en df2
print('La mezcla usando left es:\n',merge_df)
input('presiona enter para continuar...')

merge_df=pd.merge(df1,df2,on='ID',how='right')
#right muestra todas las filas de df2 con NaN si no hay coincidencias en df1
print('La mezcla usando right es:\n',merge_df)
input('presiona enter para continuar...')