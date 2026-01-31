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
from pyparsing import alphas

df = pd.read_csv('ecommerce_preparados.csv')

print(df.head().to_string())
print(df.tail().to_string())

# Gráfico de Histograma - Cód da Marca com o Preço
sns.jointplot(x='Marca_Cod', y='Preço', data=df, kind='hist')
plt.title('Relação Marca e Preço')
plt.xlabel('Marca')
plt.ylabel('Preço')
plt.show()

# Gráfico de Dispersão
# As variáveis que serão avaliadas serão Material e Temporada, para saber se existe correlação do tipo do Material com as condições climáticas

sns.jointplot(x='Material_Cod', y='Temporada_Cod', data=df, kind='scatter')
plt.title('Dispersão Material e Temporada')
plt.xlabel('Material')
plt.ylabel('Temporada')
plt.show()

# Mapa de Calor - Desconto com a Temporada_Cod e Marca_Cod
corr = df[['Marca_Cod', 'Temporada_Cod', 'Desconto']].corr()
plt.title('Mapa de Calor- Desconto e Temporada')
plt.xlabel('Marca')
plt.ylabel('Temporada')
sns.heatmap(corr, annot=True, cmap='Blues')
plt.show()

# Gráfico de barra = Quais marcas são mais compradas
df['Qtd_Vendidos_Cod'].value_counts().plot(kind='bar', color='red')
plt.title('Quantidade Vendidas')
plt.xlabel('Qtd_Vendidas')
plt.xticks(rotation=45)
plt.ylabel('Contagem de Qtd_Vendidas')
plt.show()

# Gráfico de Pizza
plt.figure(figsize=(10, 10))
plt.pie(df['Qtd_Vendidos_Cod'].value_counts(), autopct='%.1f%%')
plt.title('Distribuição de Quantidade Vendidas')
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10, 7))
sns.kdeplot(df['Marca_Cod'], fill=True, color='green')
plt.title('Densidade de Marcas')
plt.xlabel('Marca')
plt.show()

# Gráfico de Regressão
sns.regplot(x='Marca_Cod', y='Preço', data=df, color='blue', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão entre Marcas e Preços')
plt.xlabel('Marca')
plt.ylabel('Preço')
plt.show()

