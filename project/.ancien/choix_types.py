# Affiche la liste des types et renvoie celui choisi (EF-01.2 : pas de saisie libre)
def choix_type(types):
    print()
    print("Veuillez choisir un type :")
    print()
    for numero, type_objet in enumerate(types, start=1):
        print(f"{numero} : {type_objet}")
    print()

    while True:
        reponse = input("Veuillez entrer le numéro correspondant : ").strip()
        if reponse.isdigit() and 1 <= int(reponse) <= len(types):
            return types[int(reponse) - 1]
        print(f"Choix invalide, entrez un nombre entre 1 et {len(types)}.")