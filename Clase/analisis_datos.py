import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Diccionario de estados
idstate = {
    1: 'Aguascalientes', 2: 'Baja California', 3: 'Baja California Sur', 4: 'Campeche',
    5: 'Coahuila', 6: 'Colima', 7: 'Chiapas', 8: 'Chihuahua', 9: 'CDMX', 10: 'Durango',
    11: 'Guanajuato', 12: 'Guerrero', 13: 'Hidalgo', 14: 'Jalisco', 15: 'México',
    16: 'Michoacán', 17: 'Morelos', 18: 'Nayarit', 19: 'Nuevo León', 20: 'Oaxaca',
    21: 'Puebla', 22: 'Querétaro', 23: 'Quintana Roo', 24: 'San Luis Potosí',
    25: 'Sinaloa', 26: 'Sonora', 27: 'Tabasco', 28: 'Tamaulipas', 29: 'Tlaxcala',
    30: 'Veracruz', 31: 'Yucatán', 32: 'Zacatecas'
}

# Función para obtener el estado
def get_state(id):
    return idstate.get(id, "Desconocido")

# Cargar datos
data = pd.read_csv("Computos2006-Presidente.txt", sep="|")
st.markdown("# Análisis de datos de las votaciones del 2006")
st.markdown("Primero cargamos los datos")
st.write(f"Número de entradas: {data.shape[0]}")

# Mapear estados
data["ID_ESTADO"] = data["ID_ESTADO"].apply(lambda x: get_state(x))

# Mostrar primeras 10 filas
datos_10 = data.head(10)
st.markdown("### Primeras 10 filas de los datos:")
st.table(datos_10[["ID_ESTADO"]])

# Renombrar columna
data.rename(columns={"ID_ESTADO": "ESTADO"}, inplace=True)

# Mostrar número de estados únicos
num_estados = len(data.ESTADO.unique())
st.markdown(f"### Número de estados que votaron: {num_estados}")

# Filtrar datos por tipo de candidatura
votoExtranjero = data[data["TIPO_CANDIDATURA"] == 6]
votoLocal = data[data["TIPO_CANDIDATURA"] == 1]

# Eliminar columna innecesaria
votoExtranjero = votoExtranjero.drop(columns=["TIPO_CANDIDATURA"])
votoLocal = votoLocal.drop(columns=["TIPO_CANDIDATURA"])

# Sumar votos por partido
partidos = ["PAN", "APM", "PBT", "NA", "ASDC", "NO_VOTOS_VALIDOS", "NO_VOTOS_NULOS"]
suma_votos = votoLocal[partidos].sum() + votoExtranjero[partidos].sum()

# Calcular porcentaje
porcentaje = (suma_votos / suma_votos.sum())

# Mostrar gráfico de barras
st.markdown("### Porcentaje de votos por partido:")
st.bar_chart(porcentaje)