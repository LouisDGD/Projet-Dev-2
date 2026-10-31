from project.ancien.stockage import FICHES, HISTORIQUE, lire, ecrire

# Sauvegarde une fiche dans fiches.json (fiches de la session) et dans history.json (historique complet)
def save(fiche):
    for chemin in (FICHES, HISTORIQUE):
        donnees = lire(chemin)
        donnees.append(fiche)
        ecrire(chemin, donnees)
