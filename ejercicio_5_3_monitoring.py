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
