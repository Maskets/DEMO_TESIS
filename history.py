import streamlit as st
import pandas as pd

def app():
    st.title("Historial de Evaluaciones")

    st.write("Resultados previos de estudiantes evaluados:")

    datos = pd.DataFrame({
        "Nombre": ["Juan Pérez", "María López"],
        "Fecha": ["2025-06-01", "2025-05-28"],
        "Probabilidad de Desercion": ["42%", "65%"]
    })

    st.table(datos)
