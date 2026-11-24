from domaine.fiche import Fiche
from domaine.enums import Etat, Resultat
from domaine.registre import RegistreFiches
from domaine.reparateur import Reparateur
from domaine.type_objet import TypeObjet
from domaine.visiteur import Visiteur
from data.sauvegarde import Sauvegarde

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
    choisir_fonctionnalites()