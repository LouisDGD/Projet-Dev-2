from domaine.registre import RegistreFiches
from domaine.reparateur import Reparateur
from domaine.fiche import Fiche
from domaine.type_objet import TypeObjet
from domaine.visiteur import Visiteur
from datetime import datetime
from domaine.enums import Etat, Resultat
from data.sauvegarde import Sauvegarde
import interface.tui_simple as tui_simple

def initialister(liste_reparateur: list, liste_visiteur: list, liste_type_objet: list, liste_fiche: list, id_fiche: int):
    reparateurs_donnees = [['THIEL', 'Valentin', 'Grille-pain'], ['DEGAND', 'Louis', 'Ecran d\'ordinateur'], ['MARTIN', 'Loic', 'Ninja Creamy']]
    type_objet_donnees = [['Grille-pain', 1.5], ['Ecran d\'ordinateur', 0.5], ['Ninja Creamy', float(4)]]
    visiteurs_donnees = [[1, 'DERICK', 'Maxime', None, None, False], [2, 'DUBRUILLE', 'Xavier', None, None, False], [3, 'KABASELE', 'Greg', None, None, False]]
    fiches_donnees = [
        [20, 0, 0, "Ne chauffe plus d'un côté", datetime(2026, 11, 14, 14, 30), Etat.EN_ATTENTE, None, None, None],
        [30, 1, 1, "Écran noir au démarrage", datetime(2026, 11, 14, 14, 5), Etat.EN_COURS, 1, None, None],
        [40, 2, 2, "Le moteur ne tourne plus", datetime(2026, 11, 14, 14, 15), Etat.TERMINE, 2, "Courroie remplacée", Resultat.REPARE],
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
    
def main():
    '''Creation de l'environnement nécessaire pour le MVP : le registre, les réparateurs et visiteurs et les types d'objets hardcodes (fonctionnalites ulterieure)'''
    demarrage = Sauvegarde()
    etat_initial = demarrage.chargement()
    id_max = etat_initial[0] + 1
    id_max_visiteur = etat_initial[1] + 1
    registre = RegistreFiches(etat_initial[2])
    liste_reparateur = []
    liste_visiteur = []
    liste_type_objet = []
    liste_fiche = []
    id_max = initialister(liste_reparateur, liste_visiteur, liste_type_objet, liste_fiche, id_max)
    for fiche in liste_fiche:
        registre.ajout_file_attente(fiche)
    #TODO creer deux trois fiches
    
    tui_simple.lancer()
    '''boucle principale'''
    while True:

        entree = tui_simple.choisir_fonctionnalites()

        #menu principal des fonctionnalités
        match entree:
            case "0":
                print("Merci et au revoir !")
                #quitter la boucle
                break
        #F-01
            case "1": #F-01 A remplacer plus tard dans le domaine par une unique methode qui contient toutes les méthodes suivantes
                liste_visiteur = []
                for f in registre.fiches_par_ordre_arrivee():
                    liste_visiteur.append(f.visiteur)
                visiteur = tui_simple.choisir_visiteur(liste_visiteur)
                if not visiteur:
                    visiteur = Visiteur(id=id_max_visiteur, **tui_simple.demander_infos_creation_visiteur())
                    id_max_visiteur += 1
                type_objet = tui_simple.choisir_type_objet(liste_type_objet)
                panne = tui_simple.demander_panne()
                marque = tui_simple.demander_marque()
                fiche = Fiche(
                    id=id_max,
                    visiteur=visiteur,
                    type_objet=type_objet,
                    description_panne=panne,
                    marque=marque,
                )
                id_max += 1
                registre.ajout_file_attente(fiche)
                demarrage.sauver_fiche(fiche)
                tui_simple.afficher_fiche_ajoutee(fiche)

            case "2": #F-02
                if not len(liste_reparateur):
                    print("Aucun réparateur existe, contactez la coordinatrice.")
                    continue
                print("Voici la liste des réparateurs : \n")
                ordre = 1
                reparateur = None
                for r in liste_reparateur:
                    print(f"ID : {ordre}\n {r.nom} {r.prenom}\n")
                    ordre += 1
                while True:
                    reparateur_input = input("Entrez votre ID\n >>")
                    if reparateur_input.strip() in ("1", "2", "3"):
                            reparateur = liste_reparateur[int(reparateur_input) - 1]
                            break
                
                print(f"\nVous avez choisi : {reparateur.nom} {reparateur.prenom} \n")

                print("\nVoici la liste des fiches triée par ordre chronologique\n")
                fiche = tui_simple.choisir_fiche(registre, "Entrez l'ID de la fiche que vous voulez prendre en charge\n >> ")
                try:
                    fiche.prendre_en_charge(reparateur)
                    demarrage.sauver_fiche(fiche)
                    print("\nVous avez bien été assigné à cette fiche.\n")
                    tui_simple.afficher_infos_fiche(fiche)
                except ValueError as erreur:
                    print(f"\n{erreur}\n")
        
            case "3": #F-03
                print("Voici la liste des fiches disponibles : \n")
                choix_fiche = tui_simple.choisir_fiche(registre, "Entrez l'ID de la fiche que vous voulez compléter\n >> ")

                choix_action = input("Quelle action voulez-vous effectuer sur cette fiche ?\n1)Modifier le diagnostic\n2)Modifier le resultat\n>> ")   
                if choix_action.strip() in ("1", "2"):
                    #modification du diagnostic
                    if choix_action == "1":
                        diagnostic = tui_simple.demander_texte("Entrez le nouveau diagnostic.\n >> ")
                        choix_fiche.modifier_diagnostic(diagnostic)
                        demarrage.sauver_fiche(choix_fiche)
                        print(f"Le diagnostic a bien été modifié.\nLe nouveau diagnostic est : {diagnostic}\n")
                    #modification du resultat
                    elif choix_action == "2":
                        nouveau_resultat = tui_simple.choisir_resultat()
                        try:
                            choix_fiche.modifier_resultat(nouveau_resultat)
                            print(f"Le résultat a bien été modifié. Le nouveau résultat est {nouveau_resultat.value}.\n")
                            demarrage.sauver_fiche(choix_fiche)
                        except ValueError as erreur:
                            print(f"\n{erreur}\n")

            case "4": #afficher les fiches de la session
                print("Fonctionnalité à venir.")

if __name__ == "__main__":
    main()