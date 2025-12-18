import pandas as pd
import requests
from io import StringIO


def load_weather_data():
    """
    Récupère et nettoie les données météorologiques de Cambridge depuis le Met Office.
    
    Returns:
        pd.DataFrame: DataFrame contenant les données météorologiques nettoyées avec les colonnes :
                      yyyy, mm, tmax, tmin, af, rain, sun
    """
    # URL des données météorologiques
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
    df = pd.read_csv(
        data_text,
        skiprows=7,
        sep=r'\s+',
        names=['yyyy', 'mm', 'tmax', 'tmin', 'af', 'rain', 'sun'],
        na_values=['*', '---', '---*'],
        engine='python'
    )
    
    # Conversion de toutes les colonnes en types numériques
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df
