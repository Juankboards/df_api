import pandas as pd

def transformJsonToDf(file):
    df = pd.read_json(file)

    return df

def get_columns(file, columns):
    df = pd.read_json(file)
    columns_df = pd.DataFrame(df[columns])

    return columns_df

def change_columns_names(file, changes):
    df = pd.read_json(file)
    renamed_df = df.rename(columns=changes)

    return renamed_df

def cleanNaColumns(file, drop_type):
    df = pd.read_json(file)
    clean_df = df.dropna(axis='columns', how=drop_type)

    return clean_df
