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
