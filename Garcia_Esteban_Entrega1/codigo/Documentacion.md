# Proyecto de Análisis de Secuencias de ADN

Este proyecto permite analizar secuencias de ADN contenidas en un archivo FASTA. El programa procesa las secuencias para calcular su longitud y la frecuencia de nucleótidos (A, T, G, C) en cada una de ellas.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de carpetas y archivos:

### `codigo/Analyze-fasta.py`

El archivo `Analyze-fasta.py` contiene el código principal del proyecto. El código realiza las siguientes funciones:

- Lee un archivo en formato FASTA que contiene secuencias de ADN.
- Calcula la longitud de cada secuencia.
- Calcula la frecuencia de los nucleótidos A, T, G y C en cada secuencia.

#### Funcionamiento del Código

1. **Lectura del archivo FASTA:**
   El programa comienza solicitando al usuario la ruta del archivo FASTA, el cual debe estar en formato de texto y contener las secuencias de ADN en el formato estándar de FASTA (con identificadores precedidos por el símbolo `>`).

2. **Cálculo de longitud y frecuencia de nucleótidos:**
   Luego, el código calcula:
   - La longitud de cada secuencia de ADN.
   - La frecuencia de los nucleótidos (A, T, G, C) dentro de cada secuencia.

#### Código

```python
   Written by Esteban Garcia
   ''' 

__author__ = "Esteban Garcia"
__credits__ = ["Esteban Garcia"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Esteban Garcia"
__email__ = "egarciap@unal.edu.co"
__status__ = "student"
__date__ = '2024/12/02'

# ============================
# Variables globales
# ============================

ruta_entrada = ""  # Ruta o nombre del archivo FASTA proporcionado por el usuario
secuencias = {}    # Diccionario que almacena las secuencias del archivo FASTA
longitud = 0       # Longitud de cada secuencia
frecuencia = {}    # Frecuencia de nucleótidos (A, T, G, C) en cada secuencia
...
