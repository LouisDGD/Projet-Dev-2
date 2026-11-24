from domaine.fiche import Fiche
from domaine.enums import Etat, Resultat
from domaine.registre import RegistreFiches
from domaine.reparateur import Reparateur
from domaine.type_objet import TypeObjet
from domaine.visiteur import Visiteur
from data.sauvegarde import Sauvegarde
from datetime import datetime

FORMAT_HORODATAGE = "%d/%m/%Y %H:%M:%S"
def demander_texte(message_input: str) -> str:
    """Valide si l'input n'est pas vide ou composé uniquement d'espace. Affiche 'Choix Invalide : votre choix est vide ou composé uniquement d'espaces.'
    Exception si message_input est vide ou composé uniquement d'espace"""
    if not isinstance(message_input, str):
        raise TypeError("Param doit être un str")
    if not message_input.strip():
        raise ValueError("Param est vide ou composé uniquement d'espace")
    while True:
        reponse = input(message_input).strip()
        if reponse:
            return reponse
        print("Choix Invalide : votre choix est vide ou composé uniquement d'espaces.")

def afficher_tableau_listes(fiches: list[Fiche]) -> None:
    """affiche un tableau affichant les listes une à une"""
    LONGUEUR_FENETRE = 90
    print(f"{'N°':^6} | {'Heure':^5} | {'Visiteur':^17} | {'Objet':^20} | {'Statut':^12} | {'Réparateur':^17}")
    print("-" * LONGUEUR_FENETRE)
    for f in fiches:
        afficher_infos_fiche(f)

def afficher_infos_fiche(fiche: Fiche) -> None:
    """print la fiche donné en paramètre"""
    print(f"{fiche.id:>6} | {fiche.date_arrivee:%H:%M} | {get_infos_visiteur(fiche.visiteur):<17.17} | "
            f"{fiche.type_objet.categorie:<20.20} | {fiche.etat.value:<12.12} | {get_infos_reparateur(fiche.reparateur):<17.17}")

def get_infos_visiteur(visiteur: Visiteur) -> str:
    """return le visiteur donné en paramètre"""
    return f"{visiteur.nom_visiteur} {visiteur.prenom_visiteur}"

def afficher_infos_typeobjet(typeobjet: TypeObjet) -> None:
    """print le TypeObjet donné en paramètre"""
    pass

def get_infos_reparateur(reparateur: Reparateur) -> str:
    """return le reparateur donné en paramètre"""
    return f"{reparateur.prenom} {reparateur.nom}" if reparateur else "-"


#TODO
def choisir_fonctionnalites() -> str:
    print("Voici la liste des fonctionnalités qui sont disponibles")
    while True:
        print("\n  1) Enregistrer un objet\n  2) Prendre en charge\n  3) Compléter une fiche\n  4) Afficher les fiches de cette session\n  0) Quitter\n")
        choix = input('Veuillez entrer le chiffre de la fonctionnalité.\n  Exemple : Si vous voulez compléter une fiche, entrez uniquement 3 ').strip()
        if choix in ("0", "1", "2", "3", "4"):
            return choix
        print("Votre réponse ne correspond à aucune fonctionnalité.")

#TODO
def lancer() -> None:
    print("Bienvenue dans")
    print("REPAIR CAFÉ MANAGER : La Clé à Molette à Forest")

if __name__ == "__main__":
    #choisir_fonctionnalites()
    registre = RegistreFiches()
    liste_reparateur = []
    liste_visiteur = []
    liste_type_objet = []
    liste_fiche = []
    id_fiche = 1
    def initialister(liste_reparateur: list, liste_visiteur: list, liste_type_objet: list, liste_fiche: list, id_fiche: int):
        reparateurs_donnees = [['THIEL', 'Valentin', 'Grille-pain'], ['DEGAND', 'Louis', 'Ecran d\'ordinateur'], ['MARTIN', 'Loic', 'Ninja Creamy']]
        type_objet_donnees = [['Grille-pain', 1.5], ['Ecran d\'ordinateur', 0.5], ['Ninja Creamy', float(4)]]
        visiteurs_donnees = [[1, 'DERICK', 'Maxime', None, None, False], [2, 'DUBRUILLE', 'Xavier', None, None, False], [3, 'KABASELE', 'Greg', None, None, False]]
        fiches_donnees = [
            [1, 0, 0, "Ne chauffe plus d'un côté", datetime(2026, 11, 14, 14, 30), Etat.EN_ATTENTE, None, None, None],
            [2, 1, 1, "Écran noir au démarrage", datetime(2026, 11, 14, 14, 5), Etat.EN_COURS, 1, None, None],
            [3, 2, 2, "Le moteur ne tourne plus", datetime(2026, 11, 14, 14, 15), Etat.TERMINE, 2, "Courroie remplacée", Resultat.REPARE],
        ]

        for nom, prenom, specialite in reparateurs_donnees:
            liste_reparateur.append(Reparateur(nom, prenom, specialite))
        for id, nom, prenom, num, email, accord in visiteurs_donnees:
                liste_visiteur.append(Visiteur(id, nom, prenom, num, email, accord))
        for categorie, poids in type_objet_donnees:
            liste_type_objet.append(TypeObjet(categorie, poids))
        for id_fiche, i_visiteur, i_type, description, date, etat, i_reparateur, diagnostic, resultat in fiches_donnees:
            reparateur = liste_reparateur[i_reparateur] if i_reparateur is not None else None
            liste_fiche.append(Fiche(
                id=id_fiche,
                visiteur=liste_visiteur[i_visiteur],
                type_objet=liste_type_objet[i_type],
                description_panne=description,
                date_arrivee=date,
                etat=etat,
                reparateur=reparateur,
                diagnostic=diagnostic,
                resultat=resultat,
            ))
            id_fiche +=1
        return id_fiche
    id_fiche = initialister(liste_reparateur, liste_visiteur, liste_type_objet, liste_fiche, id_fiche)
    afficher_tableau_listes(liste_fiche)
