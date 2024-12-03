import pandas as pd
import matplotlib.pyplot as plt
archivo_csv='reto_academico.csv'
datos=pd.read_csv(archivo_csv)
print(datos)
plt.figure(figsize=(10,6))
plt.plot(datos['Evaluacion'],datos['Carla'],marker='o',label='Carla')
plt.plot(datos['Evaluacion'],datos['Pedro'],marker='o',label='Pedro')
plt.plot(datos['Evaluacion'],datos['Sofía'],marker='o',label='Sofía')
plt.title('Evolucion del Rendimiento Academico')
plt.xlabel('Evaluacion')
plt.ylabel('Calificacion')
plt.legend()
plt.grid(True)
plt.savefig('RendimientoAcademico.png')
plt.show()