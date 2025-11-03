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
