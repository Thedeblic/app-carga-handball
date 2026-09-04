import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

st.title("Estado del Plantel")
st.caption("Visión general de carga y disponibilidad (Últimos 7 días)")

players_df = st.session_state.players_df
sessions_df = st.session_state.sessions_df

# Cálculos rápidos
hace_7_dias = pd.to_datetime(datetime.today() - timedelta(days=7))
sesiones_recientes = sessions_df[pd.to_datetime(sessions_df['fecha']) >= hace_7_dias]
carga_por_jugador = sesiones_recientes.groupby('player_id')['carga'].sum().reset_index()

# Tarjetas KPI Superiores
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""<div class='metric-card'>
        <span style='color:gray'>Activos</span><br>
        <h2 style='margin:0'>{len(players_df[players_df['disponibilidad'] == 'Disponible'])}</h2>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div class='metric-card' style='border-left: 4px solid #E9C46A;'>
        <span style='color:gray'>En Alerta (Fatiga)</span><br>
        <h2 style='margin:0'>{len(carga_por_jugador[carga_por_jugador['carga'] > 2500])}</h2>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""<div class='metric-card' style='border-left: 4px solid #F4A261;'>
        <span style='color:gray'>Carga Alta (>3000 AU)</span><br>
        <h2 style='margin:0'>{len(carga_por_jugador[carga_por_jugador['carga'] > 3000])}</h2>
    </div>""", unsafe_allow_html=True)
with col4:
    st.markdown(f"""<div class='metric-card' style='border-left: 4px solid #2A9D8F;'>
        <span style='color:gray'>Carga Media (Equipo)</span><br>
        <h2 style='margin:0'>{int(carga_por_jugador['carga'].mean())} AU</h2>
    </div>""", unsafe_allow_html=True)

st.divider()

# Gráfico de Carga del Equipo (Semafórico)
st.subheader("Distribución de Carga Semanal")
carga_por_jugador = carga_por_jugador.merge(players_df[['player_id', 'nombre']], on='player_id')

# Definir colores según zonas
def get_color(carga):
    if carga < 1500: return '#2A9D8F' # Verde
    elif carga < 2500: return '#E9C46A' # Amarillo
    elif carga < 3500: return '#F4A261' # Naranja
    else: return '#E63946' # Rojo

carga_por_jugador['color'] = carga_por_jugador['carga'].apply(get_color)

fig = px.bar(carga_por_jugador, x='nombre', y='carga', 
             color='color', color_discrete_map="identity",
             template="plotly_dark")
fig.update_layout(showlegend=False, xaxis_title="", yaxis_title="Training Load (AU)", 
                  margin=dict(l=0, r=0, t=30, b=0),
                  paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

# Línea de carga óptima teórica
fig.add_hline(y=2500, line_dash="dash", line_color="gray", annotation_text="Límite óptimo")
st.plotly_chart(fig, use_container_width=True)
