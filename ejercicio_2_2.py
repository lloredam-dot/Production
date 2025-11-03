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
from typing import List, Dict, Optional
from datetime import datetime
import re
from dataclasses import dataclass

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
        if apple_news:
            for article in apple_news:
                print(f"Título: {article.title}")
                print(f"Fecha: {article.date}")
                print(f"Sentimiento: {article.sentiment_score}")
                print("-" * 50)
        
        # Análisis de sentimiento del mercado
        market_sentiment = analyze_market_sentiment(symbols_to_analyze)
        if market_sentiment:
            print("Sentimiento del mercado:")
            for symbol, sentiment in market_sentiment.items():
                print(f"{symbol}: {sentiment:+.2f}")
    
    finally:
        scraper.close()

# main()
