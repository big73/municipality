from constants.config import LOCAL_FILE, MATCHING_COLUMNS
import pandas as pd

def load_csv():
    """
    Load the CSV file into a Pandas DataFrame.
    """
    df = pd.read_csv(LOCAL_FILE)

    df.rename(columns=MATCHING_COLUMNS, inplace=True)
    
    return df