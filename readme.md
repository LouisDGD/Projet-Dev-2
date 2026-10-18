# Cahier des charges – Repair Café « La Clé à Molette »

> _L'IA Claude Opus 5.5 a été utilisée pour la mise en page du document au format Markdown, la correction des erreurs d'orthographe et de typographie, ainsi que pour une proposition de rédaction des exigences non fonctionnelles (section 3.2), établie à partir de l'entretien avec la cliente. Le contenu des autres sections a été rédigé par l'équipe._

## Informations sur le document

| Élément | Valeur |
|---|---|
| **Titre** | Cahier des charges – Repair Café |
| **Auteurs** | Valentin Thiel, Alexandre Borman, Loïc Martin, Louis Degand |
| **Version** | 1.0 du 18/10/2026 – première version |
| **Validation client** | En attente de validation par Mme Moreau et les bénévoles de l'accueil |

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

Au niveau des parties prenantes :
- Il y a Jacqueline Moreau, la coordinatrice de l'association, et les bénévoles de l'accueil, qui seront les personnes qui valideront le cahier des charges et prononceront la réception en comité.
- Les testeurs seront les bénévoles de l'accueil, les réparateurs et Mme Moreau, qui seront les utilisateurs clés et participeront aux démos.
- Les prestataires qui vont réaliser l'application sont Alexandre Borman, Valentin Thiel, Louis Degand et Loïc Martin.

### 1.3. Objectifs du projet

- Retrouver facilement une fiche quand quelqu'un revient avec son objet au lieu de chercher dans une boîte à chaussures.
- Ne plus perdre de fiches par inadvertance.
- Faire plus facilement les rapports à la commune.
- L'application doit être simple à utiliser, même pour les personnes peu à l'aise avec l'informatique.

**Plus-value attendue :**
- Gain de 3 h par mois pour créer le rapport destiné à la commune.
- Suivi précis des objets pendant la session : il faut savoir quel réparateur travaille sur quel objet afin d'éviter qu'un visiteur attende une heure à l'accueil.
- Zéro perte de fiches : les fiches ne peuvent plus être perdues par inadvertance.

**Risques en cas de non-réalisation, alternatives :**
- Des fiches peuvent toujours disparaître.
- Les visiteurs peuvent perdre leur temps à attendre à l'accueil.
- La création du rapport pour la commune prend 3 h par mois.
- Hugo partant en février, Mme Moreau ne sait pas qui reprendra l'Excel ou s'ils changent de processus.

---

## 2. Description générale

### 2.1. Vue d'ensemble du produit et de son environnement

- Une application en local utilisée depuis l'unique ordinateur Windows du Repair Café.
- L'application remplace l'Excel d'Hugo et les fiches papier.
- L'association ne possède aucun système informatique existant à intégrer. Mme Moreau ne trouve pas intéressant qu'on numérise les fiches papier déjà existantes ; en revanche, elle aimerait garder les données des fiches de l'Excel.
- Celle-ci doit avoir un historique de tous les objets traités (réparés, non réparables, à suivre) et être capable d'enregistrer un nouvel objet (en attente de réparation). Un réparateur doit pouvoir facilement prendre en charge un dossier, et les autres doivent le voir.
- Il faut pouvoir faire un rapport avec les informations nécessaires à la commune.
- L'ordinateur n'ayant pas d'accès stable à Internet, les fonctionnalités doivent être exclusivement hors ligne.

### 2.2. Profils utilisateurs (acteurs)

| Acteur | Description |
|---|---|
| Coordinatrice | Jacqueline Moreau s'occupe de l'organisation, planifie les sessions et fait le lien avec la commune pour le rapport annuel. Elle est peu à l'aise avec l'informatique. |
| Bénévole de l'accueil | 2 à 3 bénévoles par session, souvent des retraités. Niveaux variables avec l'informatique. Accueil des visiteurs, crée et remplit les fiches, envoie les gens vers le réparateur qui a accepté de s'occuper de l'objet. |
| Réparateur | 8 à 12 réparateurs par session. Décide de l'objet qu'il prend. Prend l'objet pour en diagnostiquer la panne et répare avec le visiteur. Il note le diagnostic et le résultat. |

### 2.3. Périmètre

**Inclus :**
- Enregistrement d'un objet par les bénévoles de l'accueil
- Gestion des objets et des données des visiteurs et leur sauvegarde automatique.
- Création, lecture et modification d'un rapport pour la commune
- Gestion et suivi de la session de réparation en cours avec possibilité de prise en charge d'objet.
- Fonctionnement hors ligne de l'application
- Sauvegarde automatique des données.
- Numérisation des fiches Excel.

**Exclus et validé par la cliente le 18/10/2026 :**
- Un accès à Internet.
- Application mobile.
- Assignation automatique des objets aux réparateurs.
- Numérisation des fiches papier existantes
- Gestion des dons d'objets.

### 2.4. Règles métier

