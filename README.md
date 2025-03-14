
# QuinLedger

## Overview / Visión General

QuinLedger is a backend project designed to integrate PostgreSQL with FastAPI, aimed at improving data management for the QuinLedger platform. The application provides a robust environment for managing and processing financial data efficiently.

QuinLedger es un proyecto backend diseñado para integrar PostgreSQL con FastAPI, con el objetivo de mejorar la gestión de datos para la plataforma QuinLedger. La aplicación proporciona un entorno robusto para gestionar y procesar datos financieros de manera eficiente.

## Features / Características

- **FastAPI Integration**: A fast and modern web framework to handle APIs.
- **PostgreSQL Database**: Configured with Docker for database management.
- **Docker**: Simplifies the setup and deployment process.

- **Integración con FastAPI**: Un framework web rápido y moderno para manejar APIs.
- **Base de Datos PostgreSQL**: Configurada con Docker para la gestión de la base de datos.
- **Docker**: Facilita el proceso de configuración y despliegue.

## Installation / Instalación

1. Clone the repository / Clona el repositorio:

```bash
git clone https://github.com/jmfranco2000/QuinLedger.git
```

2. Navigate to the project directory / Navega a la carpeta del proyecto:

```bash
cd QuinLedger/backend
```

3. Create and activate the virtual environment / Crea y activa el entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
.venv\Scripts\Activate     # For Windows
```

4. Install dependencies / Instala las dependencias:

```bash
pip install -r requirements.txt
```

5. Configure PostgreSQL and Docker / Configura PostgreSQL y Docker:
   - Ensure Docker is running on your system.
   - Follow the PostgreSQL Docker setup in `docker-compose.yml`.

6. Run the application / Ejecuta la aplicación:

```bash
uvicorn main:app --reload
```

## Configuration / Configuración

Ensure the following environment variables are correctly set:

Asegúrate de que las siguientes variables de entorno estén configuradas correctamente:

- `DATABASE_URL`: PostgreSQL connection URL.
- `SECRET_KEY`: A secure secret key for the application.
- `DEBUG`: Set to `True` for development and `False` for production.

## Testing / Pruebas

Run the tests with:

Ejecuta las pruebas con:

```bash
pytest
```

## License / Licencia

This project is licensed under the MIT License.

Este proyecto está bajo la Licencia MIT.
