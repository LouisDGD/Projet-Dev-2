from domaine.fiche import Fiche
from domaine.enums import Etat, Resultat
from domaine.registre import RegistreFiches
from domaine.reparateur import Reparateur
from domaine.type_objet import TypeObjet
from domaine.visiteur import Visiteur
from data.sauvegarde import Sauvegarde
from datetime import datetime

FORMAT_HORODATAGE = "%d/%m/%Y %H:%M:%S"
LONGUEUR_FENETRE = 90

def demander_texte(message_input: str) -> str:
    """Valide si l'input n'est pas vide ou composé uniquement d'espace. Affiche 'Choix Invalide : votre choix est vide ou composé uniquement d'espaces.'
    Exception si message_input est vide ou composé uniquement d'espace"""
    if not isinstance(message_input, str):
        raise TypeError("Param doit être un str")
    if not message_input.strip():
        raise ValueError("Param est vide ou composé uniquement d'espace")
    while True:
        reponse = input(message_input + "\n >> ").strip()
        if reponse:
            return reponse
        print("Entrée Invalide : votre choix est vide ou composé uniquement d'espaces.")

def demander_une_fiche(liste_fiches: list[Fiche]) -> None:
    while True:
        filtre = demander_texte("\nRechercher vous les objets uniquement avec le statut à suivre ?\n Entrer \"Oui\" ou \"Non\".\n Entrer 0 si vous voulez revenir au menu précédent.\n").strip().lower()
        if filtre == "0":
            return
        trouvees = []
        if filtre == "oui":
            trouvees = recherche_fiche(True, liste_fiches)
            if not trouvees:
                print("\nAucune fiche ne correspond à ce nom.")
                continue
            afficher_tableau_listes(trouvees)
        elif filtre == "non":
            trouvees = recherche_fiche(False, liste_fiches)
            if not trouvees:
                print("\nAucune fiche ne correspond à ce nom.")
                continue
            afficher_tableau_listes(trouvees)
        if trouvees:
            return trouvees

def recherche_fiche(filtre: bool, liste_fiches: list[Fiche]) -> list[Fiche]:
    choix = demander_texte("\nEntrer le nom et le prénom de la personne.\nExemple : Dubois Anne\n Entrer 0 si vous voulez revenir au menu précédent.\n").strip()
    correspondantes = []
    if filtre:
        for f in liste_fiches:
            if f"{f.visiteur.nom_visiteur} {f.visiteur.prenom_visiteur}" == choix and f.resultat == Resultat.A_SUIVRE:
                correspondantes.append(f)
    else:
        for f in liste_fiches:
            if f"{f.visiteur.nom_visiteur} {f.visiteur.prenom_visiteur}" == choix:
                correspondantes.append(f)
    return correspondantes
            
def demander_accord() -> bool:
    print("Le visiteur est-il d'accord de nous donner son adresse mail et/ou son numéro de téléphone s'il faut le recontacter en rapport avec sa réparation ?")
    while True:
        choix = demander_texte("Veuillez entrer \"Oui\" s'il est d'accord et \"Non\" s'il ne l'est pas.").strip().capitalize()
        if choix == "Oui":
            return True
        elif choix == "Non":
            return False
        print("Votre réponse ne correspond ni à Oui, ni à Non")

def demander_infos_creation_visiteur() -> dict:
    infos = {
        "nom_visiteur": demander_texte("Quel est le nom du visiteur ?"),
        "prenom_visiteur": demander_texte("Quel est le prénom du visiteur ?"),
        "accord": demander_accord(),
        "num_tel": None,
        "email": None,
    }
    if infos["accord"]:
        infos["email"] = input("Adresse e-mail (laisser vide si aucune) :\n >> ").strip() or None
        infos["num_tel"] = input("Numéro de téléphone (laisser vide si aucun) :\n >> ").strip() or None
    return infos

def afficher_infos_fiche_reparateur(fiche: Fiche) -> None:
    """print la fiche donné en paramètre"""
    resultat = " - "
    if fiche.resultat:
        resultat = fiche.resultat.value
    diagnostic = " - "
    if fiche.diagnostic:
            diagnostic = fiche.diagnostic
    print(f"{fiche.id:>6} | {fiche.date_arrivee:%H:%M} | {get_infos_visiteur(fiche.visiteur):<17.17} | "
        f"{fiche.type_objet.categorie:<12.12} | {fiche.description_panne:<15.15} | {diagnostic:<15.15} | {fiche.etat.value:<8.8} | {resultat:<8.8} | {get_infos_reparateur(fiche.reparateur):<17.17}")

def afficher_tableau_listes_reparateur(fiches: list[Fiche]) -> None:
    """Affiche la fiche avec le diag et le résultat"""
    print("\n")
    print(f"{'N°':^6} | {'Heure':^5} | {'Visiteur':^17} | {'Objet':^12} | {'Panne':^15} | {'diagnostic':^15} | {'Statut':^8} | {'État':^8} | {'Réparateur':^17}")
    print("-" * 130)
    for f in fiches:
        afficher_infos_fiche_reparateur(f)
    print("\n")

