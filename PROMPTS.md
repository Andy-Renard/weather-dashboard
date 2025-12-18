# Journal des Prompts - Weather Dashboard 

Ce document retrace l'intégralité de mon processus de réflexion et mes interactions avec l'IA pour la réalisation du projet.

---

## 🛠 Phase 1 : Acquisition et Nettoyage des données

### Tâche 1.1 : Téléchargement et Parsing (data_loader.py)
**Date :** 18 décembre 2025

**Prompt utilisé :**  
>"Je travaille sur un projet de tableau de bord météorologique en Python 3.10 et j'ai besoin de configurer le fichier `src/data_loader.py`. Peux-tu rédiger une fonction nommée `load_weather_data` qui utilise les bibliothèques `pandas` et `requests` pour récupérer les données depuis l'adresse : [URL]. Pour le parsing, il faut ignorer les 7 premières lignes d'en-tête et utiliser un séparateur d'espaces variables (`sep='\s+'`). Les colonnes doivent être nommées explicitement : 'yyyy', 'mm', 'tmax', 'tmin', 'af', 'rain' et 'sun'. Enfin, traite les symboles '*' et '---' comme des valeurs manquantes (`NaN`) et convertis toutes les colonnes en types numériques."

**Réflexion et Critique :**
* **Qualité du résultat :** L'IA a parfaitement intégré la structure complexe du fichier texte (espaces variables) et a ajouté `response.raise_for_status()` pour la sécurité.
* **Esprit Critique :** J'ai vérifié manuellement le fichier source pour confirmer que 7 lignes d'en-tête devaient être sautées.
* **Apprentissage :** J'ai compris comment utiliser `StringIO` pour lire un texte brut directement dans un DataFrame sans créer de fichier temporaire.  

---

### Tâche 1.2 : Mise en cache locale (src/data_loader.py)
**Date :** 18 décembre 2025

**Prompt utilisé :**
>"Je souhaite améliorer ma fonction load_weather_data dans le fichier src/data_loader.py en y ajoutant un système de mise en cache locale. L'objectif est d'optimiser le programme pour qu'il ne télécharge pas les données à chaque exécution. Peux-tu modifier le code pour qu'il vérifie d'abord si le fichier data/cache/cambridge_data.csv existe déjà sur mon ordinateur ? Si le fichier est présent, la fonction doit charger les données directement depuis ce CSV local. S'il est absent, la fonction doit procéder au téléchargement depuis l'URL du Met Office comme auparavant, puis sauvegarder le DataFrame obtenu dans le dossier data/cache/ avant de le retourner. Merci d'utiliser la bibliothèque os ou pathlib pour la gestion des chemins et de t'assurer que le dossier de cache est créé s'il n'existe pas encore."

**Réflexion et Critique :**
* **Qualité du résultat :** L'IA a utilisé `pathlib`, ce qui rend le code plus lisible et compatible entre Windows et Mac/Linux. Elle a bien pensé à créer le dossier automatiquement s'il n'existe pas.
* **Esprit Critique :** J'ai vérifié que la sauvegarde du cache se fait *après* le nettoyage numérique des données. C'est un bon choix technique, car le fichier CSV local sera ainsi "propre" et prêt à l'emploi dès sa lecture.
* **Apprentissage :** J'ai appris à utiliser `mkdir(parents=True)` pour créer une structure de dossiers imbriqués en une seule ligne de code.

---

## 🛠 Phase 2 : Analyse Statistique des Données

### Tâche 2.1 : Fonctions d'analyse statistique (src/analysis.py)
**Date :** 18 décembre 2025

**Prompt utilisé :**
>"Je travaille maintenant sur le fichier src/analysis.py pour mon projet de tableau de bord météo. Peux-tu rédiger une série de fonctions utilisant la bibliothèque pandas pour analyser le DataFrame que j'ai récupéré ? J'ai besoin d'une première fonction get_top_records(df, column, n=10) qui retourne les $n$ lignes ayant les valeurs les plus hautes pour une colonne spécifique (comme 'tmax' ou 'rain'). Ensuite, crée une fonction calculate_annual_averages(df) qui calcule une nouvelle colonne pour la température moyenne (la moyenne arithmétique entre 'tmax' et 'tmin') puis regroupe les données par année pour obtenir une moyenne annuelle globale. Enfin, ajoute une fonction calculate_rolling_trends(df, window=10) qui applique une moyenne mobile sur 10 ans sur les températures moyennes afin de lisser les variations saisonnières et faire ressortir la tendance climatique. Merci d'inclure des commentaires explicatifs (docstrings) et de t'assurer que les calculs ignorent correctement les valeurs manquantes (NaN)."

