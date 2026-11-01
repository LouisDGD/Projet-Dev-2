from domaine.registre import RegistreFiches
from domaine.reparateur import Reparateur
from domaine.fiche import Fiche
from domaine.type_objet import TypeObjet
from domaine.visiteur import Visiteur

def main():
    '''Creation de l'environnement nécessaire pour le MVP : le registre, les réparateurs et visiteurs et les types d'objets hardcodes (fonctionnalites ulterieure)'''
    registre = RegistreFiches()
    reparateurs_donnees = [['THIEL', 'Valentin', 'Grille-Pain'], ['DEGAND', 'Louis', 'Ecran d\'ordinateur'], ['MARTIN', 'Loic', 'Ninja Creamy']]
    type_objet_donnees = [['Grille-Pain', 1.5], ['Ecran d\'ordinateur', 0.5], ['Ninja Creamy', 4]]
    visiteurs_donnees = [[1, 'DERICK', 'Maxime', None, None, False], [2, 'DUBRUILLE', 'Xavier', None, None, False], [3, 'KABASELE', 'Greg', None, None, False]]
    liste_reparateur = []
    liste_visiteur = []
    liste_type_objet = []
    id_objet = 1
    #TODO creer deux trois fiches

    for nom, prenom, specialite in reparateurs_donnees:
        liste_reparateur.append(Reparateur(nom, prenom, specialite))
    for id, nom, prenom, num, email, accord in visiteurs_donnees:
            liste_visiteur.append(Visiteur(id, nom, prenom, num, email, accord))
    for categorie, poids in type_objet_donnees:
        liste_type_objet.append(TypeObjet(categorie, poids))

    
    print('Bienvenue dans ASBL OS !\n Que voulez vous faire?')
    '''boucle principale'''
    while True:
        print('  1) Enregistrer un objet. \n  2) Consulter les donnees d\'une fiche (Reparateur). \n  3) Completer une fiche (Reparateur).\n')
        entree = input('Veuillez entrer le chiffre de la fonctionnalité.\n >> ')

        if entree.strip() not in ("1", "2", "3"): # TODO remplacer par try except
            print("Cette réponse ne correspond à aucune fonctionnalité, veuillez réessayer. \n")
            continue
        
        entree = int(entree)

        if entree == 1:
            fiche = []
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
                    print(fiche)
            #TODO demander le type d'objet, la description de la panne et la marque
            #TODO assigner un réparateur a l'objet de manière aléatoire car fonctionnalite ulterieure

        elif entree == 2:
            #TODO permettre au reparateur de voir les donnees de la fiche (check si elle existe d'abord !)
            pass

        elif entree == 3:
            #TODO permettre au reparateur de changer diagnostic et resultat de la fiche (check si elle existe d'abord !)
            pass
        



        


if __name__ == "__main__":
    main()