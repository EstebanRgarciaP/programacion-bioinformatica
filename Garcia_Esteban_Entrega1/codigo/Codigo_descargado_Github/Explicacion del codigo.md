# FASTA Parser

Una herramienta eficiente y liviana para procesar archivos FASTA, comúnmente utilizados en bioinformática para representar secuencias biológicas (ADN, ARN, proteínas).

## Características

1. **Lectura de Archivos FASTA**  
   - La función `parse()` permite iterar sobre registros en archivos FASTA.
   - Compatible con archivos comprimidos en formatos como `.gz`, `.bz2`, `.zst` y `.lz4`.

2. **Representación de Registros**  
   - La clase `Record` representa una entrada de FASTA con los siguientes atributos:
     - `id`: Identificador único de la secuencia.
     - `seq`: Secuencia biológica (cadena de caracteres).
     - `desc`: Línea de descripción opcional.
   - Métodos útiles:
     - `format(wrap=70)`: Formatea un registro en estilo FASTA, con líneas envolventes.
     - `__len__()`: Devuelve la longitud de la secuencia.
     - `__contains__(char)`: Verifica si un carácter está presente en la secuencia.

3. **Escritura de Archivos FASTA**  
   - Permite escribir registros en archivos comprimidos o sin comprimir.

4. **Conversión a Diccionario**  
   - La función `to_dict()` convierte registros en un diccionario, donde las claves son los IDs de las secuencias.

## Instalación

El módulo requiere las bibliotecas `zstandard` y `lz4` para manejar ciertos formatos de compresión. Instálalas con:

```bash
pip install zstandard lz4
```
## Ejemplo de Uso

### Crear y Escribir un Registro

Este ejemplo muestra cómo crear un nuevo registro FASTA utilizando la clase `Record` y formatearlo para ser impreso en formato FASTA. Además, puedes especificar un límite para envolver las secuencias a una longitud de línea específica:

```python
from fasta import Record

# Crear un registro FASTA
record = Record(id='seq001', seq='ATGCATGCAT', desc='Example sequence')

# Imprimir el registro en formato FASTA con un límite de 5 caracteres por línea
print(record.format(wrap=5))

# Salida esperada:
# >seq001 Example sequence
# ATGCA
# TGCA
