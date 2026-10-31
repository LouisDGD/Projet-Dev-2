from dataclasses import dataclass
from datetime import datetime

@dataclass
class Visiteur:
    id: int
    nom_visiteur: str
    prenom_visiteur: str
    derniere_visite: datetime
    #num_tel: str | None
    #email: str | None
    #accord: bool