**Réflexion et Critique :**
* **Qualité du résultat :** L'IA a produit un code très robuste. L'utilisation de `pd.to_numeric` dans l'étape précédente porte ses fruits ici car les fonctions Pandas fonctionnent parfaitement.
* **Esprit Critique :** J'ai vérifié la formule de `tmean`. Faire la moyenne de `tmax` et `tmin` est la méthode standard acceptée dans ce projet pour estimer la température moyenne mensuelle.
* **Apprentissage :** J'ai découvert le concept de "fenêtre glissante" (rolling window) pour l'analyse de séries temporelles.

---

## 🛠 Phase 3 : Visualisation Interactive des Données

### Tâche 3.1 : Création des graphiques Plotly (src/visualization.py)
**Date :** 18 décembre 2025

**Prompt utilisé :**
>"Je travaille maintenant sur le fichier src/visualization.py pour mon projet de dashboard météo. Peux-tu rédiger des fonctions utilisant la bibliothèque plotly pour créer des graphiques interactifs basés sur mon analyse ? J'ai besoin d'une première fonction plot_temperature_trends(df_annual) qui trace l'évolution de la température moyenne annuelle ('tmean') ainsi que la courbe de tendance mobile ('tmean_trend') sur le même graphique. Ensuite, crée une fonction plot_precipitation_bar(df_annual) pour afficher les précipitations totales ('rain') sous forme de graphique à barres par année. Enfin, ajoute une fonction plot_extreme_heatmap(df) qui génère une carte de chaleur montrant les températures maximales ('tmax') avec les années en axe vertical et les mois en axe horizontal. Toutes ces fonctions doivent retourner un objet Figure de Plotly pour être facilement intégrables dans une interface Streamlit. Assure-toi que les titres et les axes sont clairement libellés en français et que les graphiques sont esthétiques."

**Réflexion et Critique :**
* **Qualité du résultat :** L'IA a généré des graphiques très complets avec des infobulles (hovertemplates) personnalisées.
* **Esprit Critique :** J'ai particulièrement apprécié l'inversion de l'axe Y dans la heatmap (`autorange='reversed'`), ce qui permet de voir les années les plus récentes en haut, rendant la lecture plus intuitive.
* **Apprentissage :** J'ai appris à utiliser `pivot_table` pour restructurer des données avant de les injecter dans une Heatmap, et l'importance des "color scales" pour représenter des données de température (rouge pour le chaud, bleu pour le froid).

---

## 🛠 Phase 4 : Interface Utilisateur (Dashboard Web)

### Tâche 4.1 : Création de l'application Streamlit (src/app.py)
**Date :** 18 décembre 2025

**Prompt utilisé :**
>"Je souhaite finaliser mon projet en créant l'interface utilisateur dans le fichier src/app.py avec la bibliothèque Streamlit. L'application doit importer les fonctions load_weather_data de src.data_loader, calculate_rolling_trends et get_top_records de src.analysis, ainsi que les trois fonctions de visualisation de src.visualization. L'interface doit afficher un titre 'Tableau de bord météo : Cambridge' suivi d'une brève introduction. Ajoute une barre latérale avec un curseur (st.sidebar.slider) permettant de filtrer les données selon une plage d'années définie par l'utilisateur. Dans le corps principal, affiche les graphiques interactifs (évolution des températures, précipitations et heatmap) en utilisant les données filtrées. Enfin, ajoute une section pour afficher les records historiques sous forme de tableaux simples pour les mois les plus chauds et les plus pluvieux. Assure-toi que la mise en page est propre et que les erreurs d'importation sont évitées."

**Réflexion et Critique :**
* **Qualité du résultat :** L'interface est très intuitive. L'utilisation d'un `sidebar` pour les filtres laisse tout l'espace central pour les graphiques.
* **Esprit Critique :** J'ai dû m'assurer que les données étaient bien filtrées *avant* de recalculer les tendances mobiles, sinon la courbe de tendance n'aurait pas correspondu à la période sélectionnée à l'écran.
* **Apprentissage :** J'ai appris à orchestrer un projet multi-fichiers en Python et à utiliser les composants de mise en page de Streamlit (colonnes, métriques, diviseurs).