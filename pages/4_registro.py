import streamlit as st
from datetime import date

st.title("📝 Registrar Sesión")
st.caption("Ingreso manual de cargas de entrenamiento y partidos")

if 'players_df' in st.session_state:
    players_df = st.session_state.players_df
    
    with st.form("registro_sesion"):
        col1, col2 = st.columns(2)
        
        with col1:
            jugador = st.selectbox("Jugador", players_df['nombre'])
            fecha = st.date_input("Fecha", date.today())
            tipo = st.selectbox("Tipo de sesión", ["Entrenamiento", "Partido", "Gimnasio", "Recuperación"])
            
        with col2:
            duracion = st.number_input("Duración (minutos activos)", min_value=0, step=15)
            srpe = st.slider("Percepción del Esfuerzo (sRPE)", 0, 10, 5)
            notas = st.text_area("Notas / Observaciones")
            
        carga_total = duracion * srpe
        st.info(f"Carga de Entrenamiento (TL) calculada: **{carga_total} AU**")
        
        submit = st.form_submit_button("Guardar Registro")
        
        if submit:
            st.success(f"✅ Sesión guardada correctamente para {jugador}.")
else:
    st.warning("Vuelve al inicio para cargar la base de datos.")
