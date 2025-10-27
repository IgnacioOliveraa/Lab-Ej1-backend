# LAB Ejercicio 1 – Backend (Django REST API)

## Descripción general
Este proyecto corresponde al **Ejercicio 1 del Laboratorio de Aplicación en AWS EKS**, donde se desarrolla una API REST con **Django + Django REST Framework** para la gestión de usuarios y el envío simulado de notificaciones por correo.

El backend permite:
- Crear usuarios (`POST /api/users/`)
- Listar usuarios (`GET /api/users/`)
- Simular el envío de un correo al crear un usuario (impreso en consola)
- Acceder al panel de administración de Django (`/admin/`)

---

## Tecnologías utilizadas
- **Python 3.14**
- **Django 5.2.7**
- **Django REST Framework 3.16.1**
- **django-cors-headers 4.9.0**

---

## Cómo ejecutar el proyecto

###  Clonar o descargar el proyecto
```bash
git clone https://github.com/tuUsuario/Lab-Ej1-backend.git
cd Lab-Ej1-backend
