from fastapi import APIRouter, HTTPException, Form, UploadFile, File
from ..models.jugador import Jugador
from ..db.db import SessionDep
from ..utils.bucket import cargarArchivo
from sqlmodel import select
from ..utils.enums import *
import os


router = APIRouter(prefix="/jugadores", tags=["Jugadores"])

@router.post("/", response_model=Jugador, status_code=201)
async def crearJugador(
    session: SessionDep,
    nombre: str = Form(...),
    numeroCamiseta: int = Form(...),
    fechaNacimiento: str = Form(...),
    foto: UploadFile = File(None),
    nacionalidad: str = Form(...),
    altura: int = Form(...),
    peso: float = Form(...),
    pieDominante: PieDominante = Form(...),
    posicion: Position = Form(...),
    valorEnMercado: float = Form(...),
    anioIngresoClub: int = Form(...),
    estado: States = Form(...)
    ):

    """
    Endpoint para crear un jugador con imagen
    """
    
    # Verificar si ya existe un jugador con ese numero de camiseta
    jugadorDB = session.exec(select(Jugador).where(Jugador.numeroCamiseta == numeroCamiseta)).first()

    # Si ya existe el SKU, mostrar error
    if jugadorDB:
        raise HTTPException(400, f"El jugador con la camiseta {numeroCamiseta} ya existe")
    
    # Manejar la imagen
    fotoURL = None
    
    # Si hay imagen, subirla
    if foto and foto.filename:
        try:
            # La función cargarArchivo ahora devuelve la URL directa de Supabase
            fotoURL = await cargarArchivo(fotoURL)
        except Exception as e:
            raise HTTPException(500, f"Error al subir la imagen: {str(e)}")
    
    # Crear el objeto del jugador
    jugador = jugador(
        nombre=nombre,
        numeroCamiseta=numeroCamiseta,
        fechaNacimiento=fechaNacimiento,
        fotoURL=fotoURL,
        nacionalidad=nacionalidad,
        altura=altura,
        peso=peso,
        pieDominante=pieDominante,
        posicion=posicion,
        valorEnMercado=valorEnMercado,
        anioIngresoClub=anioIngresoClub,
        estado=estado
    )
    
    # Insertar en la DB y guardar los cambios
    session.add(jugador)
    session.commit()
    session.refresh(jugador)

    return jugador