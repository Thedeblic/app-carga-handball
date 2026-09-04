import streamlit as st
import pandas as pd

st.title("👥 Plantel")
st.caption("Visión detallada de los jugadores y su estado actual")

if 'players_df' in st.session_state:
    players_df = st.session_state.players_df
    
    filtro_estado = st.radio("Filtrar por estado:", ["Todos", "Disponible", "Limitado", "Lesionado"], horizontal=True)
    
    if filtro_estado != "Todos":
        df_mostrar = players_df[players_df['disponibilidad'] == filtro_estado]
    else:
        df_mostrar = players_df
        
    st.dataframe(df_mostrar, use_container_width=True, hide_index=True)
else:
    st.warning("Vuelve al inicio para cargar la base de datos.")
