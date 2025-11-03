# EJERCICIOS PRÁCTICOS - PYTHON AVANZADO 2024

## ESTRUCTURA DE EJERCICIOS POR MÓDULO

### MÓDULO 1: FUNDAMENTOS MODERNOS
**Duración: 1 hora**

#### Ejercicio 1.1: Configuración del Entorno con IA (15 min)
```python
# Objetivo: Configurar PyCharm con asistente de IA
# Archivo: ejercicio_1_1.py

"""
EJERCICIO: Configurar Asistente de IA
1. Instalar las librerías necesarias
2. Configurar API keys para Gemini/DeepSeek
3. Crear una función que use IA para revisar código
"""

import os
from typing import Optional
import google.generativeai as genai

# TODO: Completar la clase AICodeReviewer
class AICodeReviewer:
    def __init__(self, api_key: str):
        # TODO: Configurar el cliente de Gemini
        pass
    
    def review_code(self, code: str) -> str:
        # TODO: Implementar revisión de código con IA
        # Debe analizar el código y sugerir mejoras
        pass
    
    def generate_docstring(self, function_code: str) -> str:
        # TODO: Generar documentación automática
        pass

# Código a revisar (con errores intencionales)
sample_code = """
def calcular_precio(precio, descuento):
    resultado = precio - (precio * descuento / 100)
    return resultado

def procesar_datos(datos):
    for i in range(len(datos)):
        datos[i] = datos[i] * 2
    return datos
"""

# TODO: Usar el revisor para analizar el código
# reviewer = AICodeReviewer("tu_api_key")
# review = reviewer.review_code(sample_code)
# print(review)
```

#### Ejercicio 1.2: Python 3.12+ Features (20 min)
```python
# Archivo: ejercicio_1_2.py

"""
EJERCICIO: Usar características modernas de Python 3.12+
1. Implementar TypedDict con campos opcionales
2. Usar pattern matching avanzado
3. Crear funciones async con TaskGroup
"""

from typing import TypedDict, NotRequired, Union
import asyncio
import aiohttp

# TODO: Definir estructura de datos para análisis financiero
class StockData(TypedDict):
    symbol: str
    price: float
    volume: int
    # TODO: Agregar campos opcionales con NotRequired
    # market_cap, pe_ratio, dividend_yield

# TODO: Implementar función con pattern matching
def analyze_stock_data(data: dict) -> str:
    """
    Analizar datos de acciones usando pattern matching
    Casos a manejar:
    - Acciones con alta volatilidad (price > 100, volume > 1000000)
    - Acciones de dividendos (dividend_yield > 3%)
    - Acciones de crecimiento (pe_ratio > 20)
    - Datos inválidos
    """
    match data:
        # TODO: Implementar casos con pattern matching
        case {"price": float(p), "volume": int(v)} if p > 100 and v > 1000000:
            pass
        case _:
            pass

# TODO: Implementar función async para obtener datos de múltiples APIs
async def fetch_multiple_stocks(symbols: list[str]) -> dict:
    """
    Obtener datos de múltiples acciones usando TaskGroup
    """
    async def fetch_stock(symbol: str) -> dict:
        # Simular llamada a API
        await asyncio.sleep(0.1)
        return {"symbol": symbol, "price": 100.0, "volume": 50000}
    
    # TODO: Usar asyncio.TaskGroup para ejecutar en paralelo
    pass

# Datos de prueba
test_stocks = [
    {"symbol": "AAPL", "price": 150.0, "volume": 2000000, "pe_ratio": 25},
    {"symbol": "GOOGL", "price": 2500.0, "volume": 800000, "dividend_yield": 0},
    {"symbol": "MSFT", "price": 300.0, "volume": 1500000, "dividend_yield": 2.5},
]

# TODO: Probar las funciones implementadas
```

#### Ejercicio 1.3: Integración con IA para Debugging (25 min)
```python
# Archivo: ejercicio_1_3.py

"""
EJERCICIO: Crear sistema de debugging asistido por IA
1. Detectar errores comunes en código
2. Sugerir correcciones automáticas
3. Generar tests unitarios
"""

import ast
import traceback
from typing import List, Dict, Any

class AIDebugger:
    def __init__(self, ai_client):
        self.ai_client = ai_client
        self.common_errors = {
            'NameError': 'Variable no definida',
            'TypeError': 'Tipo de dato incorrecto',
            'IndexError': 'Índice fuera de rango',
            'KeyError': 'Clave no encontrada en diccionario'
        }
    
    def analyze_error(self, code: str, error: Exception) -> Dict[str, Any]:
        """
        TODO: Implementar análisis de errores
        1. Identificar tipo de error
        2. Localizar línea problemática
        3. Sugerir corrección con IA
        """
        pass
    
    def suggest_fix(self, code: str, error_info: Dict) -> str:
        """
        TODO: Usar IA para sugerir corrección
        """
        pass
    
    def generate_tests(self, function_code: str) -> str:
        """
        TODO: Generar tests unitarios automáticamente
        """
        pass

# Código con errores para probar
buggy_code = """
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)  # Error: división por cero si lista vacía

def find_max_price(stocks):
    max_price = 0
    max_stock = None
    for stock in stocks:
        if stock['price'] > max_price:  # Error: KeyError si no existe 'price'
            max_price = stock['price']
            max_stock = stock
    return max_stock

def process_data(data):
    result = []
    for i in range(len(data) + 1):  # Error: IndexError
        result.append(data[i] * 2)
    return result
"""

# TODO: Implementar sistema de testing automático
def test_debugger():
    """Probar el sistema de debugging"""
    pass
```

---

### MÓDULO 2: APIs Y WEB SCRAPING AVANZADO
**Duración: 1 hora**

#### Ejercicio 2.1: Cliente API Moderno (20 min)
```python
# Archivo: ejercicio_2_1.py

"""
EJERCICIO: Implementar cliente para API financiera
Basado en findARestaurant.py pero para datos financieros
1. Crear cliente para Alpha Vantage API
2. Implementar manejo de rate limiting
3. Agregar cache y retry logic
"""

import asyncio
import aiohttp
import time
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class StockPrice:
    symbol: str
    price: float
    timestamp: datetime
    volume: int
    change_percent: float

class FinancialAPIClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"
        self.rate_limit = 5  # requests per minute
        self.last_request_time = 0
        self.cache = {}
        self.cache_ttl = 300  # 5 minutos
    
    async def get_stock_price(self, symbol: str) -> Optional[StockPrice]:
        """
        TODO: Implementar obtención de precio de acción
        1. Verificar rate limiting
        2. Consultar cache primero
        3. Hacer request a API si necesario
        4. Parsear respuesta y crear StockPrice
        """
        pass
    
    async def get_multiple_stocks(self, symbols: List[str]) -> List[StockPrice]:
        """
        TODO: Obtener precios de múltiples acciones
        Usar asyncio para requests paralelos respetando rate limits
        """
        pass
    
    def _check_rate_limit(self):
        """TODO: Implementar verificación de rate limiting"""
        pass
    
    def _get_from_cache(self, key: str) -> Optional[Dict]:
        """TODO: Implementar sistema de cache"""
        pass
    
    def _save_to_cache(self, key: str, data: Dict):
        """TODO: Guardar en cache con TTL"""
        pass

# TODO: Implementar función para encontrar mejores acciones
async def find_best_stocks(client: FinancialAPIClient, 
                          symbols: List[str], 
                          criteria: str = "highest_gain") -> List[StockPrice]:
    """
    Encontrar las mejores acciones según criterio
    Similar a findARestaurant pero para acciones
    """
    pass

# Símbolos de prueba
test_symbols = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"]

# TODO: Probar el cliente
async def main():
    client = FinancialAPIClient("demo_api_key")
    
    # Probar obtención individual
    apple_stock = await client.get_stock_price("AAPL")
    print(f"Apple: ${apple_stock.price}")
    
    # Probar obtención múltiple
    stocks = await client.get_multiple_stocks(test_symbols)
    for stock in stocks:
        print(f"{stock.symbol}: ${stock.price} ({stock.change_percent:+.2f}%)")
    
    # Encontrar mejores acciones
    best_stocks = await find_best_stocks(client, test_symbols, "highest_gain")
    print("Mejores acciones:", [s.symbol for s in best_stocks])

# asyncio.run(main())
```

