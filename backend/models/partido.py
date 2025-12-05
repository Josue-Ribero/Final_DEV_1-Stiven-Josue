from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime as dt
from utils.enums import ResultadoPartido

"""
Modelo base de Partido con atributos pero sin id autoincrementable
"""
class PartidoBase(SQLModel):
    resultado: ResultadoPartido = Field(default=ResultadoPartido.VICTORIA)
    golesAnotados: Optional[int] = Field(default=0)
    golesRecibidos: Optional[int] = Field(default=0)



"""
Modelo de Partido con atributos heredados y id autoincrementable
"""

class Partido(PartidoBase, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    estadisticasID: Optional[int] = Field(default=None, foreign_key="estadisticas.id")
    estadisticas: list["Estadisticas"] = Relationship(back_populates="Partido")
    partidoID: Optional[int] = Field(default=None, foreign_key="partido.id")
    partidos: list["Partido"] = Relationship(back_populates="Partido")



"""
Modelo de creación de Partido con atributos heredados
"""

class PartidoCreate(PartidoBase):
    pass



"""
Modelo de actualización de Partido con atributos heredados
"""

class PartidoUpdate(PartidoBase):
    pass



"""
Modelo de eliminación de Partido con atributos heredados
"""

class PartidoDelete(PartidoBase):
    pass



# importaciones diferidas
from .estadisticas import Estadisticas
from .partido import Partido