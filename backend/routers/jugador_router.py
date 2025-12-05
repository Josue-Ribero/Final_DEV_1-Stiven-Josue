from typing import List
from fastapi import APIRouter, HTTPException, Form, UploadFile, File
from ..models.jugador import Jugador, JugadorCreate
from ..db.db import SessionDep
from backend.utils.bucket import upload_file
from sqlmodel import select
from ..utils.enums import *


router = APIRouter(prefix="/jugadores", tags=["jugadores"])

@router.post("/", response_model=Jugador)
def create_jugador(
    session: SessionDep,
    nombre: str = Form(...),
    numeroCamiseta: int = Form(...),
    fechaNacimiento: str = Form(...),
    fotoURL: UploadFile = File(None),
    nacionalidad: str = Form(...),
    altura: int = Form(...),
    peso: float = Form(...),
    pieDominante: PieDominante = Form(...),
    posicion: Position = Form(...),
    valorEnMercado: float = Form(...),
    anioIngresoClub: int = Form(...),
    estado: States = Form(...)
    ):

    jugador_data = JugadorCreate(
        nombre=nombre,
        numeroCamiseta=numeroCamiseta,
        fechaNacimiento=fechaNacimiento,
        nacionalidad=nacionalidad,
        altura=altura,
        peso=peso,
        pieDominante=pieDominante,
        posicion=posicion,
        valorEnMercado=valorEnMercado,
        anioIngresoClub=anioIngresoClub,
        estado=estado
    )
    

    jugador = Jugador.from_orm(jugador_data)
    session.add(jugador)
    session.commit()
    session.refresh(jugador)
    return jugador