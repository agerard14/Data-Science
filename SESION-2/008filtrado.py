import pandas as pd
#cargamos un dataset
url="https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
df=pd.read_csv(url)

print('Dataset original (Primeras 5 filas):')
print(df.head())