# lab2.py
# Laboratorio 2 – Análisis de datos con Pandas
# Dataset: Nascar champion History Dataset.csv
# Autor: Fredys Alejandro Hernández Robles
        # Brayan Adaly Campos Martinez
        # Jeremias neftaly fuentes Mendez
# Fecha: [fecha actual]

import pandas as pd
import numpy as np

# 1. Cargar el dataset
df = pd.read_csv("Nascar champion History Dataset.csv")

# 2. Resumen estadístico
print("\n--- Resumen estadístico con describe() ---")
print(df.describe(include="all"))

# 3. Tipos de datos
print("\n--- Tipos de datos de cada columna ---")
print(df.dtypes)

# 4. Primeros y últimos registros
print("\n--- Primeros registros con head() ---")
print(df.head())
print("\n--- Últimos registros con tail() ---")
print(df.tail())

# 5. Ordenar resultados por alguna columna (ejemplo: Year)
if "Year" in df.columns:
    print("\n--- Dataset ordenado por Year ---")
    print(df.sort_values(by="Year"))

# 6. Medidas estadísticas sobre una columna numérica (ejemplo: Year si existe)
if "Year" in df.columns:
    print("\n--- Medidas estadísticas sobre la columna Year ---")
    print("Media:", np.mean(df["Year"]))
    print("Mediana:", np.median(df["Year"]))
    print("Desviación estándar:", np.std(df["Year"]))

# Si existe otra columna numérica como "Wins" se puede usar también:
if "Wins" in df.columns:
    print("\n--- Medidas estadísticas sobre la columna Wins ---")
    print("Media:", np.mean(df["Wins"]))
    print("Mediana:", np.median(df["Wins"]))
    print("Desviación estándar:", np.std(df["Wins"]))



# 7. Filtrar datos (ejemplo: campeones después del año 2000)
if "Year" in df.columns:
    print("\n--- Campeones después del año 2000 ---")
    print(df[df["Year"] > 2000])
