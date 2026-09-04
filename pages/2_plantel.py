import streamlit as st
import pandas as pd
import random

st.title("Plantel")

if 'players_df' in st.session_state:
    df_mostrar = st.session_state.players_df
    
    st.text_input("🔍 Buscar jugador...", placeholder="Ej: Tomás Fernández")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Renderizado de lista idéntica al prototipo
    for index, row in df_mostrar.iterrows():
        # Simulamos los estados de carga para el diseño visual
        estado_rand = random.choice(["Baja", "Moderada", "Alta"])
        if estado_rand == "Baja":
            color = "#2A9D8F" # Verde
            barras = "ılı"
        elif estado_rand == "Moderada":
            color = "#E9C46A" # Amarillo
            barras = "ıl"
        else:
            color = "#E63946" # Rojo
            barras = "ı"
            
        st.markdown(f"""
        <div style='background-color: #161618; padding: 12px 16px; border-radius: 12px; margin-bottom: 8px; display: flex; align-items: center; border: 1px solid #2A2A2D;'>
            <div style='width: 32px; height: 32px; border-radius: 6px; background-color: #2A2A2D; display: flex; justify-content: center; align-items: center; margin-right: 16px; font-weight: bold; font-size: 14px; color: #FFF;'>
                {row['player_id']}
            </div>
            <div style='flex-grow: 1;'>
                <div style='font-size: 15px; font-weight: 600; color: #FFFFFF; line-height: 1.2;'>{row['nombre']}</div>
                <div style='font-size: 12px; color: #8A8A8E; margin-top: 2px;'>{row['posicion']}</div>
            </div>
            <div style='text-align: right; display: flex; align-items: center;'>
                <span style='color: {color}; font-size: 14px; font-weight: 600; margin-right: 6px;'>{barras}</span>
                <span style='color: {color}; font-size: 13px; font-weight: 600;'>{estado_rand}</span>
                <span style='color: #4A4A4D; margin-left: 12px; font-size: 18px;'>›</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.warning("Vuelve al inicio para cargar la base de datos.")
