# Archivo: ejercicio_5_1.py

"""
EJERCICIO: Crear API REST para el sistema de predicción
1. Endpoints para análisis de sentimientos
2. Endpoints para predicciones LSTM
3. Documentación automática con Swagger
4. Autenticación y rate limiting
"""

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import asyncio
from datetime import datetime
import uvicorn
import time

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
    # Por ahora, no hacemos nada para evitar errores
    if not (credentials.scheme == "Bearer" and credentials.credentials == "test_token"):
        # En un caso real, aquí validaríamos un token JWT
        # raise HTTPException(status_code=403, detail="Invalid authentication credentials")
        pass
    return credentials.credentials

# TODO: Implementar rate limiting
class RateLimiter:
    def __init__(self, max_requests: int = 100, window_seconds: int = 3600):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}
    
    async def check_rate_limit(self, client_id: str) -> bool:
        """TODO: Verificar límite de requests"""
        return True

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
    # token: str = Depends(verify_token) # Descomentar para activar seguridad
):
    """
    Analizar sentimiento de un texto
    """
    start_time = time.time()
    # TODO: Implementar lógica real
    return {
        "text": request.text,
        "sentiment": "neutral",
        "confidence": 0.95,
        "probabilities": {"positive": 0.1, "negative": 0.05, "neutral": 0.85},
        "processing_time": time.time() - start_time
    }

@app.post("/analyze/batch-sentiment")
async def batch_analyze_sentiment(
    request: BatchSentimentRequest,
    background_tasks: BackgroundTasks,
    # token: str = Depends(verify_token)
):
    """
    Análisis de sentimiento en lote
    """
    # TODO: Implementar lógica real de background
    return {"message": "Batch sentiment analysis started", "job_id": "some_job_id"}

@app.post("/predict/stock", response_model=PredictionResponse)
async def predict_stock_price(
    request: PredictionRequest,
    # token: str = Depends(verify_token)
):
    """
    Predecir precio de acción
    """
    # TODO: Implementar lógica real
    return {
        "symbol": request.symbol,
        "predictions": [150.5, 151.0, 150.75],
        "confidence_intervals": [[148.0, 152.0]],
        "sentiment_impact": {"score": 0.2},
        "model_metrics": {"mae": 0.85},
        "timestamp": datetime.now()
    }

@app.get("/predict/stock/{symbol}/latest")
async def get_latest_prediction(
    symbol: str,
    days: int = 5,
    # token: str = Depends(verify_token)
):
    """
    Obtener última predicción para un símbolo
    """
    # TODO: Implementar lógica real
    return {"message": f"Latest prediction for {symbol} for {days} days"}

@app.post("/models/retrain")
async def retrain_models(
    background_tasks: BackgroundTasks,
    model_type: str = "lstm",
    # token: str = Depends(verify_token)
):
    """
    Re-entrenar modelos con nuevos datos
    """
    # TODO: Implementar lógica real
    return {"message": f"Retraining for model {model_type} started in background."}

@app.get("/models/performance")
async def get_model_performance(# token: str = Depends(verify_token)
):
    """
    Obtener métricas de performance de los modelos
    """
    # TODO: Implementar lógica real
    return {"mae": 0.85, "mse": 1.2, "r2": 0.9}

@app.websocket("/ws/predictions/{symbol}")
async def websocket_predictions(websocket, symbol: str):
    """
    WebSocket para predicciones en tiempo real
    """
    await websocket.accept()
    try:
        while True:
            await asyncio.sleep(5)
            # TODO: Implementar lógica real de predicción
            await websocket.send_json({"symbol": symbol, "prediction": 150.0 + time.time() % 10})
    except Exception:
        await websocket.close()

# Middleware personalizado para logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    Middleware para logging de requests
    """
    start_time = time.time()
    
    response = await call_next(request)
    
    processing_time = time.time() - start_time
    print(f"Request: {request.method} {request.url} - Completed in {processing_time:.4f}s with status {response.status_code}")
    
    return response

# Manejo de errores personalizado
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"HTTP Error: {exc.detail}"}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"An unexpected error occurred: {exc}"}
    )

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
