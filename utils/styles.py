import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .metric-card {
            background-color: #1E1E1E;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            border-left: 4px solid #E63946;
        }
        </style>
    """, unsafe_allow_html=True)
