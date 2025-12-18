import pandas as pd


def get_top_records(df, column, n=10):
    """
    Retourne les n lignes ayant les valeurs les plus hautes pour une colonne donnée.
    
    Args:
        df (pd.DataFrame): Le DataFrame contenant les données météorologiques
        column (str): Le nom de la colonne à analyser (ex: 'tmax', 'rain', 'sun')
        n (int): Le nombre de lignes à retourner (par défaut 10)
    
    Returns:
        pd.DataFrame: Les n lignes avec les valeurs les plus élevées, triées par ordre décroissant
    """
    # Tri par ordre décroissant et sélection des n premiers
    # dropna() ignore les valeurs manquantes
    top_records = df.sort_values(by=column, ascending=False, na_position='last').head(n)
    
    return top_records


def calculate_annual_averages(df):
    """
    Calcule la température moyenne annuelle à partir des températures maximales et minimales.
    
    Étapes :
    1. Calcule la température moyenne (tmean) = (tmax + tmin) / 2
    2. Regroupe les données par année
    3. Calcule la moyenne annuelle pour toutes les variables
    
    Args:
        df (pd.DataFrame): Le DataFrame contenant les données météorologiques
                          avec les colonnes 'yyyy', 'tmax', 'tmin'
    
    Returns:
        pd.DataFrame: DataFrame avec les moyennes annuelles pour chaque variable
    """
    # Création d'une copie pour éviter de modifier le DataFrame original
    df_copy = df.copy()
    
    # Calcul de la température moyenne (moyenne arithmétique entre tmax et tmin)
    # Les NaN sont automatiquement propagés dans le calcul
    df_copy['tmean'] = (df_copy['tmax'] + df_copy['tmin']) / 2
    
    # Regroupement par année et calcul de la moyenne annuelle
    # Le paramètre numeric_only=True ignore les colonnes non numériques
    annual_averages = df_copy.groupby('yyyy').mean(numeric_only=True)
    
    return annual_averages


def calculate_rolling_trends(df, window=10):
    """
    Applique une moyenne mobile sur les températures moyennes annuelles pour lisser
    les variations saisonnières et faire ressortir les tendances climatiques à long terme.
    
    Args:
        df (pd.DataFrame): Le DataFrame contenant les données météorologiques
                          avec les colonnes 'yyyy', 'tmax', 'tmin'
        window (int): La taille de la fenêtre pour la moyenne mobile (par défaut 10 ans)
    
    Returns:
        pd.DataFrame: DataFrame avec une colonne 'tmean_trend' représentant la tendance lissée
    """
    # Calcul des moyennes annuelles
    annual_avg = calculate_annual_averages(df)
    
    # Application de la moyenne mobile (rolling mean)
    # min_periods=1 permet de calculer la moyenne même si la fenêtre n'est pas complète
    # center=False pour une moyenne mobile arrière (utilise les valeurs passées)
    annual_avg['tmean_trend'] = annual_avg['tmean'].rolling(
        window=window, 
        min_periods=1,
        center=False
    ).mean()
    
    return annual_avg
