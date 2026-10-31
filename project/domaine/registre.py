from dataclasses import dataclass, field
from domaine.fiche import Fiche
from domaine.visiteur import Visiteur

@dataclass
class RegistreFiches:

    file_attente: list[Fiche] = field(default_factory=list)

    def ajout_file_attente(self, fiche: Fiche):
        self.file_attente.append(fiche)
        return None

    def prochain_id(self):
        if not self.file_attente:
            return 1
        return max(fiche.id for fiche in self.file_attente) + 1

    def trouver_visiteur(self, nom, prenom):
        nom = nom.lower()
        prenom = prenom.lower()
        for fiche in self.file_attente:
            if fiche.visiteur.nom_visiteur.lower() == nom:
                if fiche.visiteur.prenom_visiteur.lower() == prenom:
                    return fiche.visiteur
        return None
    
    def fiches_par_ordre_arrivee(self) -> list[Fiche]:
        """F-02 : renvoie toutes les fiches, de la plus ancienne à la plus récente."""
        return sorted(self.file_attente, key=lambda fiche: fiche.date_arrivee)