import streamlit as st
from utils.styles import apply_custom_css
from data.mock_data import generate_mock_data

st.set_page_config(page_title="Jockey Club Handball | Performance", layout="wide", initial_sidebar_state="expanded")
apply_custom_css()

# Cargar datos en Session State (Singleton)
if 'players_df' not in st.session_state:
    st.session_state.players_df, st.session_state.sessions_df = generate_mock_data()

st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Escudo_del_Jockey_Club_Córdoba.png/120px-Escudo_del_Jockey_Club_Córdoba.png", width=100) # Reemplazar con logo real
st.sidebar.title("JOCKEY CLUB")
st.sidebar.caption("PERFORMANCE & TRAINING LOAD")

st.sidebar.markdown("---")
st.sidebar.page_link("app.py", label="🏠 Inicio / Dashboard")
st.sidebar.page_link("pages/2_plantel.py", label="👥 Plantel")
st.sidebar.page_link("pages/3_perfil.py", label="📊 Perfil Individual")
st.sidebar.page_link("pages/4_registro.py", label="📝 Registrar Sesión")
