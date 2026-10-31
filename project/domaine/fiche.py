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
    etat: Etat = Etat.EN_ATTENTE
    resultat: Resultat | None = None
    diagnostic: str | None = None
    reparateur: str | None = None
    marque: str | None = None
    date_arrivee: datetime = field(default_factory=datetime.now)
    

    def modifier_diagnostic(self, diagnostic: str) -> None:
        """Modifie le diagnostic F-03 tout en mettant une erreur si le diagnostic est vide ou ne contient que des espaces"""
        diagnostic = diagnostic.strip()
        if not diagnostic:
            raise ValueError("Veuillez entrer du texte.")
        self.diagnostic = diagnostic

    def modifier_resultat(self, resultat: Resultat) -> None:
        """Modifie le resultat F-03 et passe l'état de l'intervention de cette session à terminé"""
        if not isinstance(resultat, Resultat):
            raise TypeError("Pas le type Resultat")
        self.resultat = resultat
        self.etat = Etat.TERMINE

    def prendre_en_charge(self, reparateur: Reparateur) -> None:
        """F-02 Incrit le réparateur qui prend en charge l'objet."""
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