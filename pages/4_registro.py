import streamlit as st
from datetime import date
from utils.styles import apply_custom_css

# Forzar la identidad visual premium
apply_custom_css()

# Encabezado visual alineado a la identidad
st.markdown("<div class='page-title'>REGISTRAR SESIÓN</div>", unsafe_allow_html=True)
st.markdown("<div class='page-subtitle'>Ingresá los datos de tu entrenamiento y descanso diario.</div>", unsafe_allow_html=True)

with st.form("registro_sesion"):
    
    # Tarjeta sutil simulando el usuario logueado
    st.markdown("<div class='account-badge'>Jugador: <span>Licari, Juan Lautaro (Central)</span></div>", unsafe_allow_html=True)
    
    # Bloque 1: Contexto de la sesión
    col1, col2 = st.columns(2)
    with col1:
        fecha = st.date_input("Fecha", date.today())
    with col2:
        tipo = st.selectbox("Tipo de sesión", ["Entrenamiento", "Partido", "Gimnasio", "Recuperación"])
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Bloque 2: Carga y Bienestar
    col3, col4 = st.columns(2)
    with col3:
        duracion = st.number_input("Duración (minutos activos)", min_value=0, step=15)
    with col4:
        sueno = st.selectbox("Calidad de Sueño", [
            "Menos de 6 horas / Poco reparador",
            "6-7 horas / Regular",
            "7-8 horas / Reparador",
            "Más de 8 horas / Muy reparador"
        ])
        
    # El slider de sRPE va en ancho completo porque en celulares es más fácil de arrastrar con el pulgar
    st.markdown("<br>", unsafe_allow_html=True)
    srpe = st.slider("Percepción del Esfuerzo (sRPE)", 0, 10, 5, help="0 = Reposo absoluto | 10 = Esfuerzo máximo")
    
    notas = st.text_area("Notas / Observaciones (Opcional)", placeholder="Molestias musculares, sensaciones, etc.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Botón principal rojo institucional
    submit = st.form_submit_button("Guardar Registro")
    
    if submit:
        carga_total = duracion * srpe
        st.success(f"✅ Sesión guardada en tu historial. Carga calculada: **{carga_total} AU**")
