from project.ancien.stockage import HISTORIQUE, lire

# Renvoie le prochain identifiant libre, basé sur l'historique
def get_id():
    historique = lire(HISTORIQUE)
    if not historique:
        return 1
    return max(fiche["id"] for fiche in historique) + 1
