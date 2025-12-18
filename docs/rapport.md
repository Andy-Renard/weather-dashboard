# Rapport d'Analyse : Dashboard Météo Cambridge

## 1. Introduction
Ce projet consiste en la création d'une application web interactive d'analyse de données météorologiques historiques pour la ville de Cambridge (Royaume-Uni). L'objectif est de transformer des données brutes provenant du Met Office en indicateurs visuels exploitables pour observer l'évolution climatique.

## 2. Architecture Technique
L'application repose sur une architecture modulaire en Python :
* **Collecte et Nettoyage (`data_loader.py`)** : Récupération des données par HTTP et gestion du cache local pour optimiser les performances.
* **Traitement Statistique (`analysis.py`)** : Calcul des moyennes annuelles et des tendances glissantes sur 10 ans.
* **Visualisation (`visualization.py`)** : Génération de graphiques interactifs (Scatter plots, Bar charts, Heatmaps) avec la bibliothèque Plotly.
* **Interface Utilisateur (`app.py`)** : Orchestration de l'application via le framework Streamlit.

## 3. Analyse des Données de Cambridge
L'analyse des relevés historiques met en évidence plusieurs points clés :
* **Tendance Thermique** : La courbe de tendance lissée montre une augmentation progressive de la température moyenne annuelle au cours des dernières décennies.
* **Saisonalité et Extrêmes** : La "Heatmap" permet d'identifier visuellement les étés caniculaires récents, confirmant une fréquence accrue des pics de chaleur.
* **Précipitations** : Les données montrent une forte variabilité annuelle, essentielle pour comprendre les risques de sécheresse ou d'inondation locale.

## 4. Utilisation de l'IA (GitHub Copilot)
L'intelligence artificielle a servi de "partenaire de programmation" tout au long du cycle de développement :
* **Accélération** : Génération rapide des structures de base pour les fonctions de calcul et de visualisation.
* **Débuggage** : Aide précieuse pour interpréter les erreurs de parsing (`ParserError`) liées au format complexe du fichier source.
* **Optimisation** : Suggestions pertinentes pour le nettoyage des données (conversion numérique et gestion des valeurs manquantes).

## 5. Défis Rencontrés et Solutions
* **Format de Données Complexe** : Le fichier source présentait des colonnes à espacement variable et des notes de bas de page.
    * *Solution* : Utilisation de paramètres avancés dans Pandas (`sep=r'\s+'` et `on_bad_lines='skip'`).
* **Erreurs de Syntaxe de l'IA** : L'IA a parfois suggéré des méthodes obsolètes ou légèrement erronées (ex: `update_yaxis` au lieu de `update_yaxes`).
    * *Solution* : Vérification systématique via les messages d'erreur et consultation de la documentation officielle de Plotly.

## 6. Conclusion
Ce projet démontre qu'une collaboration efficace entre un développeur et une IA permet de produire une application robuste et professionnelle en un temps réduit. La modularité du code assure une maintenance facile et permet d'envisager l'ajout de nouvelles stations météo à l'avenir.