import streamlit as st
import requests
import datetime

st.title("Taxi Fare Prediction")

# Controles para seleccionar los datos del viaje
col1, col2 = st.columns(2)

with col1:
    date = st.date_input("Fecha del viaje", datetime.date.today())
    pickup_longitude = st.number_input("Longitud de recogida", value=-73.985428, format="%.6f")
    dropoff_longitude = st.number_input("Longitud de bajada", value=-73.985428, format="%.6f")

with col2:
    time = st.time_input("Hora del viaje", datetime.time(12, 0))
    pickup_latitude = st.number_input("Latitud de recogida", value=40.748817, format="%.6f")
    dropoff_latitude = st.number_input("Latitud de bajada", value=40.748817, format="%.6f")

passenger_count = st.number_input("Número de pasajeros", min_value=1, max_value=8, value=1)

# Construir el formato de fecha y hora para la API (YYYY-MM-DD HH:MM:SS)
pickup_datetime = f"{date} {time}"

# Diccionario con los parámetros para la API
params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": int(passenger_count)
}

url = 'https://taxifare.lewagon.ai/predict'

# Llamada a la API al hacer clic en el botón
if st.button("Calcular tarifa"):
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        prediction = response.json().get("fare", 0)
        st.success(f"💰 La tarifa estimada es: **${prediction:.2f}**")
    else:
        st.error("Error al conectar con la API de predicción.")
