from django.urls import path
from .views import UsuarioListCreate

urlpatterns = [
    path("users/", UsuarioListCreate.as_view(), name="users-list-create"),
]
