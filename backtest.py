import matplotlib.pyplot as plt
from data_fetcher import fetch_data
from strategy import calculate_spread

def backtest(
    ticker_a: str,
    ticker_b: str,
    start: str,
    end: str,
    window: int = 20,
    entry_z: float = 1.0
):
    # 1. Fetch price series
    price_a = fetch_data(ticker_a, start, end)
    price_b = fetch_data(ticker_b, start, end)

    # 2. Compute spread and z-score
    df, beta = calculate_spread(price_a, price_b, window)

    # 3. Generate positions
    df["PosA"] = 0
    df["PosB"] = 0
    df.loc[df["ZScore"] >  entry_z, ["PosA","PosB"]] = [-1,  beta]
    df.loc[df["ZScore"] < -entry_z, ["PosA","PosB"]] = [ 1, -beta]
    df[["PosA","PosB"]] = df[["PosA","PosB"]].ffill().fillna(0)

    # 4. Calculate returns
    df["RetA"] = df["A"].pct_change()
    df["RetB"] = df["B"].pct_change()
    df["StratRet"] = (
        df["PosA"].shift(1) * df["RetA"]
      + df["PosB"].shift(1) * df["RetB"]
    )
    df["Equity"] = (1 + df["StratRet"].fillna(0)).cumprod()

    # 5. Plot equity curve
    plt.figure(figsize=(10,6))
    plt.plot(df.index, df["Equity"], label="Equity Curve")
    plt.title(f"Pairs Trading Equity Curve: {ticker_a}/{ticker_b}")
    plt.xlabel("Date"); plt.ylabel("Equity Multiple")
    plt.legend(); plt.grid(True); plt.show()

    # 6. Print performance
    total_return = df["Equity"].iloc[-1] - 1
    print(f"Total return: {total_return:.2%}")
