import streamlit as st

# Configuration de la page (titre de l'onglet, icône, mise en page)
st.set_page_config(
    page_title="Municipality",
    page_icon="🗺️",
    layout="wide"
)

st.title("Municipality 🇫🇷")
st.write("Cette application permettra de visualiser la répartition des élus en France.")

# Navigation
# Define the pages with appropriate paths, titles, and icons
app_page = st.Page("pages/app.py", title="Accueil", icon="🏠")
cartography_page = st.Page("pages/cartography.py", title="Cartographie", icon="🗺️")
demography_page = st.Page("pages/demography.py", title="Démographie", icon="👥")
pyramid_page = st.Page("pages/pyramid.py", title="Pyramide des âges", icon="📊")
search_page = st.Page("pages/search.py", title="Recherche", icon="🔍")

# Set up navigation
pg = st.navigation([app_page, cartography_page, demography_page, pyramid_page, search_page])

# Run the selected page
pg.run()