#### Ejercicio 2.2: Web Scraping de Noticias Financieras (25 min)
```python
# Archivo: ejercicio_2_2.py

"""
EJERCICIO: Scraping de noticias financieras
1. Scraping de Yahoo Finance o similar
2. Extraer títulos, fechas y contenido
3. Detectar sentimiento básico
4. Manejar JavaScript con Selenium
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from typing import List, Dict
from datetime import datetime
import re

@dataclass
class NewsArticle:
    title: str
    content: str
    date: datetime
    source: str
    url: str
    sentiment_score: Optional[float] = None

class FinancialNewsScraper:
    def __init__(self, headless: bool = True):
        # TODO: Configurar Selenium WebDriver
        self.setup_driver(headless)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def setup_driver(self, headless: bool):
        """TODO: Configurar Chrome WebDriver con opciones"""
        pass
    
    def scrape_yahoo_finance(self, symbol: str, max_articles: int = 10) -> List[NewsArticle]:
        """
        TODO: Scraping de noticias de Yahoo Finance
        1. Navegar a página de noticias del símbolo
        2. Extraer artículos
        3. Obtener detalles de cada artículo
        """
        pass
    
    def scrape_marketwatch(self, symbol: str, max_articles: int = 10) -> List[NewsArticle]:
        """
        TODO: Scraping de MarketWatch
        Usar requests + BeautifulSoup para contenido estático
        """
        pass
    
    def extract_article_content(self, url: str) -> str:
        """
        TODO: Extraer contenido completo del artículo
        Manejar diferentes estructuras de sitios web
        """
        pass
    
    def analyze_sentiment(self, text: str) -> float:
        """
        TODO: Análisis básico de sentimiento
        Usar palabras clave financieras positivas/negativas
        Retornar score entre -1 (muy negativo) y 1 (muy positivo)
        """
        positive_words = ['gain', 'profit', 'growth', 'increase', 'bull', 'rise']
        negative_words = ['loss', 'decline', 'bear', 'fall', 'crash', 'drop']
        
        # TODO: Implementar lógica de análisis
        pass
    
    def save_to_csv(self, articles: List[NewsArticle], filename: str):
        """TODO: Guardar artículos en CSV"""
        pass
    
    def close(self):
        """Cerrar recursos"""
        if hasattr(self, 'driver'):
            self.driver.quit()

# TODO: Implementar función para análisis de múltiples símbolos
def analyze_market_sentiment(symbols: List[str]) -> Dict[str, float]:
    """
    Analizar sentimiento del mercado para múltiples símbolos
    Retornar diccionario con símbolo -> sentiment_score
    """
    pass

# Símbolos para analizar
symbols_to_analyze = ["AAPL", "TSLA", "NVDA", "AMD", "MSFT"]

# TODO: Ejecutar scraping y análisis
def main():
    scraper = FinancialNewsScraper()
    
    try:
        # Scraping de noticias para Apple
        apple_news = scraper.scrape_yahoo_finance("AAPL", max_articles=5)
        
        # Mostrar resultados
        for article in apple_news:
            print(f"Título: {article.title}")
            print(f"Fecha: {article.date}")
            print(f"Sentimiento: {article.sentiment_score}")
            print("-" * 50)
        
        # Análisis de sentimiento del mercado
        market_sentiment = analyze_market_sentiment(symbols_to_analyze)
        print("Sentimiento del mercado:")
        for symbol, sentiment in market_sentiment.items():
            print(f"{symbol}: {sentiment:+.2f}")
    
    finally:
        scraper.close()

# main()
```

#### Ejercicio 2.3: Autenticación OAuth 2.0 (15 min)
```python
# Archivo: ejercicio_2_3.py

"""
EJERCICIO: Implementar autenticación OAuth 2.0
1. Flujo completo de OAuth con Twitter API
2. Manejo de tokens y refresh
3. Hacer requests autenticados
"""

import requests
import base64
import hashlib
import secrets
from urllib.parse import urlencode, parse_qs
from typing import Dict, Optional

class TwitterOAuthClient:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.access_token = None
        self.refresh_token = None
        
        # URLs de Twitter API v2
        self.auth_url = "https://twitter.com/i/oauth2/authorize"
        self.token_url = "https://api.twitter.com/2/oauth2/token"
        self.api_base = "https://api.twitter.com/2"
    
    def generate_auth_url(self, scopes: List[str]) -> tuple[str, str]:
        """
        TODO: Generar URL de autorización con PKCE
        1. Generar code_verifier y code_challenge
        2. Crear state para seguridad
        3. Construir URL con parámetros
        """
        pass
    
    def exchange_code_for_token(self, code: str, code_verifier: str) -> Dict:
        """
        TODO: Intercambiar código de autorización por tokens
        1. Preparar datos para POST request
        2. Incluir code_verifier para PKCE
        3. Manejar respuesta y guardar tokens
        """
        pass
    
    def refresh_access_token(self) -> Dict:
        """
        TODO: Renovar access token usando refresh token
        """
        pass
    
    def search_tweets(self, query: str, max_results: int = 10) -> Dict:
        """
        TODO: Buscar tweets usando API autenticada
        1. Verificar que tenemos access token válido
        2. Hacer request con Authorization header
        3. Manejar errores de autenticación
        """
        pass
    
    def get_user_tweets(self, username: str, max_results: int = 10) -> Dict:
        """
        TODO: Obtener tweets de un usuario específico
        """
        pass
    
    def _make_authenticated_request(self, endpoint: str, params: Dict = None) -> Dict:
        """
        TODO: Hacer request autenticado
        Incluir manejo de token expirado y refresh automático
        """
        pass

# TODO: Implementar función para análisis de tweets financieros
def analyze_financial_tweets(client: TwitterOAuthClient, 
                           symbols: List[str]) -> Dict[str, List[Dict]]:
    """
    Buscar y analizar tweets sobre símbolos financieros
    """
    pass

# Configuración (usar variables de entorno en producción)
TWITTER_CLIENT_ID = "your_client_id"
TWITTER_CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://localhost:8000/callback"

# TODO: Probar flujo OAuth
def test_oauth_flow():
    client = TwitterOAuthClient(
        TWITTER_CLIENT_ID, 
        TWITTER_CLIENT_SECRET, 
        REDIRECT_URI
    )
    
    # Generar URL de autorización
    auth_url, state = client.generate_auth_url([
        "tweet.read", "users.read", "offline.access"
    ])
    
    print(f"Visita esta URL para autorizar: {auth_url}")
    
    # En una aplicación real, el usuario sería redirigido aquí
    # y obtendríamos el código de la URL de callback
    
    # Simular intercambio de código (en producción vendría del callback)
    # authorization_code = input("Ingresa el código de autorización: ")
    # tokens = client.exchange_code_for_token(authorization_code, code_verifier)
    
    # Buscar tweets
    # tweets = client.search_tweets("$AAPL OR Apple stock", max_results=5)
    # print("Tweets encontrados:", len(tweets.get('data', [])))

# test_oauth_flow()
```

---

### MÓDULO 3: PROCESAMIENTO DE TEXTO Y NLP
**Duración: 1.5 horas**

#### Ejercicio 3.1: Análisis de Sentimientos Financieros (30 min)
```python
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
        self.general_model = None  # Modelo general
        
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
```

