# Pairs Trading Strategy Backtester

A simple Python-based mean-reversion backtester that uses historical price spreads and z-score thresholds to generate trading signals for two correlated assets.

---

## Overview

This project demonstrates a basic **pairs trading** strategy:

1. **Fetch** adjusted close prices for two tickers.  
2. **Estimate** the hedge ratio (β) via linear regression.  
3. **Compute** the price spread: `spread = price_A − β × price_B`.  
4. **Calculate** rolling mean and standard deviation of the spread, then derive a z-score.  
5. **Generate** long/short signals when the z-score crosses ±entry thresholds.  
6. **Backtest** the strategy, plot the equity curve, and report total return.

---

## Installation

1. **Clone or download** this repository:  
   ```bash
   git clone https://github.com/your-username/pairs-trading-strategy.git
   cd pairs-trading-strategy
