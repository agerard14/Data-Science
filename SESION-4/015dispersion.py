import pandas as pd
import matplotlib.pyplot as plt
gapminder=pd.read_csv('gapminder.csv')
plt.figure(figsize=(10,6))
#plt.scatter crea un gráfico de dispersión
scatter= plt.scatter(
    #datos para el eje X
    gapminder['lifeExp'],
    #datos para el eje Y
    gapminder['pop'],
    #los puntos se van a colorear en función de la esperanza de vida
    c=gapminder['lifeExp'],
    #viridis: paleta de colores graudales del azul a amarillo.
    cmap='viridis',
    #0.7 hace los puntos ligeramente transparentes
    alpha=0.7)
#crea una barra de colores
plt.colorbar(scatter,label='Esperanza de vida')
plt.title('Relación entre Esperanza de vida y Población',fontsize=14)
plt.xlabel('Esperanza de vida',fontsize=12)
plt.ylabel('Población',fontsize=12)
plt.grid(True, linestyle='--',alpha=0.5)
plt.legend('[lifeExp]',loc='upper left')
#ajustaremos los márgenes del gráfico automáticamente para que los elementos
#no se superpongan
plt.tight_layout()
plt.show()