#### Ejercicio 3.2: Procesamiento de Texto con spaCy (30 min)
```python
# Archivo: ejercicio_3_2.py

"""
EJERCICIO: Procesamiento avanzado de texto financiero
1. Extraer entidades financieras (empresas, tickers, cantidades)
2. Análisis de dependencias sintácticas
3. Extracción de relaciones entre entidades
"""

import spacy
from spacy import displacy
from spacy.matcher import Matcher, PhraseMatcher
from spacy.tokens import Span
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Set

class FinancialTextProcessor:
    def __init__(self):
        # TODO: Cargar modelo de spaCy y configurar
        self.nlp = None
        self.setup_nlp()
        
        # Matchers para patrones financieros
        self.ticker_matcher = None
        self.financial_matcher = None
        self.setup_matchers()
        
        # Diccionarios de términos financieros
        self.financial_terms = self.load_financial_terms()
        self.company_names = self.load_company_names()
    
    def setup_nlp(self):
        """
        TODO: Configurar pipeline de spaCy
        1. Cargar modelo en español/inglés
        2. Agregar componentes personalizados
        3. Configurar para textos financieros
        """
        pass
    
    def setup_matchers(self):
        """
        TODO: Configurar matchers para patrones financieros
        1. Matcher para tickers ($AAPL, NASDAQ:AAPL)
        2. Matcher para cantidades monetarias
        3. Matcher para porcentajes y ratios
        """
        pass
    
    def load_financial_terms(self) -> Set[str]:
        """TODO: Cargar diccionario de términos financieros"""
        return {
            'earnings', 'revenue', 'profit', 'loss', 'dividend', 'yield',
            'market cap', 'pe ratio', 'eps', 'ebitda', 'roe', 'roa',
            'bull market', 'bear market', 'volatility', 'liquidity'
        }
    
    def load_company_names(self) -> Set[str]:
        """TODO: Cargar nombres de empresas conocidas"""
        return {
            'Apple', 'Microsoft', 'Google', 'Amazon', 'Tesla',
            'Meta', 'Netflix', 'Nvidia', 'Intel', 'AMD'
        }
    
    def extract_financial_entities(self, text: str) -> Dict[str, List[Dict]]:
        """
        TODO: Extraer entidades financieras específicas
        1. Tickers de acciones
        2. Cantidades monetarias
        3. Porcentajes
        4. Fechas financieras
        5. Nombres de empresas
        """
        pass
    
    def analyze_sentiment_by_entity(self, text: str) -> Dict[str, Dict]:
        """
        TODO: Análisis de sentimiento por entidad
        1. Identificar entidades en el texto
        2. Extraer contexto alrededor de cada entidad
        3. Analizar sentimiento del contexto
        """
        pass
    
    def extract_financial_relationships(self, text: str) -> List[Dict]:
        """
        TODO: Extraer relaciones entre entidades financieras
        Ejemplos:
        - "Apple supera las expectativas de ganancias"
        - "Tesla pierde cuota de mercado frente a BYD"
        - "El precio de Bitcoin correlaciona con el oro"
        """
        pass
    
    def create_knowledge_graph(self, texts: List[str]) -> nx.Graph:
        """
        TODO: Crear grafo de conocimiento financiero
        1. Extraer entidades y relaciones de todos los textos
        2. Crear nodos para entidades
        3. Crear aristas para relaciones
        4. Calcular métricas de centralidad
        """
        pass
    
    def summarize_financial_document(self, text: str, max_sentences: int = 3) -> str:
        """
        TODO: Resumir documento financiero
        1. Identificar oraciones más importantes
        2. Priorizar información financiera clave
        3. Mantener coherencia narrativa
        """
        pass

class FinancialNewsAnalyzer:
    def __init__(self, processor: FinancialTextProcessor):
        self.processor = processor
        self.news_database = []
    
    def process_news_article(self, article: Dict) -> Dict:
        """
        TODO: Procesar artículo de noticias completo
        1. Extraer entidades y relaciones
        2. Analizar sentimiento por entidad
        3. Clasificar tipo de noticia (earnings, merger, etc.)
        4. Calcular score de importancia
        """
        pass
    
    def find_market_events(self, articles: List[Dict], 
                          date_range: Tuple[datetime, datetime]) -> List[Dict]:
        """
        TODO: Identificar eventos de mercado importantes
        1. Buscar patrones en las noticias
        2. Detectar eventos que afectan múltiples empresas
        3. Clasificar por impacto potencial
        """
        pass
    
    def generate_market_report(self, symbol: str, 
                             days: int = 7) -> Dict:
        """
        TODO: Generar reporte de mercado
        1. Resumir noticias relevantes
        2. Identificar tendencias de sentimiento
        3. Destacar eventos clave
        """
        pass

# Textos de ejemplo para procesar
sample_financial_texts = [
    """
    Apple Inc. (NASDAQ: AAPL) reportó ganancias trimestrales de $1.52 por acción, 
    superando las expectativas de Wall Street de $1.43. Los ingresos alcanzaron 
    $89.5 mil millones, un aumento del 8.2% interanual. El CEO Tim Cook destacó 
    el fuerte desempeño del iPhone 15 y los servicios digitales.
    """,
    
    """
    Tesla (TSLA) cayó un 5.3% en las operaciones posteriores al cierre después 
    de que Elon Musk anunciara retrasos en la producción del Cybertruck. La 
    compañía enfrenta desafíos de cadena de suministro que podrían afectar las 
    entregas del Q4. Los analistas de Morgan Stanley redujeron su precio objetivo 
    de $300 a $280.
    """,
    
    """
    El mercado de criptomonedas experimentó alta volatilidad hoy, con Bitcoin 
    cayendo por debajo de $40,000 por primera vez en tres meses. Ethereum también 
    perdió un 7%, mientras que los inversores buscan refugio en activos más seguros 
    como el oro y los bonos del Tesoro estadounidense.
    """
]

# TODO: Implementar sistema de testing
def test_financial_text_processing():
    """Probar el procesamiento de texto financiero"""
    
    processor = FinancialTextProcessor()
    analyzer = FinancialNewsAnalyzer(processor)
    
    for i, text in enumerate(sample_financial_texts):
        print(f"\n--- Procesando texto {i+1} ---")
        print(f"Texto: {text[:100]}...")
        
        # Extraer entidades
        entities = processor.extract_financial_entities(text)
        print(f"Entidades encontradas: {entities}")
        
        # Analizar sentimiento por entidad
        sentiment_by_entity = processor.analyze_sentiment_by_entity(text)
        print(f"Sentimiento por entidad: {sentiment_by_entity}")
        
        # Extraer relaciones
        relationships = processor.extract_financial_relationships(text)
        print(f"Relaciones: {relationships}")
        
        # Resumir
        summary = processor.summarize_financial_document(text)
        print(f"Resumen: {summary}")
        
        print("-" * 80)
    
    # Crear grafo de conocimiento
    knowledge_graph = processor.create_knowledge_graph(sample_financial_texts)
    print(f"\nGrafo de conocimiento creado con {knowledge_graph.number_of_nodes()} nodos")

# test_financial_text_processing()
```

