# Cahier des charges – Repair Café « La Clé à Molette »

> _L'IA Claude Opus 5.5 a été utilisée pour la mise en page du document au format Markdown, la correction des erreurs d'orthographe et de typographie, ainsi que pour une proposition de rédaction des exigences non fonctionnelles (section 3.2), établie à partir de l'entretien avec la cliente. Le contenu des autres sections a été rédigé par l'équipe._

## Informations sur le document

| Élément | Valeur |
|---|---|
| **Titre** | Cahier des charges – Repair Café |
| **Auteurs** | Valentin Thiel, Alexandre Borman, Loïc Martin, Louis Degand |
| **Version** | 1.0 du 14/10/2026 – première version |
| **Validation client** | En attente de validation par Mme Moreau |

### Conventions d'identification

| Élément | Format | Exemple |
|---|---|---|
| Règle métier | RM-xx | RM-01 |
| Donnée | D-xx | D-03 |
| Fonctionnalité | F-xx | F-03 |
| Exigence fonctionnelle | EF-xx.y | EF-03.2 |
| Exigence non fonctionnelle | ENF-xx | ENF-02 |
| Question ouverte | Q-xx | Q-01 |

---

## 1. Contexte

### 1.1. Présentation du client

Jacqueline Moreau, ancienne professeure de physique, est la coordinatrice bénévole du Repair Café « La Clé à Molette » à Forest, créé il y a 4 ans avec des voisins.

Les membres se retrouvent une fois par mois, le deuxième samedi du mois de 14 h à 17 h, à la maison de quartier de Forest. Les visiteurs viennent avec des objets à réparer et les bénévoles les aident à les réparer gratuitement. Les bénévoles ne réparent pas à leur place, mais les aident à réparer.

### 1.2. Présentation du projet

Actuellement, chaque objet a sa propre fiche papier à l'accueil, mais ces fiches passent de main en main et se perdent : personne ne sait qui travaille sur quoi, ni quand. Après la session, le petit-fils de Mme Moreau recopie toutes ces fiches dans un fichier Excel pour un rapport à la commune. Il part en Erasmus en février : l'association a donc besoin d'un outil simple pour remplacer ces fiches et l'Excel, sur le vieil ordinateur portable de l'association.

### 1.3. Objectifs du projet

- Retrouver facilement une fiche quand quelqu'un revient avec son objet.
- Faire plus facilement les rapports à la commune.

---

## 2. Description générale

### 2.1. Vue d'ensemble du produit et de son environnement

- Une application/site (en local) utilisée depuis l'unique ordinateur Windows du Repair Café.
- Celle-ci doit avoir un historique des objets réparés et être capable d'enregistrer un nouvel objet (en attente de réparation). Un bénévole doit pouvoir facilement prendre en charge un dossier, et les autres doivent le voir (synchronisation).
- Il faut pouvoir faire un rapport avec les informations nécessaires à la commune (à revoir avec Mme Moreau).
- L'ordinateur n'ayant pas d'accès stable à Internet, les fonctionnalités doivent être exclusivement hors ligne.

### 2.2. Profils utilisateurs (acteurs)

Il existe plusieurs utilisateurs ayant le même profil : des bénévoles du quartier, avec des niveaux en informatique variables, qui encodent les données des différents dossiers dont ils s'occupent.

### 2.3. Périmètre

**Inclus :**
- Un historique complet ainsi qu'un système de recherche facile à utiliser.
- La possibilité d'enregistrer de nouvelles données (un objet à réparer).
- Une fonction pour imprimer directement un dossier ou un groupe de dossiers (grâce à la recherche).
- Un retour en temps réel de l'état d'un dossier.

**Exclus :**
- Un accès à Internet.

### 2.4. Règles métier

- **RM-01** : L'application est en Python.
- **RM-02** : L'application est accessible à différents niveaux d'aisance informatique.
- **RM-03** : Un historique, la recherche et la création de dossiers, le tout synchronisé.

