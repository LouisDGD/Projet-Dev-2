import json
import os
from pathlib import Path

# Les fichiers de données sont rangés à côté du code, peu importe d'où on lance le programme
DOSSIER_DATA = Path(__file__).resolve().parent / "data"
FICHES = DOSSIER_DATA / "fiches.json"
TYPES = DOSSIER_DATA / "types.json"


def lire(chemin):
    #Lit une liste JSON. Renvoie une liste vide si le fichier n'existe pas ou est vide.
    if not chemin.exists() or chemin.stat().st_size == 0:
        return []
    with open(chemin, "r", encoding="utf-8") as file:
        return json.load(file)


def ecrire(chemin, donnees):
    DOSSIER_DATA.mkdir(parents=True, exist_ok=True)
    temporaire = chemin.with_suffix(".tmp")
    with open(temporaire, "w", encoding="utf-8") as file:
        json.dump(donnees, file, indent=4, ensure_ascii=False)
    os.replace(temporaire, chemin)
