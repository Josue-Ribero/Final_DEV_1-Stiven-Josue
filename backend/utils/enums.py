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

class Position(Enum):
    ARQUERO = "ARQUERO"
    DEFENSA_C= "DEFENSA CENTRAL"
    DEFENSA_L = "DEFENSA LATERAL"
    VOLANTE_D = "VOLANTE DEFENSIVO"
    VOLANTE_O = "VOLANTE OFENSIVO"
    VOLANTE_C = "VOLANTE CENTRAL"
    VOLANTE_E = "VOLANTE EXTREMO"
    DELANTERO_C = "DELANTERO CENTRAL"
    DELANTERO_P = "DELANTERO PUNTA"

class States(Enum):
    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"
    LESIONADO= "LESIONADO"
    AMONESTADO= "AMONESTADO"