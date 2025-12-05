<div align="center">

# ⚽ sigmotoa FC

Plataforma web para gestionar y visualizar equipo, jugadores, partidos y estadísticas de un quipo. API en FastAPI con vistas Jinja2, PostgreSQL y SQLModel.

[![FastAPI](https://img.shields.io/badge/FastAPI-%20-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-%20-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%20-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLModel](https://img.shields.io/badge/SQLModel-%20-1E7B85)](https://sqlmodel.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-%20-000000)](https://www.uvicorn.org/)
---
</div>

## 🚀 Arranque Rápido (Windows / PowerShell)

1) Crear entorno e instalar deps

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2) Configurar variables de entorno (.env)

```dotenv
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=golagol
```

3) Ejecutar el servidor

```powershell
uvicorn main:app --reload --port 8000
```

Abrir: `http://127.0.0.1:8000/` · API: `/docs`

---
