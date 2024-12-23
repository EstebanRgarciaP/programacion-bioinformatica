# ============================
# Metadatos
# ============================
'''
   Written by Esteban Garcia
'''

__author__ = "Esteban Garcia"
__credits__ = ["Esteban Garcia"]
__license__ = "MIT"
__version__ = "3.13.0"
__maintainer__ = "Esteban Garcia"
__email__ = "egarciap@unal.edu.co"
__status__ = "student"
__date__ = '2024/12/23'

# ============================
# Código principal
# ============================

# Importar bibliotecas necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lectura del conjunto de datos Iris desde seaborn
data = sns.load_dataset('iris')  # Este conjunto de datos contiene información de tres especies de Iris

# Vista general de los datos
print(data.head())  # Muestra las primeras filas del conjunto de datos para entender su estructura

# Análisis descriptivo
summary = data.describe()  # Genera un resumen estadístico para las variables numéricas
print(summary)

# Crear y guardar gráficos individualmente como archivos PDF

# Gráfico 1: Distribución de las especies
plt.figure(figsize=(8, 6))
sns.countplot(data=data,
              x='species',
              hue='species',
              palette='viridis',
              dodge=False)  # Gráfico de conteo para visualizar la distribución de especies
plt.title('Distribución de las especies de Iris')
plt.xlabel('Especie')
plt.ylabel('Cantidad')
plt.legend(title='Especie', loc='upper right')
plt.savefig('grafico_distribucion_especies.pdf')  # Guarda el gráfico como archivo PDF
plt.close()

# Gráfico 2: Diagrama de caja para las longitudes de pétalo por especie
plt.figure(figsize=(8, 6))
sns.boxplot(data=data,
            x='species',
            y='petal_length',
            hue='species',
            palette='Set2',
            dodge=False)  # Visualiza la variabilidad de longitud de pétalos por especie
plt.title('Distribución de la longitud de pétalo por especie')
plt.xlabel('Especie')
plt.ylabel('Longitud de pétalo (cm)')
plt.legend(title='Especie', loc='upper right')
plt.savefig('grafico_caja_longitud_petalo.pdf')
plt.close()

# Gráfico 3: Diagrama de dispersión entre longitud y ancho de pétalo por especie
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data,
                x='petal_length',
                y='petal_width',
                hue='species',
                palette='cool')  # Muestra la relación entre longitud y ancho de pétalos
plt.title('Relación entre longitud y ancho de pétalo')
plt.xlabel('Longitud de pétalo (cm)')
plt.ylabel('Ancho de pétalo (cm)')
plt.legend(title='Especie')
plt.savefig('grafico_dispersion_petalo.pdf')
plt.close()

# Gráfico 4: Mapa de calor de correlaciones
plt.figure(figsize=(8, 6))
correlation = data.drop(columns=['species']).corr()  # Calcula la correlación entre variables numéricas
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')  # Visualiza la matriz de correlación
plt.title('Matriz de correlación entre las variables')
plt.savefig('grafico_mapa_calor.pdf')
plt.close()

# Gráfico 5: Distribuciones KDE de las variables de sépalo
plt.figure(figsize=(10, 6))
sns.kdeplot(data=data,
            x='sepal_length',
            hue='species',
            fill=True,
            common_norm=False,
            palette='pastel')  # Gráfico de densidad para comparar distribuciones
plt.title('Distribuciones KDE de la longitud de sépalo por especie')
plt.xlabel('Longitud de sépalo (cm)')
plt.ylabel('Densidad')
plt.savefig('grafico_kde_sepal_length.pdf')
plt.close()

# Respuesta a la pregunta biológica
# Observaciones:
# 1. Las especies tienen distribuciones diferenciadas en términos de longitud y ancho de los pétalos.
# 2. Setosa tiene pétalos más pequeños que las otras especies.
# 3. Existe una fuerte correlación entre la longitud y el ancho del pétalo.
# 4. Las longitudes de sépalo no son tan discriminantes como las medidas de pétalo.

# Exportar análisis descriptivo a un archivo externo
summary.to_csv('iris_summary.csv', index=True)  # Guarda el resumen estadístico en formato CSV

print("Gráficas guardadas en archivos PDF individuales.")
