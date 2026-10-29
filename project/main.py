from datetime import datetime

from choix_types import choix_type
from get_id import get_id
from save import save

TYPES = ["Grille-pain", "Lampe", "Aspirateur", "Téléviseur", "Micro-ondes", "Ordinateur", "Autre"]


def demander_non_vide(question):
    #Redemande tant que la réponse est vide.
    reponse = input(question).strip()
    while not reponse:
        print("Ce champ est obligatoire.")
        reponse = input(question).strip()
    return reponse

def nouvelle_fiche(nom_visiteur, type_objet, marque, description):

    return {
        "id": get_id(),
        "nom_visiteur": nom_visiteur,
        "type_objet": type_objet,
        "marque": marque or None,  # facultative
        "description": description,
        "date_arrivee": datetime.now().isoformat(timespec="seconds"),
        "etat": "en attente",
        "reparateur": None,
        "diagnostic": None,
        "resultat": None,
        "piece_attendue": None,
    }

def creer_fiche():
    #F-01 : saisie à l'accueil puis enregistrement.
    fiche = nouvelle_fiche(
        nom_visiteur=demander_non_vide("Nom du visiteur : "),
        type_objet=choix_type(TYPES),
        marque=input("Marque (facultatif) : ").strip(),
        description=demander_non_vide("Description du problème : "),
    )
    save(fiche)
    print(f"\nFiche n°{fiche['id']} enregistrée pour {fiche['nom_visiteur']}.")
    return fiche


if __name__ == "__main__":
    creer_fiche()