### 2.5. Données

#### D-01 — Application
- **Contenu** : un exécutable, les fonctionnalités de l'application.
- **Volume** : autant que le PC de la cliente le permet.
- **Origine** : —
- **Conservation** : « infinie », tant que Mme Moreau utilisera l'ordinateur.

#### D-02 — Gestion des dossiers
- **Contenu** : un historique des dossiers, la création de dossiers, la recherche de dossiers.
- **Volume** : autant que nécessaire.
- **Origine** : visiteurs amenant leurs objets à réparer.
- **Conservation** : liée à D-01.

#### D-03 — Exportation des dossiers pour la commune
- **Contenu** : un ou plusieurs dossiers et les données liées, dans un format adapté à la commune.
- **Volume** : selon la fréquence à laquelle un rapport est dû à la commune (à déterminer avec la cliente).
- **Origine** : les dossiers complets dans la base de données de l'application.
- **Conservation** : liée à D-01.

---

## 3. Exigences

### 3.1. Exigences fonctionnelles

#### Vue d'ensemble

Ce tableau reprend la liste de toutes les fonctionnalités, avec les intervenants concernés par chacune d'elles.

| ID | Fonctionnalité | Acteur(s) | Priorité |
|---|---|---|---|
| F-01 | Enregistrer les informations d'un objet à l'accueil | Bénévoles de l'accueil | Indispensable |
| F-02 | Consultation des données pour les réparateurs | Réparateurs, coordinatrice | Indispensable |
| F-03 | Compléter une fiche (diagnostic et résultat) | Réparateurs | Indispensable |
| F-04 | Rechercher une fiche | Réparateurs, coordinatrice | Indispensable |
| F-05 | Afficher les indicateurs de la session | Coordinatrice | Souhaitable |
| F-06 | Générer le rapport imprimable pour la commune | Responsable | Indispensable |
| F-07 | Gérer les coordonnées des visiteurs | Responsable, coordinatrice | Indispensable |
| F-08 | Sauvegarde automatique des données | Système | Indispensable |
| F-09 | Rappel pour les objets « à suivre » | À définir | À définir |

Priorités : **indispensable**, **souhaitable**, **optionnelle** (si le temps le permet).

---

#### F-01 — Enregistrer les informations d'un objet à l'accueil

| | |
|---|---|
| **Auteur** | Louis Degand |
| **Acteur(s)** | Bénévoles de l'accueil |
| **Priorité** | Indispensable |
| **Description** | Permettre aux bénévoles d'enregistrer les informations relatives à un objet pour en créer une fiche. |

**Exigences**
- **EF-01.1** : Le bénévole introduit le nom du visiteur, la marque, l'adresse e-mail ainsi que la description de l'objet.
- **EF-01.2** : Le type d'objet est choisi dans une liste, sans saisie libre.
- **EF-01.3** : La fiche est automatiquement ajoutée à la file d'attente, par ordre d'arrivée (premier arrivé, premier servi).

**Critères d'acceptation**
- **EF-01.1** : Un bénévole crée une fiche complète sans aide.
- **EF-01.2** : Tous les types cités par la cliente sont proposés dans la liste.
- **EF-01.3** : La fiche apparaît en fin de file d'attente.

---

#### F-02 — Consultation des données pour les réparateurs

| | |
|---|---|
| **Auteur** | Louis Degand |
| **Acteur(s)** | Réparateurs du café, coordinatrice |
| **Priorité** | Indispensable |
| **Description** | L'écran principal affiche la liste des objets de la session en cours et indique qui travaille sur quoi. |

**Exigences**
- **EF-02.1** : L'écran affiche pour chaque objet le nom du visiteur, le type d'objet, le réparateur assigné et l'état (en attente, en cours, terminé).
- **EF-02.2** : Un réparateur peut prendre en charge un objet en y inscrivant son nom.
- **EF-02.3** : L'application n'assigne jamais un objet automatiquement.

