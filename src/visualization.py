import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def plot_temperature_trends(df_annual):
    """
    Trace l'évolution de la température moyenne annuelle avec la courbe de tendance mobile.
    
    Args:
        df_annual (pd.DataFrame): DataFrame avec les moyennes annuelles contenant
                                  les colonnes 'tmean' et 'tmean_trend', indexé par année
    
    Returns:
        go.Figure: Graphique Plotly interactif montrant les températures et la tendance
    """
    # Création de la figure
    fig = go.Figure()
    
    # Ajout de la courbe de température moyenne annuelle
    fig.add_trace(go.Scatter(
        x=df_annual.index,
        y=df_annual['tmean'],
        mode='lines+markers',
        name='Température moyenne annuelle',
        line=dict(color='#FF6B6B', width=2),
        marker=dict(size=4),
        opacity=0.7
    ))
    
    # Ajout de la courbe de tendance mobile
    fig.add_trace(go.Scatter(
        x=df_annual.index,
        y=df_annual['tmean_trend'],
        mode='lines',
        name='Tendance mobile (10 ans)',
        line=dict(color='#4ECDC4', width=3),
    ))
    
    # Mise en forme du graphique
    fig.update_layout(
        title={
            'text': 'Évolution de la température moyenne à Cambridge',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'family': 'Arial, sans-serif'}
        },
        xaxis_title='Année',
        yaxis_title='Température moyenne (°C)',
        hovermode='x unified',
        template='plotly_white',
        font=dict(size=12),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        )
    )
    
    return fig


def plot_precipitation_bar(df_annual):
    """
    Affiche les précipitations totales annuelles sous forme de graphique à barres.
    
    Args:
        df_annual (pd.DataFrame): DataFrame avec les moyennes annuelles contenant
                                  la colonne 'rain', indexé par année
    
    Returns:
        go.Figure: Graphique Plotly à barres des précipitations annuelles
    """
    # Création du graphique à barres
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=df_annual.index,
        y=df_annual['rain'],
        name='Précipitations',
        marker=dict(
            color=df_annual['rain'],
            colorscale='Blues',
            showscale=True,
            colorbar=dict(title='mm')
        ),
        hovertemplate='<b>Année:</b> %{x}<br>' +
                      '<b>Précipitations:</b> %{y:.1f} mm<br>' +
                      '<extra></extra>'
    ))
    
    # Mise en forme du graphique
    fig.update_layout(
        title={
            'text': 'Précipitations moyennes annuelles à Cambridge',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'family': 'Arial, sans-serif'}
        },
        xaxis_title='Année',
        yaxis_title='Précipitations moyennes (mm)',
        template='plotly_white',
        font=dict(size=12),
        showlegend=False
    )
    
    return fig


def plot_extreme_heatmap(df):
    """
    Génère une carte de chaleur montrant les températures maximales par mois et par année.
    
    Args:
        df (pd.DataFrame): DataFrame contenant les colonnes 'yyyy', 'mm' et 'tmax'
    
    Returns:
        go.Figure: Carte de chaleur Plotly des températures maximales
    """
    # Création d'un pivot table avec années en lignes et mois en colonnes
    heatmap_data = df.pivot_table(
        values='tmax',
        index='yyyy',
        columns='mm',
        aggfunc='mean'  # En cas de doublons, prendre la moyenne
    )
    
    # Noms des mois en français
    month_names = {
        1: 'Jan', 2: 'Fév', 3: 'Mar', 4: 'Avr', 5: 'Mai', 6: 'Juin',
        7: 'Juil', 8: 'Août', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Déc'
    }
    
    # Renommer les colonnes avec les noms de mois
    heatmap_data.columns = [month_names.get(col, col) for col in heatmap_data.columns]
    
    # Création de la carte de chaleur
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=heatmap_data.columns,
        y=heatmap_data.index,
        colorscale='RdYlBu_r',  # Rouge pour chaud, bleu pour froid
        colorbar=dict(title='°C'),
        hovertemplate='<b>Mois:</b> %{x}<br>' +
                      '<b>Année:</b> %{y}<br>' +
                      '<b>Température max:</b> %{z:.1f}°C<br>' +
                      '<extra></extra>'
    ))
    
    # Mise en forme du graphique
    fig.update_layout(
        title={
            'text': 'Carte de chaleur des températures maximales mensuelles',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'family': 'Arial, sans-serif'}
        },
        xaxis_title='Mois',
        yaxis_title='Année',
        template='plotly_white',
        font=dict(size=12),
        height=700,  # Hauteur ajustée pour une meilleure lisibilité
    )
    
    # Inverser l'axe Y pour avoir les années récentes en haut
    fig.update_yaxes(autorange='reversed')
    
    return fig
