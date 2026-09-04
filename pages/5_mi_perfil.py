import streamlit as st

st.title("👤 Configurar Perfil")
st.caption("Completa tus datos por única vez. Quedarán vinculados a tu correo.")

# Simulación del correo detectado automáticamente al iniciar sesión
correo_actual = "licari@ejemplo.com" 

with st.form("form_perfil"):
    st.markdown(f"**Cuenta vinculada:** `{correo_actual}`")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        apellido = st.text_input("Apellido")
        nombre = st.text_input("Nombre")
        
    with col2:
        posicion_principal = st.selectbox("Posición Principal", ["Lateral", "Central", "Pivot", "Extremo", "Arquero"])
        posicion_secundaria = st.selectbox("Posición Secundaria", ["Ninguna", "Lateral", "Central", "Pivot", "Extremo", "Arquero"])
        
    guardar = st.form_submit_button("Guardar Datos")
    
    if guardar:
        if apellido and nombre:
            st.success(f"✅ Perfil de {apellido}, {nombre} guardado exitosamente. Ya puedes registrar tus sesiones.")
        else:
            st.error("⚠️ Por favor, completa tu Nombre y Apellido.")
