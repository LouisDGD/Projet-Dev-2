from domaine.registre import RegistreFiches
from domaine.reparateur import Reparateur
from domaine.fiche import Fiche
from domaine.type_objet import TypeObjet

def main():
    registre = RegistreFiches()
    reparateur1 = Reparateur('THIEL', 'Valentin', 'Grille-Pain')
    reparateur2 = Reparateur('DEGAND', 'Louis', 'Ecran d\'ordinateur')
    reparateur3 = Reparateur('MARTIN', 'Loic', 'Ninja Creamy')
    liste_reparateur = [reparateur1, reparateur2, reparateur3]

    visiteur1 = Visiteur(1, 'DERICK', 'Maxime', None, None, False)
    visiteur2 = Visiteur(2, 'DUBRUIILLE', 'Xavier', None, None, False)
    visiteur3 = Visiteur(3, 'KABASELE', 'Greg', None, None, False)
    liste_visiteur = [visiteur1, visiteur2, visiteur3]
    id = 1
    print('Bienvenue dans ASBL OS !\n Que voulez vous faire ?')
    while True:
        print('1) Enregistrer un objet.')
        print('2) Consulter les donnees d\'une fiche (Reparateur).')
        print('3) Completer une fiche (Reparateur).')

        entree = input('Veuillez entrer le chiffre de la fonctionnalité.')
        if entree == 1:
            fiche = list()
            print('Voici la liste des visiteurs enregistrés:\n')
            for v in liste_visiteur:
                print(v)
            visiteur_input = input('Qui est le visiteur ? Entrez son id.\n')
            for v in liste_visiteur:
                if v.id == visiteur_input:
                    fiche.append(v)



        


if __name__ == "__main__":
    main()