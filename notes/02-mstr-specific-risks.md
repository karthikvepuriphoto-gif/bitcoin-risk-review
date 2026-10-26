# MSTR / Strategy Inc — risks on top of Bitcoin

**Entity:** Strategy Inc (formerly MicroStrategy), Nasdaq: **MSTR** (common), plus preferreds STRF/STRC/STRK/STRD/STRE, convertibles.  
**Snapshot dates:** Company investor materials Oct 2–18, 2026; market prices via Yahoo Finance through 2026-10-23.  
**Not financial advice.** Company metrics (mNAV, Net Reserve, Amplification, BTC Rating) are **supplemental/illustrative**, not GAAP NAV or liquidation value — Strategy says so explicitly.

---

## Capital structure snapshot (Oct 2026)

| Item | Figure | Source / date |
|------|--------|----------------|
| BTC holdings | **848,000** (Oct 4) → **848,517** (Oct 18) | MSTR Investor Briefing as of 2026-10-04; STRE Briefing / Oct 19 8-K as of 2026-10-18 |
| Share of BTC supply | ~4.04% | MSTR Briefing Oct 2 dashboard |
| Avg cost basis | ~$75,446 / BTC (Oct 18 cost $64.02B) | TokenPost citing company; Oct 18 |
| BTC Reserve mark | ~$71.48B at $84,289 (Oct 4) / ~$69.13B at $81,468 (Oct 18) | Company briefings |
| USD Assets | $5,711M (Oct 4) → $5,280M (Oct 18: Reserve $4,833M + Cash $447M) | Same |
| Debt notional | ~$6.71B | MSTR Briefing |
| Preferred notional | ~$13.95B | MSTR Briefing |
| Net Reserve (company metric) | ~$57.33B | MSTR Briefing Oct 4 |
| Market cap (basic) | ~$67.54B at $160.01 (Oct 2 close) | MSTR Briefing |
| mNAV | **1.20×** | Price / Net BTC per share |
| Amplification | **1.25×** | BTC Reserve / Net Reserve |
| Annual int + pref dividends | ~$1.58B | MSTR Briefing |
| USD coverage of int+div | ~3.4–3.6 years at then-current run-rate | Briefings |
| YTD capital raised (through Oct 4) | ~$21.18B (common $13.66B + pref $7.52B) | MSTR Briefing |

**Critical structural note (company’s own words):** MSTR is **common equity, junior to all debt and preferred stock**. It is **not** a spot bitcoin ETF; shareholders have **no direct claim** on specific bitcoin.

Convertible notes (example from Sept 30, 2025 8-K — structure evolves; verify latest 10-Q/8-K): series due 2028–2032 with coupons from 0% to 2.25%, multi-billion aggregate. Preferred stack includes STRC (variable high coupon, non-convertible flagship), STRF, STRK (convertible into MSTR at 0.1 share per STRK when terms allow), STRD, STRE (euro perpetual, non-convertible).

---

## MSTR-specific risk list

### 1. Levered BTC proxy (without a fixed leverage ratio)
- Economic value is dominated by BTC holdings minus senior claims.
- Company “Amplification” ~1.25× at Oct 2026 snapshot means residual reserve is *somewhat* levered to BTC — **and amplification rises if BTC falls** (denominator Net Reserve shrinks faster).
- Common is last in line: debt + prefs (~$20B+ notional class) sit above.

### 2. Dilution: ATM equity, convertibles, preferreds
- Ongoing **ATM sales of MSTR** fund BTC buys and liquidity (e.g., Oct 12–18, 2026: 140,872 shares → $22M net → 267 BTC).
- Preferred issuance creates **senior claims and ~$1.58B/yr cash burden**.
- Convertibles can dilute if converted when in-the-money.
- Dilution can still raise **BTC per share** if issuance is at a premium and proceeds buy BTC — or **destroy** per-share value if issued into weakness. Path-dependent.

### 3. mNAV premium/discount
- At 1.20× mNAV (Oct 2), market priced a modest premium to Net BPS.
- Premium can collapse to 1.0× or a discount; then MSTR can **underperform BTC even if BTC rises**.
- Company sensitivity table (illustrative): Net Reserve/share ~$45.83 at $40k BTC vs ~$132.89 at $84,289 — mechanical BTC sensitivity before mNAV multiple changes.

