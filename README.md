# Bella Studio — Sistema de Ventas

Sistema de ventas desarrollado con Django y MariaDB. El proyecto permite gestionar cuentas de clientes y está preparado para incorporar un catálogo de productos, carrito de compras, pedidos y administración de ventas.

## Tecnologías

- Python 3.12
- Django 5.2.19 LTS
- MariaDB 11.4
- MySQL/MariaDB mediante mysqlclient
- HTML, CSS y JavaScript
- python-dotenv para variables de entorno

## Estructura del proyecto

- **usuarios:** registro, inicio de sesión, perfiles y direcciones.
- **catalogo:** modelos de productos, categorías y descuentos.
- **ventas:** pedidos, detalles, transportadoras y facturas.
- **templates:** plantillas HTML.
- **static:** archivos CSS, JavaScript e imágenes.

## Instalación local

### 1. Crear el entorno virtual

Desde la raíz del repositorio:

```powershell
python -m venv venv
```

Activarlo en PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

### 3. Configurar MariaDB

Instalar MariaDB 11.4 y crear una base de datos llamada `peluqueria_paris`.

Crear un usuario de base de datos con permisos sobre esta base. La configuración local utilizada durante el desarrollo es:

- Host: `127.0.0.1`
- Puerto: `3307`
- Usuario: `bella_django`

Restaurar la estructura y los datos desde un respaldo SQL autorizado. Los datos y contraseñas reales no se incluyen en el repositorio.

### 4. Configurar variables de entorno

Copiar `.env.example` como `.env` y completar:

```dotenv
DJANGO_SECRET_KEY=
DJANGO_DB_PASSWORD=
```

No utilizar contraseñas compartidas ni subir `.env` a GitHub.

### 5. Ejecutar Django

Entrar al directorio del proyecto:

```powershell
cd sistema_ventas
```

Comprobar la configuración:

```powershell
python manage.py check
```

Comprobar las migraciones pendientes:

```powershell
python manage.py migrate --plan
```

En una base de datos nueva, revisar y ejecutar las migraciones correspondientes según el procedimiento de instalación. Algunas tablas existentes se representan mediante modelos con `managed = False`, por lo que requieren su estructura SQL previamente restaurada.

Iniciar el servidor:

```powershell
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## Estado del desarrollo

- Registro de clientes: implementado y probado manualmente.
- Inicio de sesión: implementado y probado manualmente.
- Cierre de sesión: implementado y probado manualmente.
- Arquitectura de modelos: reorganizada.
- Integración con MariaDB: comprobada.
- Catálogo, carrito y pedidos: siguientes etapas de desarrollo.

## Seguridad

Las contraseñas y claves secretas se almacenan fuera del repositorio mediante variables de entorno. La configuración de desarrollo no debe utilizarse directamente en producción.

## Control de versiones

El desarrollo actual se realiza sobre la rama `rama_martinez`.

El proyecto continuará con pruebas, nuevas funcionalidades y mejoras de seguridad antes de su publicación.