import pandas as pd
#url de internet
url="https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
df=pd.read_csv(url)

promedio_gdp=df.groupby('continent')['gdpPercap'].mean().reset_index()
#el resultado de groupby es una Serie, por lo que usamos reset_index()
#para convertirlo en un dataFrame
promedio_gdp=promedio_gdp.sort_values(by='gdpPercap')
#ordena las filas en función de la columna gdpPercap (por defecto de menor
#a mayor)
print('el ingreso per cápita por continente ordenado de menor a mayor es:')
print(promedio_gdp)

### si lo quieres ver de mayor a menor
promedio_gdp=df.groupby('continent')['gdpPercap'].mean().reset_index()
promedio_gdp=promedio_gdp.sort_values(by='gdpPercap',ascending=False)
print('el ingreso per cápita por continente ordenado de mayor a menor es:')
print(promedio_gdp)

#Ordenar la esperanza de vida promedio (lifeExp) por continente de
#menor a mayor
promedio_life_exp=df.groupby('continent')['lifeExp'].mean().reset_index()
promedio_life_exp=promedio_life_exp.sort_values(by='continent')
print('Los promedios de esperanza de vida por continente son:')
print(promedio_life_exp,'\n')
#mostrar el total de poblacion (pop) por pais, de mayor a menor
total_poblacion=df.groupby('country')['pop'].sum().reset_index()
total_poblacion=total_poblacion.sort_values(by='pop',ascending=False)
print('El total de población por país de mayor a menor es:')
print(total_poblacion,'\n')
#ordenar el promedio de ingresos per cápita(gdpPercap) en el año 2007
#de menor a mayor agrupado por continente
df_2007=df[df['year']==2007]#filtrar solo los datos del año 2007
promedio_gdp_2007=df_2007.groupby('continent')['gdpPercap'].mean().reset_index()
promedio_gdp_2007=promedio_gdp_2007.sort_values(by='gdpPercap')
print('Promedio de ingresos per cápita del año 2007 por continentes de menor a mayor:')
print(promedio_gdp_2007,'\n')

#filtraremos datos del año 2007 y paises de Asia, luego calcularemos el 
# promedio de esperanza de vidad (lifeExp) por país, ordenado de mayor a menor

#filtrar solo datos del año 2007 y del continente Asia
df_2007_asia=df[(df['year']==2007) & (df['continent']=='Asia')]
#calcular el promedio de esperanza de vida por pais
promedio_life_exp_asia=df_2007_asia.groupby('country')['lifeExp'].mean().reset_index()
#ordenamos de mayor a menor
promedio_life_exp_asia=promedio_life_exp_asia.sort_values(by='lifeExp',ascending=False)
print('Promedio de esperanza de vida en Asia (2007) ordenado de mayor a menor: ')
print(promedio_life_exp_asia,'\n')

#filtrar los datos del continente Africa con un ingreso per cápita (gdpPercap) 
# mayor a 1000, y calcular el total de población (pop) por país, ordenado de 
# menor a mayor 

#filtrar datos de Africa con ingreso per cápita mayor a 1000
df_africa_gdp=df[(df['continent']=='Africa')&(df['gdpPercap']>1000)]
#calcular el total de población por país
total_poblacion_africa=df_africa_gdp.groupby('country')['pop'].sum().reset_index()
#ordenar de menor a mayor
total_poblacion_africa=total_poblacion_africa.sort_values(by='pop')
print('El total de población en África con ingresos per cápita>1000  de menor a mayor son:')
print(total_poblacion_africa,'\n')