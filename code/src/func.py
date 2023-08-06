
import pandas as pd
import numpy as np



def check_nan_cols(df: pd.DataFrame, method = 'sum', disp = True) -> pd.Series:
    
    """
    check_nan_cols: recibe un dataframe y retorna una serie, con el número de 
    nulos por cada columna del dataframe (method = 'sum'), o el porcentaje 
    (method = 'avg').
    Si se asigna a una variable, muestra el resultado con las columnas que
    tengan nulos, a menos que se indique lo contrario (disp = False).
    """

    nan_cols = df.isna().sum() if method == 'sum' else round(df.isna().mean() * 100, 2)
    
    if disp:
        print(nan_cols[nan_cols > 0])
    
    return nan_cols



def cols_info(df: pd.DataFrame) -> pd.DataFrame:

    """
    Devuelve información detallada de cada columna.
    """

    cols_info = {}

    for col in df:
        info = {
            'Col Type': df[col].dtype,
            'Nulos': df[col].isna().sum(),
            'Str': df[col].apply(lambda x: isinstance(x, str)).sum(),
            'Float': df[col].apply(lambda x: isinstance(x, float)).sum(),
            'Int': df[col].apply(lambda x: isinstance(x, int)).sum(),
            'Bool': df[col].apply(lambda x: isinstance(x, bool)).sum(),
            'Date': df[col].apply(lambda x: isinstance(x, np.datetime64)).sum(),
            'Float == Nan': df[col].isna().all(),
            'Unique': df[col].nunique(),
            'Unique %': round(df[col].nunique() / df.shape[0] * 100, 2),
        }
        cols_info[col] = info
    
    df = pd.DataFrame(cols_info).T
    
    return df.loc[:, (df != 0).any()]