**Critères d'acceptation**
- **EF-02.1** : La coordinatrice peut consulter qui travaille sur quoi.
- **EF-02.2** : Le nom du réparateur est inscrit sur la ligne de l'objet.
- **EF-02.3** : Aucun objet n'a de réparateur assigné automatiquement.

---

#### F-03 — Compléter une fiche (diagnostic et résultat)

| | |
|---|---|
| **Auteur** | Louis Degand |
| **Acteur(s)** | Réparateurs |
| **Priorité** | Indispensable |
| **Description** | Le réparateur note son diagnostic et le résultat de la réparation. |

**Exigences**
- **EF-03.1** : Le réparateur saisit un diagnostic.
- **EF-03.2** : Le réparateur saisit un statut pour la réparation (en cours, réparé, à suivre – pièce manquante).

**Critères d'acceptation**
- **EF-03.1** : Le diagnostic saisi par le réparateur est affiché.
- **EF-03.2** : Le statut de la réparation saisi par le réparateur est affiché.
- **EF-03.2** : Les objets avec le statut « à suivre » sont retrouvables lors des sessions suivantes.

---

#### F-04 — Rechercher une fiche

| | |
|---|---|
| **Auteur** | Louis Degand |
| **Acteur(s)** | Responsable et réparateurs |
| **Priorité** | Indispensable |
| **Description** | Les réparateurs ainsi que la responsable peuvent rechercher sans difficulté une fiche liée à un objet. |

**Exigences**
- **EF-04.1** : La recherche se fait par nom de visiteur.
- **EF-04.2** : Un filtre affiche uniquement les objets « à suivre ».

**Critères d'acceptation**
- **EF-04.1** : En tapant « Dubois », la fiche du grille-pain de Mme Dubois s'affiche (test proposé par la cliente).
- **EF-04.2** : Seuls les objets avec le statut « à suivre » s'affichent.

---

#### F-05 — Afficher les indicateurs de la session

| | |
|---|---|
| **Auteur** | Louis Degand |
| **Acteur(s)** | Responsable |
| **Priorité** | Souhaitable |
| **Description** | La responsable suit la progression de la session en cours. |

**Exigences**
- **EF-05.1** : L'application affiche le nombre d'objets arrivés, réparés et repartis sans solution.

**Critères d'acceptation**
- **EF-05.1** : Les données correspondent au contenu de la liste et se mettent à jour automatiquement.

---

#### F-06 — Générer le rapport imprimable pour la commune

| | |
|---|---|
| **Auteur** | Louis Degand |
| **Acteur(s)** | Responsable |
| **Priorité** | Indispensable |
| **Description** | Génération automatique des rapports à fournir à la commune. |

**Exigences**
- **EF-06.1** : L'application génère un document imprimable sur une période donnée.
- **EF-06.2** : Le rapport indique le nombre d'objets reçus et réparés, ainsi qu'une estimation du nombre de kilos de déchets évités.
- **EF-06.3** : La responsable peut relire les rapports avant impression.

**Critères d'acceptation**
- **EF-06.1** : Le document est correctement mis en page et correspond bien à la période renseignée.
- **EF-06.2** : Les nombres sont corrects et correspondent aux chiffres réels.
- **EF-06.3** : Les rapports sont affichés avant impression.

---

#### F-07 — Gérer les coordonnées des visiteurs

| | |
|---|---|
| **Auteur** | Louis Degand |
| **Acteur(s)** | Responsable et bénévoles |
| **Priorité** | Indispensable |
| **Description** | Les coordonnées ne sont enregistrées qu'avec l'accord des visiteurs et sont supprimées automatiquement après un an. |

**Exigences**
- **EF-07.1** : Les champs de coordonnées sont bloqués tant que le visiteur n'a pas donné son accord et que la case n'est pas cochée.
- **EF-07.2** : Le système efface automatiquement les données 365 jours après leur enregistrement.

