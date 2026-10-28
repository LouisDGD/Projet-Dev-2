import json
from datetime import datetime

types = ["Grilles-Pain", "Lampe", "Aspirateur", "Téléviseur", "Micro-Ondes", "Ordinateur", "Autre"]
id = 0

#F01 - Enregistrer les infos d'un objet a l'accueil
def creer_fiche():
    #structure par défaut d'une fiche
    client = { 
        "id": 1 , #Valeur fixe pour l'insant
        "nom_visiteur": str(input("Veuillez entrer le nom du visiteur : ")),
        "type_objet": choix_type(), #fait appel a la fonction de choix de type, qui se base sur la liste types[]
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

# Fonction de choix de type en fonction de la liste types []
def choix_type():
    numValue = int(0)
    print('')
    print("Veuillez choisir un type :")
    print('')
    for i in types: #Itère parmi les éléments de la liste types []
        print(f"{numValue + 1} : {i}")
        numValue = numValue + 1
    print('')
    choix = int(input("Veuillez entrer le numéro correspondant : "))
    return types[choix-1]

# Fonction de sauvegarde, sauvegarde sur le fichier fiches.json qui servira de db et sur le fichier history.json qui servira de db d'historique
def save(data):
    with open("fiches.json", "r", encoding="utf-8") as file:
        fichier = json.load(file)

    fichier.append(data)

    with open("fiches.json", "w", encoding="utf-8") as file:
        json.dump(fichier, file, indent=4, ensure_ascii=False)
    with open("history.json", "w", encoding="utf-8") as file:
            json.dump(fichier, file, indent=4, ensure_ascii=False)

creer_fiche() #histoire de lancer tout ca hein :) 