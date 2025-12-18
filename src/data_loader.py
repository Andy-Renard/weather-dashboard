import pandas as pd
import requests
from io import StringIO
from pathlib import Path


def load_weather_data():
    """
    Récupère et nettoie les données météorologiques de Cambridge depuis le Met Office.
    Utilise un système de cache local pour éviter les téléchargements répétés.
    
    Returns:
        pd.DataFrame: DataFrame contenant les données météorologiques nettoyées avec les colonnes :
                      yyyy, mm, tmax, tmin, af, rain, sun
    """
    # Définition du chemin du cache
    cache_dir = Path("data/cache")
    cache_file = cache_dir / "cambridge_data.csv"
    
    # Vérification si le fichier cache existe
    if cache_file.exists():
        print(f"Chargement des données depuis le cache : {cache_file}")
        df = pd.read_csv(cache_file)
        return df
    
    # Si le cache n'existe pas, téléchargement des données
    print("Téléchargement des données depuis le Met Office...")
    url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/cambridgedata.txt"
    
    # Récupération des données
    response = requests.get(url)
    response.raise_for_status()  # Vérifie les erreurs HTTP
    
    # Conversion du contenu en StringIO pour pandas
    data_text = StringIO(response.text)
    
    # Lecture du fichier avec pandas
    # skiprows=7 : ignore les 7 premières lignes d'en-tête
    # sep='\s+' : séparateur d'espaces variables
    # na_values : traite '*' et '---' comme NaN
    # on_bad_lines='skip' : ignore les lignes malformées (notes de bas de page, commentaires)
    df = pd.read_csv(
        data_text,
        skiprows=7,
        sep=r'\s+',
        names=['yyyy', 'mm', 'tmax', 'tmin', 'af', 'rain', 'sun'],
        na_values=['*', '---', '---*'],
        engine='python',
        on_bad_lines='skip'
    )
    
    # Conversion de toutes les colonnes en types numériques
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Création du dossier de cache s'il n'existe pas
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    # Sauvegarde dans le cache
    df.to_csv(cache_file, index=False)
    print(f"Données sauvegardées dans le cache : {cache_file}")
    
    return df