- **RM-01** : Le réparateur choisit l'objet dont il s'occupe.
- **RM-02** : Une réparation se termine par un des trois résultats : réparé, non réparable, à suivre.
- **RM-03** : Pour un objet à suivre, le visiteur commande la pièce lui-même et revient avec elle à une autre session.
- **RM-04** : On rappelle au visiteur de venir avec la pièce qui sert à réparer l'objet avant la prochaine session.
- **RM-05** : Les coordonnées d'un visiteur ne sont enregistrées qu'avec son accord.
- **RM-06** : La réparation est gratuite.
- **RM-07** : Le rapport pour la commune est annuel et comprend une estimation du poids moyen des déchets évités selon le tableau fourni à Mme Moreau.
- **RM-08** : Les coordonnées des visiteurs sont supprimées 365 jours compris après leur dernière visite.
- **RM-09** : Aucun objet n'est gardé.

### 2.5. Données

#### D-01 — Visiteur
- **Contenu** : nom du visiteur ; numéro de téléphone, e-mail (les deux sont facultatifs, voir RM-05), utilisés uniquement pour prévenir le visiteur de venir avec la pièce nécessaire à la réparation.
- **Volume** : 30 à 40 en moyenne avec un pic jusqu'à 50 à Noël.
- **Origine** : saisie dans le système et reprise du fichier Excel existant.
- **Conservation** : 365 jours compris (RM-08)

| *Opération* | *Acteur* | *Fonctionnalité* |
| --- | --- | --- |
| *Créer* | *Bénévole de l'accueil, Système* | *F-01* |
| *Restaurer* | *Système* | *F-08* |
| *Consulter* | *Bénévole de l'accueil, coordinatrice, réparateur* | *F-02, F-04* |
| *Effacer* | *Système* | *F-08* |
| *Modifier* | *Bénévole de l'accueil* | *F-01* |


#### D-02 — Fiche de réparation
- **Contenu** : visiteur concerné (D-01) ; type d'objet (D-03) ; description de la panne ; nom du réparateur ; marque de l'objet (facultative) ; diagnostic ; résultat (réparé, non réparable, à suivre) ; pièce attendue (facultative, si à suivre) ; état (en attente, en cours, terminé)
- **Volume** : 30 à 40 en moyenne avec un pic jusqu'à 50 à Noël.
- **Origine** : créée à l’accueil, puis complétée par le réparateur. Reprise du fichier Excel existant.
- **Conservation** : illimitée

| *Opération* | *Acteur* | *Fonctionnalité* |
| --- | --- | --- |
| *Créer* | *Bénévole de l'accueil* | *F-01* |
| *Restaurer* | *Système* | *F-08* |
| *Modifier* | *Bénévole de l'accueil* | *F-07* |
| *Consulter* | *Bénévole de l'accueil, coordinatrice, réparateur* | *F-02 à F-06* |
| *Prendre en charge* | *Réparateur* | *F-02* |
| *Ajout du diagnostic et du résultat* | *Réparateur* | *F-03* |

#### D-03 — Tableau de poids moyens par type d'objet
- **Contenu** : nom du type d'objet ; catégorie de l'objet ; poids moyen en kg
- **Volume** : liste fixe de quelques dizaines de types (à confirmer avec Q-10)
- **Origine** : tableau de poids moyens du réseau des Repair Cafés, fourni par Mme Moreau.
- **Conservation** : tant que l’application est utilisée.

| *Opération* | *Acteur* | *Fonctionnalité* |
| --- | --- | --- |
| *Consulter le poids des objets* | *Coordinatrice* | *F-06* |
| *Consulter le type d'objet* | *Bénévole de l'accueil* | *F-01* |
| *Modifier si changement de la liste* | *Coordinatrice* | - |

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
| F-06 | Générer le rapport imprimable pour la commune | Responsable | Souhaitable |
| F-07 | Gérer les coordonnées des visiteurs | Responsable, coordinatrice | Indispensable |
| F-08 | Sauvegarde automatique des données | Système | Souhaitable |
| F-09 | Rappel pour les objets « à suivre » | Coordinatrice | Optionnelle |

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
| **Priorité** | Souhaitable |
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
| **Priorité** | Souhaitable |
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

| | |
|---|---|
| **Auteur** | Valentin Thiel |
| **Acteur(s)** | Coordinatrice |
| **Priorité** | Optionnelle |
| **Description** | Quelques jours avant la session suivante, la coordinatrice retrouve la liste des visiteurs à appeler pour leur rappeler d'apporter la pièce nécessaire à la réparation (voir RM-03 et RM-04). |

**Exigences**
- **EF-09.1** : L’application affiche la liste des objets « à suivre », avec pour chacun le nom du visiteur, la pièce attendue et ce qu’il reste à faire.
- **EF-09.2** : Le numéro de téléphone du visiteur est affiché s'il l'a donné (voir RM-05). Sinon, la liste indique qu'il ne peut pas être contacté.
- **EF-09.3** : Un objet disparaît de la liste dès que son statut n'est plus « à suivre ».