def choisir_fiche_reparateur(registre: RegistreFiches, message: str) -> Fiche:
    afficher_tableau_listes_reparateur(registre.fiches_par_ordre_arrivee())
    while True:
        choix = demander_texte(message)
        try:
            fiche = registre.trouver_par_id(int(choix))
        except ValueError:
            fiche = None
        if fiche:
            return fiche
        print("Cette fiche n'existe pas. Veuillez réessayer.")

def afficher_tableau_listes(fiches: list[Fiche]) -> None:
    """affiche un tableau affichant les listes une à une"""
    print("\n")
    print(f"{'N°':^6} | {'Heure':^5} | {'Visiteur':^17} | {'Objet':^20} | {'Statut':^12} | {'Réparateur':^17}")
    print("-" * LONGUEUR_FENETRE)
    for f in fiches:
        afficher_infos_fiche(f)
    print("\n")

def afficher_infos_fiche(fiche: Fiche) -> None:
    """print la fiche donné en paramètre"""
    print(f"{fiche.id:>6} | {fiche.date_arrivee:%H:%M} | {get_infos_visiteur(fiche.visiteur):<17.17} | "
            f"{fiche.type_objet.categorie:<20.20} | {fiche.etat.value:<12.12} | {get_infos_reparateur(fiche.reparateur):<17.17}")

def get_infos_visiteur(visiteur: Visiteur) -> str:
    """return le visiteur donné en paramètre"""
    return f"{visiteur.nom_visiteur} {visiteur.prenom_visiteur}"

def afficher_tableau_visiteurs(visiteurs: list[Visiteur]) -> None:
    deja_print = []
    """Affi(éche l'en-tête une seule fois, puis une ligne par visiteur."""
    print(f"{'N°':^6} | {'Nom':^20} | {'Prénom':^20}")
    print("-" * LONGUEUR_FENETRE)
    for v in visiteurs:
        if v.id not in deja_print:
            afficher_infos_visiteur(v)
            deja_print.append(v.id)

def afficher_infos_visiteur(visiteur: Visiteur) -> None:
    "Affiche les informations du visiteurs"
    print(f"{visiteur.id:>6} | {visiteur.nom_visiteur:<20.20} | {visiteur.prenom_visiteur:<20.20}")


def get_infos_typeobjet(typeobjet: TypeObjet) -> str:
    """print le TypeObjet donné en paramètre"""
    return f"{typeobjet.categorie} - {typeobjet.poids_moyen}"


def get_infos_reparateur(reparateur: Reparateur) -> str:
    """return le reparateur donné en paramètre"""
    return f"{reparateur.prenom} {reparateur.nom}" if reparateur else "-"


#TODO
def choisir_fonctionnalites() -> str:
    CHOIX_AUTORISES = ("0", "1", "2", "3", "4", "5", "6")
    print("\nVoici la liste des fonctionnalités qui sont disponibles")
    while True:
        print("\n  1) Enregistrer un objet\n  2) Prendre en charge\n  3) Compléter une fiche\n  4) Afficher les fiches de cette session\n  5) Rechercher la fiche d'un visiteur\n  6) Restaurer une sauvegarde\n  0) Quitter\n")
        choix = demander_texte('Veuillez entrer le chiffre de la fonctionnalité.\n  Exemple : Si vous voulez compléter une fiche, entrez uniquement 3\n').strip()
        if choix in CHOIX_AUTORISES:
            return choix
        print("Votre réponse ne correspond à aucune fonctionnalité.")

#TODO
def lancer() -> None:
    print("Bienvenue dans")
    print("REPAIR CAFÉ MANAGER : La Clé à Molette à Forest")

def choisir_fiche(registre: RegistreFiches, message: str) -> Fiche:
    afficher_tableau_listes(registre.fiches_par_ordre_arrivee())
    while True:
        choix = demander_texte(message)
        try:
            fiche = registre.trouver_par_id(int(choix))
        except ValueError:
            fiche = None
        if fiche:
            return fiche
        print("Cette fiche n'existe pas. Veuillez réessayer.")

def choisir_resultat() -> Resultat:
    while True:
        print("1) Réparé\n2) Non réparable\n3) A suivre")
        choix = demander_texte("Entrez le numéro du résultat.\n >> ")
        if choix == "1":
            return Resultat.REPARE
        if choix == "2":
            return Resultat.NON_REPARABLE
        if choix == "3":
            return Resultat.A_SUIVRE
        print("Ce choix ne correspond à aucun résultat. Veuillez réessayer.")

