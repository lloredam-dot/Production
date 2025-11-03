# Archivo: ejercicio_3_1.py

"""
EJERCICIO: Sistema completo de análisis de sentimientos
Basado en la tesis de análisis de sentimientos con FinBERT
1. Implementar analizador con múltiples modelos
2. Procesar tweets y noticias financieras
3. Crear índice de sentimiento agregado
"""

from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import numpy as np
from typing import List, Dict, Tuple
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

class AdvancedFinancialSentimentAnalyzer:
    def __init__(self):
        # TODO: Cargar múltiples modelos
        self.finbert = None  # FinBERT para textos financieros
        self.twitter_model = None  # Modelo especializado en Twitter
        self.general_model = None  # Modelo general como fallback
        
        self.load_models()
    
    def load_models(self):
        """
        TODO: Cargar modelos de sentiment analysis
        1. FinBERT para textos financieros formales
        2. Modelo específico para Twitter
        3. Modelo general como fallback
        """
        pass
    
    def preprocess_financial_text(self, text: str) -> str:
        """
        TODO: Preprocesamiento específico para textos financieros
        Basado en el preprocesamiento de la tesis
        1. Normalizar tickers ($AAPL -> TICKER_AAPL)
        2. Normalizar porcentajes y números
        3. Limpiar pero preservar contexto financiero
        """
        pass
    
    def preprocess_tweet(self, tweet: str) -> str:
        """
        TODO: Preprocesamiento específico para tweets
        1. Manejar hashtags y menciones
        2. Convertir emojis a texto
        3. Normalizar URLs
        """
        pass
    
    def analyze_text(self, text: str, text_type: str = "financial") -> Dict:
        """
        TODO: Análisis de sentimiento con modelo apropiado
        1. Seleccionar modelo según tipo de texto
        2. Preprocesar texto
        3. Obtener predicción con probabilidades
        4. Calcular score de confianza
        """
        pass
    
    def batch_analyze(self, texts: List[str], text_types: List[str] = None) -> List[Dict]:
        """
        TODO: Análisis en lote para eficiencia
        """
        pass
    
    def create_sentiment_index(self, results: List[Dict], 
                             weights: List[float] = None) -> Dict:
        """
        TODO: Crear índice de sentimiento agregado
        Basado en la fórmula de la tesis: SMI = (M_pos - M_neg) / (M_pos + M_neu + M_neg)
        """
        pass

class MarketSentimentTracker:
    def __init__(self, analyzer: AdvancedFinancialSentimentAnalyzer):
        self.analyzer = analyzer
        self.sentiment_history = []
    
    def process_daily_data(self, date: datetime, 
                          tweets: List[str], 
                          news: List[str],
                          opinions: List[str]) -> Dict:
        """
        TODO: Procesar datos diarios como en la tesis
        1. Analizar cada tipo de contenido por separado
        2. Agregar por día
        3. Calcular métricas de sentimiento
        4. Considerar volumen de publicaciones
        """
        pass
    
    def calculate_market_indicators(self, symbol: str, 
                                  days: int = 30) -> Dict:
        """
        TODO: Calcular indicadores de mercado
        1. Sentimiento promedio por período
        2. Volatilidad del sentimiento
        3. Correlación con precio (si disponible)
        """
        pass
    
    def plot_sentiment_trends(self, symbol: str, days: int = 30):
        """
        TODO: Visualizar tendencias de sentimiento
        """
        pass

# Datos de ejemplo (simular datos reales)
sample_tweets = [
    "🚀 $AAPL to the moon! Great earnings report! #bullish",
    "Apple stock looking weak today, might be time to sell $AAPL",
    "Just bought more $AAPL shares, love this company! 💪",
    "Market crash incoming? $AAPL down 5% today 📉",
    "Apple's new iPhone is amazing! $AAPL 🔥"
]

sample_news = [
    "Apple Inc. reported strong quarterly earnings, beating analyst expectations by 12%",
    "Apple faces supply chain challenges in China, stock price volatile",
    "New iPhone sales exceed projections, Apple stock rises 3%",
    "Apple announces major investment in renewable energy projects",
    "Analysts downgrade Apple stock citing market saturation concerns"
]

sample_opinions = [
    "Apple remains a solid long-term investment despite short-term volatility",
    "The company's innovation pipeline looks weak compared to competitors",
    "Apple's services revenue growth is impressive and sustainable",
    "Valuation concerns as P/E ratio reaches historical highs",
    "Strong brand loyalty will drive continued growth in emerging markets"
]

# TODO: Implementar sistema de testing
def test_sentiment_analysis():
    """Probar el sistema completo de análisis de sentimientos"""
    
    # Inicializar analizador
    analyzer = AdvancedFinancialSentimentAnalyzer()
    tracker = MarketSentimentTracker(analyzer)
    
    # Procesar datos de ejemplo
    today = datetime.now()
    daily_sentiment = tracker.process_daily_data(
        today, sample_tweets, sample_news, sample_opinions
    )
    
    print("Sentimiento diario para AAPL:")
    print(f"Índice de sentimiento: {daily_sentiment['sentiment_index']:.3f}")
    print(f"Distribución: {daily_sentiment['distribution']}")
    
    # Analizar textos individuales
    for tweet in sample_tweets[:3]:
        result = analyzer.analyze_text(tweet, "twitter")
        print(f"Tweet: {tweet[:50]}...")
        print(f"Sentimiento: {result['sentiment']} (confianza: {result['confidence']:.3f})")
        print("-" * 50)

# test_sentiment_analysis()
