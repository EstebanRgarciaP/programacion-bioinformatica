# Análisis Exploratorio del Conjunto de Datos Iris

Este repositorio contiene un script de Python para realizar un análisis exploratorio del conjunto de datos Iris. Este conjunto de datos clásico es ampliamente utilizado en estadística y aprendizaje automático, y describe las medidas de tres especies de flores: *Iris setosa*, *Iris versicolor* y *Iris virginica*.

## Características

1. **Carga de Datos**
   - El conjunto de datos Iris se carga directamente desde la biblioteca `seaborn`.

2. **Análisis Descriptivo**
   - Se genera un resumen estadístico de las variables numéricas utilizando `pandas`.
   - Este resumen se exporta a un archivo CSV para facilitar su revisión.

3. **Generación de Gráficos**
   - Se crean y guardan gráficos visuales que ayudan a entender mejor los datos:
     - Distribución de las especies.
     - Diagramas de caja para analizar las longitudes de los pétalos por especie.
     - Diagramas de dispersión entre longitud y ancho de pétalo.
     - Mapas de calor de correlaciones entre variables numéricas.
     - Distribuciones KDE (Kernel Density Estimation) para la longitud del sépalo.
   - Cada gráfico se guarda como un archivo PDF en el directorio de trabajo.

4. **Respuesta a Preguntas Biológicas**
   - Observaciones clave extraídas de los datos:
     - Diferencias en las distribuciones de las especies.
     - Identificación de correlaciones significativas entre las medidas.
     - Setosa tiene pétalos más pequeños que las otras especies.

## Requisitos de Instalación

Este script requiere las siguientes bibliotecas de Python:

```bash
pip install pandas seaborn matplotlib
```

## Ejemplo de Uso

Este ejemplo muestra cómo ejecutar el script para analizar el conjunto de datos Iris y generar gráficos:

1. **Ejecución del Script**

   Ejecuta el script en tu entorno de Python:

   ```bash
   python iris_analysis.py
   ```

2. **Salida Esperada**

   - Se imprimirá en la consola el resumen descriptivo de los datos.
   - Se generarán cinco gráficos en formato PDF:
     - `grafico_distribucion_especies.pdf`
     - `grafico_caja_longitud_petalo.pdf`
     - `grafico_dispersion_petalo.pdf`
     - `grafico_mapa_calor.pdf`
     - `grafico_kde_sepal_length.pdf`
   - El archivo CSV con el análisis descriptivo (`iris_summary.csv`) también estará disponible en el directorio de trabajo.

3. **Análisis Realizado**

   El script responde a preguntas como:
   - ¿Cuáles son las diferencias entre las especies en términos de sus características medibles?
   - ¿Existen correlaciones entre las variables?
   - ¿Qué características distinguen mejor a las especies?

## Contribución

Si deseas contribuir a este proyecto, puedes hacerlo mediante un *pull request*. También puedes enviar tus sugerencias o reportar errores abriendo un *issue* en este repositorio.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.

