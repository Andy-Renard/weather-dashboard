# 🌦️ Weather Dashboard - Cambridge

Un tableau de bord interactif permettant d'analyser les données climatiques historiques de la station de Cambridge (UK). Ce projet utilise les données officielles du **Met Office** pour visualiser les tendances du réchauffement climatique et les records de précipitations.

## Fonctionnalités
- **Acquisition automatique** : Téléchargement et parsing des données depuis l'URL officielle.
- **Mise en cache** : Sauvegarde locale des données pour un chargement instantané.
- **Analyse Statistique** : Calcul des moyennes annuelles, records historiques et tendances lissées (moyenne mobile 10 ans).
- **Visualisations Interactives** : Graphiques d'évolution, barres de précipitations et carte de chaleur (Heatmap) réalisés avec Plotly.
- **Interface Web** : Dashboard complet et filtrable par période avec Streamlit.

## Installation et Configuration

Pour faire fonctionner ce projet sur votre machine, suivez précisément les étapes suivantes dans votre terminal :

### 1. Préparation de l'environnement
Avant de lancer l'application, vous devez installer les bibliothèques logicielles nécessaires (dépendances). Nous utilisons un fichier `requirements.txt` pour automatiser cette étape et garantir la compatibilité du projet.

**Commande à exécuter :**
```bash
python -m pip install -r requirements.txt
```

**À quoi sert cette commande ?**

* **`python -m pip` :** Lance le gestionnaire de paquets Python de manière sécurisée en s'assurant qu'il correspond à la version de Python installée sur votre système.

* **`install -r requirements.txt` :** Lit le fichier de configuration à la racine du projet et installe automatiquement toutes les bibliothèques indispensables (Pandas, Plotly, Streamlit, Requests). Cela permet de recréer l'environnement de développement exact.

### 2. Lancement du Dashboard
Une fois les dépendances installées, vous pouvez démarrer l'interface utilisateur web interactive.

Commande à exécuter :

```bash
python -m streamlit run src/app.py
```

**À quoi sert cette commande ?**

* **`python -m streamlit run` :** Démarre le serveur local de l'application Streamlit.

* **`src/app.py` :** Indique au programme le chemin du fichier principal qui orchestre l'interface et les visualisations.

* **Résultat :** Une page web s'ouvrira automatiquement dans votre navigateur pour afficher le tableau de bord.

## Structure du projet
`src/data_loader.py` : Acquisition des données via URL, nettoyage (gestion des NaN et ParserError) et mise en cache locale.

`src/analysis.py` : Logique des calculs statistiques (moyennes, tendances glissantes, records).

`src/visualization.py` : Fonctions de génération des graphiques interactifs avec la bibliothèque Plotly.

`src/app.py` : Interface utilisateur réalisée avec Streamlit qui assemble tous les modules.

`docs/rapport.md` : Rapport d'analyse final détaillant les choix techniques et les conclusions sur les données.

`PROMPTS.md` : Journal de bord documentant l'utilisation de l'IA (GitHub Copilot) pour chaque étape du projet.