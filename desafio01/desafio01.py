import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
df = pd.read_csv('gxndinDatabase\desafio01\president_heights.csv')
print(df.head())

height = np.array(df['height(cm)'])
print(height)

# FUNÇÃO ROUND - ARREDONDA O NÚMERO PARA UMA DETERMINADA QUANTIDADE DE CASAS DECIMAIS
print('Média das alturas =: ', round(height.mean(),2))

print('Altura mínima: ', height.min())
print('Altura máxima: ', height.max())

# CARREGA DATASET
plt.hist(height)
plt.title('Altura dos presidentes EUA')
# EIXO X
plt.xlabel('Altura')
# EIXO Y
plt.ylabel('Numero')
plt.show()