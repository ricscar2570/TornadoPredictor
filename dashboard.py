
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("TornadoPredictor Dashboard")
st.sidebar.header("Filtri")

precipitation_layer = st.sidebar.checkbox("Mostra Precipitazioni", value=True)
wind_layer = st.sidebar.checkbox("Mostra Vento", value=True)
opacity = st.sidebar.slider("Trasparenza dei layer", 0.0, 1.0, 0.7)

data = pd.read_csv("weather_data.csv")
st.dataframe(data)

map_center = [data['latitude'].mean(), data['longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=5)

if precipitation_layer:
    folium.TileLayer(
        tiles='https://tile.openweathermap.org/map/precipitation_new/{z}/{x}/{y}.png?appid=YOUR_API_KEY',
        attr="OpenWeatherMap",
        name="Precipitazioni",
        opacity=opacity
    ).add_to(m)

if wind_layer:
    folium.TileLayer(
        tiles='https://tile.openweathermap.org/map/wind_new/{z}/{x}/{y}.png?appid=YOUR_API_KEY',
        attr="OpenWeatherMap",
        name="Vento",
        opacity=opacity
    ).add_to(m)

st_folium(m, width=700, height=500)
