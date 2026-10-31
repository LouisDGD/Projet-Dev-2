from dataclasses import dataclass, field
from visiteur import Visiteur
from type_objet import TypeObjet
from enums import Etat, Resultat
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