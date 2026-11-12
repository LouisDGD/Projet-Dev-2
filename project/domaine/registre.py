from dataclasses import dataclass, field
from domaine.fiche import Fiche
from domaine.visiteur import Visiteur
from domaine.enums import Resultat

@dataclass
class RegistreFiches:

    file_attente: list[Fiche] = field(default_factory=list)

    def ajout_file_attente(self, fiche: Fiche):
        """Ajoute l'élement a la file d'attente
                PRE : aucune.
                POST : L'élément est ajouté a la file d'attente file_attente[].
        """
        self.file_attente.append(fiche)
        return None

    def prochain_id(self):
        """Retourne l'id le plus élevé de la file d'attente +1
                PRE : aucune.
                POST : L'id est renvoyé
        """ 
        if not self.file_attente:
            return 1
        return max(fiche.id for fiche in self.file_attente) + 1

    def trouver_visiteur(self, nom, prenom):
        """Retourne la fiche du visiteur dont le nom et le prénom sont données en paramètres
                PRE : aucune.
                POST : La fiche contenant le prénom et le nom donnés en paramètres est renvoyé
        """ 
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

    def rappel_a_suivre(self) -> list[Fiche]:
        """Renvoie la liste des fiches qui ont le résultat Resultat.A_SUIVRE
        PRE : aucune.
        POST : renvoie une liste de fiches trié par odre chronologique qui ont l'attribut résultat Resultat.A_SUIVRE
        Renvoie une liste vide si aucune fiche ne correspond.
        Ne modifie rien
        """
        liste_a_suivre = []
        for fiche in self.file_attente:
            if fiche.resultat == Resultat.A_SUIVRE:
                liste_a_suivre.append(fiche)
        return sorted(liste_a_suivre, key=lambda fiche: fiche.date_arrivee)
