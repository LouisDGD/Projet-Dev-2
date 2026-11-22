from datetime import datetime
class Visiteur:
    def __init__(self, id : int, nom_visiteur: str, prenom_visiteur: str, num_tel : str | None = None , email : str | None = None, accord : bool = False, derniere_visite : datetime | None = None) -> None:
        if not isinstance(id, int) or isinstance(id, bool):
            raise TypeError("L'ID doit être un entier")
        if id <= 0:
            raise ValueError("L'ID  doit être strictement positif")
        if not isinstance(nom_visiteur, str):
            raise TypeError("Le nom doit être un str")
        nom_visiteur = nom_visiteur.strip()
        if not nom_visiteur:
            raise ValueError("Le nom est vide ou n'est composé que d'espaces")
        if not isinstance(prenom_visiteur, str):
            raise TypeError("Le prénom doit être un str")
        prenom_visiteur = prenom_visiteur.strip()
        if not prenom_visiteur:
          raise ValueError("Le prénom est vide ou n'est composé que d'espaces")
        if not isinstance(accord, bool):
            raise TypeError("L'accord doit être un booléen")
        if accord:
            if email is not None:
                if not isinstance(email, str):
                    raise TypeError("L'email doit être un str")
                email = email.strip()
                if not email:
                    raise ValueError("l'email est vide ou n'est composé que d'espaces")
            if num_tel is not None:
                if not isinstance(num_tel, str):
                    raise TypeError("Le numéro de téléphone doit être un str")
                num_tel = num_tel.strip()
                if not num_tel:
                    raise ValueError("Le numéro est vide ou n'est composé que d'espaces")
        if derniere_visite is not None and not isinstance(derniere_visite, datetime):
            raise TypeError("Derniere_visite doit être un datetime")
        
        self.__id = id
        self.__nom_visiteur = nom_visiteur.title()
        self.__prenom_visiteur = prenom_visiteur.title()
        self.__accord = accord
        self.__derniere_visite = derniere_visite or datetime.now()
        if accord == True:
            self.__email = email
            self.__num_tel = num_tel
        else:
            self.__email = None
            self.__num_tel = None

    @property
    def id(self) -> int:
        return self.__id
    @property
    def nom_visiteur(self) -> str:
        return self.__nom_visiteur
    @property
    def prenom_visiteur(self) -> str:
        return self.__prenom_visiteur
    @property
    def accord(self) -> bool:
        return self.__accord
    @property
    def derniere_visite(self) -> datetime:
        return self.__derniere_visite
    @property
    def email(self) -> str | None:
        return self.__email
    @property
    def num_tel(self) -> str |None:
        return self.__num_tel

    def __str__(self) -> str:
        return f"{self.id} {self.nom_visiteur} {self.prenom_visiteur} - {self.accord} {self.email} {self.num_tel} - {self.derniere_visite}"