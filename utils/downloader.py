import pandas as pd
import streamlit as st
from constants.config import DATA_URL, LOCAL_FILE


@st.cache_data(show_spinner=False)
def download_csv():
    """
    Télécharge le fichier CSV s'il n'est pas présent localement,
    puis le charge dans un DataFrame Pandas depuis le fichier local.
    """

    if not LOCAL_FILE.exists():
        LOCAL_FILE.parent.mkdir(parents=True, exist_ok=True)
        df = pd.read_csv(DATA_URL, sep=";", low_memory=False)
        df.to_csv(LOCAL_FILE, index=False)

        print('File downloaded successfully:', LOCAL_FILE)

    return LOCAL_FILE
