import pandas as pd
#url de internet
url="https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
#cargaremos el dataset
df=pd.read_csv(url)
#Mostrar las primeras filas para verificar el contenido del dataset
print('Primeras filas del dataset:')
print(df.head(),'\n')
input() #recuerda que estos inputs vacios son opcionales se pueden quitar
#calcularemos el promedio de 'gdp_per_capita' por continente
promedio_gdp=df.groupby('continent')['gdpPercap'].mean()
print('Promedio de DGP per capita por continente:')
print(promedio_gdp,'\n')
input()
#Calcular la esperanza de vida máxima('life_expectancy') por continente
max_life_expectancy=df.groupby('continent')['lifeExp'].max()
print('La esperanza de vida máxima por continente:')
print(max_life_expectancy,'\n')
input()
#calcular la esperanza de vida máxima por país
max_life_expectancy2=df.groupby('country')['lifeExp'].max()
print('La esperanza de vida máxima por país:')
print(max_life_expectancy2,'\n')
input()
#calcular la esperanza de vida mínima por país
min_life_expectancy=df.groupby('country'),['lifeExp'].min()
print('La esperanza de vida mínima por país es:')
print(min_life_expectancy,'\n')