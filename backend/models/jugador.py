from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime as dt
from utils.enums import PieDominante
from utils.positions import Position
from utils.states import States

"""
Modelo base de Jugador con atributos pero sin id autoincrementable
"""
class JugadorBase(SQLModel):
    nombre: Optional[str] = Field(default=None)
    numeroCamiseta: Optional[int] = Field(default=1)
    fechaNacimiento: int = Field(default=2007)
    fotoURL: Optional[str] = Field(default=None)
    nacionalidad: Optional[str] = Field(default=None)
    altura: Optional[int] = Field(default=160)
    peso: Optional[float] = Field(default=70.0)
    pieDominante: PieDominante = Field(default=PieDominante.DERECHO)
    posicion: Position = Field(default=Position.DELANTERO_C)
    valorEnMercado: Optional[float] = Field(default=0)
    anioIngresoClub: Optional[int] = Field(default=2025)
    estado: States = Field(default=States.ACTIVO)



"""
Modelo de Jugador con atributos heredados y id autoincrementable
"""

class Jugador(JugadorBase, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    estadisticasID: Optional[int] = Field(default=None, foreign_key="estadisticas.id")
    estadisticas: list["Estadisticas"] = Relationship(back_populates="jugador")
    partidoID: Optional[int] = Field(default=None, foreign_key="partido.id")
    partidos: list["Partido"] = Relationship(back_populates="jugador")



"""
Modelo de creación de Jugador con atributos heredados
"""

class JugadorCreate(JugadorBase):
    pass



"""
Modelo de actualización de Jugador con atributos heredados
"""

class JugadorUpdate(JugadorBase):
    pass



"""
Modelo de eliminación de Jugador con atributos heredados
"""

class JugadorDelete(JugadorBase):
    pass



# importaciones diferidas
from .estadisticas import Estadisticas
from .partido import Partido