**Critères d'acceptation**
- **EF-07.1** : Le champ de coordonnées se débloque lors de la validation de l'accord du visiteur.
- **EF-07.2** : Le système a correctement effacé les données après 365 jours (avec des dates simulées, les coordonnées disparaissent et les fiches restent).

---

#### F-08 — Sauvegarde automatique des données

| | |
|---|---|
| **Auteur** | Loïc Martin |
| **Acteur(s)** | Système |
| **Priorité** | Indispensable |
| **Description** | L'application sauvegarde automatiquement les données (fiches et historiques) dans un dossier de l'ordinateur de l'accueil, afin de pouvoir les récupérer en cas de suppression accidentelle ou de fichier corrompu. |

**Exigences**
- **EF-08.1** : L'application crée automatiquement une copie de toutes les données à chaque fermeture.
- **EF-08.2** : La copie est enregistrée dans un dossier sur le disque de l'ordinateur.
- **EF-08.3** : L'application crée un dossier dédié sur l'ordinateur, qui contiendra les sauvegardes.
- **EF-08.4** : L'application se limite à 10 copies et supprime la plus ancienne s'il en existe déjà 10.
- **EF-08.5** : L'application affiche un message d'erreur au démarrage suivant si la sauvegarde a échoué.
- **EF-08.6** : La responsable, Mme Moreau, peut restaurer une sauvegarde depuis l'application.
- **EF-08.7** : Une sauvegarde n'est pas conservée plus de 365 jours.

**Critères d'acceptation**
- **EF-08.1** : Après la fermeture de l'application, un nouveau fichier de sauvegarde daté est créé dans le dossier prévu.
- **EF-08.2** : Le dossier de sauvegarde contient la sauvegarde créée à la fermeture de l'application.
- **EF-08.3** : Le dossier de sauvegarde existe sur le dispositif de stockage de l'ordinateur.
- **EF-08.4** : Lors de la création d'une onzième sauvegarde, la plus ancienne est supprimée pour rester à un maximum de 10 sauvegardes.
- **EF-08.5** : Un message d'erreur apparaît lorsque la date de la dernière sauvegarde ne correspond pas à la dernière fermeture.
- **EF-08.6** : Après avoir modifié une fiche, on restaure une sauvegarde et on vérifie que la fiche a retrouvé son état d'avant la modification.
- **EF-08.7** : Avec une date simulée, la sauvegarde de plus de 365 jours est supprimée.

---

#### F-09 — Rappel pour les objets « à suivre »

_À compléter._

---

### 3.2. Exigences non fonctionnelles

Les valeurs marquées _(à valider)_ n'ont pas été chiffrées par la cliente et doivent être confirmées avec elle.

| ID | Exigence | Vérification |
|---|---|---|
| ENF-01 | L'application fonctionne entièrement hors ligne, sans aucune connexion à Internet. | Session simulée de 3 h avec le Wi-Fi et le câble réseau désactivés : toutes les fonctionnalités restent utilisables. |
| ENF-02 | L'application fonctionne sur l'ordinateur portable Windows de l'association (environ 2015). | Installation et test complet sur la machine réelle de l'accueil. |
| ENF-03 | L'interface est utilisable par des bénévoles débutants : police de grande taille (≥ 16 pt _(à valider)_), boutons explicites, codes couleur. | Un bénévole de l'accueil crée une fiche sans aide en moins de 2 minutes _(à valider)_. |
| ENF-04 | L'application supporte au moins 50 objets par session sans ralentissement perceptible. | Saisie de 50 fiches lors d'une session simulée, puis consultation et recherche. |
| ENF-05 | Chaque écran et chaque résultat de recherche s'affiche en moins de 2 secondes _(à valider)_. | Mesure du temps d'affichage sur l'ordinateur de l'association, avec un historique de 12 sessions simulées. |
| ENF-06 | Aucune donnée saisie n'est perdue en cas de fermeture brutale ou de plantage. | Fermeture forcée de l'application pendant une saisie, puis vérification des fiches au redémarrage. |
| ENF-07 | Les fiches ne sont jamais supprimées de l'historique (conservation pour les rapports à la commune). | Vérification de la présence de toutes les fiches après plusieurs sessions simulées. |
| ENF-08 | Les coordonnées des visiteurs ne sont conservées qu'avec leur accord et sont effacées après un an (RGPD). | Test avec des dates simulées (voir EF-07.2). |
| ENF-09 | L'application peut être installée et lancée sans connexion à Internet. | Installation sur l'ordinateur de l'accueil, réseau désactivé. |
| ENF-10 | Un guide utilisateur simple, rédigé sans jargon technique, est fourni aux bénévoles. | Relecture et validation du guide par Mme Moreau. |
| ENF-11 | Le code source est en Python (RM-01). | Analyse du dépôt GitHub. |

