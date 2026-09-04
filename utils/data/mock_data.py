import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_data():
    # 1. Tabla de Jugadores
    players = pd.DataFrame({
        'player_id': range(1, 21),
        'nombre': ['Tomás Fernández', 'Ignacio Herrera', 'Santiago Ruiz', 'Mateo Torres', 'Juan Lautaro Licari', 'Juan Cruz Díaz', 'Lautaro Silva', 'Agustín Peralta', 'Facundo Gómez', 'Martín Soler', 'Lucas Blanco', 'Diego Navarro', 'Enzo Pérez', 'Julián Castro', 'Bruno Costa', 'Thiago López', 'Mateo Rossi', 'Joaquín Vega', 'Simón Arce', 'Felipe Ortiz'],
        'posicion': ['Central', 'Lateral', 'Extremo', 'Pivote', 'Central', 'Arquero', 'Lateral', 'Extremo', 'Central', 'Pivote', 'Arquero', 'Lateral', 'Extremo', 'Central', 'Lateral', 'Pivote', 'Extremo', 'Arquero', 'Central', 'Lateral'],
        'disponibilidad': ['Disponible', 'Disponible', 'Disponible', 'Limitado', 'Disponible', 'Disponible', 'Disponible', 'Lesionado'] + ['Disponible']*12
    })
    
    # 2. Tabla de Sesiones (Últimos 28 días)
    fechas = [datetime.today() - timedelta(days=x) for x in range(28)]
    sessions = []
    
    for _, player in players.iterrows():
        base_rpe = np.random.randint(4, 7)
        for fecha in fechas:
            # Simular 5 días de entrenamiento por semana
            if fecha.weekday() < 5: 
                duracion = np.random.choice([60, 90, 120])
                srpe = max(1, min(10, base_rpe + np.random.randint(-2, 3)))
                carga = duracion * srpe
                sessions.append({
                    'player_id': player['player_id'],
                    'fecha': fecha,
                    'tipo': 'Entrenamiento' if fecha.weekday() != 4 else 'Partido',
                    'duracion': duracion,
                    'srpe': srpe,
                    'carga': carga,
                    'bienestar': np.random.randint(3, 6)
                })
                
    sessions_df = pd.DataFrame(sessions)
    return players, sessions_df
