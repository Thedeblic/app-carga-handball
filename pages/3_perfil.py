import streamlit as st

st.title("📊 Perfil Individual")
st.caption("Análisis detallado e historial (Fase: Contextualizar)")

if 'players_df' in st.session_state:
    players_df = st.session_state.players_df
    
    jugador_seleccionado = st.selectbox("Seleccionar Jugador", players_df['nombre'])
    
    tab1, tab2, tab3 = st.tabs(["Resumen", "Historial", "Comparativa"])
    
    with tab1:
        st.info(f"Métricas recientes para {jugador_seleccionado} (En desarrollo)")
    with tab2:
        st.write("Gráfico longitudinal de carga (En desarrollo)")
    with tab3:
        st.write("Comparativa vs Promedio de su posición (En desarrollo)")
else:
    st.warning("Vuelve al inicio para cargar la base de datos.")
