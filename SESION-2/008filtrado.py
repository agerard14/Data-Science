import pandas as pd
#cargamos un dataset
url="https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
df=pd.read_csv(url)

print('Dataset original (Primeras 5 filas):')
print(df.head())
#seleccionar las filas donde 'life_expectancy'>70
df_filtro_esperanza_vida=df[df['lifeExp']>75]
print('\nFilas donde fileExp es >70 (primeras 5 filas):')
print(df_filtro_esperanza_vida.head())
#filtraremos y seleccionamos las columnas country y year
df_selected_columns=df_filtro_esperanza_vida[['country','year']]
print('\nFiltrado y seleccion de columnas country y year (primeras 5 filas):')
print(df_selected_columns.head())
#mostraremos todos los datos
pd.set_option('display.max_rows',None)
print(df_filtro_esperanza_vida)
#regresar la configuracion por defecto
pd.set_option('display-max_rows')#deja la configuracion donde estaba 
#mostrar un rango especifico de filas 
print('Muestra los 10 primeros registros:')
print(df_filtro_esperanza_vida.iloc[0:10])
#guarda el archivo del dataframe en un archivo local en mi computadora
df_filtro_esperanza_vida.to_csv('filtrado_esperanza_vida.csv',index=False)
print('Archivo guardado como: filtrado_esperanza_vida.csv')