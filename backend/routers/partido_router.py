from fastapi import APIRouter, HTTPException, Form, UploadFile, File
from ..models.jugador import Jugador
from ..db.db import SessionDep
from ..utils.bucket import cargarArchivo
from sqlmodel import select
from ..utils.enums import *
import os


router = APIRouter(prefix="/partidos", tags=["Partidos"])