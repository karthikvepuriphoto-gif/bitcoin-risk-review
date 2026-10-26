#!/usr/bin/env python3
"""Compute MSTR beta vs BTC-USD and SPY. Not financial advice."""
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf

OUT = Path(__file__).resolve().parents[1] / "data"


def close_col(df: pd.DataFrame) -> pd.Series:
    if isinstance(df.columns, pd.MultiIndex):
        c = df["Close"]
        return c.iloc[:, 0] if getattr(c, "ndim", 1) > 1 else c
    return df["Close"]


def main() -> None:
    end = datetime.now()
    start = end - timedelta(days=365 * 5)
    mstr = yf.download("MSTR", start=start.strftime("%Y-%m-%d"), auto_adjust=True, progress=False)
    btc = yf.download("BTC-USD", start=start.strftime("%Y-%m-%d"), auto_adjust=True, progress=False)
    spy = yf.download("SPY", start=start.strftime("%Y-%m-%d"), auto_adjust=True, progress=False)

    df = pd.concat(
        [
            close_col(mstr).rename("MSTR"),
            close_col(btc).rename("BTC"),
            close_col(spy).rename("SPY"),
        ],
        axis=1,
    ).dropna()
    rets = df.pct_change().dropna()

    rows = []
    for name, days in [("1Y", 365), ("2Y", 730), ("5Y", None)]:
        w = rets if days is None else rets.loc[rets.index >= (rets.index.max() - pd.Timedelta(days=days))]
        if len(w) < 20:
            continue
        rows.append(
            {
                "window": name,
                "mstr_beta_vs_btc": round(float(w["MSTR"].cov(w["BTC"]) / w["BTC"].var()), 2),
                "mstr_beta_vs_spy": round(float(w["MSTR"].cov(w["SPY"]) / w["SPY"].var()), 2),
                "mstr_ann_vol": round(float(w["MSTR"].std() * (252**0.5)), 3),
                "btc_ann_vol": round(float(w["BTC"].std() * (252**0.5)), 3),
                "vol_ratio_mstr_btc": round(float(w["MSTR"].std() / w["BTC"].std()), 2),
                "corr_mstr_btc": round(float(w["MSTR"].corr(w["BTC"])), 3),
                "n_days": len(w),
            }
        )
    OUT.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUT / "mstr_btc_beta.csv", index=False)
    df.to_csv(OUT / "mstr_btc_spy_prices.csv")
    print(pd.DataFrame(rows).to_string(index=False))


if __name__ == "__main__":
    main()
