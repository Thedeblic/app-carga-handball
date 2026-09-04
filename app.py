import streamlit as st
import pandas as pd
from datetime import date

# 1. Configuración principal de la aplicación
st.set_page_config(page_title="App Handball - Control de Cargas", layout="wide")

# 2. Menú Lateral: Sistema de Login
st.sidebar.title("🔐 Acceso al Sistema")
email = st.sidebar.text_input("Correo electrónico").lower()
pin = st.sidebar.text_input("PIN de acceso", type="password")
btn_ingresar = st.sidebar.button("Iniciar Sesión")

# 3. Lógica de vistas separadas (Privacidad estricta)
if btn_ingresar:
    
    # --- VISTA CUERPO TÉCNICO ---
    # Simulamos el acceso del CT (luego esto se validará con tu Google Sheet)
    if email == "ct@equipo.com" and pin == "1234":
        st.sidebar.success("Sesión iniciada: Cuerpo Técnico")
        
        st.title("📊 Panel de Control General (Cuerpo Técnico)")
        st.write("Vista de información cruzada. Solo el CT tiene acceso a esta pantalla.")
        
        # Muestra de cómo se verá la tabla cruzada de los 20 jugadores
        st.subheader("Alertas de Carga Semanal")
        datos_simulados_ct = pd.DataFrame({
            "Nombre y Apellido": ["Jugador 1", "Jugador 2", "Jugador 3"],
            "Carga Aguda (7d)": [2500, 3100, 1800],
            "ACWR": [1.1, 1.5, 0.9],
            "Motivo de Alerta": ["Óptimo", "⚠️ Peligro sobrecarga (ACWR > 1.3)", "Normal"]
        })
        st.dataframe(datos_simulados_ct, use_container_width=True)
        
    # --- VISTA JUGADOR ---
    # Si ingresa cualquier otro usuario con PIN correcto
    elif email != "" and pin == "0000":
        st.sidebar.success(f"Sesión iniciada: {email}")
        
        st.title("🤾‍♂️ Perfil Físico Individual")
        st.info("Tus datos están protegidos. Solo tú y el Cuerpo Técnico pueden ver esta información.")
        
        # Formulario para que el jugador cargue sus datos diarios
        st.subheader("📝 Cargar sesión del día")
        with st.form("carga_diaria"):
            col1, col2 = st.columns(2)
            
            with col1:
                fecha = st.date_input("Fecha del estímulo", date.today())
                duracion = st.number_input("Duración de la sesión (min. activos)", min_value=0)
                rpe = st.slider("Percepción del Esfuerzo (sRPE 0-10)", 0, 10, 5)
            
            with col2:
                sueno = st.text_input("Calidad del sueño (horas y sensación)")
                # Los cálculos de Carga Diaria, Aguda y Crónica los hará el sistema automáticamente por detrás
            
            enviado = st.form_submit_button("Subir datos al sistema")
            
            if enviado:
                st.success("✅ Datos registrados exitosamente. El CT ya los tiene en su base.")
                
    else:
        st.sidebar.error("❌ Correo o PIN incorrectos")

else:
    st.info("👈 Por favor, ingresa tus credenciales en el menú lateral para acceder.")
