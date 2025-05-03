import pandas as pd
import os

def leer_excel(path, name_sheet):
    try:
        df = pd.read_excel(path, sheet_name=name_sheet)
        return df
    except FileNotFoundError:
        print(f"❌ El archivo '{path}' no se encuentra en la carpeta 'input/'")
        return None
    except ValueError as e:
        print(f"❌ Error al leer la hoja '{name_sheet}': {e}")
        return None
