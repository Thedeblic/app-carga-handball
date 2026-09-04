import streamlit as st
from datetime import date

st.title("📝 Registrar Sesión")
st.caption("Ingreso manual de cargas de entrenamiento")

# El sistema detecta quién inició sesión y muestra su nombre fijo
st.info("👤 Cargando datos como: **Licari, Juan Lautaro** (Central)")

with st.form("registro_sesion"):
    col1, col2 = st.columns(2)
    
    with col1:
        fecha = st.date_input("Fecha", date.today())
        tipo = st.selectbox("Tipo de sesión", ["Entrenamiento", "Partido", "Gimnasio", "Recuperación"])
        
    with col2:
        duracion = st.number_input("Duración (minutos activos)", min_value=0, step=15)
        srpe = st.slider("Percepción del Esfuerzo (sRPE)", 0, 10, 5)
        
    notas = st.text_area("Notas / Observaciones (Opcional)")
    
    submit = st.form_submit_button("Guardar Registro")
    if submit:
        carga_total = duracion * srpe
        st.success(f"✅ Sesión guardada en tu historial. Carga calculada: **{carga_total} AU**")