**Critères d'acceptation**
- **EF-09.1** : La coordinatrice voit les fiches des objets « à suivre », avec le nom du visiteur et la pièce manquante.
- **EF-09.2** : Seuls les visiteurs ayant donné leur numéro apparaissent dans la liste, et leur numéro est affiché.
- **EF-09.3** : Quand un objet passe de « à suivre » à « réparé » ou « non réparable », il n'apparaît plus dans la liste.

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
| ENF-10 | Un guide utilisateur simple, rédigé sans jargon technique, est fourni aux bénévoles. | Relecture du guide par Mme Moreau. |

---

## 4. Contraintes

- **Matériel** : l'application doit fonctionner sur l'unique ordinateur portable Windows de l'association, datant d'environ 2015. Aucun achat de matériel n'est possible (voir ENF-02).

- **Connexion** : le wifi de la maison de quartier n'est pas fiable et l'ordinateur n'est pas toujours connecté. L'application doit s'installer et fonctionner entièrement hors ligne (voir ENF-01 et ENF-09).

- **Budget d'exploitation** : l'association n'a aucun budget pour le projet, réalisé en partenariat avec l'école. L'application et son utilisation ne doivent entraîner aucun coût.

- **Utilisateurs** : les bénévoles de l'accueil sont surtout des retraités avec des niveaux en informatique variables. L'interface doit être très simple, avec de grosses lettres et des boutons évidents (voir ENF-03).

- **Administration** : après le départ du petit-fils de Mme Moreau, qui compile actuellement les données, personne dans l'association n'est chargé de l'informatique. L'utilisation courante, y compris les sauvegardes, ne doit demander aucune intervention technique (voir F-08 et ENF-10).

- **Réglementation** : le traitement des coordonnées des visiteurs respecte le RGPD : accord du visiteur, utilisation uniquement pour le recontacter, effacement un an après son dernier passage (voir F-07 et ENF-08).

- **Obligations externes** : la commune demande chaque année le nombre d'objets reçus et réparés, ainsi que les kilos de déchets évités, séparés par catégorie. Les kilos sont estimés à partir d’un tableau de poids moyens par type d’objet, fourni par la cliente (voir F-06).

- **Délais** : l'application doit être utilisable avant le départ en Erasmus du petit-fils de Mme Moreau, en février.

---

## 5. Budget

L'association ne dispose d'aucun budget pour ce projet. L'application doit fonctionner sur l'ordinateur portable existant de l'association, datant d'environ 2015, sans aucun achat de matériel. Son utilisation ne doit entraîner aucun coût (voir section 4).

---

## 6. Livrables et planning

### 6.1. Livrables

L'association reçoit un programme qui fonctionne sur son ordinateur portable, sans connexion à Internet, accompagné d'un guide d'utilisation simple, rédigé pour des bénévoles qui ne sont pas à l'aise avec l'informatique (voir ENF-10). Le code source est également livré avec une documentation technique, destinée à toute personne qui reprendrait la maintenance de l'application (voir section 8).

L'application démarre sans données. La reprise des chiffres des années passées, contenus dans le fichier Excel actuel, afin de les intégrer aux statistiques, est optionnelle et ne sera réalisée que si le temps le permet.

### 6.2. Échéances

Une première version, limitée aux fonctionnalités indispensables (MVP), est présentée à Mme Moreau le 02/11/2026. Une version intermédiaire, comprenant davantage de fonctionnalités, est présentée le 23/11/2026. La version finale est livrée le 07/12/2026.

### 6.3. Retours vers le client

- Différents appels téléphoniques avec Mme Moreau, les bénévoles d'accueil et les réparateurs, entre le 19/10/2026 et le 14/11/2026, pour affiner les demandes et découvrir des contraintes métier et/ou des exigences fonctionnelles supplémentaires.
- Rendez-vous lors de la session du Repair Café du 14/11/2026, afin d'observer le fonctionnement d'une session et de confirmer, voire découvrir, des contraintes métier.
- Démonstration d'un MVP du produit avec Mme Moreau, les bénévoles d'accueil et les réparateurs le 02/11/2026.
- Démonstration d'une version intermédiaire du produit avec les mêmes parties prenantes, comprenant plus de fonctionnalités, le 23/11/2026.

---

## 7. Validation du projet

| | |
|---|---|
| **Qui** | Mme Moreau, les bénévoles de l'accueil et Loïc Martin |
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
- **Q-07** : Comme il n'y a qu'un seul ordinateur à l'accueil, comment les réparateurs notent-ils le diagnostic et le résultat de la réparation ?
- **Q-08** : Faut-il supprimer les fiches des objets à un moment ?
- **Q-09** : Que contient le tableau de poids moyens par type d'objet qui lui permet de faire le rapport annuel à la commune ?

---

## 10. Glossaire

| Terme | Définition |
|---|---|
| **MVP** | _Minimum Viable Product_ : première version livrée, limitée aux fonctionnalités indispensables. |

---

## 11. Annexes

- **Annexe A** : Transcription partielle du premier entretien avec Mme Moreau, intitulée « historique client » et disponible sur le dépôt GitHub.
