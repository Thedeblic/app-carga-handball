import streamlit as st
from utils.styles import apply_custom_css

apply_custom_css()

# Encabezado visual (Sin emojis, jerarquía profesional)
st.markdown("<div class='page-title'>CONFIGURAR PERFIL</div>", unsafe_allow_html=True)
st.markdown("<div class='page-subtitle'>Completá tus datos para personalizar tu experiencia.</div>", unsafe_allow_html=True)

# Lógica existente de sesión
correo_actual = "licari@ejemplo.com" 

# El formulario ahora tomará automáticamente el diseño de la "Card Principal" gracias al CSS
with st.form("form_perfil"):
    
    # Tarjeta sutil para la cuenta vinculada
    st.markdown(f"<div class='account-badge'>Cuenta vinculada: <span>{correo_actual}</span></div>", unsafe_allow_html=True)
    
    # Layout de 2 columnas para campos
    col_foto, col_datos = st.columns([1, 2.5])
    
    with col_foto:
        foto_subida = st.file_uploader("Foto de Perfil", type=["jpg", "png", "jpeg"], label_visibility="visible")
        if foto_subida is not None:
            st.image(foto_subida, use_container_width=True)
            
    with col_datos:
        # Fila 1: Nombres
        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            apellido = st.text_input("Apellido")
        with row1_col2:
            nombre = st.text_input("Nombre")
            
        # Fila 2: Posiciones
        row2_col1, row2_col2 = st.columns(2)
        with row2_col1:
            posicion_principal = st.selectbox("Posición Principal", ["Lateral", "Central", "Pivot", "Extremo", "Arquero"])
        with row2_col2:
            posicion_secundaria = st.selectbox("Posición Secundaria", ["Ninguna", "Lateral", "Central", "Pivot", "Extremo", "Arquero"])
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # El botón tomará automáticamente el color Rojo Institucional desde el CSS
    guardar = st.form_submit_button("Guardar Datos")
    
    # Lógica de guardado intacta
    if guardar:
        if apellido and nombre:
            st.success(f"Perfil de {apellido}, {nombre} guardado exitosamente.")
        else:
            st.error("Por favor, completa tu Nombre y Apellido.")
