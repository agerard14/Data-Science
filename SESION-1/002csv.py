import pandas as pd
from io import StringIO

#cargaremos un archivo csv
csv_file='gapminder.csv'
#usaremos la funcion pd.read_csv() para cargar los datos
df_csv=pd.read_csv(csv_file)
#mostraremos las primeras 5 filas del archivo
print('Primeras 5 filas del archivo csv: ')
print(df_csv.head()) # .head() muestra las 5 primeras filas del archivo
