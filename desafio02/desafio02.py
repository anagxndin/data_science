# ANÁLISE DEMOGRÁFICA POR COORDENADAS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

df_cidades = pd.read_csv('gxndinDatabase\desafio02\california_cities.csv')
print(df_cidades.head())

#APAGAR COLUNAS VAZIAS
df_cidades = df_cidades.dropna(subset='elevation_m')
colunas_exclusão =  ['elevation_ft']
df_cidades = df_cidades.drop(colunas_exclusão, axis=1)

#ARMAZENANDO INFOS EM VARIÁVEIS
latitude, longitude = df_cidades['latd'], df_cidades['longd']
population, area = df_cidades['population_total'], df_cidades['area_total_km2']

#CONFIGURAÇÕES DO GRÁFICO
plt.scatter(longitude, latitude, label=None, c=np.log10(population), cmap='viridis', s=area, linewidth=0, alpha=0.5)
plt.axis('equal')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3,7)

for area in {100, 300, 500}:
    plt.scatter([], [], c='k', alpha=0.3, s=area, label=str(area)+ 'km$^2$')

plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Area da cidade')
plt.title("Area e População das cidades da California")
plt.show()