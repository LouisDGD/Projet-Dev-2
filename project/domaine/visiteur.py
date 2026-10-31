from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Visiteur:
    id: int
    nom_visiteur: str
    prenom_visiteur: str
    num_tel: str | None
    email: str | None
    accord: bool
    derniere_visite: datetime = field(default_factory=datetime.now)