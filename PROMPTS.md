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
