from domaine.visiteur import Visiteur
from domaine.type_objet import TypeObjet
from domaine.enums import Etat, Resultat
from domaine.reparateur import Reparateur
from datetime import datetime

class Fiche:
    def __init__(self, id: int, visiteur: Visiteur, type_objet: TypeObjet, description_panne: str, marque: str | None = None, date_arrivee: datetime | None = None, reparateur: Reparateur | None = None, etat: Etat = Etat.EN_ATTENTE, resultat: Resultat | None = None, diagnostic: str | None = None) -> None:
        if not isinstance(id, int) or isinstance(id, bool):
            raise TypeError("L'id doit être un entier")
        if id < 1:
            raise ValueError("L'id doit être strictement positif ")
        if not isinstance(visiteur, Visiteur):
            raise TypeError("Pas le type Visiteur")
        if not isinstance(type_objet, TypeObjet):
            raise TypeError("Pas le type TypeObjet")
        if not isinstance(description_panne, str):
            raise TypeError("La description doit être un texte")
        description_panne = description_panne.strip()
        if not description_panne:
            raise ValueError("La description de la panne est obligatoire.")
        if marque is not None:
            if not isinstance(marque, str):
                raise TypeError("La marque doit être un texte")
            marque = marque.strip()
            if not marque:
                raise ValueError("La marque de la panne est obligatoire.")
        if date_arrivee is not None and not isinstance(date_arrivee, datetime):
            raise TypeError("La date d'arrivée n'est pas une date")
        if reparateur is not None and not isinstance(reparateur, Reparateur):
            raise TypeError("Le réparateur doit être de type Reparateur")
        if not isinstance(etat, Etat):
            raise TypeError("L'état n'est pas de type Etat")
        if resultat is not None and not isinstance(resultat, Resultat):
            raise TypeError("Le résultat n'est pas de type Resultat")
        if diagnostic is not None:
            if not isinstance(diagnostic, str):
                raise TypeError("Le diagnostic doit être un texte")
            diagnostic = diagnostic.strip()
            if not diagnostic:
                raise ValueError("Le diagnostic de la panne est obligatoire.")
        
        self.__id = id
        self.__visiteur = visiteur
        self.__type_objet = type_objet
        self.__description_panne = description_panne
        self.__marque = marque
        self.__date_arrivee = date_arrivee or datetime.now()
        self.__reparateur = reparateur
        self.__etat = etat
        self.__resultat = resultat
        self.__diagnostic = diagnostic
        
    @property
    def id(self) -> int:
        return self.__id

    @property
    def visiteur(self) -> Visiteur:
        return self.__visiteur

    @property
    def type_objet(self) -> TypeObjet:
        return self.__type_objet

    @property
    def description_panne(self) -> str:
        return self.__description_panne

    @property
    def marque(self) -> str | None:
        return self.__marque

    @property
    def reparateur(self) -> Reparateur | None:
        return self.__reparateur

    @property
    def etat(self) -> Etat:
        return self.__etat

    @property
    def resultat(self) -> Resultat | None:
        return self.__resultat

    @property
    def diagnostic(self) -> str | None:
        return self.__diagnostic

    @property
    def date_arrivee(self) -> datetime:
        return self.__date_arrivee
        
    def modifier_diagnostic(self, diagnostic: str) -> None:
        """Modifie l'attribut diagnostic de la fiche
        PRE : aucune.
        POST : la fiche contient un diagnostic qui est un str de taille variable.
        Les autres attributs sont inchangés.
        Ne renvoie rien.
        Exceptions :
             ValueError si le diagnostic est vide ou composé uniquement d'espaces
             TypeError si le diagnostic n'est pas un str
        Dans ces cas, diagnostic n'est pas changé
        """
        if not isinstance(diagnostic, str):
            raise TypeError("Veuillez entrer du texte.")
        diagnostic = diagnostic.strip()
        if not diagnostic:
            raise ValueError("Le texte est vide ou composé d'espaces")
        self.__diagnostic = diagnostic

    def __str__(self) -> str:
        return (f"Fiche id={self.id}\nvisiteur={self.visiteur}\ntype={self.type_objet}\netat={self.etat}\nreparateur={self.reparateur}\nresultat={self.resultat}\ndiagnostic={self.diagnostic}\n")

    def modifier_resultat(self, resultat: Resultat) -> None:
        """Modifie le resultat F-03 et passe l'état de l'intervention de cette session à terminé
        PRE : aucune.
        POST : la fiche contient un resultat qui correspond à l'un des membres.
        L'attribut état devient Etat.TERMINE
        Les autres attributs sont inchangés.
        Ne renvoie rien.
        Exceptions :
             TypeError si le resultat n'est pas un membre de Resultat
             ValueError si le resultat est deja Resultat.REPARE
        Dans ces cas, resultat et état ne sont pas changés
        """
        if not isinstance(resultat, Resultat):
            raise TypeError("Pas le type Resultat")
        if self.__resultat == Resultat.REPARE:
            raise ValueError("L'objet a déjà été réparé")
        if resultat == self.__resultat:
            raise ValueError(f"Le résultat est déjà « {resultat.value} ».")
        self.__resultat = resultat
        self.__etat = Etat.TERMINE

    def prendre_en_charge(self, reparateur: Reparateur) -> None:
        """Inscrit le réparateur qui prend en charge l'objet.
        PRE : aucune.
        POST : la fiche contient le réparateur reçu et son état est Etat.EN_COURS.
        Exceptions :
            TypeError si reparateur n'est pas un Reparateur
            ValueError si le nom du réparateur est vide
            ValueError si la fiche n'est pas Etat.EN_ATTENTE
            Dans ce cas, la fiche n'est pas modifiée.
        """
        if not isinstance(reparateur, Reparateur):
            raise TypeError("Pas le type Reparateur")
        if not reparateur.nom.strip():
            raise ValueError("Le nom du réparateur est obligatoire.")
        if self.__etat != Etat.EN_ATTENTE:
            if self.__reparateur is not None:
                raise ValueError(f"Objet déjà pris en charge par {self.__reparateur.nom}.")
            raise ValueError("Cet objet n'est plus en attente.")
        self.__reparateur = reparateur
        self.__etat = Etat.EN_COURS        

if __name__ == "__main__":
    test = Fiche(1, Visiteur(1, "Jean", "Dean", "", "", False), TypeObjet("cookie maker", 4.3),
             "Fonctionne plus")
    print(test)
    test.modifier_resultat(Resultat.A_SUIVRE)
    print(test)