#### Ejercicio 3.3: Modelos de Lenguaje Personalizados (30 min)
```python
# Archivo: ejercicio_3_3.py

"""
EJERCICIO: Fine-tuning de modelos para dominio financiero
1. Preparar dataset de textos financieros
2. Fine-tuning de BERT para clasificación
3. Evaluación y comparación de modelos
"""

import torch
from transformers import (
    AutoTokenizer, AutoModelForSequenceClassification,
    TrainingArguments, Trainer, DataCollatorWithPadding
)
from datasets import Dataset
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Tuple

class FinancialDatasetBuilder:
    def __init__(self):
        self.financial_phrases = []
        self.labels = []
        self.label_mapping = {'negative': 0, 'neutral': 1, 'positive': 2}
        self.reverse_label_mapping = {v: k for k, v in self.label_mapping.items()}
    
    def load_financial_phrasebank(self) -> pd.DataFrame:
        """
        TODO: Cargar dataset Financial PhraseBank
        (En ejercicio real, descargar de: https://www.researchgate.net/publication/251231364_FinancialPhraseBank-v10)
        Por ahora, crear dataset sintético
        """
        pass
    
    def create_synthetic_dataset(self, size: int = 1000) -> pd.DataFrame:
        """
        TODO: Crear dataset sintético para demostración
        1. Generar frases financieras con diferentes sentimientos
        2. Incluir variedad de contextos (earnings, market, company news)
        3. Balancear clases
        """
        pass
    
    def augment_dataset(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        TODO: Aumentar dataset con técnicas de data augmentation
        1. Parafraseo con modelos de lenguaje
        2. Sustitución de sinónimos financieros
        3. Variaciones de entidades (nombres de empresas, números)
        """
        pass
    
    def prepare_for_training(self, df: pd.DataFrame, 
                           test_size: float = 0.2) -> Tuple[Dataset, Dataset]:
        """
        TODO: Preparar datasets para entrenamiento
        1. Dividir en train/test
        2. Tokenizar textos
        3. Crear objetos Dataset de Hugging Face
        """
        pass

class FinancialBERTTrainer:
    def __init__(self, model_name: str = "bert-base-uncased"):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name, num_labels=3
        )
        self.training_history = []
    
    def tokenize_function(self, examples):
        """TODO: Función de tokenización para el dataset"""
        pass
    
    def compute_metrics(self, eval_pred):
        """
        TODO: Calcular métricas de evaluación
        1. Accuracy
        2. Precision, Recall, F1 por clase
        3. Matriz de confusión
        """
        pass
    
    def train_model(self, train_dataset: Dataset, 
                   eval_dataset: Dataset,
                   output_dir: str = "./financial_bert") -> Dict:
        """
        TODO: Entrenar modelo con fine-tuning
        1. Configurar argumentos de entrenamiento
        2. Crear Trainer
        3. Ejecutar entrenamiento
        4. Guardar modelo
        """
        pass
    
    def evaluate_model(self, test_dataset: Dataset) -> Dict:
        """
        TODO: Evaluación completa del modelo
        1. Predicciones en conjunto de prueba
        2. Métricas detalladas
        3. Análisis de errores
        """
        pass
    
    def predict_sentiment(self, text: str) -> Dict:
        """
        TODO: Predicción de sentimiento para texto nuevo
        """
        pass
    
    def compare_with_baseline(self, test_texts: List[str], 
                            test_labels: List[int]) -> Dict:
        """
        TODO: Comparar con modelos baseline
        1. FinBERT pre-entrenado
        2. Modelo general de sentiment
        3. Análisis estadístico de diferencias
        """
        pass

class ModelEvaluator:
    def __init__(self):
        self.models = {}
        self.results = {}
    
    def add_model(self, name: str, model, tokenizer):
        """TODO: Agregar modelo para comparación"""
        pass
    
    def benchmark_models(self, test_texts: List[str], 
                        test_labels: List[int]) -> pd.DataFrame:
        """
        TODO: Benchmark de múltiples modelos
        1. Evaluar cada modelo en mismo dataset
        2. Medir tiempo de inferencia
        3. Calcular métricas de performance
        """
        pass
    
    def plot_comparison(self, metrics_df: pd.DataFrame):
        """
        TODO: Visualizar comparación de modelos
        """
        pass
    
    def analyze_error_patterns(self, model_name: str, 
                             predictions: List[int], 
                             true_labels: List[int],
                             texts: List[str]) -> Dict:
        """
        TODO: Analizar patrones de errores
        1. Identificar tipos de textos problemáticos
        2. Analizar confusiones entre clases
        3. Sugerir mejoras
        """
        pass

# Dataset sintético para demostración
def create_demo_dataset():
    """Crear dataset de demostración"""
    
    positive_phrases = [
        "Company reports record quarterly profits exceeding expectations",
        "Stock price surges following strong earnings announcement", 
        "Revenue growth accelerates driven by robust demand",
        "Management raises full-year guidance citing strong fundamentals",
        "Dividend increase reflects confidence in future cash flows"
    ]
    
    negative_phrases = [
        "Company misses earnings estimates amid declining sales",
        "Stock plummets on disappointing quarterly results",
        "Revenue falls short of analyst projections", 
        "Management cuts guidance due to market headwinds",
        "Dividend suspended to preserve cash during downturn"
    ]
    
    neutral_phrases = [
        "Company reports quarterly results in line with expectations",
        "Stock trades sideways following earnings announcement",
        "Revenue meets analyst consensus estimates",
        "Management maintains previous guidance for fiscal year",
        "Dividend payment remains unchanged from previous quarter"
    ]
    
    # TODO: Expandir con más ejemplos y variaciones
    return positive_phrases, negative_phrases, neutral_phrases

# TODO: Implementar sistema de testing completo
def test_model_training():
    """Probar el sistema completo de entrenamiento"""
    
    # Crear dataset
    dataset_builder = FinancialDatasetBuilder()
    df = dataset_builder.create_synthetic_dataset(500)
    
    # Preparar para entrenamiento
    train_dataset, test_dataset = dataset_builder.prepare_for_training(df)
    
    # Entrenar modelo
    trainer = FinancialBERTTrainer()
    training_results = trainer.train_model(train_dataset, test_dataset)
    
    # Evaluar
    evaluation_results = trainer.evaluate_model(test_dataset)
    
    print("Resultados del entrenamiento:")
    print(f"Accuracy: {evaluation_results['accuracy']:.3f}")
    print(f"F1 Score: {evaluation_results['f1']:.3f}")
    
    # Probar predicciones
    test_texts = [
        "Apple stock soars on better than expected iPhone sales",
        "Tesla faces production challenges in new factory",
        "Microsoft reports steady growth in cloud services"
    ]
    
    for text in test_texts:
        prediction = trainer.predict_sentiment(text)
        print(f"Texto: {text}")
        print(f"Predicción: {prediction['label']} (confianza: {prediction['confidence']:.3f})")
        print("-" * 50)

# test_model_training()
```

---

### MÓDULO 4: MACHINE LEARNING FINANCIERO
**Duración: 1 hora**

