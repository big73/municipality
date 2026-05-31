from constants.config import LOCAL_FILE, MATCHING_COLUMNS
import pandas as pd

def load_csv():
    """
    Load the CSV file into a Pandas DataFrame.
    """
    # Lire le CSV en forçant les codes géographiques en str pour conserver les zéros initiaux
    # (ex: "01" pour l'Ain au lieu de 1) et éviter le DtypeWarning.
    df = pd.read_csv(
        LOCAL_FILE,
        dtype={
            "Code du département": str,
            "Code de la commune": str,
            "Code de la collectivité à statut particulier": str
        },
        low_memory=False
    )

    df.rename(columns=MATCHING_COLUMNS, inplace=True)

    # Normaliser les codes géographiques (remplissage avec des zéros initiaux)
    # Département sur 2 caractères (ex: "1" -> "01")
    df["code_departement"] = df["code_departement"].str.zfill(2)
    # Commune sur 5 caractères (ex: "1001" -> "01001")
    df["code_commune"] = df["code_commune"].str.zfill(5)

    # Calculer l'âge en utilisant le format de date correct (YYYY-MM-DD)
    df["date_naissance"] = pd.to_datetime(df["date_naissance"], format="%Y-%m-%d", errors="coerce")
    df["age"] = (pd.Timestamp.now() - df["date_naissance"]).dt.days // 365
    
    return df