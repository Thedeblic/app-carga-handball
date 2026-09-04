import streamlit as st
import pandas as pd

st.title("👥 Plantel")
st.caption("Visión detallada de los jugadores y su estado actual")

if 'players_df' in st.session_state:
    players_df = st.session_state.players_df
    
    # Filtros superiores
    filtro_estado = st.radio("Filtrar por estado:", ["Todos", "Disponible", "Limitado", "Lesionado"], horizontal=True)
    
    if filtro_estado != "Todos":
        df_mostrar = players_df[players_df['disponibilidad'] == filtro_estado]
    else:
        df_mostrar = players_df
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Renderizado de lista estilo App (Reemplaza a la tabla genérica)
    for index, row in df_mostrar.iterrows():
        # Asignación de colores según el estado físico
        if row['disponibilidad'] == "Disponible":
            color_estado = "#2A9D8F" # Verde
        elif row['disponibilidad'] == "Limitado":
            color_estado = "#F4A261" # Naranja
        else:
            color_estado = "#E63946" # Rojo
            
        st.markdown(f"""
        <div style='background-color: #1E1E1E; padding: 15px 20px; border-radius: 8px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; border-left: 3px solid {color_estado};'>
            <div>
                <h4 style='margin: 0; color: white; font-size: 18px;'>{row['nombre']}</h4>
                <span style='color: gray; font-size: 14px;'>{row['posicion']}</span>
            </div>
            <div style='text-align: right;'>
                <span style='color: {color_estado}; font-weight: bold; font-size: 14px;'>{row['disponibilidad'].upper()}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.warning("Vuelve al inicio para cargar la base de datos.")