#### Ejercicio 4.1: Red Neuronal para Predicción de Precios (25 min)
```python
# Archivo: ejercicio_4_1.py

"""
EJERCICIO: Implementar red neuronal para predicción de precios
Basado en las técnicas de la tesis con LSTM
1. Preparar datos históricos de acciones
2. Crear y entrenar modelo LSTM
3. Evaluar predicciones y visualizar resultados
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from typing import Tuple, List, Dict
import yfinance as yf
from datetime import datetime, timedelta

class StockDataProcessor:
    def __init__(self, sequence_length: int = 60):
        self.sequence_length = sequence_length
        self.price_scaler = MinMaxScaler()
        self.feature_scaler = MinMaxScaler()
    
    def download_stock_data(self, symbol: str, period: str = "2y") -> pd.DataFrame:
        """
        TODO: Descargar datos históricos de Yahoo Finance
        1. Obtener datos OHLCV
        2. Calcular indicadores técnicos básicos
        3. Limpiar datos faltantes
        """
        pass
    
    def calculate_technical_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        TODO: Calcular indicadores técnicos
        1. Medias móviles (SMA, EMA)
        2. RSI (Relative Strength Index)
        3. MACD
        4. Bollinger Bands
        5. Volumen promedio
        """
        pass
    
    def create_target_variable(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        TODO: Crear variable objetivo
        Basado en la tesis: variación porcentual intradía
        target = (Close - Open) / Open
        """
        pass
    
    def prepare_sequences(self, df: pd.DataFrame, 
                         target_col: str = 'target') -> Tuple[np.ndarray, np.ndarray]:
        """
        TODO: Crear secuencias para LSTM
        1. Normalizar datos
        2. Crear ventanas deslizantes
        3. Separar características y target
        """
        pass
    
    def split_data(self, X: np.ndarray, y: np.ndarray, 
                  train_ratio: float = 0.8) -> Tuple:
        """
        TODO: Dividir datos manteniendo orden temporal
        """
        pass

class FinancialLSTM(nn.Module):
    def __init__(self, input_size: int, hidden_sizes: List[int], 
                 dropout_rate: float = 0.2):
        super(FinancialLSTM, self).__init__()
        
        # TODO: Implementar arquitectura LSTM
        # Basada en la configuración de la tesis:
        # - Múltiples capas LSTM
        # - Dropout para regularización
        # - Capas densas finales
        pass
    
    def forward(self, x):
        # TODO: Implementar forward pass
        pass

class StockPredictor:
    def __init__(self, config: Dict):
        self.config = config
        self.model = None
        self.data_processor = StockDataProcessor(config['sequence_length'])
        self.training_history = {'train_loss': [], 'val_loss': []}
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    def prepare_data(self, symbol: str) -> Dict:
        """
        TODO: Preparar datos completos para entrenamiento
        1. Descargar datos históricos
        2. Calcular indicadores
        3. Crear secuencias
        4. Dividir train/test
        """
        pass
    
    def build_model(self, input_size: int):
        """TODO: Construir modelo LSTM"""
        pass
    
    def train(self, data_dict: Dict, epochs: int = 100) -> Dict:
        """
        TODO: Entrenar modelo
        1. Configurar optimizador y loss function
        2. Implementar loop de entrenamiento
        3. Validación y early stopping
        4. Guardar mejor modelo
        """
        pass
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """TODO: Hacer predicciones"""
        pass
    
    def evaluate_model(self, data_dict: Dict) -> Dict:
        """
        TODO: Evaluación completa del modelo
        1. Métricas de regresión (MSE, MAE, R²)
        2. Precisión direccional (% aciertos en dirección)
        3. Análisis de residuos
        """
        pass
    
    def predict_future(self, last_sequence: np.ndarray, steps: int = 5) -> np.ndarray:
        """
        TODO: Predicción multi-step
        Predecir múltiples días hacia el futuro
        """
        pass
    
    def plot_predictions(self, data_dict: Dict, predictions: np.ndarray):
        """
        TODO: Visualizar predicciones vs valores reales
        """
        pass
    
    def analyze_feature_importance(self, data_dict: Dict) -> Dict:
        """
        TODO: Analizar importancia de características
        Usar técnicas como permutation importance
        """
        pass

class ModelComparator:
    def __init__(self):
        self.models = {}
        self.results = {}
    
    def add_model(self, name: str, model: StockPredictor):
        """TODO: Agregar modelo para comparación"""
        pass
    
    def compare_models(self, symbol: str) -> pd.DataFrame:
        """
        TODO: Comparar múltiples configuraciones
        1. Diferentes arquitecturas LSTM
        2. Diferentes conjuntos de características
        3. Diferentes longitudes de secuencia
        """
        pass
    
    def plot_comparison(self, results_df: pd.DataFrame):
        """TODO: Visualizar comparación de modelos"""
        pass

# Configuraciones para probar
model_configs = [
    {
        'name': 'LSTM_Simple',
        'sequence_length': 60,
        'hidden_sizes': [50],
        'dropout_rate': 0.2,
        'learning_rate': 0.001
    },
    {
        'name': 'LSTM_Deep',
        'sequence_length': 60,
        'hidden_sizes': [50, 50],
        'dropout_rate': 0.3,
        'learning_rate': 0.001
    },
    {
        'name': 'LSTM_Long_Sequence',
        'sequence_length': 120,
        'hidden_sizes': [64, 32],
        'dropout_rate': 0.2,
        'learning_rate': 0.0005
    }
]

# TODO: Implementar sistema de testing
def test_stock_prediction():
    """Probar sistema completo de predicción"""
    
    # Símbolo para probar
    symbol = "AAPL"
    
    # Probar cada configuración
    comparator = ModelComparator()
    
    for config in model_configs:
        print(f"\nEntrenando modelo: {config['name']}")
        
        # Crear y entrenar modelo
        predictor = StockPredictor(config)
        data_dict = predictor.prepare_data(symbol)
        
        # Entrenar
        training_results = predictor.train(data_dict, epochs=50)
        
        # Evaluar
        evaluation_results = predictor.evaluate_model(data_dict)
        
        print(f"Resultados para {config['name']}:")
        print(f"  MSE: {evaluation_results['mse']:.6f}")
        print(f"  MAE: {evaluation_results['mae']:.6f}")
        print(f"  R²: {evaluation_results['r2']:.3f}")
        print(f"  Precisión direccional: {evaluation_results['directional_accuracy']:.1f}%")
        
        # Agregar a comparador
        comparator.add_model(config['name'], predictor)
        
        # Visualizar predicciones
        predictions = predictor.predict(data_dict['X_test'])
        predictor.plot_predictions(data_dict, predictions)
    
    # Comparar todos los modelos
    comparison_results = comparator.compare_models(symbol)
    comparator.plot_comparison(comparison_results)
    
    print("\nComparación final de modelos:")
    print(comparison_results)

# test_stock_prediction()
```

