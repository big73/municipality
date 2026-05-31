import streamlit as st
import plotly.express as px

from utils.loader import load_csv, load_geojson

# Configuration de la page
st.markdown("# Cartographie")
st.sidebar.markdown("# Cartographie")

st.info(
    "🗺️ **Carte de France des élus :** Découvrez la répartition du nombre d'élus municipaux par département. "
    "Survolez les départements pour voir le détail."
)

# Chargement des données
df = load_csv()

# Agrégation des données par département
dept_data = df.groupby(["code_departement", "libelle_departement"], observed=False).size().reset_index(name="Nombre d'élus")

# Création de la carte
with st.spinner("Génération de la carte en cours..."):
    geojson = load_geojson()
    
    fig = px.choropleth_mapbox(
        dept_data,
        geojson=geojson,
        locations="code_departement",
        featureidkey="properties.code",
        color="Nombre d'élus",
        color_continuous_scale="Blues", # Un beau dégradé de bleus
        range_color=(0, dept_data["Nombre d'élus"].max()),
        mapbox_style="carto-positron", # Style de fond de carte clair et épuré
        zoom=4.8, # Zoom adapté pour afficher la France métropolitaine
        center={"lat": 46.5, "lon": 2.5},
        opacity=0.8,
        hover_name="libelle_departement",
        hover_data={"code_departement": True, "Nombre d'élus": True}
    )
    
    # Ajustement des marges pour utiliser tout l'espace disponible
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        height=700
    )

    st.plotly_chart(fig, use_container_width=True)