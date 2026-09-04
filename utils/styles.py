import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        /* Fondo general negro profundo tipo App */
        .stApp {
            background-color: #050505;
        }
        /* Ocultar elementos nativos */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Estilo de tarjetas UI (como el prototipo) */
        .kpi-card {
            background-color: #161618;
            border-radius: 12px;
            padding: 16px;
            border: 1px solid #2A2A2D;
            display: flex;
            flex-direction: column;
        }
        .kpi-label {
            font-size: 13px;
            color: #8A8A8E;
            margin-bottom: 8px;
        }
        .kpi-value {
            font-size: 24px;
            font-weight: 700;
            color: #FFFFFF;
            margin: 0;
        }
        </style>
    """, unsafe_allow_html=True)
