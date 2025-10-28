# 🖥️ Backend — Laboratorio Ejercicio 1

Este proyecto implementa el **backend** de una aplicación CRUD simple con **Django + Django REST Framework**.  
Permite registrar, listar y gestionar usuarios, sirviendo como API para el frontend.

---

## ⚙️ Tecnologías utilizadas

- Python 3
- Django
- Django REST Framework
- PostgreSQL (o SQLite por defecto)

---

## 🚀 Instrucciones para ejecutar

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/IgnacioOliveraa/Lab-Ej1-backend.git
   cd Lab-Ej1-backend

Crear y activar entorno virtual (opcional pero recomendado):

python -m venv venv
venv\Scripts\activate  # en Windows

Instalar dependencias:

pip install -r requirements.txt

Aplicar migraciones y levantar servidor:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Acceder en el navegador:

Panel admin → http://127.0.0.1:8000/admin

API usuarios → http://127.0.0.1:8000/api/users/

Estructura principal del proyecto:

backend/
├── backend/
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── evidencias/
│   ├── backend_admin_users.png
│   ├── backend_get_users_after_create.png
│   ├── backend_get_users_despues.json.png
│   ├── backend_get_users_inicial.json.png
│   ├── backend_post_response.json.png
│   └── requirements.txt


Evidencias
Evidencia	Descripción

	Vista del panel de administración de usuarios

	Lista de usuarios después de crear uno nuevo

	Respuesta JSON luego de insertar datos

	Estado inicial del endpoint de usuarios

	Respuesta del endpoint POST
📄 requirements.txt
	Archivo de dependencias utilizadas

Endpoints principales

Método	Endpoint	Descripción
GET	/api/users/	Lista todos los usuarios
POST	/api/users/	Crea un nuevo usuario
GET	/api/users/{id}/	Muestra un usuario específico