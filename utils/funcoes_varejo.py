import pandas as pd
from datetime import datetime

def padronizar_data(df, DATA):
    """
    Converte a coluna de DATA (string) para o tipo datetime.
    Usa dayfirst=True pois o formato da base é dd/mm/yyyy.
    Datas inválidas viram NaT e são reportadas.
    """
    df[DATA] = pd.to_datetime(df[DATA], dayfirst=True, errors='coerce')
    
    invalidas = df[DATA].isna().sum()
    print(f'Datas inválidas (NaT) em "{DATA}": {invalidas}')
    print(f'Tipo da coluna após conversão: {df[DATA].dtype}')
    
    return df