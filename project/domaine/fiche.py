from dataclasses import dataclass
from datetime import datetime
from domaine.visiteur import Visiteur
from domaine.type_objet import TypeObjet
from domaine.enums import Etat

@dataclass
class Fiche:
    id: int
    visiteur: Visiteur
    type: TypeObjet
    description_panne: str
    marque: str | None
    date_arrivee: datetime
    etat: Etat = Etat.EN_ATTENTE