#### Ejercicio 4.2: Análisis de Sentimientos + LSTM (20 min)
```python
# Archivo: ejercicio_4_2.py

"""
EJERCICIO: Integrar análisis de sentimientos con predicción LSTM
Replicar el enfoque de la tesis que combina variables emocionales con técnicas
1. Combinar datos de precios con sentimientos
2. Evaluar impacto de variables emocionales
3. Comparar modelos con y sin sentimiento
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, accuracy_score

# Importar clases de ejercicios anteriores
# from ejercicio_4_1 import StockPredictor, FinancialLSTM
# from ejercicio_3_1 import AdvancedFinancialSentimentAnalyzer

class SentimentStockDataProcessor:
    def __init__(self, sequence_length: int = 60):
        self.sequence_length = sequence_length
        self.price_scaler = StandardScaler()
        self.sentiment_scaler = StandardScaler()
        self.combined_scaler = StandardScaler()
    
    def load_stock_and_sentiment_data(self, symbol: str, 
                                    start_date: str, 
                                    end_date: str) -> pd.DataFrame:
        """
        TODO: Cargar datos de precios y sentimientos
        1. Datos históricos de precios
        2. Datos de sentimientos (tweets, noticias, opiniones)
        3. Alinear por fecha (días laborables)
        4. Manejar días sin datos de sentimiento
        """
        pass
    
    def create_sentiment_features(self, sentiment_data: pd.DataFrame) -> pd.DataFrame:
        """
        TODO: Crear características de sentimiento
        Basado en la metodología de la tesis:
        1. Probabilidades promedio por día (pos, neg, neu)
        2. Número de publicaciones por tipo
        3. Índice de sentimiento agregado (SMI)
        4. Volatilidad del sentimiento
        """
        pass
    
    def add_market_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        TODO: Agregar indicadores de mercado
        1. VIX (índice de volatilidad)
        2. Indicadores de riesgo geopolítico
        3. Volumen de trading
        4. Variables de días laborables
        """
        pass
    
    def create_combined_features(self, price_data: pd.DataFrame, 
                               sentiment_data: pd.DataFrame) -> pd.DataFrame:
        """
        TODO: Combinar características de precio y sentimiento
        1. Merge por fecha
        2. Crear variables lag (retardos)
        3. Normalizar todas las características
        """
        pass
    
    def prepare_model_variants(self, df: pd.DataFrame) -> Dict[str, Dict]:
        """
        TODO: Preparar variantes del modelo
        1. Solo variables técnicas
        2. Solo variables de sentimiento  
        3. Combinación completa
        4. Diferentes longitudes de secuencia
        """
        pass

class SentimentEnhancedLSTM(FinancialLSTM):
    def __init__(self, price_features: int, sentiment_features: int,
                 hidden_sizes: List[int], dropout_rate: float = 0.2):
        
        # TODO: Extender LSTM para manejar múltiples tipos de características
        # 1. Ramas separadas para precio y sentimiento
        # 2. Capa de fusión
        # 3. Capas LSTM compartidas
        pass
    
    def forward(self, price_input, sentiment_input):
        # TODO: Forward pass con múltiples entradas
        pass

class SentimentImpactAnalyzer:
    def __init__(self):
        self.models = {}
        self.results = {}
    
    def train_model_variants(self, data_variants: Dict) -> Dict:
        """
        TODO: Entrenar diferentes variantes del modelo
        1. Modelo base (solo precios)
        2. Modelo con sentimientos
        3. Modelo solo sentimientos
        4. Comparar resultados
        """
        pass
    
    def analyze_sentiment_contribution(self, results: Dict) -> Dict:
        """
        TODO: Analizar contribución del sentimiento
        1. Mejora en MSE/MAE
        2. Mejora en precisión direccional
        3. Análisis estadístico de significancia
        """
        pass
    
    def feature_importance_analysis(self, model, data: Dict) -> Dict:
        """
        TODO: Análisis de importancia de características
        1. Permutation importance
        2. SHAP values para interpretabilidad
        3. Correlación con performance
        """
        pass
    
    def temporal_analysis(self, predictions: Dict, 
                         actual_values: np.ndarray,
                         dates: pd.DatetimeIndex) -> Dict:
        """
        TODO: Análisis temporal del impacto
        1. Performance por período (bull/bear markets)
        2. Impacto durante eventos específicos
        3. Estabilidad temporal del modelo
        """
        pass
    
    def plot_sentiment_impact(self, results: Dict):
        """
        TODO: Visualizar impacto del sentimiento
        1. Comparación de métricas
        2. Series temporales de predicciones
        3. Distribución de errores
        """
        pass

class MarketRegimeAnalyzer:
    def __init__(self):
        self.regimes = ['bull_market', 'bear_market', 'sideways', 'high_volatility']
    
    def identify_market_regimes(self, price_data: pd.DataFrame) -> pd.Series:
        """
        TODO: Identificar regímenes de mercado
        1. Tendencias alcistas/bajistas
        2. Períodos de alta volatilidad
        3. Mercados laterales
        """
        pass
    
    def analyze_sentiment_by_regime(self, sentiment_data: pd.DataFrame,
                                  regimes: pd.Series) -> Dict:
        """
        TODO: Analizar sentimiento por régimen de mercado
        1. Sentimiento promedio por régimen
        2. Volatilidad del sentimiento
        3. Correlación con returns
        """
        pass
    
    def evaluate_model_by_regime(self, predictions: Dict,
                                actual_values: np.ndarray,
                                regimes: pd.Series) -> Dict:
        """
        TODO: Evaluar modelos por régimen
        1. Performance en diferentes condiciones de mercado
        2. Cuándo el sentimiento es más/menos útil
        """
        pass

# Datos sintéticos para demostración
def create_synthetic_sentiment_data(dates: pd.DatetimeIndex, 
                                  price_returns: pd.Series) -> pd.DataFrame:
    """
    TODO: Crear datos sintéticos de sentimiento
    Correlacionados con los returns pero con ruido
    """
    np.random.seed(42)
    
    # Sentimiento base correlacionado con returns
    base_sentiment = price_returns * 0.3 + np.random.normal(0, 0.1, len(dates))
    
    sentiment_data = pd.DataFrame({
        'date': dates,
        'prob_positive_tweet': np.clip(0.4 + base_sentiment + np.random.normal(0, 0.1, len(dates)), 0, 1),
        'prob_negative_tweet': np.clip(0.3 - base_sentiment + np.random.normal(0, 0.1, len(dates)), 0, 1),
        'prob_neutral_tweet': np.clip(0.3 + np.random.normal(0, 0.05, len(dates)), 0, 1),
        'num_tweets': np.random.poisson(100, len(dates)),
        'num_news': np.random.poisson(10, len(dates)),
        'vix_close': 20 + np.random.normal(0, 5, len(dates)),
    })
    
    # Normalizar probabilidades
    prob_sum = (sentiment_data['prob_positive_tweet'] + 
                sentiment_data['prob_negative_tweet'] + 
                sentiment_data['prob_neutral_tweet'])
    
    sentiment_data['prob_positive_tweet'] /= prob_sum
    sentiment_data['prob_negative_tweet'] /= prob_sum  
    sentiment_data['prob_neutral_tweet'] /= prob_sum
    
    # Crear índice de sentimiento
    sentiment_data['sentiment_index'] = (
        (sentiment_data['prob_positive_tweet'] - sentiment_data['prob_negative_tweet']) /
        (sentiment_data['prob_positive_tweet'] + sentiment_data['prob_negative_tweet'] + 
         sentiment_data['prob_neutral_tweet'])
    )
    
    return sentiment_data

# TODO: Implementar sistema de testing completo
def test_sentiment_enhanced_prediction():
    """Probar sistema completo con sentimientos"""
    
    print("=== ANÁLISIS DE IMPACTO DEL SENTIMIENTO ===\n")
    
    # Configuración
    symbol = "AAPL"
    start_date = "2020-01-01"
    end_date = "2023-12-31"
    
    # Procesar datos
    processor = SentimentStockDataProcessor()
    
    # Cargar datos (en implementación real)
    # combined_data = processor.load_stock_and_sentiment_data(symbol, start_date, end_date)
    
    # Para demostración, crear datos sintéticos
    dates = pd.date_range(start_date, end_date, freq='B')  # Business days
    price_returns = np.random.normal(0.001, 0.02, len(dates))  # Returns diarios
    sentiment_data = create_synthetic_sentiment_data(dates, pd.Series(price_returns))
    
    print(f"Datos cargados: {len(dates)} días de trading")
    print(f"Características de sentimiento: {sentiment_data.columns.tolist()}")
    
    # Preparar variantes del modelo
    data_variants = processor.prepare_model_variants(sentiment_data)
    
    # Analizar impacto
    analyzer = SentimentImpactAnalyzer()
    
    # Entrenar modelos
    model_results = analyzer.train_model_variants(data_variants)
    
    # Analizar contribución del sentimiento
    sentiment_impact = analyzer.analyze_sentiment_contribution(model_results)
    
    print("\n=== RESULTADOS DE COMPARACIÓN ===")
    for model_name, metrics in sentiment_impact.items():
        print(f"\n{model_name}:")
        print(f"  MSE: {metrics['mse']:.6f}")
        print(f"  MAE: {metrics['mae']:.6f}")
        print(f"  Precisión direccional: {metrics['directional_accuracy']:.1f}%")
        print(f"  R²: {metrics['r2']:.3f}")
    
    # Calcular mejoras
    base_mse = sentiment_impact['price_only']['mse']
    sentiment_mse = sentiment_impact['price_and_sentiment']['mse']
    improvement = ((base_mse - sentiment_mse) / base_mse) * 100
    
    print(f"\n=== IMPACTO DEL SENTIMIENTO ===")
    print(f"Mejora en MSE: {improvement:.1f}%")
    
    base_acc = sentiment_impact['price_only']['directional_accuracy']
    sentiment_acc = sentiment_impact['price_and_sentiment']['directional_accuracy']
    acc_improvement = sentiment_acc - base_acc
    
    print(f"Mejora en precisión direccional: +{acc_improvement:.1f} puntos porcentuales")
    
    # Análisis por régimen de mercado
    regime_analyzer = MarketRegimeAnalyzer()
    # regimes = regime_analyzer.identify_market_regimes(price_data)
    # regime_analysis = regime_analyzer.evaluate_model_by_regime(model_results, actual_values, regimes)
    
    # Visualizar resultados
    analyzer.plot_sentiment_impact(model_results)
    
    print("\n=== CONCLUSIONES ===")
    print("1. Las variables de sentimiento mejoran significativamente la predicción")
    print("2. El impacto es mayor en la precisión direccional que en el error absoluto")
    print("3. El modelo combinado es más robusto en diferentes condiciones de mercado")

# test_sentiment_enhanced_prediction()
```

#### Ejercicio 4.3: Visualización Avanzada con Plotly (15 min)
```python
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
```

---

### MÓDULO 5: INTEGRACIÓN Y DESPLIEGUE
**Duración: 0.5 horas**

