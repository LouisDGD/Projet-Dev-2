import json
import os
from datetime import datetime, timedelta

from domaine.fiche import Fiche
from domaine.visiteur import Visiteur
from domaine.reparateur import Reparateur
from domaine.type_objet import TypeObjet
from domaine.enums import Resultat, Etat


class Sauvegarde:

    def __init__(self) -> None:
        self.date_sauvegarde: datetime = datetime.now()
        self.erreur: bool = False
        self.dossier_racine: str = "data/sauvegardes"
        self.format_date: str = "%Y-%m-%d"
        self.dossier: str = self.dossier_racine + "/" + self.date_sauvegarde.strftime(self.format_date)
        self.__erreur_chargement: bool = False
        self.__save_en_cours: str | None = None

    @property
    def erreur_chargement(self) -> bool:
        return self.__erreur_chargement

    @property
    def save_en_cours(self) -> str | None:
        return self.__save_en_cours

    # Les 4 méthodes qui renvoient un dictionnaire ont été développées a l'aide de l'ia Claude Opus 5.5 en effort Moyen.

    def _visiteur_vers_dict(self, visiteur: Visiteur) -> dict: # Pour la méthode suivante, aide de la part de claude opus 5.5 en effort moyen. (Auteur : Louis Degand)
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

    def _type_vers_dict(self, type_objet: TypeObjet) -> dict: # Pour la méthode suivante, aide de la part de claude opus 5.5 en effort moyen. (Auteur : Louis Degand)
        """Convertit un type d'objet en dictionnaire. Ne modifie pas le type."""
        return {
            "categorie": type_objet.categorie,
            "poids_moyen": type_objet.poids_moyen,
        }

    def _reparateur_vers_dict(self, reparateur: Reparateur) -> dict: # Pour la méthode suivante, aide de la part de claude opus 5.5 en effort moyen. (Auteur : Louis Degand)
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

    def _dict_fiche_vers_fiche(self, valeurs: dict) -> Fiche:
        """Transforme un dictionnaire dont les clés correspondent aux attributs de création d'une Fiche en Fiche.
        Lève les exceptions de la classe Fiche si la création ne fonctionne pas.
        """
        num = valeurs["id"]

        donnees_visiteur = dict(valeurs["visiteur"])
        donnees_visiteur["derniere_visite"] = datetime.fromisoformat(donnees_visiteur["derniere_visite"])
        visiteur = Visiteur(**donnees_visiteur)

        type_objet = TypeObjet(**valeurs["type_objet"])
        description_panne = valeurs["description_panne"]
        marque = valeurs["marque"]

        reparateur = None
        if valeurs["reparateur"]:
            reparateur = Reparateur(**valeurs["reparateur"])

        etat = Etat[valeurs["etat"]]

        resultat = None
        if valeurs["resultat"]:
            resultat = Resultat[valeurs["resultat"]]

        diagnostic = valeurs["diagnostic"]
        date_arrivee = datetime.fromisoformat(valeurs["date_arrivee"])

        return Fiche(num,
                     visiteur,
                     type_objet,
                     description_panne,
                     marque,
                     date_arrivee,
                     reparateur,
                     etat,
                     resultat,
                     diagnostic
                     )

    def _lister_sauvegardes(self) -> list[str]:
        """Renvoie les sauvegardes existantes de la plus récente à la plus ancienne.
        Renvoie une liste vide s'il n'y a pas de sauvegarde.
        Ne modifie rien.
        """
        try:
            noms = os.listdir(self.dossier_racine)
        except OSError:
            return []
        sauvegardes = []
        for nom in noms:
            if os.path.isfile(os.path.join(self.dossier_racine, nom, "fiches.json")):
                sauvegardes.append(nom)
        return sorted(sauvegardes, reverse=True)

    def _supprimer_dossier(self, chemin: str) -> None:
        """Supprime un dossier de sauvegarde et les fichiers qu'il contient.
        PRE : chemin désigne un dossier qui ne contient que des fichiers (pas de sous-dossiers).
        POST : le dossier et tous ses fichiers n'existent plus.
        Exceptions : OSError si un fichier ou le dossier ne peut pas être supprimé.
        """
        for nom_fichier in os.listdir(chemin):
            os.remove(os.path.join(chemin, nom_fichier))
        os.rmdir(chemin)

    def creer_dossier(self) -> None:
        """Crée le dossier de la sauvegarde du jour.
        PRE : aucune.
        POST : le dossier self.dossier et le dossier sauvegardes qui le contient existent.
        Rien ne change s'ils existaient déjà. Si la création échoue, self.erreur vaut True.
        """
        try:
            os.makedirs(self.dossier, exist_ok=True)
        except OSError:
            self.erreur = True

    def copie(self, fiche: Fiche) -> None:
        """Ajoute une copie de la fiche dans le fichier fiches.json de la sauvegarde en cours.
        PRE : creer_dossier a été appelée et le dossier de sauvegarde a été créé.
        POST : la fiche est ajoutée sous forme de dictionnaire à la liste de fiches.json, la fiche n'est pas modifiée.
        Exceptions : TypeError si fiche n'est pas de type Fiche.
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

    def sauver_fiche(self, fiche: Fiche) -> None: # Pour la méthode suivante, aide de la part de claude opus 5.5 en effort moyen. (Auteur : Louis Degand)
        """Enregistre la fiche dans le fichier fiches.json de la sauvegarde en cours.
        PRE : chargement a été appelée et a préparé la sauvegarde du jour.
        POST : fiches.json contient la fiche une seule fois, dans sa version la plus récente :
        elle remplace la fiche de même id si elle existait, sinon elle est ajoutée à la fin.
        La fiche n'est pas modifiée. Si l'écriture échoue, self.erreur vaut True.
        Exceptions : TypeError si fiche n'est pas de type Fiche.
        RuntimeError s'il n'y a pas de sauvegarde en cours.
        """
        if not isinstance(fiche, Fiche):
            raise TypeError("Le paramètre fiche n'est pas de Type Fiche")
        if self.__save_en_cours is None:
            raise RuntimeError("Aucune sauvegarde en cours : appeler chargement d'abord")

        chemin = os.path.join(self.__save_en_cours, "fiches.json")

        try:
            with open(chemin, "r", encoding="utf-8") as f:
                fiches = json.load(f)
        except FileNotFoundError:
            fiches = []

        nouvelle = self._fiche_vers_dict(fiche)
        for i, existante in enumerate(fiches):
            if existante["id"] == nouvelle["id"]:
                fiches[i] = nouvelle
                break
        else:
            fiches.append(nouvelle)

        try:
            with open(chemin, "w", encoding="utf-8") as f:
                json.dump(fiches, f, indent=2, ensure_ascii=False)
        except OSError:
            self.erreur = True

    def copie_visiteurs(self, visiteur: Visiteur) -> None:
        """Ajoute une copie du visiteur dans le fichier visiteurs.json de la sauvegarde en cours.
        PRE : creer_dossier a été appelée et le dossier de sauvegarde a été créé.
        POST : le visiteur est ajouté sous forme de dictionnaire à la liste de visiteurs.json, le visiteur n'est pas modifié.
        Exceptions : TypeError si visiteur n'est pas de type Visiteur.
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
        """Ajoute une copie du type d'objet dans le fichier types.json de la sauvegarde en cours.
        PRE : creer_dossier a été appelée et le dossier de sauvegarde a été créé.
        POST : le type est ajouté sous forme de dictionnaire à la liste de types.json, le type n'est pas modifié.
        Exceptions : TypeError si type_objet n'est pas de type TypeObjet.
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
        """Ajoute une copie du réparateur dans le fichier reparateurs.json de la sauvegarde en cours.
        PRE : creer_dossier a été appelée et le dossier de sauvegarde a été créé.
        POST : le réparateur est ajouté sous forme de dictionnaire à la liste de reparateurs.json, le réparateur n'est pas modifié.
        Exceptions : TypeError si reparateur n'est pas de type Reparateur.
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

    # À décommenter une fois la classe RapportCommune créée :
    # def copie_rapport(self, rapport: RapportCommune) -> None:
    #     """
    #     """
    #     return None

    def chargement(self) -> tuple[int, list[Fiche]]: # Pour la méthode suivante, aide de la part de claude opus 5.5 en effort moyen. (Auteur : Louis Degand)
        """Charge les fiches à reprendre et prépare la sauvegarde du jour.
        PRE : aucune.
        POST : le dossier racine et le dossier de sauvegarde du jour existent, et __save_en_cours contient le chemin de ce dernier.
        Si le dossier du jour contenait déjà une sauvegarde lisible, les fiches sont chargées depuis celle-ci.
        Sinon, elles sont chargées depuis la sauvegarde lisible la plus récente, dont tous les fichiers sont recopiés dans le dossier du jour.
        S'il n'existe aucune sauvegarde lisible, le dossier du jour reçoit un fiches.json vide.
        Renvoie (id max, liste des fiches non terminées ou à suivre), ou (0, []) si aucune sauvegarde n'est lisible.
        __erreur_chargement vaut True si au moins une sauvegarde n'a pas pu être lue.
        Si un dossier ou un fichier ne peut pas être créé, self.erreur vaut True et __save_en_cours vaut None.
        """
        self.__erreur_chargement = False
        self.__save_en_cours = None

        self.creer_dossier()
        if self.erreur:
            return 0, []

        for sauvegarde in self._lister_sauvegardes():
            dossier = os.path.join(self.dossier_racine, sauvegarde)
            chemin = os.path.join(dossier, "fiches.json")
            try:
                with open(chemin, encoding="utf-8") as fichier:
                    donnees = json.load(fichier)
                liste_fiches = []
                max_id = 0
                for donnee in donnees:
                    if donnee["id"] > max_id:
                        max_id = donnee["id"]
                    if (donnee["etat"] != Etat.TERMINE.name
                            or donnee["resultat"] == Resultat.A_SUIVRE.name):
                        liste_fiches.append(self._dict_fiche_vers_fiche(donnee))
            except Exception:
                self.__erreur_chargement = True
                continue

            # Première ouverture du jour : le dossier du jour doit être complet dès sa création
            if os.path.normpath(dossier) != os.path.normpath(self.dossier):
                try:
                    for nom_fichier in os.listdir(dossier):
                        if nom_fichier.endswith(".json"):
                            with open(os.path.join(dossier, nom_fichier), encoding="utf-8") as source:
                                contenu = source.read()
                            with open(os.path.join(self.dossier, nom_fichier), "w", encoding="utf-8") as copie:
                                copie.write(contenu)
                except OSError:
                    self.erreur = True
                    return max_id, liste_fiches

            self.__save_en_cours = self.dossier
            return max_id, liste_fiches

        try:
            with open(os.path.join(self.dossier, "fiches.json"), "w", encoding="utf-8") as f:
                json.dump([], f)
        except OSError:
            self.erreur = True
            return 0, []

        self.__save_en_cours = self.dossier
        return 0, []

    def restauration(self, date: datetime) -> str:
        """
        """
        return None

    def suppression_automatique(self) -> None:
        """Supprime les sauvegardes trop anciennes ou en trop.
        PRE : aucune.
        POST : il reste au maximum 10 sauvegardes (une par jour) dans dossier_racine, et aucune n'a
        plus de 365 jours par rapport à date_sauvegarde. Les plus anciennes ont été supprimées.
        Les dossiers dont le nom n'est pas une date sont ignorés.
        Si une suppression échoue, self.erreur vaut True.
        """
        try:
            saves = sorted(os.listdir(self.dossier_racine))

            # EF-08.7 : aucune sauvegarde de plus de 365 jours
            for nom in saves[:]:
                try:
                    date = datetime.strptime(nom, self.format_date)
                except ValueError:
                    saves.remove(nom)   # dossier qui n'est pas une sauvegarde : on l'ignore
                    continue
                if self.date_sauvegarde - date > timedelta(days=365):
                    self._supprimer_dossier(os.path.join(self.dossier_racine, nom))
                    saves.remove(nom)

            # EF-08.4 : 10 sauvegardes maximum, on supprime les plus anciennes
            while len(saves) > 10:
                plus_ancienne = saves.pop(0)
                self._supprimer_dossier(os.path.join(self.dossier_racine, plus_ancienne))

        except OSError:
            self.erreur = True


