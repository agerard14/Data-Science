#el programa genera datos de forma aleatoria para ser usados por
#otras aplicaciones
import pandas as pd
import numpy as np

#Generar datos ficticios
np.random.seed(42)
n_samples=500
data={
    "Producto":np.random.choice(["Balón","Raqueta","Zapatilla","Pesas"],size=n_samples),
    "Precio":np.round(np.random.uniform(20,150,size=n_samples),2),
    "Cantidad_Vendida":np.random.randint(1,50,size=n_samples)
}
df=pd.DataFrame(data)
#Guardar como archivo csv
df.to_csv('ventas_productos.csv',index=False)
print('Archivo ventas_productos.csv creado con éxito')