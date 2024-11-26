import pandas as pd

#crearemos el dataframe con los datos 
data={
    'Nombre':['Ana','Luis','Pedro',None],
    'Edad':[25,30,None,22],
    'Ciudad':['Madrid',None,'Barcelona','Valencia']
}
df=pd.DataFrame(data)
print('Dataframe original: ')
print(df)
#identificar las celdas nulas
print('\nCeldas nulas identificadas: ')
print(df.isnull())
#reemplazaremos valores nulos con valores predeterminados
df_reemplazo_predeterminado=df.copy()#tomamos una copia del dataframe
df_reemplazo_predeterminado['Ciudad']=df_reemplazo_predeterminado['Ciudad'].fillna('Desconocido')
df_reemplazo_predeterminado['Edad']=df_reemplazo_predeterminado['Edad'].fillna(0)
print('\nDataframe con valores predeterminados: ')
print(df_reemplazo_predeterminado)
#reemplazaremos los valores nulos en edad con el promedio de la columna
df_reemplazo_promedio=df.copy()
promedio_edad=df['Edad'].mean(skipna=True)#calcula el promedio ignorando los nulos
#el promedio se calcula como (25+30+22)/3=25.6667
df_reemplazo_predeterminado['Edad']=df_reemplazo_promedio['Edad'].fillna(promedio_edad)
print('\nDataframe con valores nulos en la columna edad Reemplazados por el promedio: ')
print(df_reemplazo_promedio)