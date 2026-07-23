import pandas as pd


def create_new_features(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()
    df["balance_per_product"] = df["balance"] / df["products_number"]
    df["balance_per_tenure"] = df["balance"] / (df["tenure"] + 1)

    return df
