import yfinance as yf
import pandas as pd

def fetch_data(ticker: str, start: str, end: str) -> pd.Series:
    """
    Download Adjusted Close prices for a ticker.
    """
    df = yf.download(ticker, start=start, end=end, progress=False)
    return df["Adj Close"]
