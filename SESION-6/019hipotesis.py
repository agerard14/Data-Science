#se desea determinar si en dos equipos de trabajo de una empresa existe
#diferencia significativa en la cantidad de tareas completas por semana
import numpy as np
from scipy.stats import ttest_ind

np.random.seed(42)
equipoA=np.random.normal(loc=50, scale=8,size=30)
equipoB=np.random.normal(loc=55,scale=10,size=30)
stat,p=ttest_ind(equipoA,equipoB)

print('Productividad semanal promedio del equipo A:',np.mean(equipoA))
print('Productividad semanal promedio del equipo B:',np.mean(equipoB))
print('\nEstadistico t:',stat)
print('valor p:',p)
#nivel de significancia
alpha=0.05
if p<alpha:
    print('\nRechazamos la hipótesis nula: Hay una diferencia significativa'
          ' entre la productividad de ambos equipos')
else:
    print('\nNo rechazamos la hipótesis nula: no hay evidencia suficiente'
          'para afirmar que las productividades son diferentes')