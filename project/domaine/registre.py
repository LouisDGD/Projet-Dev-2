from domaine.fiche import Fiche
from domaine.enums import Resultat


class RegistreFiches:

    def __init__(self, fiches_existantes: list[Fiche] = None):
        self.__file_attente = fiches_existantes if fiches_existantes else None

    def ajout_file_attente(self, fiche: Fiche) -> None:
        """Ajoute l'élement a la file d'attente
                PRE : aucune.
                POST : L'élément est ajouté a la file d'attente file_attente[].
        """
        self.__file_attente.append(fiche)
        
        return None

    def retire_file_attente(self, fiche:Fiche) -> None:
        for fiche_file_attente in self.__file_attente:
            if fiche_file_attente.id == fiche.id:
                self.__file_attente.remove(fiche_file_attente)
                return
        raise ValueError("Cette fiche n'existe pas")

    def prochain_id(self):
        """Retourne l'id le plus élevé de la file d'attente +1
                PRE : aucune.
                POST : L'id est renvoyé
        """ 
        if not self.__file_attente:
            return 1
        return max(fiche.id for fiche in self.__file_attente) + 1

    def trouver_visiteur(self, nom, prenom):
        """Retourne la fiche du visiteur dont le nom et le prénom sont données en paramètres
                PRE : aucune.
                POST : La fiche contenant le prénom et le nom donnés en paramètres est renvoyé
        """ 
        nom = nom.title()
        prenom = prenom.title()
        for fiche in self.__file_attente:
            if fiche.visiteur.nom_visiteur == nom and fiche.visiteur.prenom_visiteur == prenom:
                    return fiche.visiteur
        return None
    
    def fiches_par_ordre_arrivee(self) -> list[Fiche]:
        """Renvoie toutes les fiches, de la plus ancienne à la plus récente.
        PRE : chaque fiche de file_attente a une date_arrivee de type datetime.
        POST : renvoie une nouvelle liste contenant toutes les fiches de file_attente,
        triées par date_arrivee croissante.
        Renvoie une liste vide si file_attente est vide.
        Ne modifie rien
        """
        return sorted(self.__file_attente, key=lambda fiche: fiche.date_arrivee)

    def rappel_a_suivre(self) -> list[Fiche]:
        """Renvoie la liste des fiches qui ont le résultat Resultat.A_SUIVRE
        PRE : aucune.
        POST : renvoie une liste de fiches trié par odre chronologique qui ont l'attribut résultat Resultat.A_SUIVRE
        Renvoie une liste vide si aucune fiche ne correspond.
        Ne modifie rien
        """
        liste_a_suivre = []
        for fiche in self.__file_attente:
            if fiche.resultat == Resultat.A_SUIVRE:
                liste_a_suivre.append(fiche)
        return sorted(liste_a_suivre, key=lambda fiche: fiche.date_arrivee)

    def trouver_fiche(self, nom_visiteur: str, prenom_visiteur: str) -> list[Fiche]:
        """Renvoie toutes les fiches du visiteur dont le nom et le prénom sont donnés
        PRE : aucune.
        POST : renvoie une liste de fiches triée par ordre chronologique, dont le visiteur
        a le nom et le prénom donnés, sans tenir compte des majuscules ni des espaces autour.
        Renvoie une liste vide si aucune fiche ne correspond.
        Ne modifie rien
        """
        nom = nom_visiteur.strip().title()
        prenom = prenom_visiteur.strip().title()
        fiches_trouvees = []
        for fiche in self.__file_attente:
            if fiche.visiteur.nom_visiteur == nom:
                if fiche.visiteur.prenom_visiteur == prenom:
                    fiches_trouvees.append(fiche)
        return sorted(fiches_trouvees, key=lambda fiche: fiche.date_arrivee)
    
    def trouver_par_id(self, id_fiche: int) -> Fiche | None:
        for fiche in self.file_attente:
            if fiche.id == id_fiche:
                return fiche
        return None