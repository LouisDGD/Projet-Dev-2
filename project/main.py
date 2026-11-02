from domaine.registre import RegistreFiches
from domaine.reparateur import Reparateur
from domaine.fiche import Fiche
from domaine.type_objet import TypeObjet
from domaine.visiteur import Visiteur
from datetime import datetime
from domaine.enums import Etat, Resultat


def initialister(liste_reparateur: list, liste_visiteur: list, liste_type_objet: list, liste_fiche: list, id_fiche: int):
    reparateurs_donnees = [['THIEL', 'Valentin', 'Grille-pain'], ['DEGAND', 'Louis', 'Ecran d\'ordinateur'], ['MARTIN', 'Loic', 'Ninja Creamy']]
    type_objet_donnees = [['Grille-pain', 1.5], ['Ecran d\'ordinateur', 0.5], ['Ninja Creamy', 4]]
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

def main():
    '''Creation de l'environnement nécessaire pour le MVP : le registre, les réparateurs et visiteurs et les types d'objets hardcodes (fonctionnalites ulterieure)'''
    registre = RegistreFiches()
    liste_reparateur = []
    liste_visiteur = []
    liste_type_objet = []
    liste_fiche = []
    id_fiche = 1
    id_fiche = initialister(liste_reparateur, liste_visiteur, liste_type_objet, liste_fiche, id_fiche)
    for fiche in liste_fiche:
        registre.ajout_file_attente(fiche)
    #TODO creer deux trois fiches
    
    print('Bienvenue dans ASBL OS !\n Que voulez vous faire?')
    '''boucle principale'''
    while True:
        print('  1) Enregistrer un objet. \n  2) Consulter les donnees d\'une fiche (Reparateur). \n  3) Completer une fiche (Reparateur).\n')
        entree = input('Veuillez entrer le chiffre de la fonctionnalité.\n >> ')

        if entree.strip() not in ("1", "2", "3"): # TODO remplacer par try except
            print("Cette réponse ne correspond à aucune fonctionnalité, veuillez réessayer. \n")
            continue
        
        entree = int(entree)

        #F-01
        if entree == 1:
            fiche = [id_fiche]

            #demande visiteur
            while True:
                '''Verifier que l'input du benevole correspond a un visiteur'''
                print('Voici la liste des visiteurs enregistrés:\n')
                for v in liste_visiteur:
                    print(f"ID:{v.id} - {v.nom_visiteur} {v.prenom_visiteur}")
                print("\n")
                visiteur_input = input('Qui est le proprietaire de l\'objet ? Entrez son id.\n>>')

                if visiteur_input.strip() in ("1", "2", "3"): # TODO remplacer par try except
                    break
                print("Cette réponse ne correspond pas à un visiteur, veuillez réessayer.")

            visiteur_input = int(visiteur_input)
            '''ajout visiteur à la fiche'''
            for v in liste_visiteur:
                if v.id == visiteur_input:
                    fiche.append(v)
                    print("Le visiteur a été ajouté à la fiche.\n")

            #Demande categorie
            while True:
                categories = []
                for t in liste_type_objet:
                    print(f"- {t.categorie}\n")
                    categories.append(t.categorie)
                type_objet_input = input('Quel est le type de l\'objet ? Entrer un des types affichés. >> ').strip()
                if type_objet_input in categories:
                    for t in liste_type_objet:
                        if t.categorie == type_objet_input:
                            fiche.append(t)
                    print("Le type de l'objet a été ajouté. \n")
                    break
                print("\nCe type n'existe pas. Veuillez réessayer.\n")
            
            #Demande panne
            while True:
                panne = input("Veuillez décrire la panne.\n >>").strip()
                if len(panne) == 0:
                    print("\nLa panne ne peut pas être vide\n")
                    continue
                reponse = input(f"Vous avez écrit : \n {panne}\n Entrez [Y] si vous êtes d'accord avec votre entrée. \n Entrez [N] si vous voulez recommencer\n >> ")
                if reponse == "N":
                    continue
                fiche.append(panne)
                print("La description de la panne a été ajoutée. \n")
                break

            #Demande marque
            while True:
                marque = input("Veuillez décrire la marque. Si vous ne la connaissez pas, n'entrez rien\n >> ")
                reponse = input(f"Vous avez écrit : \n {marque}\n Entrez [Y] si vous êtes d'accord avec votre entrée. \n Entrez [N] si vous voulez recommencer\n >> ")
                if reponse == "N":
                    continue
                if marque:
                    fiche.append(marque)
                print("La description de la panne a été ajoutée. \n")
                break
            fiche = Fiche(*fiche)
            print(fiche)
            registre.ajout_file_attente(fiche)
            print("Ajout de la fiche. Merci de votre coopération.\n")

        #F-02
        elif entree == 2:
            if not len(liste_reparateur):
                print("Aucun réparateur existe, contactez la coordinatrice.")
                break
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

            print("\nVoici la liste des fiches triée par ordre chronologique")
            id_fiches= []
            for f in registre.fiches_par_ordre_arrivee():
                id_fiches.append(str(f.id))
                if f.reparateur:
                    identite_reparateur = f"{f.reparateur.nom} {f.reparateur.prenom}"
                else:
                    identite_reparateur = "pas de réparateur"
                print(f"\nFiche ID : {f.id}\n Visiteur : {f.visiteur.nom_visiteur} {f.visiteur.prenom_visiteur}\n Type de l'objet : {f.type_objet.categorie}\n Marque : {f.marque}\n Réparateur : {identite_reparateur} \n Etat : {f.etat.value}\n Résultat : {f.resultat}\n Diagnostic : {f.diagnostic}\n Date d'arrivée : {f.date_arrivee} \n")

            while True:
                choix_fiche = input("Entrez l'ID de la fiche que vous voulez prendre en charge\n >>")
                if choix_fiche.strip() in id_fiches:
                    choix_fiche = int(choix_fiche)
                    for f in registre.fiches_par_ordre_arrivee():
                        if f.id == choix_fiche:
                            if f.reparateur:
                                print("\nCette fiche est déjà prise en charge.\n")
                                break
                            f.prendre_en_charge(reparateur)
                            print("Vous avez bien été assigné à cette fiche. \n")
                            identite_reparateur = f"{f.reparateur.nom} {f.reparateur.prenom}"
                            print(f"\nFiche ID : {f.id}\n Visiteur : {f.visiteur.nom_visiteur} {f.visiteur.prenom_visiteur}\n Type de l'objet : {f.type_objet.categorie}\n Marque : {f.marque}\n Réparateur : {identite_reparateur} \n Etat : {f.etat.value}\n Résultat : {f.resultat}\n Diagnostic : {f.diagnostic}\n Date d'arrivée : {f.date_arrivee} \n")
                    break
                print("\nCette fiche n'est pas disponible ou n'existe pas.\n")



        elif entree == 3:
            #TODO permettre au reparateur de changer diagnostic et resultat de la fiche (check si elle existe d'abord !)
            pass
        



        


if __name__ == "__main__":
    main()