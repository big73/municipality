import streamlit as st
import plotly.express as px
from utils.loader import load_csv

# Main page content
st.markdown("# Démographie")
st.sidebar.markdown("# Démographie")

# load dataframe
df = load_csv()

# Distribution des âges ordonnée par âge
st.subheader("Distribution des âges")
st.bar_chart(df["age"].value_counts().sort_index())

# Parité hommes femmes format camembert avec Plotly
st.subheader("Parité hommes femmes")

# Préparation des données
gender_counts = df["code_sexe"].value_counts().reset_index()
gender_counts.columns = ["Genre", "Nombre"]
gender_counts["Genre"] = gender_counts["Genre"].map({"M": "Hommes", "F": "Femmes"})

# Création d'un donut chart ultra-premium
fig = px.pie(
    gender_counts, 
    values="Nombre", 
    names="Genre", 
    color="Genre",
    color_discrete_map={"Hommes": "#3b82f6", "Femmes": "#ec4899"},
    hole=0.4
)

# Ajustement esthétique du graphique
fig.update_layout(
    margin=dict(t=10, b=10, l=10, r=10),
    legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5)
)

st.plotly_chart(fig, use_container_width=True)

# Population par code départment format bar chart
st.subheader("Population par département")

# Préparation des données
department_counts = df["code_departement"].value_counts().reset_index()
department_counts = department_counts.sort_values(by="code_departement")
print(department_counts)

# Bar chart avec ordre par departement ascendant
st.bar_chart(department_counts, x="code_departement", y="count")

