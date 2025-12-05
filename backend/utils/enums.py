from enum import Enum

# Enumeración de pie dominante
class PieDominante(Enum):
    DERECHO = "DERECHO"
    IZQUIERDO = "IZQUIERDO"



# Enumeración de equipos
class Equipos(Enum):
    LOCAL = "SIGMOTOA_FC"
    VISITANTE = "EL_RIVAL"



# Enumeración de resultado de partido
class ResultadoPartido(Enum):
    VICTORIA = "VICTORIA"
    DERROTA = "DERROTA"
    EMPATE = "EMPATE"