class TypeObjet:
    __categorie: str
    __poids_moyen: float

    def __init__(self, categorie: str, poids_moyen : float) -> None:
        if not isinstance(categorie, str):
            raise TypeError("La catégorie doit être un str")
        if not isinstance(poids_moyen, float):
            raise TypeError("Le poids doit être un float")
        cat = categorie.strip()
        if not cat:
            raise ValueError("Catégorie est vide ou n'est composé que d'espaces")
        if poids_moyen <= 0:
            raise ValueError("Le poids doit être strictement positif")
        self.__categorie = cat.capitalize()
        self.__poids_moyen = poids_moyen

    @property
    def categorie(self) -> str:
        return self.__categorie

    @property
    def poids_moyen(self) -> float:
        return self.__poids_moyen
    
    def __str__(self):
        return f"Cat : {self.categorie} Poids : {self.poids_moyen}"