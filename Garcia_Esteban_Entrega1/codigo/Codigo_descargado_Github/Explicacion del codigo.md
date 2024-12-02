# FASTA File Handling and Compression

Este script de Python proporciona utilidades para leer y escribir archivos FASTA, que se utilizan comúnmente en bioinformática para almacenar datos de secuencias (ADN, ARN, proteínas). El script incluye soporte para varios formatos comprimidos (gzip, bz2, lz4, zstandard) y ofrece métodos para analizar, iterar y formatear registros FASTA. Además, proporciona detección de tipo de compresión y métodos para cargar archivos FASTA en memoria como diccionarios para un fácil acceso por identificador de secuencia.

---

## Componentes del Código

### 1. **Clase `Record`**
   La clase `Record` representa un registro FASTA, encapsulando el identificador de secuencia (`id`), la secuencia (`seq`) y una descripción opcional (`desc`).

   - **Atributos**:
     - `id` (str): El identificador de la secuencia.
     - `seq` (str): La cadena de la secuencia.
     - `desc` (str, opcional): La línea de descripción que sigue al '>' en los archivos FASTA.
     
   - **Métodos Principales**:
     - `__str__(self)`: Devuelve el registro FASTA como una cadena formateada.
     - `format(self, wrap=70)`: Devuelve el formato FASTA, con una opción para envolver las secuencias a una longitud de línea especificada.
     - `__len__(self)`: Devuelve la longitud de la secuencia.
     - `__iter__(self)`: Itera sobre cada carácter en la secuencia.
     - `__contains__(self, char)`: Verifica si un carácter está presente en la secuencia.
     - `description(self)`: Devuelve la línea de descripción (defline).

   Ejemplo:
   ```python
   record = Record(id="NP_055309.2", seq="MRELEAKAT", desc="TNRC6A")
   print(record)  # >NP_055309.2 TNRC6A
   print(record.seq)  # MRELEAKAT