---

## 4. Contraintes

_À compléter._

## 5. Budget

_À compléter._

---

## 6. Livrables et planning

### 6.1. Livrables

_À compléter._

### 6.2. Échéances

_À compléter._

### 6.3. Retours vers le client

- Différents appels téléphoniques avec Mme Moreau, les agents d'accueil et les réparateurs, entre le 19/10/2026 et le 14/11/2026, pour affiner les demandes et découvrir des contraintes métier et/ou des exigences fonctionnelles supplémentaires.
- Rendez-vous lors de la session du Repair Café du 07/11/2026, afin d'observer le fonctionnement d'une session et de confirmer, voire découvrir, des contraintes métier.
- Démonstration d'un MVP du produit avec Mme Moreau le 02/11/2026.
- Démonstration d'une version intermédiaire du produit, comprenant plus de fonctionnalités, le 23/11/2026.

---

## 7. Validation du projet

| | |
|---|---|
| **Qui** | Mme Moreau et Loïc Martin |
| **Quand** | Le 02/11/2026 pour le MVP, le 23/11/2026 pour la démonstration intermédiaire et le 07/12/2026 pour la version finale. |
| **Sur quelle base** | Les critères d'acceptation de la section 3.1 et la vérification des exigences non fonctionnelles de la section 3.2. |
| **Suivi des anomalies** | Chaque anomalie est consignée dans une issue GitHub, avec l'identifiant de l'exigence concernée et sa gravité (bloquante, majeure, mineure). |

---

## 8. Maintenance

Notre équipe corrigera les anomalies jusqu'au 07/12/2026 compris. Après la livraison et la recette par Mme Moreau, une maintenance de 2 heures pourra être effectuée par notre équipe, sous réserve d'acceptation de Mme Moreau, qui a confirmé que c'était envisageable. Cette maintenance comprendrait la résolution d'anomalies et l'ajout potentiel de fonctionnalités. Il est néanmoins nécessaire d'obtenir l'accord de Mme Moreau et de toute notre équipe pour valider les modalités de cette maintenance.

---

## 9. Questions ouvertes

Questions à poser à Mme Moreau :

- **Q-01** : Quelles sont les modalités de la maintenance (heures, échéance, joignabilité) et les différents services assurés par notre équipe ?
- **Q-02** : Quels sont les composants de l'ordinateur utilisé à l'accueil ?
- **Q-03** : Quelles fonctionnalités sont accessibles uniquement à Mme Moreau ?
- **Q-04** : Quelles fonctionnalités ne devraient pas être accessibles à certains acteurs (Mme Moreau, bénévoles, réparateurs) ?
- **Q-05** : Combien de sauvegardes faut-il conserver ?
- **Q-06** : Mme Moreau doit-elle être la seule à pouvoir restaurer une sauvegarde de l'application ?

---

## 10. Glossaire

| Terme | Définition |
|---|---|
| **MVP** | _Minimum Viable Product_ : première version livrée, limitée aux fonctionnalités indispensables. |

---

## 11. Annexes

- **Annexe A** : Transcription partielle du premier entretien avec Mme Moreau, intitulée « historique client » et disponible sur le dépôt GitHub.
