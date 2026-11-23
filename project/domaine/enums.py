from enum import Enum

class Etat(Enum):
    EN_ATTENTE = "en attente"
    EN_COURS = "en cours"
    TERMINE = "terminé"

class Resultat(Enum):
    REPARE = "réparé"
    NON_REPARABLE = "non réparable"
    A_SUIVRE = "à suivre"
