import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        /* =========================================
           1. FONDOS Y ESTRUCTURA BASE
           ========================================= */
        .stApp { background-color: #050505; }
        
        /* Reducir padding superior excesivo */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
            max-width: 800px; /* Centrar y contener el formulario */
        }
        
        header {background-color: transparent !important;}
        #MainMenu, footer {visibility: hidden;}
        
        /* =========================================
           2. TIPOGRAFÍA Y ENCABEZADOS
           ========================================= */
        .page-title {
            color: #FFFFFF;
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 4px;
            letter-spacing: -0.5px;
        }
        .page-subtitle {
            color: #8A8A8E;
            font-size: 15px;
            margin-bottom: 24px;
        }
        
        /* =========================================
           3. TARJETAS Y FORMULARIOS (UI CARDS)
           ========================================= */
        /* Convertir el formulario nativo de Streamlit en una Card Premium */
        [data-testid="stForm"] {
            background-color: #161618 !important;
            border: 1px solid #2A2A2D !important;
            border-radius: 12px !important;
            padding: 24px !important;
            box-shadow: none !important;
        }
        
        /* Badge/Pill para la cuenta vinculada */
        .account-badge {
            background-color: #1E1E20;
            border: 1px solid #2A2A2D;
            color: #8A8A8E;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 13px;
            display: inline-block;
            margin-bottom: 20px;
        }
        .account-badge span { color: #FFFFFF; font-weight: 500; }
        
        /* =========================================
           4. CAMPOS DE ENTRADA (INPUTS & SELECTS)
           ========================================= */
        /* Estilizar inputs de texto y selectores */
        .stTextInput input, div[data-baseweb="select"] > div {
            background-color: #1E1E20 !important;
            border: 1px solid #2A2A2D !important;
            border-radius: 8px !important;
            color: #FFFFFF !important;
        }
        /* Color del texto de las etiquetas (labels) */
        .stTextInput label, .stSelectbox label {
            color: #8A8A8E !important;
            font-size: 13px !important;
            font-weight: 500 !important;
        }
        
        /* =========================================
           5. BOTONES (ELIMINAR GRIS DEFAULT)
           ========================================= */
        [data-testid="stFormSubmitButton"] button {
            background-color: #E63946 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            padding: 10px 24px !important;
            transition: all 0.2s ease;
            width: 100%;
        }
        [data-testid="stFormSubmitButton"] button:hover {
            background-color: #D62828 !important;
        }
        
        /* =========================================
           6. PANEL LATERAL (SIDEBAR)
           ========================================= */
        /* Fondo negro/gris carbón y sin violeta */
        [data-testid="stSidebar"] {
            background-color: #0F0F11 !important;
            border-right: 1px solid #2A2A2D !important;
        }
        /* Color de los enlaces inactivos */
        [data-testid="stSidebarNav"] a { color: #8A8A8E !important; }
        /* Elemento seleccionado (gris oscuro, sin azul/violeta) */
        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background-color: #1E1E20 !important;
            color: #FFFFFF !important;
        }
        [data-testid="stSidebarNav"] a[aria-current="page"] span {
            color: #E63946 !important; /* Acento rojo */
        }
        </style>
    """, unsafe_allow_html=True)