### 4. Governance / key-person
- Strategy and public narrative heavily associated with Michael Saylor (Executive Chairman) and capital-markets execution by management (CEO Phong Le et al.).
- Board policy (USD Reserve, buybacks, BTC monetization) can change; **not contractual protection for common**.

### 5. Accounting (fair value) & EPS volatility
- Fair-value accounting for bitcoin produces large non-cash swings in GAAP earnings (e.g., Q3 2025 release highlighted large net income tied to BTC marks — historical example of the mechanism).
- Complicates traditional P/E; tax valuation allowances can flip.

### 6. Debt / preferred stress if BTC crashes
- No classic bank-style margin loan on BTC disclosed as the core model; risk is **refinancing + dividend coverage + forced capital markets access**.
- Company model metrics: BTC Floor ARR ~−17%, Breakeven ~2.2%, Hurdle ~10.6% (Oct briefing) — **illustrative**, not covenants.
- USD Reserve is Board policy for pref dividends & interest (12-month minimum), funded partly via equity — can be changed.
- BTC Monetization Program (up to $1.25B+ authority) allows selling BTC for liquidity — reduces upside for common.

### 7. Equity volatility vs spot BTC (measured)
From Yahoo Finance daily closes (trading days), 2021-10-26 → 2026-10-23:

| Window | β (MSTR on BTC) | Corr | Ann. vol MSTR | Ann. vol BTC | Vol ratio |
|--------|-----------------|------|---------------|--------------|-----------|
| 1Y | **1.53** | 0.81 | 82% | 44% | **1.89×** |
| 2Y | **1.46** | 0.75 | 86% | 44% | **1.95×** |
| 5Y | **1.32** | 0.75 | 91% | 52% | **1.77×** |

Yearly β vs BTC: 2022 1.34; 2023 1.11; 2024 1.37; 2025 1.37; 2026 YTD **1.58**.  
Max drawdown in sample: MSTR **−84%**, BTC **−77%**.  
Company briefing (Oct 2): Hist vol 1Y ~80%, 30D ~94%; noted **−55% 1Y return** at that snapshot.

**Interpretation:** MSTR has recently moved ~1.3–1.6× BTC on average daily beta, with nearly **2×** realized volatility — plus idiosyncratic mNAV/financing noise.

### 8. Tax
- Holding MSTR is equity taxation (cap gains), not the same as holding BTC directly (which has its own lot tracking).
- Preferred ROC character (company expectations for some 2026 pref distributions) does **not** flow to common as a structural benefit.
- Corporate-level tax on BTC gains can affect book equity / deferred taxes.

### 9. Index inclusion / exclusion
- Inclusion in major indices can force buying; exclusion or capping (volatility, single-stock concentration rules) can force selling.
- High options open interest (~$43B cited Oct 2) means dealer hedging can amplify moves.

### 10. Software business is not a hedge
- Q2 2026 software revenue ~$122.4M — real but small vs ~$70B BTC reserve. Enterprise value remains BTC-dominated.

---

## How MSTR differs from spot BTC / IBIT

| | Spot BTC / spot ETF | MSTR |
|--|---------------------|------|
| Claim on coins | Direct / trust | None |
| Leverage | Usually 1× (ETF) | Structural (debt+pref) + mNAV |
| Dilution | Expense ratio | ATM, convert, prefs |
| Cash yield burden | Low | ~$1.58B int+div run-rate |
| Tracking error | Low | High (β, mNAV, news) |
| Bankruptcy remote? | ETF structures vary | Corporate credit stack |

---

## Bottom line for heavy MSTR holders
You are long **BTC + corporate leverage + capital-markets franchise − senior claims − dilution optionality − governance**. The same flywheel that grew BTC/share can reverse via mNAV crush, closed financing windows, or sustained BTC below the cost of credit. Size the position for **equity-like 70–90%+ vol** and **worse drawdowns than BTC**, not for ETF tracking.
