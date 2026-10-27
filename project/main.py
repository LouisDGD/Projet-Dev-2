import json
from datetime import datetime

types = ["Grilles-Pain", "Lampe", "Aspirateur", "Téléviseur", "Micro-Ondes", "Ordinateur", "Autre"]
id = 0

#F01 - Enregistrer les infos d'un objet a l'accueil
def creer_fiche():
    client = {
        "id": 1 , #Valeur fixe pour l'insant
        "nom_visiteur": str(input("Veuillez entrer le nom du visiteur : ")),
        "type_objet": choix_type(),
        "marque": str(input("Nom de la Marque : ")),
        "description": str(input("Description du problème : ")),
        "date_arrivee": datetime.now().isoformat(timespec="seconds"),
        "etat": "en attente",
        "reparateur": None,
        "diagnostic": None,
        "resultat": None,
        "piece_attendue": None
    }

    save(client)

def choix_type():
    print('')
    print("Veuillez choisir un type :")
    print('')
    print("1 : Grilles Pain")
    print("2 : Lampe")
    print("3 : Aspirateur")
    print("4 : Téléviseur")
    print("5 : Micro-Ondes")
    print("6 : Ordinateur")
    print("7 : Autre")
    print('')
    choix = int(input("Veuillez entrer le numéro correspondant : "))

    return types[choix-1]


def save(data):
    with open("fiches.json", "r", encoding="utf-8") as file:
        fichier = json.load(file)

    fichier.append(data)

    with open("fiches.json", "w", encoding="utf-8") as file:
        json.dump(fichier, file, indent=4, ensure_ascii=False)

creer_fiche()