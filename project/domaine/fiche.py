from dataclasses import dataclass, field
from domaine.visiteur import Visiteur
from domaine.type_objet import TypeObjet
from domaine.enums import Etat, Resultat
from domaine.reparateur import Reparateur
from datetime import datetime

@dataclass
class Fiche:
    id: int
    visiteur: Visiteur
    type_objet: TypeObjet
    description_panne: str
    marque: str | None = None
    reparateur: Reparateur | None = None
    etat: Etat = Etat.EN_ATTENTE
    resultat: Resultat | None = None
    diagnostic: str | None = None
    date_arrivee: datetime = field(default_factory=datetime.now)
    

    def modifier_diagnostic(self, diagnostic: str) -> None:
        """Modifie l'attribut diagnostic de la fiche
        PRE : aucune.
        POST : le registre contient un diagnostic qui est un str de taille variable.
        Les autres attributs sont inchangés.
        Ne renvoie rien.
        Exceptions :
             ValueError si le diagnostic est vide
             TypeError si le diagnostic n'est pas un str
        Dans ces cas, diagnostic n'est pas changé
        """
        if not isinstance(diagnostic, str):
            raise TypeError("Veuillez entrer du texte.")
        diagnostic = diagnostic.strip()
        if not diagnostic:
            raise ValueError("Le texte est vide")
        self.diagnostic = diagnostic

    def modifier_resultat(self, resultat: Resultat) -> None:
        """Modifie le resultat F-03 et passe l'état de l'intervention de cette session à terminé
        PRE : aucune.
        POST : le registre contient un resultat qui correspond à l'un des membres.
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
        if self.resultat == Resultat.REPARE:
            raise ValueError("L'objet a déjà été réparé")
        self.resultat = resultat
        self.etat = Etat.TERMINE

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
        if self.etat != Etat.EN_ATTENTE:
            if self.reparateur is not None:
                raise ValueError(f"Objet déjà pris en charge par {self.reparateur.nom}.")
            raise ValueError(f"Cet objet n'est plus en attente.")
        self.reparateur = reparateur
        self.etat = Etat.EN_COURS

if __name__ == "__main__":
    test = Fiche(1, Visiteur(1, "Jean", "Dean", "", "", False), TypeObjet("cookie maker", 4.3),
             "Fonctionne plus")
    print(test.diagnostic)
    test.modifier_diagnostic("kikiiii")
    print(test.diagnostic)
    print(test.resultat)
    print(test.etat.value)
    test.modifier_resultat(Resultat.REPARE)
    print(test.resultat.value)
    print(test.etat.value)