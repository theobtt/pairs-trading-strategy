import argparse
from backtest import backtest

def main():
    p = argparse.ArgumentParser(
        description="Pairs Trading Backtest: two tickers, date range, window, entry z-score"
    )
    p.add_argument("ticker_a", help="First stock ticker (long leg)")
    p.add_argument("ticker_b", help="Second stock ticker (short leg)")
    p.add_argument("--start",  required=True, help="YYYY-MM-DD")
    p.add_argument("--end",    required=True, help="YYYY-MM-DD")
    p.add_argument("--window", type=int, default=20,  help="Rolling window size")
    p.add_argument("--entry_z",type=float, default=1.0, help="Z-score entry threshold")
    args = p.parse_args()

    backtest(
        args.ticker_a,
        args.ticker_b,
        args.start,
        args.end,
        args.window,
        args.entry_z
    )

if __name__ == "__main__":
    main()
