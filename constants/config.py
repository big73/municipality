# data url
from pathlib import Path

DATA_URL = "https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260505-151851/elus-conseillers-municipaux-cm.csv"
DATA_DIR = Path("data")
LOCAL_FILE = DATA_DIR / "elus_municipaux.csv"

MATCHING_COLUMNS = {
    "Code du département": "code_departement",
    "Libellé du département": "libelle_departement",
    "Code de la collectivité à statut particulier": "code_collectivite_statut_particulier",
    "Libellé de la collectivité à statut particulier": "libelle_collectivite_statut_particulier",
    "Code de la commune": "code_commune",
    "Libellé de la commune": "libelle_commune",
    "Nom de l'élu": "nom_elu",
    "Prénom de l'élu": "prenom_elu",
    "Code sexe": "code_sexe",
    "Date de naissance": "date_naissance",
    "Code de la catégorie socio-professionnelle": "code_categorie_socio_professionnelle",
    "Libellé de la catégorie socio-professionnelle": "libelle_categorie_socio_professionnelle",
    "Date de début du mandat": "date_debut_mandat",
    "Libellé de la fonction": "libelle_fonction",
    "Date de début de la fonction": "date_debut_fonction",
    "Code nationalité": "code_nationalite"
}