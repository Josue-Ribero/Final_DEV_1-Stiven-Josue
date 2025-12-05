from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime as dt

"""
Modelo base de Estadisticas con atributos pero sin id autoincrementable
"""
class EstadisticasBase(SQLModel):
    goles: Optional[int] = Field(default=0)
    tiempoEnCancha: dt = Field(default_factory=dt.now)
    faltas: Optional[int] = Field(default=0)
    tarjetas: Optional[int] = Field(default=0)
    encuentrosPerdidos: Optional[int] = Field(default=0)
    encuentrosAPerder: Optional[int] = Field(default=0)



"""
Modelo de Estadisticas con atributos heredados y id autoincrementable
"""

class Estadisticas(EstadisticasBase, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    jugadorID: Optional[int] = Field(default=None, foreign_key="jugador.id")
    jugador: Optional["Jugador"] = Relationship(back_populates="estadisticas")
    partidoID: Optional[int] = Field(default=None, foreign_key="partido.id")
    partidos: list["Partido"] = Relationship(back_populates="estadisticas")



"""
Modelo de creación de Estadisticas con atributos heredados
"""

class EstadisticasCreate(EstadisticasBase):
    pass



"""
Modelo de actualización de Estadisticas con atributos heredados
"""

class EstadisticasUpdate(EstadisticasBase):
    pass



"""
Modelo de eliminación de Estadisticas con atributos heredados
"""

class EstadisticasDelete(EstadisticasBase):
    pass



# importaciones diferidas
from .jugador import Jugador
from .partido import Partido