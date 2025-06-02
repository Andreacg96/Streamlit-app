import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análisis Exploratorio de Datos - Vehículos")
@st.cache_data
def cargar_datos():
    return pd.read_csv("vehicles_us.csv")
df = cargar_datos()

# Mostrar datos
st.write("### Vista previa del dataset")
st.dataframe(df.head(20))

mostrar_histograma = st.checkbox("Mostrar histograma de precios")

if mostrar_histograma:
    st.write("Histograma de precios de vehículos")
    fig_hist = px.histogram(df, x="price", nbins=50, title="Distribución de precios de vehículos")
    st.plotly_chart(fig_hist)

# Casilla para scatter plot
mostrar_dispersion = st.checkbox("Mostrar gráfico de dispersión: Precio vs. Kilometraje")

if mostrar_dispersion:
    st.write("Gráfico de dispersión entre precio y kilometraje (odometer)")
    fig_scatter = px.scatter(
        df, x="odometer", y="price", color="type",
        title="Relación entre Precio y Kilometraje", opacity=0.6
    )
    st.plotly_chart(fig_scatter)