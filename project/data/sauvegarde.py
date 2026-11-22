import json
from dataclasses import dataclass, field
from datetime import datetime

from domaine.fiche import Fiche
from domaine.visiteur import Visiteur
from domaine.reparateur import Reparateur
from domaine.type_objet import TypeObjet


@dataclass
class Sauvegarde:
    date_sauvegarde: datetime = field(default_factory=datetime.now)
    erreur: bool = False

    def copie(self, fiche: Fiche) -> None:
        """
        """
        return None

    def creer_dossier(self) -> None:
        """
        """
        return None

    def copie_visiteurs(self, visiteur: Visiteur) -> None:
        """
        """
        return None

    def copie_type(self, type: TypeObjet) -> None:
        """
        """
        return None

    def suppression_automatique(self) -> None:
        """
        """
        return None

    def restauration(self, date: datetime) -> str:
        """
        """
        return None

    def copie_reparateur(self, reparateur: Reparateur) -> None:
        """
        """
        return None

    # À décommenter une fois la classe RapportCommune créée :
    # def copie_rapport(self, rapport: RapportCommune) -> None:
    #     """
    #     """
    #     return None