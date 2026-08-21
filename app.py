import datetime
import streamlit as st

st.set_page_config(
    page_title="Taxi Fare Prediction",
    page_icon="🚕",
    layout="wide"
)

# Estilos CSS
st.markdown("""
<style>
    /* Fondo general */
    .stApp {
        background-color: #F4EBE1;
    }
    
    /* Tarjeta principal que envuelve todo */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #F0EAE1 !important;
        border-radius: 20px !important;
        border: 1px solid #D8CDBF !important;
        padding: 30px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
    }

    /* Estilo de los inputs */
    div[data-baseweb="input"] {
        border-radius: 8px !important;
        background-color: #F0F2F6 !important;
    }

    /* Botón borgoña */
    div.stButton > button {
        background-color: #701D2B !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
        height: 2.8rem !important;
        padding: 0 2rem !important;
    }
    div.stButton > button:hover {
        background-color: #4A111C !important;
    }
</style>
""", unsafe_allow_html=True)

# Contenedor único para todo el formulario e ilustración
with st.container(border=True):
    # Encabezado: Título a la izquierda + Taxi a la derecha
    c_title, c_taxi = st.columns([2.5, 1])
    with c_title:
        st.markdown("<h1 style='color: #2A0812; font-weight: 900; margin-top: 20px; font-size: 2.5rem;'>TAXI FARE PREDICTION</h1>", unsafe_allow_html=True)
    with c_taxi:
        st.image("taxi_ilustration.png", width=240)

    st.write("---")

    # 1. Trip Details
    st.markdown("##### 🗓️ Trip Details")
    c1, c2 = st.columns(2)
    with c1:
        fecha = st.date_input("Fecha", value=datetime.date(2027, 11, 4))
    with c2:
        hora = st.time_input("Hora", value=datetime.time(12, 0))

    # 2. Locations
    st.markdown("##### 📍 Pickup & Drop-off Locations")
    cp1, cp2 = st.columns(2)
    with cp1:
        pickup_long = st.number_input("Longitud recogida", value=-73.985428, format="%.6f")
    with cp2:
        pickup_lat = st.number_input("Latitud recogida", value=40.748817, format="%.6f")

    cd1, cd2 = st.columns(2)
    with cd1:
        dropoff_long = st.number_input("Longitud bajada", value=-73.985428, format="%.6f")
    with cd2:
        dropoff_lat = st.number_input("Latitud bajada", value=40.748817, format="%.6f")

    # 3. Passengers
    st.markdown("##### 👥 Number of Passengers")
    pasajeros = st.number_input("Pasajeros", min_value=1, max_value=6, value=1)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Botón y resultado
    if st.button("Calcular tarifa"):
        st.success("💰 **La tarifa estimada es: $5.61**")