#### Ejercicio 5.1: API con FastAPI (15 min)
```python
# Archivo: ejercicio_5_1.py

"""
EJERCICIO: Crear API REST para el sistema de predicción
1. Endpoints para análisis de sentimientos
2. Endpoints para predicciones LSTM
3. Documentación automática con Swagger
4. Autenticación y rate limiting
"""

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import asyncio
from datetime import datetime
import uvicorn

# TODO: Importar clases de ejercicios anteriores
# from ejercicio_3_1 import AdvancedFinancialSentimentAnalyzer
# from ejercicio_4_2 import SentimentEnhancedLSTM

# Modelos Pydantic para requests/responses
class SentimentRequest(BaseModel):
    text: str = Field(..., description="Texto para analizar")
    text_type: str = Field("financial", description="Tipo de texto (financial, twitter, news)")

class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    confidence: float
    probabilities: Dict[str, float]
    processing_time: float

class PredictionRequest(BaseModel):
    symbol: str = Field(..., description="Símbolo de la acción")
    historical_data: List[List[float]] = Field(..., description="Datos históricos")
    include_sentiment: bool = Field(True, description="Incluir análisis de sentimiento")
    prediction_days: int = Field(1, description="Días a predecir")

class PredictionResponse(BaseModel):
    symbol: str
    predictions: List[float]
    confidence_intervals: Optional[List[List[float]]] = None
    sentiment_impact: Optional[Dict[str, float]] = None
    model_metrics: Dict[str, float]
    timestamp: datetime

class BatchSentimentRequest(BaseModel):
    texts: List[str] = Field(..., description="Lista de textos")
    text_type: str = Field("financial", description="Tipo de textos")

# Crear aplicación FastAPI
app = FastAPI(
    title="Financial ML API",
    description="API para análisis de sentimientos y predicción de precios con ML",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Seguridad
security = HTTPBearer()

# Variables globales para modelos (en producción usar dependency injection)
sentiment_analyzer = None
lstm_predictor = None

# TODO: Implementar autenticación
async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    TODO: Verificar token de autenticación
    En producción, verificar contra base de datos o JWT
    """
    pass

# TODO: Implementar rate limiting
class RateLimiter:
    def __init__(self, max_requests: int = 100, window_seconds: int = 3600):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}
    
    async def check_rate_limit(self, client_id: str) -> bool:
        """TODO: Verificar límite de requests"""
        pass

rate_limiter = RateLimiter()

@app.on_event("startup")
async def startup_event():
    """
    TODO: Inicialización al arrancar
    1. Cargar modelos pre-entrenados
    2. Configurar conexiones a base de datos
    3. Inicializar cache
    """
    global sentiment_analyzer, lstm_predictor
    
    print("🚀 Iniciando Financial ML API...")
    
    # TODO: Cargar modelos
    # sentiment_analyzer = AdvancedFinancialSentimentAnalyzer()
    # lstm_predictor = SentimentEnhancedLSTM.load_pretrained("models/lstm_model.pth")
    
    print("✅ Modelos cargados exitosamente")

@app.get("/")
async def root():
    """Endpoint raíz con información de la API"""
    return {
        "message": "Financial ML API",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "sentiment": "/analyze/sentiment",
            "batch_sentiment": "/analyze/batch-sentiment", 
            "prediction": "/predict/stock",
            "health": "/health",
            "docs": "/docs"
        },
        "timestamp": datetime.now()
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now(),
        "models": {
            "sentiment_analyzer": sentiment_analyzer is not None,
            "lstm_predictor": lstm_predictor is not None
        },
        "uptime": "TODO: calcular uptime"
    }

@app.post("/analyze/sentiment", response_model=SentimentResponse)
async def analyze_sentiment(
    request: SentimentRequest,
    token: str = Depends(verify_token)
):
    """
    TODO: Analizar sentimiento de un texto
    1. Validar entrada
    2. Preprocesar texto según tipo
    3. Ejecutar análisis
    4. Retornar resultado estructurado
    """
    pass

@app.post("/analyze/batch-sentiment")
async def batch_analyze_sentiment(
    request: BatchSentimentRequest,
    background_tasks: BackgroundTasks,
    token: str = Depends(verify_token)
):
    """
    TODO: Análisis de sentimiento en lote
    1. Procesar en background para lotes grandes
    2. Retornar job_id para seguimiento
    3. Endpoint separado para obtener resultados
    """
    pass

@app.post("/predict/stock", response_model=PredictionResponse)
async def predict_stock_price(
    request: PredictionRequest,
    token: str = Depends(verify_token)
):
    """
    TODO: Predecir precio de acción
    1. Validar datos históricos
    2. Obtener datos de sentimiento si se solicita
    3. Ejecutar predicción con LSTM
    4. Calcular intervalos de confianza
    """
    pass

@app.get("/predict/stock/{symbol}/latest")
async def get_latest_prediction(
    symbol: str,
    days: int = 5,
    token: str = Depends(verify_token)
):
    """
    TODO: Obtener última predicción para un símbolo
    """
    pass

@app.post("/models/retrain")
async def retrain_models(
    background_tasks: BackgroundTasks,
    model_type: str = "lstm",
    token: str = Depends(verify_token)
):
    """
    TODO: Re-entrenar modelos con nuevos datos
    Ejecutar en background
    """
    pass

@app.get("/models/performance")
async def get_model_performance(token: str = Depends(verify_token)):
    """
    TODO: Obtener métricas de performance de los modelos
    """
    pass

@app.websocket("/ws/predictions/{symbol}")
async def websocket_predictions(websocket, symbol: str):
    """
    TODO: WebSocket para predicciones en tiempo real
    1. Aceptar conexión
    2. Enviar predicciones periódicamente
    3. Manejar desconexiones
    """
    pass

# Middleware personalizado para logging
@app.middleware("http")
async def log_requests(request, call_next):
    """
    TODO: Middleware para logging de requests
    1. Log de entrada
    2. Medir tiempo de procesamiento
    3. Log de salida con métricas
    """
    pass

# Manejo de errores personalizado
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """TODO: Manejo personalizado de errores HTTP"""
    pass

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """TODO: Manejo de errores generales"""
    pass

# TODO: Implementar funciones de testing
def test_api_endpoints():
    """Probar endpoints de la API"""
    
    # TODO: Tests unitarios para cada endpoint
    # Usar pytest y httpx para testing async
    pass

if __name__ == "__main__":
    # Configuración para desarrollo
    uvicorn.run(
        "ejercicio_5_1:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
```

#### Ejercicio 5.2: Containerización con Docker (10 min)
```python
# Archivo: ejercicio_5_2_docker_setup.py

"""
EJERCICIO: Containerizar la aplicación con Docker
1. Crear Dockerfile optimizado
2. Docker Compose para servicios múltiples
3. Configuración de producción
"""

# Dockerfile
dockerfile_content = """
# TODO: Completar Dockerfile
FROM python:3.12-slim

# Configurar variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \\
    PYTHONUNBUFFERED=1 \\
    PYTHONPATH=/app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \\
    # TODO: Agregar dependencias necesarias
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# TODO: Copiar y instalar requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# TODO: Copiar código de aplicación
COPY . .

# TODO: Crear usuario no-root para seguridad

# TODO: Configurar health check

# TODO: Exponer puerto

# TODO: Comando de inicio
"""

# docker-compose.yml
docker_compose_content = """
# TODO: Completar docker-compose.yml
version: '3.8'

services:
  # Servicio principal de la API
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      # TODO: Variables de entorno
    depends_on:
      # TODO: Dependencias
    volumes:
      # TODO: Volúmenes para logs y modelos
    restart: unless-stopped
    healthcheck:
      # TODO: Health check

  # Base de datos PostgreSQL
  db:
    image: postgres:15
    environment:
      # TODO: Configuración de PostgreSQL
    volumes:
      # TODO: Persistencia de datos
    ports:
      - "5432:5432"

  # Redis para cache
  redis:
    image: redis:7-alpine
    # TODO: Configuración de Redis

  # Nginx como reverse proxy
  nginx:
    image: nginx:alpine
    # TODO: Configuración de Nginx

  # Prometheus para métricas
  prometheus:
    image: prom/prometheus
    # TODO: Configuración de monitoreo

volumes:
  # TODO: Definir volúmenes

networks:
  # TODO: Definir redes
"""

# nginx.conf
nginx_config = """
# TODO: Configuración de Nginx
events {
    worker_connections 1024;
}

http {
    upstream api {
        # TODO: Configurar upstream
    }
    
    server {
        listen 80;
        
        # TODO: Configurar proxy pass
        # TODO: Configurar SSL
        # TODO: Configurar rate limiting
    }
}
"""

def create_docker_files():
    """
    TODO: Crear archivos de Docker
    1. Escribir Dockerfile
    2. Escribir docker-compose.yml
    3. Crear configuraciones adicionales
    """
    pass

def build_and_test_container():
    """
    TODO: Construir y probar contenedor
    1. docker build
    2. docker run con tests
    3. Verificar health checks
    """
    pass

# Comandos útiles de Docker
docker_commands = """
# TODO: Documentar comandos útiles

# Construir imagen
docker build -t financial-ml-api .

# Ejecutar contenedor
docker run -p 8000:8000 financial-ml-api

# Ejecutar con docker-compose
docker-compose up -d

# Ver logs
docker-compose logs -f api

# Escalar servicios
docker-compose up -d --scale api=3

# Actualizar servicios
docker-compose pull && docker-compose up -d

# Backup de base de datos
docker-compose exec db pg_dump -U user financial_db > backup.sql
"""
```

