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