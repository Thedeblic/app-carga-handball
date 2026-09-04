import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        /* Fondo negro profundo */
        .stApp { background-color: #050505; }
        
        /* Eliminar el margen superior gigante de Streamlit */
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
        }
        
        /* Hacer la barra superior transparente pero MANTENER el botón funcional */
        header {background-color: transparent !important;}
        
        /* Ocultar solo el menú derecho de Streamlit (los tres puntos) y el pie de página */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Tarjetas KPI limpias */
        .kpi-card {
            background-color: #161618;
            border-radius: 12px;
            padding: 16px;
            border: 1px solid #2A2A2D;
        }
        </style>
    """, unsafe_allow_html=True)
