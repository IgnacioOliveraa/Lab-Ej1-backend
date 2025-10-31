from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer
import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all().order_by("-creado")
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        # 1. Primero guardar el usuario en la base de datos
        usuario = serializer.save()
        
        # 2. Enviar notificación al servicio externo
        self.send_notification(usuario)
    
    def send_notification(self, usuario):
        """
        Envía notificación al servicio de notificaciones independiente
        """
        try:
            # URL del servicio de notificaciones (local para desarrollo)
            notification_url = "http://notification-service:5000/notify"
            
            # Datos para la notificación
            notification_data = {
                "nombre": usuario.nombre,
                "email": usuario.email,
                "telefono": usuario.telefono,
                "creado": usuario.creado.isoformat() if usuario.creado else None,
                "source": "users-api"
            }
            
            # Enviar request al servicio de notificaciones
            response = requests.post(
                notification_url,
                json=notification_data,
                headers={'Content-Type': 'application/json'},
                timeout=5  # timeout de 5 segundos
            )
            
            if response.status_code == 200:
                logger.info(f"✅ Notificación enviada exitosamente para usuario: {usuario.nombre}")
                print(f"✅ Notificación enviada al servicio externo para: {usuario.nombre}")
            else:
                logger.warning(f"⚠️  Servicio de notificaciones respondió con error: {response.status_code}")
                print(f"⚠️  Error en notificación: {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            logger.error("❌ No se pudo conectar al servicio de notificaciones")
            print("❌ Error: Servicio de notificaciones no disponible")
        except requests.exceptions.Timeout:
            logger.error("⏰ Timeout al conectar con servicio de notificaciones")
            print("⏰ Timeout: Servicio de notificaciones no responde")
        except Exception as e:
            logger.error(f"🚨 Error inesperado en notificación: {str(e)}")
            print(f"🚨 Error inesperado: {e}")