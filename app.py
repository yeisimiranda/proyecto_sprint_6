import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("\vehicles_us.csv")

st.header("Anucnios de Ventas de Coches en USA")

hist_button = st.button("Crea Histograma")

if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Crear Gráfica Dispersión")

if scatter_button:
    st.write("Creación de una gráfica de dispersión para el conjunto de datos de anuncios de venta de coches")
    fig_sactter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_sactter, use_container_width=True)