def demander_reparateur(registre: RegistreFiches) -> Reparateur | None:
    """Demande au réparateur son nom, son prénom et sa spécialité.
    Renvoie None s'il a déjà une fiche en cours.
    """
    nom = demander_texte("Entrez votre nom.")
    prenom = demander_texte("Entrez votre prénom.")
    specialite = demander_texte("Entrez votre spécialité.")
    reparateur = Reparateur(nom, prenom, specialite)
    print(f"\nVous êtes : {get_infos_reparateur(reparateur)}\n")
    for f in registre.fiches_par_ordre_arrivee():
        if f.etat == Etat.EN_COURS and f.reparateur is not None:
            if f.reparateur.nom.lower() == nom.lower() and f.reparateur.prenom.lower() == prenom.lower():
                print(f"Vous avez déjà la fiche n°{f.id} en cours. Terminez-la avant d'en prendre une autre.\n")
                return None
    return reparateur

def afficher_prise_en_charge(fiche: Fiche) -> None:
    """Confirme la prise en charge et affiche la fiche."""
    print("\nVous avez bien été assigné à cette fiche.\n")
    afficher_infos_fiche(fiche)

def afficher_erreur(erreur: Exception) -> None:
    """Affiche le message d'une erreur."""
    print(f"\n{erreur}\n")

def choisir_visiteur(visiteurs: list[Visiteur]) -> Visiteur | None:
    """Affiche les visiteurs et demande d'en choisir un par son id.
    Redemande tant que l'id ne correspond à aucun visiteur.
    """
    print("Voici la liste des visiteurs enregistrés :\n")
    afficher_tableau_visiteurs(visiteurs)
    while True:
        choix = demander_texte("\nQui est le propriétaire de l'objet ? Entrez son id.\nEntrez 0 si le visiteur n'est pas déjà connu.")
        if choix == "0":
            print("Le visiteur n'existe pas encore.")
            return None
        for v in visiteurs:
            if str(v.id) == choix:
                print(f"Vous avez choisi : {get_infos_visiteur(v)}\n")
                return v
                
        print("Aucun visiteur ne correspond a cet ID. Veuillez réessayer.")

def choisir_type_objet(types_objet: list[TypeObjet]) -> TypeObjet:
    """Affiche les types d'objet et demande d'en choisir un par son nom.
    Redemande tant que le nom ne correspond à aucun type.
    """
    while True:
        print("Types d'objet disponibles :")
        for t in types_objet:
            print(f"{t.categorie}")
        choix = demander_texte("Quel est le type de l'objet ? Entrez un des types affichés.")
        for t in types_objet:
            if t.categorie == choix:
                print("Le type de l'objet a été ajouté.\n")
                return t
        print("Ce type n'existe pas. Veuillez réessayer.\n")

def demander_panne() -> str:
    """Demande la description de la panne, puis une confirmation.
    Redemande tant que le bénévole n'a pas validé sa description.
    """
    while True:
        panne = demander_texte("Veuillez décrire la panne.")
        reponse = input(f"Vous avez écrit :\n {panne}\n Entrez [Y] si vous êtes d'accord avec votre entrée.\n Entrez [N] si vous voulez recommencer\n >> ")
        if reponse.strip().lower() == "n":
            continue
        print("La description de la panne a été ajoutée.\n")
        return panne

def demander_marque() -> str | None:
    """Demande la marque de l'objet, puis une confirmation.
    """
    while True:
        marque = input("Veuillez décrire la marque. Si vous ne la connaissez pas, n'entrez rien\n >> ").strip()
        reponse = input(f"Vous avez écrit :\n {marque}\n Entrez [Y] si vous êtes d'accord avec votre entrée.\n Entrez [N] si vous voulez recommencer\n >> ")
        if reponse.strip().lower() == "n":
            continue
        print("La marque a été ajoutée.\n")
        return marque or None
def afficher_fiche_ajoutee(fiche: Fiche) -> None:
    """Message de confirmation d'ajou d'une fiche a la liste"""
    print(f"Ajout de la fiche n°{fiche.id}. Merci de votre coopération.\n")
    afficher_infos_fiche(fiche)

def choisir_sauvegarde(sauvegardes: list[str]) -> str | None:
    """Affiche les sauvegardes numérotées, demande d'en choisir une puis de confirmer l'écrasement.
    Renvoie le nom de la sauvegarde choisie, ou None si l'utilisateur annule.
    """
    print("Sauvegardes disponibles :")
    for numero, nom in enumerate(sauvegardes, 1):
        print(f"{numero}) {nom}")
    print("0) Annuler")
    while True:
        choix = demander_texte("Entrez le numéro de la sauvegarde.")
        if choix == "0":
            return None
        if choix.isdigit() and 1 <= int(choix) <= len(sauvegardes):
            nom = sauvegardes[int(choix) - 1]
            print(f"\nATTENTION : les données d'aujourd'hui vont être remplacées par celles du {nom}.")
            confirmation = demander_texte("Entrez \"Oui\" pour confirmer, ou autre chose pour annuler.").capitalize()
            if confirmation == "Oui":
                return nom
            return None
        print("Ce numéro ne correspond à aucune sauvegarde.")


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
    choisir_fonctionnalites()
