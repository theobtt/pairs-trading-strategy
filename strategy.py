import numpy as np
import pandas as pd

def calculate_spread(price_a: pd.Series, price_b: pd.Series, window: int = 20):
    """
    Aligns two price series, fits beta via OLS,
    computes spread, rolling mean/std, and z-score.
    Returns a DataFrame and the estimated beta.
    """
    df = pd.DataFrame({"A": price_a, "B": price_b}).dropna()
    beta = np.polyfit(df["B"], df["A"], 1)[0]
    df["Spread"] = df["A"] - beta * df["B"]
    df["Mean"]   = df["Spread"].rolling(window=window).mean()
    df["Std"]    = df["Spread"].rolling(window=window).std()
    df["ZScore"] = (df["Spread"] - df["Mean"]) / df["Std"]
    return df, beta
