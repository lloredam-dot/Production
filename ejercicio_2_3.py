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
from typing import Dict, List, Optional

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
    auth_url_data = client.generate_auth_url([
        "tweet.read", "users.read", "offline.access"
    ])
    
    if auth_url_data:
        auth_url, state = auth_url_data
        print(f"Visita esta URL para autorizar: {auth_url}")
    
    # En una aplicación real, el usuario sería redirigido aquí
    # y obtendríamos el código de la URL de callback
    
    # Simular intercambio de código (en producción vendría del callback)
    # authorization_code = input("Ingresa el código de autorización: ")
    # tokens = client.exchange_code_for_token(authorization_code, code_verifier)
    
    # Buscar tweets
    # tweets = client.search_tweets("$AAPL OR Apple stock", max_results=5)
    # if tweets:
    #     print("Tweets encontrados:", len(tweets.get('data', [])))

# test_oauth_flow()
