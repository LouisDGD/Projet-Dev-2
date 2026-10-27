import json
from datetime import datetime

id = 0

#F01 - Enregistrer les infos d'un objet a l'accueil
def creer_fiche():
    client = {
        "id": 1,
        "nom_visiteur": str(input("Veuillez entrer le nom du visiteur : ")),
        "type_objet": "A déterminer",
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

def save(data):
    with open("fiches.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

creer_fiche()