import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_state(id):
    return idstate[id]

data = pd.read_csv("Computos2006-Presidente.txt", sep="|")
print("Número de entradas:", data.shape)

st.markdown("# Análisis de datos de las votaciones del 2006")
st.markdown("Primero cargamos los datos")
st.markdown(f"Número de entradas: {data.shape}")





idstate = {1: 'Aguascalientes', 2:'Baja California', 3: 'Baja California Sur', 4: 'Campeche',
           5: 'Coahuila', 6: 'Colima', 7: 'Chiapas', 8: 'Chihuahua', 9:'CDMX', 10: 'Durango',
           11: 'Guanajuato', 12: 'Guerrero', 13: 'Hidalgo', 14: 'Jalisco', 15: 'México',
           16: 'Michoacán', 17: 'Morelos', 18: 'Nayarit', 19: 'Nuevo León', 20: 'Oaxaca',
           21: 'Puebla', 22: 'Querétaro', 23: 'Quintana Roo', 24: 'San Luis Potosí',
           25: 'Sinaloa', 26: 'Sonora', 27: 'Tabasco', 28: 'Tamaulipas', 29: 'Tlaxcala',
           30: 'Veracruz', 31: 'Yucatán', 32: 'Zacatecas'}


data["ID_ESTADO"] = data["ID_ESTADO"].apply(lambda x: idstate[x])

datos_10 = data.head(10)

print(datos_10["ID_ESTADO"])

st.table(datos_10["ID_ESTADO"])

data.rename(columns={"ID_ESTADO": "ESTADO"}, inplace=True)

len(data.ESTADO.unique())

st.markdown("Los estados que votaron son:{len(data.ESTADO.unique())}")

votoExtranjero = data[data["TIPO_CANDIDATURA"]== 6]
votoLocal = data[data["TIPO_CANDIDATURA"]== 1]

votoExtranjero = votoExtranjero.drop(columns=["TIPO_CANDIDATURA"])
votoLocal = votoLocal.drop(columns=["TIPO_CANDIDATURA"])

partidos = ["PAN", "APM", "PBT", "NA", "ASDC", "NO_VOTOS_VALIDOS", "NO_VOTOS_NULOS"]

suma_votos = votoLocal[partidos].sum() + votoExtranjero[partidos].sum()

porcentaje = (suma_votos / suma_votos.sum())

st.bar_chart(porcentaje.plot(kind="bar"))