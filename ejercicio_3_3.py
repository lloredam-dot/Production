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
