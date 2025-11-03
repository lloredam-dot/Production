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
