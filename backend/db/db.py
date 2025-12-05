from sqlmodel import create_engine, Session, SQLModel, select
from fastapi import FastAPI, Depends
from typing import Annotated
from datetime import datetime as dt
import os
from dotenv import load_dotenv

"""
    Módulo de configuración de la base de datos.

    Gestiona la conexión con PostgreSQL, la creación del motor de base de datos,
    la gestión de sesiones y la inicialización de tablas
"""

# Cargar variables de entorno
load_dotenv()

# URL de la base de datos en Render
db_url = os.getenv("DB_URL")

# Crear motor de la base de datos
engine = create_engine(db_url)

# Funcion para crear tablas
def createAllTables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

# Sesion de la DB
def getSession():
    with Session(engine) as session:
        yield session

# Dependencia de la DB
SessionDep = Annotated[Session, Depends(getSession)]