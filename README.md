# Backend - Lab Ejercicio 1

Este proyecto contiene el **backend** de la aplicación de registro de usuarios, desarrollado en **Django**.

## Descripción
- Implementa una API REST para **crear y consultar usuarios**.
- Cada usuario tiene:
  - `nombre`  
  - `email` (único)  
  - `telefono`  
  - `creado` (fecha y hora de creación)

- Envía notificaciones cuando se crea un usuario (simulado con función interna).

## Dependencias
- Python 3.x
- Django 4.x
- djangorestframework

Instalación de dependencias:

```bash
pip install -r requirements.txt

Migraciones y Base de Datos

python manage.py makemigrations
python manage.py migrate

Cómo ejecutar

python manage.py runserver
## corre en .http://127.0.0.1:8000

Endpoints:

GET → lista usuarios/api/users/

POST → crear usuario/api/users/

{
  "nombre": "Juan",
  "email": "juan@mail.com",
  "telefono": "12345678"
}

Estructura del proyecto

backend/
├── core/
├── users/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
├── manage.py
├── requirements.txt
└── evidencias/