import json
import os
from datetime import datetime

from domaine.fiche import Fiche
from domaine.visiteur import Visiteur
from domaine.reparateur import Reparateur
from domaine.type_objet import TypeObjet


class Sauvegarde:

    def __init__(self) -> None:
        self.date_sauvegarde: datetime = datetime.now()
        self.erreur: bool = False
        self.dossier: str = "data/sauvegardes/" + self.date_sauvegarde.strftime("%Y-%m-%d_%H-%M")

    # Conversions en dictionnaire

    def _visiteur_vers_dict(self, visiteur: Visiteur) -> dict:
        """Convertit un visiteur en dictionnaire. Ne modifie pas le visiteur."""
        return {
            "id": visiteur.id,
            "nom_visiteur": visiteur.nom_visiteur,
            "prenom_visiteur": visiteur.prenom_visiteur,
            "num_tel": visiteur.num_tel,
            "email": visiteur.email,
            "accord": visiteur.accord,
            "derniere_visite": visiteur.derniere_visite.isoformat(),
        }

    def _type_vers_dict(self, type_objet: TypeObjet) -> dict:
        """Convertit un type d'objet en dictionnaire. Ne modifie pas le type."""
        return {
            "categorie": type_objet.categorie,
            "poids_moyen": type_objet.poids_moyen,
        }

    def _reparateur_vers_dict(self, reparateur: Reparateur) -> dict:
        """Convertit un réparateur en dictionnaire. Ne modifie pas le réparateur."""
        return {
            "nom": reparateur.nom,
            "prenom": reparateur.prenom,
            "specialite": reparateur.specialite,
        }

    def _fiche_vers_dict(self, fiche: Fiche) -> dict:  # Pour la méthode suivante, aide de la part de claude opus 5.5 en effort moyen. (Auteur : Louis Degand)
        """Convertit une fiche (et ce qu'elle contient) en dictionnaire. Ne modifie pas la fiche."""
        return {
            "id": fiche.id,
            "visiteur": self._visiteur_vers_dict(fiche.visiteur),
            "type_objet": self._type_vers_dict(fiche.type_objet),
            "description_panne": fiche.description_panne,
            "marque": fiche.marque,
            "reparateur": (self._reparateur_vers_dict(fiche.reparateur)
                           if fiche.reparateur is not None else None),
            "etat": fiche.etat.name,
            "resultat": fiche.resultat.name if fiche.resultat is not None else None,
            "diagnostic": fiche.diagnostic,
            "date_arrivee": fiche.date_arrivee.isoformat(),
        }

    # Méthodes

    def creer_dossier(self) -> None:
        """Crée le dossier de la sauvegarde en cours.
        PRE : aucune.
        POST : le dossier self.dossier et le dossier sauvegardes qui le contient existent.
        Rien ne change s'ils existaient déjà. Si la création échoue, self.erreur vaut True.
        """
        try:
            os.makedirs(self.dossier, exist_ok=True)
        except OSError:
            self.erreur = True

    def copie(self, fiche: Fiche) -> None:
        """
        Ajoute une copie de la fiche dans le fichier fiches.json de la sauvegarde en cours
        PRE: creer_dossier a été appelée et le dossier de sauvegarde a été créé.
        POST: La fiche est ajoutée sous forme de dictionnaire à la liste de fiches.json, la fiche n'est pas modifiée
        Exceptions: TypeError si fiche n'est pas de type Fiche
        """
        if not isinstance(fiche, Fiche):
            raise TypeError("Le paramètre fiche n'est pas de Type Fiche")

        chemin = self.dossier + "/fiches.json"

        try:
            with open(chemin, "r", encoding="utf-8") as f:
                fiches = json.load(f)
        except FileNotFoundError:
            fiches = []

        fiches.append(self._fiche_vers_dict(fiche))

        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(fiches, f, indent=2, ensure_ascii=False)

    def copie_visiteurs(self, visiteur: Visiteur) -> None:
        """
        Ajoute une copie du visiteur dans le fichier visiteurs.json de la sauvegarde en cours
        PRE: creer_dossier a été appelée et le dossier de sauvegarde a été créé.
        POST: Le visiteur est ajouté sous forme de dictionnaire à la liste de visiteurs.json, le visiteur n'est pas modifié
        Exceptions: TypeError si visiteur n'est pas de type Visiteur
        """
        if not isinstance(visiteur, Visiteur):
            raise TypeError("Le paramètre visiteur n'est pas de Type Visiteur")

        chemin = self.dossier + "/visiteurs.json"

        try:
            with open(chemin, "r", encoding="utf-8") as f:
                visiteurs = json.load(f)
        except FileNotFoundError:
            visiteurs = []

        visiteurs.append(self._visiteur_vers_dict(visiteur))

        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(visiteurs, f, indent=2, ensure_ascii=False)

    def copie_type(self, type_objet: TypeObjet) -> None:
        """
        Ajoute une copie du type d'objet dans le fichier types.json de la sauvegarde en cours
        PRE: creer_dossier a été appelée et le dossier de sauvegarde a été créé.
        POST: Le type est ajouté sous forme de dictionnaire à la liste de types.json, le type n'est pas modifié
        Exceptions: TypeError si type_objet n'est pas de type TypeObjet
        """
        if not isinstance(type_objet, TypeObjet):
            raise TypeError("Le paramètre type_objet n'est pas de Type TypeObjet")

        chemin = self.dossier + "/types.json"

        try:
            with open(chemin, "r", encoding="utf-8") as f:
                types = json.load(f)
        except FileNotFoundError:
            types = []

        types.append(self._type_vers_dict(type_objet))

        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(types, f, indent=2, ensure_ascii=False)

    def copie_reparateur(self, reparateur: Reparateur) -> None:
        """
        Ajoute une copie du réparateur dans le fichier reparateurs.json de la sauvegarde en cours
        PRE: creer_dossier a été appelée et le dossier de sauvegarde a été créé.
        POST: Le réparateur est ajouté sous forme de dictionnaire à la liste de reparateurs.json, le réparateur n'est pas modifié
        Exceptions: TypeError si reparateur n'est pas de type Reparateur
        """
        if not isinstance(reparateur, Reparateur):
            raise TypeError("Le paramètre reparateur n'est pas de Type Reparateur")

        chemin = self.dossier + "/reparateurs.json"

        try:
            with open(chemin, "r", encoding="utf-8") as f:
                reparateurs = json.load(f)
        except FileNotFoundError:
            reparateurs = []

        reparateurs.append(self._reparateur_vers_dict(reparateur))

        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(reparateurs, f, indent=2, ensure_ascii=False)

    def suppression_automatique(self) -> None:
        """Supprime les sauvegardes trop anciennes ou en trop.
        PRE : aucune.
        POST : il reste au maximum 10 sauvegardes dans dossier_racine, et aucune n'a
        plus de 365 jours par rapport à date_sauvegarde. Les plus anciennes ont été supprimées.
        Si une suppression échoue, self.erreur vaut True.
        """
        try:
            saves = sorted(os.listdir(self.dossier_racine))

            for nom in saves[:]:
                try:
                    date = datetime.strptime(nom, "%Y-%m-%d_%H-%M")
                except ValueError:
                    saves.remove(nom)   
                    continue
                if self.date_sauvegarde - date > timedelta(days=365):
                    shutil.rmtree(os.path.join(self.dossier_racine, nom))
                    saves.remove(nom)

            while len(saves) > 10:
                plus_ancienne = saves.pop(0)
                shutil.rmtree(os.path.join(self.dossier_racine, plus_ancienne))

        except OSError:
            self.erreur = True 

    def restauration(self, date: datetime) -> str:
        """
        """
        return None

    # À décommenter une fois la classe RapportCommune créée :
    # def copie_rapport(self, rapport: RapportCommune) -> None:
    #     """
    #     """
    #     return None


#CODE DE TEST GENERE PAR CLAUDE
if __name__ == "__main__":
    test = Sauvegarde()
    test.creer_dossier()
    print(test.dossier)
    print(test.erreur)

    fiche1 = Fiche(
        1,
        Visiteur(1, "Dubois", "Marie", None, None, False),
        TypeObjet("grille-pain", 1.5),
        "Ne chauffe plus",
    )
    fiche2 = Fiche(
        2,
        Visiteur(2, "Martin", "Paul", "0470123456", "paul@mail.be", True),
        TypeObjet("lampe", 2.0),
        "Ne s'allume plus",
        "Ikea",
    )

    test.copie(fiche1)
    test.copie(fiche2)
    test.copie_visiteurs(fiche1.visiteur)
    test.copie_visiteurs(fiche2.visiteur)
    test.copie_type(fiche1.type_objet)
    test.copie_type(fiche2.type_objet)
    test.copie_reparateur(Reparateur("Lemaire", "Jules", "électroménager"))

    print("Copie terminée, vérifie le dossier", test.dossier)