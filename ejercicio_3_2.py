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
from datetime import datetime

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
        if entities:
            print(f"Entidades encontradas: {entities}")
        
        # Analizar sentimiento por entidad
        sentiment_by_entity = processor.analyze_sentiment_by_entity(text)
        if sentiment_by_entity:
            print(f"Sentimiento por entidad: {sentiment_by_entity}")
        
        # Extraer relaciones
        relationships = processor.extract_financial_relationships(text)
        if relationships:
            print(f"Relaciones: {relationships}")
        
        # Resumir
        summary = processor.summarize_financial_document(text)
        if summary:
            print(f"Resumen: {summary}")
        
        print("-" * 80)
    
    # Crear grafo de conocimiento
    knowledge_graph = processor.create_knowledge_graph(sample_financial_texts)
    if knowledge_graph:
        print(f"\nGrafo de conocimiento creado con {knowledge_graph.number_of_nodes()} nodos")

# test_financial_text_processing()
