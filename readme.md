# Projet Dev 2 – Repair Café « La Clé à Molette »

Application de suivi des réparations pour le Repair Café « La Clé à Molette » (Forest), réalisée dans le cadre du cours de développement informatique à l'EPHEC.

L'ia claude opus 5.5 en effort moyen a été utilisée pour aider a la rédaction de ce readme

**Équipe** : Alexandre Borman, Louis Degand, Loïc Martin, Valentin Thiel

📄 Cahier des charges complet : voir le [Wiki](https://github.com/LouisDGD/Projet-Dev-2/wiki)

---

## Contexte

Aujourd'hui, chaque objet apporté au Repair Café a sa fiche papier, et ces fiches se perdent. L'application les remplace : l'accueil enregistre les objets, les réparateurs voient qui travaille sur quoi et notent leur diagnostic, et la coordinatrice peut sortir le rapport annuel pour la commune.

Contraintes principales :
- fonctionne **entièrement hors ligne** ;
- tourne sur un **vieux portable Windows** (≈ 2015) ;
- utilisable par des bénévoles **peu à l'aise avec l'informatique**.

---

## Choix techniques

- **Langage** : Python 3
- **Stockage** : fichiers JSON (pas de base de données)
  - `fiches.json` : base de données active, modifiée pendant les sessions
  - `history.json` : conservation de toutes les fiches (pour l'instant)
- **Encodage** : toujours ouvrir les fichiers en `utf-8` et écrire le JSON avec `ensure_ascii=False`, pour garder les accents lisibles

---

## Lancer le projet

```bash
python project/main.py
```

⚠️ Le chemin vers `fiches.json` dépend du dossier depuis lequel on lance le script. Vérifiez que tout le monde lit et écrit le même fichier.

⚠️ `fiches.json` et `history.json` doivent contenir une **liste**. Pour démarrer avec un fichier vide, mettez simplement `[]` dedans.

---

## Format d'une fiche

Tout le monde utilise **exactement** ces noms de champs :

```json
{
  "id": 1,
  "nom_visiteur": "Dubois",
  "type_objet": "Grille-pain",
  "marque": "Moulinex",
  "description": "Ne chauffe plus d'un côté",
  "date_arrivee": "2026-11-14T14:05:00",
  "etat": "en attente",
  "reparateur": null,
  "diagnostic": null,
  "resultat": null,
  "piece_attendue": null
}
```

| Champ | Rempli par | Remarque |
|---|---|---|
| `id` | F-01 (auto) | dernier id + 1 |
| `nom_visiteur`, `type_objet`, `marque`, `description` | F-01 (accueil) | `marque` peut être vide |
| `date_arrivee` | F-01 (auto) | format ISO ; trier sur ce champ donne la file d'attente |
| `etat` | F-01 puis F-02 / F-03 | `en attente` → `en cours` → `terminé` |
| `reparateur` | F-02 | `null` tant que personne n'a pris l'objet |
| `diagnostic`, `resultat`, `piece_attendue` | F-03 | `resultat` : `réparé`, `non réparable` ou `à suivre` |

**Types d'objets** (liste provisoire, en attente du tableau de Mme Moreau – Q-09) : Grille-pain, Lampe, Aspirateur, Téléviseur, Micro-ondes, Ordinateur, Autre.

---

## Avancement

| ID | Fonctionnalité | Priorité | Statut |
|---|---|---|---|
| F-01 | Enregistrer un objet à l'accueil | Indispensable |  En cours |
| F-02 | Consultation pour les réparateurs | Indispensable |  À faire |
| F-03 | Compléter une fiche (diagnostic et résultat) | Indispensable | Fait (MVP) |
| F-04 | Rechercher une fiche | Souhaitable |  À faire |
| F-05 | Indicateurs de la session | Souhaitable |  À faire |
| F-06 | Rapport imprimable pour la commune | Souhaitable |  À faire |
| F-07 | Coordonnées des visiteurs (RGPD) | Souhaitable |  À faire |
| F-08 | Sauvegarde automatique | Souhaitable |  À faire |
| F-09 | Rappel pour les objets « à suivre » | Optionnelle |  À faire |

---

## Échéances

- **02/11/2026** : démo du MVP (F-01, F-02, F-03)
- **23/11/2026** : version intermédiaire
- **07/12/2026** : version finale
