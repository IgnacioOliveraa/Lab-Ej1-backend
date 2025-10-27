from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer
from django.core.mail import send_mail
from django.conf import settings

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all().order_by("-creado")
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        usuario = serializer.save()
        subject = "Nuevo usuario creado"
        message = f"Se creó: {usuario.nombre} - {usuario.email} - {usuario.telefono}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
