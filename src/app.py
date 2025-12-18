import streamlit as st
import pandas as pd
from src.data_loader import load_weather_data
from src.analysis import calculate_rolling_trends, get_top_records
from src.visualization import (
    plot_temperature_trends,
    plot_precipitation_bar,
    plot_extreme_heatmap
)

# Configuration de la page
st.set_page_config(
    page_title="Tableau de bord météo - Cambridge",
    page_icon="🌤️",
    layout="wide"
)

# Titre principal
st.title("🌤️ Tableau de bord météo : Cambridge")

# Introduction
st.markdown("""
Bienvenue sur le tableau de bord météorologique interactif de Cambridge ! 
Cette application analyse les données historiques du Met Office britannique pour explorer 
les tendances climatiques, les précipitations et les températures extrêmes.

**Source des données :** Met Office UK - Station météorologique de Cambridge
""")

st.divider()

# Chargement des données avec un spinner
with st.spinner("Chargement des données météorologiques..."):
    df = load_weather_data()

# Barre latérale - Filtres
st.sidebar.header("⚙️ Paramètres")

# Déterminer la plage d'années disponibles
min_year = int(df['yyyy'].min())
max_year = int(df['yyyy'].max())

# Slider pour sélectionner la plage d'années
year_range = st.sidebar.slider(
    "Sélectionner la plage d'années",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1
)

st.sidebar.markdown(f"""
**Période sélectionnée :** {year_range[0]} - {year_range[1]}
""")

# Filtrage des données selon la plage d'années sélectionnée
df_filtered = df[(df['yyyy'] >= year_range[0]) & (df['yyyy'] <= year_range[1])].copy()

# Affichage des statistiques générales
st.sidebar.divider()
st.sidebar.subheader("📊 Statistiques générales")
st.sidebar.metric("Nombre d'années", year_range[1] - year_range[0] + 1)
st.sidebar.metric("Nombre de mesures", len(df_filtered))

# Calcul des tendances avec les données filtrées
df_annual = calculate_rolling_trends(df_filtered, window=10)

# Section 1 : Évolution des températures
st.header("📈 Évolution des températures")
st.markdown("Analyse des tendances de température avec une moyenne mobile sur 10 ans.")

fig_temp = plot_temperature_trends(df_annual)
st.plotly_chart(fig_temp, use_container_width=True)

# Section 2 : Précipitations
st.header("💧 Précipitations annuelles")
st.markdown("Visualisation des précipitations moyennes par année.")

fig_precip = plot_precipitation_bar(df_annual)
st.plotly_chart(fig_precip, use_container_width=True)

# Section 3 : Carte de chaleur des températures maximales
st.header("🔥 Carte de chaleur des températures maximales")
st.markdown("Distribution des températures maximales mensuelles au fil des années.")

fig_heatmap = plot_extreme_heatmap(df_filtered)
st.plotly_chart(fig_heatmap, use_container_width=True)

# Section 4 : Records historiques
st.header("🏆 Records historiques")
st.markdown("Les mois les plus extrêmes enregistrés à Cambridge.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 Les 10 mois les plus chauds")
    top_hot = get_top_records(df_filtered, 'tmax', n=10)
    
    # Formatage du tableau
    display_hot = top_hot[['yyyy', 'mm', 'tmax']].copy()
    display_hot.columns = ['Année', 'Mois', 'Température max (°C)']
    display_hot = display_hot.reset_index(drop=True)
    display_hot.index = display_hot.index + 1
    
    st.dataframe(display_hot, use_container_width=True)

with col2:
    st.subheader("💧 Les 10 mois les plus pluvieux")
    top_rain = get_top_records(df_filtered, 'rain', n=10)
    
    # Formatage du tableau
    display_rain = top_rain[['yyyy', 'mm', 'rain']].copy()
    display_rain.columns = ['Année', 'Mois', 'Précipitations (mm)']
    display_rain = display_rain.reset_index(drop=True)
    display_rain.index = display_rain.index + 1
    
    st.dataframe(display_rain, use_container_width=True)

# Pied de page
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <p>Données fournies par le Met Office UK | Tableau de bord créé avec Streamlit et Plotly</p>
</div>
""", unsafe_allow_html=True)