#### Ejercicio 5.3: Monitoreo y Logging (5 min)
```python
# Archivo: ejercicio_5_3_monitoring.py

"""
EJERCICIO: Sistema de monitoreo y logging
1. Métricas con Prometheus
2. Logging estructurado
3. Alertas automáticas
"""

import logging
import json
from datetime import datetime
from prometheus_client import Counter, Histogram, Gauge, start_http_server
import psutil
import time

# TODO: Configurar logging estructurado
class JSONFormatter(logging.Formatter):
    """TODO: Formatter para logs en JSON"""
    pass

def setup_logging():
    """TODO: Configurar sistema de logging"""
    pass

# TODO: Configurar métricas de Prometheus
class MetricsCollector:
    def __init__(self):
        # Métricas de API
        self.api_requests = Counter(
            'api_requests_total',
            'Total API requests',
            ['method', 'endpoint', 'status']
        )
        
        self.api_duration = Histogram(
            'api_request_duration_seconds',
            'API request duration',
            ['method', 'endpoint']
        )
        
        # Métricas de ML
        self.ml_predictions = Counter(
            'ml_predictions_total',
            'Total ML predictions',
            ['model_type', 'symbol']
        )
        
        self.ml_latency = Histogram(
            'ml_prediction_latency_seconds',
            'ML prediction latency',
            ['model_type']
        )
        
        # Métricas del sistema
        self.system_cpu = Gauge('system_cpu_percent', 'CPU usage')
        self.system_memory = Gauge('system_memory_percent', 'Memory usage')
        
    def record_api_request(self, method: str, endpoint: str, 
                          status: int, duration: float):
        """TODO: Registrar request de API"""
        pass
    
    def record_ml_prediction(self, model_type: str, symbol: str, 
                           latency: float):
        """TODO: Registrar predicción de ML"""
        pass
    
    def update_system_metrics(self):
        """TODO: Actualizar métricas del sistema"""
        pass

# TODO: Sistema de alertas
class AlertManager:
    def __init__(self):
        self.thresholds = {
            'cpu_high': 80.0,
            'memory_high': 85.0,
            'api_error_rate': 5.0,
            'ml_latency_high': 10.0
        }
    
    def check_alerts(self, metrics: dict):
        """TODO: Verificar condiciones de alerta"""
        pass
    
    def send_alert(self, alert_type: str, message: str):
        """TODO: Enviar alerta (email, Slack, etc.)"""
        pass

# TODO: Health checks
class HealthChecker:
    def __init__(self):
        self.checks = {
            'database': self.check_database,
            'redis': self.check_redis,
            'models': self.check_models,
            'disk_space': self.check_disk_space
        }
    
    def check_database(self) -> bool:
        """TODO: Verificar conexión a base de datos"""
        pass
    
    def check_redis(self) -> bool:
        """TODO: Verificar conexión a Redis"""
        pass
    
    def check_models(self) -> bool:
        """TODO: Verificar que los modelos están cargados"""
        pass
    
    def check_disk_space(self) -> bool:
        """TODO: Verificar espacio en disco"""
        pass
    
    def run_all_checks(self) -> dict:
        """TODO: Ejecutar todos los health checks"""
        pass

# TODO: Implementar dashboard de monitoreo
def create_monitoring_dashboard():
    """
    TODO: Crear dashboard con Grafana
    1. Configurar datasources
    2. Crear paneles para métricas clave
    3. Configurar alertas
    """
    pass

# Configuración de monitoreo
monitoring_config = """
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'financial-ml-api'
    static_configs:
      - targets: ['api:8000']
    metrics_path: '/metrics'
    scrape_interval: 5s

# grafana/dashboards/financial-ml.json
# TODO: Configuración de dashboard de Grafana

# alertmanager.yml
# TODO: Configuración de alertas
"""

if __name__ == "__main__":
    # Iniciar servidor de métricas
    start_http_server(8001)
    
    # TODO: Iniciar recolección de métricas
    collector = MetricsCollector()
    
    # TODO: Iniciar health checks
    health_checker = HealthChecker()
    
    print("Sistema de monitoreo iniciado en puerto 8001")
```

---

## EVALUACIÓN Y CERTIFICACIÓN

### Proyecto Final Integrador (30 min)
```python
# proyecto_final.py

"""
PROYECTO FINAL: Sistema Completo de Análisis Financiero con IA
Integrar todos los módulos en un sistema funcional completo

REQUISITOS:
1. API REST completa con FastAPI
2. Análisis de sentimientos con FinBERT
3. Predicción de precios con LSTM
4. Dashboard interactivo con Streamlit/Plotly
5. Containerización con Docker
6. Monitoreo y logging
7. Documentación completa
8. Tests unitarios

ENTREGABLES:
- Código fuente completo
- Documentación técnica
- Demo en vivo
- Presentación de resultados
"""

class FinancialMLSystem:
    """Sistema completo de ML financiero"""
    
    def __init__(self):
        # TODO: Inicializar todos los componentes
        pass
    
    def setup_system(self):
        """TODO: Configurar sistema completo"""
        pass
    
    def run_end_to_end_demo(self):
        """TODO: Demo completo del sistema"""
        pass

# Criterios de evaluación
evaluation_criteria = {
    'functionality': 40,  # Funcionalidad completa
    'code_quality': 20,   # Calidad del código
    'documentation': 15,  # Documentación
    'innovation': 15,     # Innovación y creatividad
    'presentation': 10    # Presentación
}
```

---

## RECURSOS ADICIONALES

### Enlaces y Referencias
```markdown
# RECURSOS PARA CONTINUAR APRENDIENDO

## APIs y Datos Financieros
- Alpha Vantage API: https://www.alphavantage.co/
- Yahoo Finance API: https://pypi.org/project/yfinance/
- Quandl: https://www.quandl.com/
- IEX Cloud: https://iexcloud.io/

## Modelos de Lenguaje
- Hugging Face Transformers: https://huggingface.co/transformers/
- FinBERT: https://huggingface.co/ProsusAI/finbert
- Financial PhraseBank: https://www.researchgate.net/publication/251231364

## Machine Learning
- PyTorch: https://pytorch.org/
- TensorFlow: https://tensorflow.org/
- Scikit-learn: https://scikit-learn.org/

## Visualización
- Plotly: https://plotly.com/python/
- Streamlit: https://streamlit.io/
- Dash: https://dash.plotly.com/

## Despliegue
- FastAPI: https://fastapi.tiangolo.com/
- Docker: https://docs.docker.com/
- Kubernetes: https://kubernetes.io/

## IAs para Programación
- Google Gemini: https://ai.google.dev/
- DeepSeek: https://www.deepseek.com/
- GitHub Copilot: https://github.com/features/copilot
```

### Próximos Pasos
```markdown
# ROADMAP DE APRENDIZAJE CONTINUO

## Nivel Intermedio (próximos 3 meses)
1. Profundizar en MLOps y deployment
2. Aprender más sobre transformers y attention
3. Explorar reinforcement learning para trading
4. Estudiar técnicas avanzadas de feature engineering

## Nivel Avanzado (6-12 meses)
1. Implementar sistemas de trading algorítmico
2. Desarrollar modelos de riesgo avanzados
3. Explorar quantum machine learning
4. Contribuir a proyectos open source

## Especialización (1-2 años)
1. Certificaciones en cloud (AWS, GCP, Azure)
2. Especialización en fintech o regtech
3. Investigación en nuevas arquitecturas de ML
4. Liderazgo técnico en equipos de data science
```