#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
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

# ============================
# Parte (a): Leer el archivo FASTA
# ============================

def leer_fasta(ruta_archivo):
    """
    Lee un archivo FASTA y devuelve un diccionario con los identificadores de las secuencias
    como claves y las secuencias como valores.
    """
    secuencias = {}
    with open(ruta_archivo, 'r') as archivo:
        identificador = None
        secuencia = ""  # Almacena la secuencia como una sola cadena
        for linea in archivo:
            linea = linea.strip()
            # Si la línea comienza con ">", es un identificador
            if linea.startswith(">"):
                # Si ya teníamos una secuencia anterior, la guardamos en el diccionario
                if identificador:
                    secuencias[identificador] = secuencia
                identificador = linea[1:]  # Remover el ">" al inicio del identificador
                secuencia = ""  # Reiniciar la secuencia
            else:
                # Agregar las líneas de secuencia directamente como una sola cadena
                secuencia += linea
        # Agregar la última secuencia
        if identificador:
            secuencias[identificador] = secuencia
    return secuencias

# ============================
# Parte (b): Calcular la frecuencia de nucleótidos (A, T, G, C)
# ============================

def frecuencia_nucleotidos(secuencia):
    """
    Calcula la frecuencia de nucleótidos (A, T, G, C) en una secuencia de ADN.
    """
    return {
        "A": secuencia.count("A"),
        "T": secuencia.count("T"),
        "G": secuencia.count("G"),
        "C": secuencia.count("C"),
    }

# ============================
# Código principal
# ============================

if __name__ == "__main__":
    # Solicitar al usuario la ruta del archivo FASTA
    print("Por favor, proporciona la ruta del archivo FASTA:")
    ruta_entrada = input("Ruta del archivo FASTA: ").strip()

    # Leer las secuencias del archivo FASTA
    secuencias = leer_fasta(ruta_entrada)

    # Mostrar los resultados en consola
    for identificador, secuencia in secuencias.items():
        longitud = len(secuencia)
        frecuencia = frecuencia_nucleotidos(secuencia)
        print(f"Secuencia: {identificador}")
        print(f"Longitud: {longitud}")
        print(f"Frecuencia de nucleótidos: {frecuencia}")
        print("-" * 30)
