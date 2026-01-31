#   ATIVIDADE DO MÓDULO 10

# Passo a passo
#
# Leia o arquivo ‘ecommerce_estatistica.csv’ dentro de um dataframe .
#
# Faça uma análise detalhada dos dados, descubra quais dados gostaria de destacar e crie os seguintes gráficos:
#
# Gráfico de Histograma
#
# Gráfico de dispersão
#
# Mapa de calor
#
# Gráfico de barra
#
# Gráfico de pizza
#
# Gráfico de densidade
#
# Gráfico de Regressão
#
# Adicione títulos nos gráficos e nos eixos para ficar claro os objetivos dos gráficos

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_preparados.csv')

print(df.head().to_string())
print(df.tail().to_string())

# Gráfico de Histograma - Cód da Marca com o Preço
sns.jointplot(x='Marca_Cod', y='Preço', data=df, kind='hist')
plt.show()

# Gráfico de Dispersão
# As variáveis que serão avaliadas serão Material e Temporada, para saber se existe correlação do tipo do Material com as condições climáticas

sns.jointplot(x='Material_Cod', y='Temporada_Cod', data=df, kind='scatter')
plt.show()

# Mapa de Calor - Desconto com a Temporada_Cod e Marca_Cod
corr = df[['Marca_Cod', 'Temporada_Cod', 'Desconto']].corr()
sns.heatmap(corr, annot=True, cmap='Blues')
plt.show()


