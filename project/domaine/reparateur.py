class Reparateur:
    def __init__(self, nom: str, prenom : str, specialite : str) -> None:
        if not isinstance(nom, str):
            raise TypeError("Le nom doit être un str")
        nom = nom.strip()
        if not nom:
            raise ValueError("Le nom est vide ou est composé que d'espaces")
        if not isinstance(prenom, str):
            raise TypeError("Le prénom doit être un str")
        prenom = prenom.strip()
        if not prenom:
            raise ValueError("Le prénom est vide ou est composé que d'espaces")
        if not isinstance(specialite, str):
            raise TypeError("La spécialité doit être un str")
        specialite = specialite.strip()
        if not specialite:
            raise ValueError("La spécialité est vide ou est composée que d'espaces")

        self.__nom = nom.title()
        self.__prenom = prenom.title()
        self.__specialite = specialite.capitalize()

    @property
    def nom(self) -> str:
            return self.__nom
    @property
    def prenom(self) -> str:
            return self.__prenom
    @property
    def specialite(self) -> str:
            return self.__specialite

    def __str__(self) -> str:
            return f"{self.nom} {self.prenom} : {self.specialite}"
