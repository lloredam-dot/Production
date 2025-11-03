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
