import pandas as pd 
import os

def load_file(filepath):
    #Detect file type
    if filepath.endswith(".csv"):
        df = pd.read_csv(filepath)
    elif filepath.endswith((".xlsx", ".xls")):
        df = pd.read_excel(filepath)
    else:
        return None
    

    return df