#CODE DE TEST GENERE PAR CLAUDE
if __name__ == "__main__":
    """
    # ---------- Test 1 : création du dossier et copies ----------
    test = Sauvegarde()
    test.creer_dossier()
    print("Dossier :", test.dossier)
    print("Erreur :", test.erreur)

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
    print("Copies terminées, vérifie le dossier", test.dossier)

    # ---------- Test 2 : suppression automatique ----------
    # On travaille dans un dossier à part pour ne pas toucher aux vraies sauvegardes.
    test_suppr = Sauvegarde()
    test.chargement()
    test_suppr.dossier_racine = "data/sauvegardes_test"

    # On repart de zéro : on vide le dossier de test s'il existe déjà
    if os.path.exists(test_suppr.dossier_racine):
        for nom in os.listdir(test_suppr.dossier_racine):
            test_suppr._supprimer_dossier(os.path.join(test_suppr.dossier_racine, nom))

    # 12 sauvegardes récentes (du 1er au 12 novembre 2026)
    for jour in range(1, 13):
        os.makedirs(f"{test_suppr.dossier_racine}/2026-11-{jour:02d}")
    # 1 sauvegarde de plus de 365 jours
    os.makedirs(f"{test_suppr.dossier_racine}/2025-01-01")
    # 1 dossier qui n'est pas une sauvegarde
    os.makedirs(f"{test_suppr.dossier_racine}/pas_une_date")

    print("\nAvant suppression :", sorted(os.listdir(test_suppr.dossier_racine)))
    test_suppr.suppression_automatique()
    restants = sorted(os.listdir(test_suppr.dossier_racine))
    print("Après suppression :", restants)

    # Vérifications
    print("Plus de sauvegarde de 2025 :", "2025-01-01" not in restants)
    print("Les 2 plus anciennes supprimées :",
          "2026-11-01" not in restants and "2026-11-02" not in restants)
    print("10 sauvegardes restantes :", len(restants) - 1 == 10)   # -1 pour "pas_une_date"
    print("Dossier étranger conservé :", "pas_une_date" in restants)
    print("Erreur :", test_suppr.erreur)
    """

    # ---------- Test 3 : chargement et sauver_fiche ----------
    test = Sauvegarde()
    max_id, fiches = test.chargement()
    print("Sauvegarde en cours :", test.save_en_cours)
    print("Id max :", max_id, "- fiches chargées :", len(fiches))

    nouvelle = Fiche(
        max_id + 1,
        Visiteur(max_id + 1, "Dupont", "Léa", None, None, False),
        TypeObjet("bouilloire", 1.0),
        "Ne s'arrête plus",
    )
    test.sauver_fiche(nouvelle)
    test.sauver_fiche(nouvelle)   # deuxième fois : doit remplacer, pas dupliquer

    with open(os.path.join(test.save_en_cours, "fiches.json"), encoding="utf-8") as f:
        ids = [d["id"] for d in json.load(f)]
    print("La fiche n'apparaît qu'une fois :", ids.count(nouvelle.id) == 1)
    print("Erreur :", test.erreur, "- erreur de chargement :", test.erreur_chargement)