# Archivo: ejercicio_4_3.py

"""
EJERCICIO: Dashboard interactivo para análisis financiero
1. Gráficos interactivos de precios y predicciones
2. Visualización de sentimientos en tiempo real
3. Dashboard completo con métricas
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit as st
from typing import Dict, List

class FinancialDashboard:
    def __init__(self):
        self.colors = {
            'primary': '#1f77b4',
            'secondary': '#ff7f0e', 
            'success': '#2ca02c',
            'danger': '#d62728',
            'warning': '#ff9800',
            'info': '#17a2b8'
        }
    
    def create_price_prediction_chart(self, df: pd.DataFrame, 
                                    predictions: np.ndarray,
                                    title: str = "Predicción de Precios") -> go.Figure:
        """
        TODO: Crear gráfico interactivo de predicciones
        1. Precios históricos
        2. Predicciones del modelo
        3. Intervalos de confianza
        4. Zoom y pan interactivo
        """
        pass
    
    def create_sentiment_timeline(self, sentiment_df: pd.DataFrame) -> go.Figure:
        """
        TODO: Timeline de sentimientos
        1. Sentimiento positivo/negativo/neutral por día
        2. Volumen de publicaciones
        3. Eventos importantes marcados
        """
        pass
    
    def create_correlation_heatmap(self, df: pd.DataFrame) -> go.Figure:
        """
        TODO: Heatmap de correlaciones
        Entre variables de precio, técnicas y sentimiento
        """
        pass
    
    def create_performance_metrics_chart(self, metrics: Dict) -> go.Figure:
        """
        TODO: Gráfico de métricas de performance
        Comparación entre diferentes modelos
        """
        pass
    
    def create_feature_importance_chart(self, importance_data: Dict) -> go.Figure:
        """
        TODO: Gráfico de importancia de características
        """
        pass
    
    def create_residuals_analysis(self, actual: np.ndarray, 
                                predicted: np.ndarray) -> go.Figure:
        """
        TODO: Análisis de residuos interactivo
        1. Scatter plot de residuos
        2. Histograma de distribución
        3. Q-Q plot
        """
        pass
    
    def create_market_regime_chart(self, df: pd.DataFrame, 
                                 regimes: pd.Series) -> go.Figure:
        """
        TODO: Visualizar regímenes de mercado
        Con colores diferentes para cada régimen
        """
        pass

class StreamlitDashboard:
    def __init__(self):
        self.dashboard = FinancialDashboard()
    
    def setup_sidebar(self):
        """
        TODO: Configurar sidebar con controles
        1. Selector de símbolo
        2. Rango de fechas
        3. Parámetros del modelo
        4. Opciones de visualización
        """
        pass
    
    def main_dashboard(self):
        """
        TODO: Dashboard principal
        1. Métricas clave en la parte superior
        2. Gráfico principal de precios y predicciones
        3. Gráficos secundarios de sentimiento
        4. Tablas de resultados
        """
        pass
    
    def model_comparison_page(self):
        """
        TODO: Página de comparación de modelos
        """
        pass
    
    def sentiment_analysis_page(self):
        """
        TODO: Página dedicada al análisis de sentimientos
        """
        pass

def create_sample_data():
    """Crear datos de ejemplo para el dashboard"""
    
    # Datos de precios
    dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
    np.random.seed(42)
    
    prices = 100 + np.cumsum(np.random.normal(0.1, 2, len(dates)))
    volume = np.random.lognormal(15, 0.5, len(dates))
    
    price_df = pd.DataFrame({
        'date': dates,
        'price': prices,
        'volume': volume,
        'returns': np.concatenate([[0], np.diff(prices) / prices[:-1]])
    })
    
    # Predicciones simuladas
    predictions = prices + np.random.normal(0, 1, len(prices))
    
    # Datos de sentimiento
    sentiment_df = pd.DataFrame({
        'date': dates,
        'positive': np.random.beta(2, 5, len(dates)),
        'negative': np.random.beta(5, 2, len(dates)),
        'neutral': np.random.beta(3, 3, len(dates)),
        'volume_tweets': np.random.poisson(1000, len(dates)),
        'sentiment_score': np.random.normal(0, 0.3, len(dates))
    })
    
    # Normalizar sentimientos
    total_sentiment = sentiment_df[['positive', 'negative', 'neutral']].sum(axis=1)
    sentiment_df[['positive', 'negative', 'neutral']] = (
        sentiment_df[['positive', 'negative', 'neutral']].div(total_sentiment, axis=0)
    )
    
    return price_df, predictions, sentiment_df

# TODO: Implementar funciones de visualización
def create_interactive_price_chart():
    """Ejemplo de gráfico interactivo de precios"""
    
    price_df, predictions, sentiment_df = create_sample_data()
    
    # Crear subplots
    fig = make_subplots(
        rows=3, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.05,
        subplot_titles=('Precio y Predicciones', 'Volumen', 'Sentimiento'),
        row_heights=[0.6, 0.2, 0.2]
    )
    
    # TODO: Agregar trazas de precio
    fig.add_trace(
        go.Scatter(
            x=price_df['date'],
            y=price_df['price'],
            name='Precio Real',
            line=dict(color='blue', width=2)
        ),
        row=1, col=1
    )
    
    # TODO: Agregar predicciones
    fig.add_trace(
        go.Scatter(
            x=price_df['date'],
            y=predictions,
            name='Predicciones',
            line=dict(color='red', width=2, dash='dash')
        ),
        row=1, col=1
    )
    
    # TODO: Agregar volumen
    fig.add_trace(
        go.Bar(
            x=price_df['date'],
            y=price_df['volume'],
            name='Volumen',
            marker_color='lightblue'
        ),
        row=2, col=1
    )
    
    # TODO: Agregar sentimiento
    fig.add_trace(
        go.Scatter(
            x=sentiment_df['date'],
            y=sentiment_df['sentiment_score'],
            name='Sentimiento',
            line=dict(color='green', width=2),
            fill='tonexty'
        ),
        row=3, col=1
    )
    
    # Configurar layout
    fig.update_layout(
        title='Dashboard Financiero Interactivo',
        height=800,
        showlegend=True,
        hovermode='x unified'
    )
    
    # Configurar ejes
    fig.update_xaxes(title_text="Fecha", row=3, col=1)
    fig.update_yaxes(title_text="Precio ($)", row=1, col=1)
    fig.update_yaxes(title_text="Volumen", row=2, col=1)
    fig.update_yaxes(title_text="Sentimiento", row=3, col=1)
    
    return fig

def create_sentiment_heatmap():
    """TODO: Crear heatmap de sentimientos por día de la semana y hora"""
    pass

def create_model_comparison_chart():
    """TODO: Comparar performance de diferentes modelos"""
    pass

# Streamlit App
def main_streamlit_app():
    """
    TODO: Aplicación principal de Streamlit
    """
    st.set_page_config(
        page_title="Financial ML Dashboard",
        page_icon="📈",
        layout="wide"
    )
    
    st.title("🚀 Dashboard de Machine Learning Financiero")
    
    # Sidebar
    st.sidebar.header("Configuración")
    
    symbol = st.sidebar.selectbox(
        "Símbolo de Acción",
        ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"]
    )
    
    date_range = st.sidebar.date_input(
        "Rango de Fechas",
        value=[datetime(2023, 1, 1), datetime(2023, 12, 31)]
    )
    
    model_type = st.sidebar.selectbox(
        "Tipo de Modelo",
        ["LSTM Simple", "LSTM + Sentimiento", "Ensemble"]
    )
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("MSE", "0.0023", "-12.3%")
    
    with col2:
        st.metric("Precisión Direccional", "67.8%", "+5.2%")
    
    with col3:
        st.metric("R² Score", "0.342", "+0.089")
    
    with col4:
        st.metric("Sharpe Ratio", "1.23", "+0.15")
    
    # Gráfico principal
    st.subheader("📊 Análisis de Precios y Predicciones")
    
    # Crear y mostrar gráfico
    fig = create_interactive_price_chart()
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabs para diferentes análisis
    tab1, tab2, tab3 = st.tabs(["🎯 Predicciones", "💭 Sentimientos", "📈 Comparación"])
    
    with tab1:
        st.subheader("Análisis de Predicciones")
        # TODO: Contenido de predicciones
        
    with tab2:
        st.subheader("Análisis de Sentimientos")
        # TODO: Contenido de sentimientos
        
    with tab3:
        st.subheader("Comparación de Modelos")
        # TODO: Contenido de comparación

# Para ejecutar: streamlit run ejercicio_4_3.py
if __name__ == "__main__":
    # Crear gráfico de ejemplo
    fig = create_interactive_price_chart()
    fig.show()
    
    # Para Streamlit, descomentar:
    # main_streamlit_app()
