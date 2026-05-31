from utils.loader import load_csv
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Main page content
st.markdown("# Pyramide des âges")
st.sidebar.markdown("# Pyramide des âges")

st.info(
    "💡 **Pyramide des âges :** Visualisez la répartition par tranche d'âge et par genre. "
    "Une base étroite indique une sous-représentation des jeunes, tandis qu'un sommet large "
    "montre une forte proportion d'élus expérimentés."
)

df = load_csv()

# Calculer les tranches d'âge
df_pyramid = df[df["age"].notna() & df["code_sexe"].notna()]

bins = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 120]
labels = [
    "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", 
    "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", 
    "75-79", "80-84", "85-89", "90+"
]

df_pyramid["tranche_age"] = pd.cut(df_pyramid["age"], bins=bins, labels=labels, right=False)

grouped = df_pyramid.groupby(["tranche_age", "code_sexe"], observed=False).size().reset_index(name="count")

# Séparation Hommes / Femmes
men_data = grouped[grouped["code_sexe"] == "M"].copy()
women_data = grouped[grouped["code_sexe"] == "F"].copy()

# Valeurs absolues pour hommes
men_data["count"] = -men_data["count"]

# Barres avec Plotly
fig = go.Figure(
    data=[
        go.Bar(
            y=men_data["tranche_age"],
            x=men_data["count"],
            orientation="h",
            name="Hommes",
            marker=dict(color="#3b82f6"),
            hoverinfo="text",
            hovertemplate="Hommes: %{x}"
        ),
        go.Bar(
            y=women_data["tranche_age"],
            x=women_data["count"],
            orientation="h",
            name="Femmes",
            marker=dict(color="#ec4899"),
            hoverinfo="text",
            hovertemplate="Femmes: %{x}"
        )
    ]
)

# Ajustements du design
max_val = grouped["count"].max()
fig.update_layout(
    barmode="overlay",
    bargap=0.1,
    title=dict(text="Pyramide des âges des élus municipaux", x=0.5),
    xaxis=dict(
        title="Nombre d'élus",
        gridcolor="rgba(200,200,200,0.2)",
        showgrid=True,
    ),
    yaxis=dict(
        title="Tranche d'âge",
        gridcolor="rgba(200,200,200,0.2)",
        showgrid=True
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.2,
        xanchor="center",
        x=0.5
    ),
    margin=dict(t=60, b=70, l=50, r=50),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    height=600
)

# Affichage
st.plotly_chart(fig, use_container_width=True)
