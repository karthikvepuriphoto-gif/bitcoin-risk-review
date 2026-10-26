# Bitcoin & MSTR risk review

Deep-dive notes for a long-term holder with **heavy MicroStrategy / Strategy Inc (MSTR)** exposure: Bitcoin risk taxonomy, MSTR-specific leverage and capital-structure risks, how Bitcoin cryptography actually works, and whether quantum computers threaten it **today**.

**As of:** 2026-10-25 (America/Chicago).  
**Not financial advice.** Educational research only. Figures go stale; re-check Strategy 8-Ks and primary papers.

## Direct answers (start here)

### Have quantum computers broken — or had a real chance to break — Bitcoin encryption today?
**No.** There is no cryptographically relevant quantum computer (CRQC). Breaking secp256k1 with Shor’s algorithm needs on the order of **~1,200+ logical qubits** and (under published assumptions) **~0.5–320 million physical qubits** with fault tolerance. 2026 hardware is roughly **~1,000–1,200 physical qubits** with logical qubits still in the tens–low hundreds. See [`notes/04-quantum-threat.md`](notes/04-quantum-threat.md).

### How does Bitcoin “encryption” work?
Bitcoin mostly uses **hashes** (SHA-256) and **digital signatures** (ECDSA/Schnorr on secp256k1), not encryption of coin balances. Your **private key** signs spends; **addresses** often hide the public key until first spend. Details: [`notes/03-bitcoin-cryptography.md`](notes/03-bitcoin-cryptography.md).

### Top risks if you are long a lot of MSTR
1. **BTC price path** — MSTR has recently run ~**1.5× beta** and ~**1.9× volatility** vs BTC (1Y, yfinance through 2026-10-23).
2. **Junior equity** — ~$6.7B debt + ~$14B preferred notionals sit above common; ~$1.58B/yr interest+dividends.
3. **Dilution / ATM / credit flywheel reversing** — issuance can help or hurt BTC-per-share.
4. **mNAV compression** — stock can lag BTC if the premium (~1.20× in early Oct 2026 briefing) collapses.
5. **Custody & confidence shocks** on BTC itself (exchange failures historically; quantum is a **future** fat tail).

Full MSTR write-up: [`notes/02-mstr-specific-risks.md`](notes/02-mstr-specific-risks.md).

## Repo layout

```
notes/
  01-bitcoin-risk-taxonomy.md   # protocol, custody, reg, market, macro, ranked
  02-mstr-specific-risks.md     # holdings, debt/pref, beta, mNAV
  03-bitcoin-cryptography.md    # SHA-256, ECDSA, Schnorr, addresses
  04-quantum-threat.md          # Shor vs Grover, timelines, BIPs
  05-monitoring-checklist.md    # watches & hedge types (descriptive)
data/
  mstr_btc_beta.csv
  mstr_btc_spy_prices.csv
scripts/
  mstr_btc_beta.py
sources.md
```

## Strategy snapshot (Oct 2026, company materials)

| Metric | Value | As of |
|--------|-------|-------|
| BTC held | **848,517** | Oct 18, 2026 (8-K / STRE briefing) |
| Approx. mark | ~$69B at ~$81k/BTC | Oct 18 assumptions |
| Debt notional | ~$6.71B | Oct 4 briefing |
| Preferred notional | ~$13.95B | Oct 4 briefing |
| USD Assets | ~$5.3–5.7B | Oct 4–18 |
| mNAV | ~1.20× | Oct 2 market / Oct 4 company framework |
| Amplification | ~1.25× | same |

MSTR is **not** a Bitcoin ETF. Common shareholders have **no redeemable claim** on the coins.

## MSTR vs BTC (measured)

Daily returns, Yahoo Finance, through **2026-10-23**:

| Window | β(MSTR, BTC) | Correlation | Vol(MSTR)/Vol(BTC) |
|--------|--------------|-------------|--------------------|
| 1Y | 1.53 | 0.81 | 1.89× |
| 2Y | 1.46 | 0.75 | 1.95× |
| 5Y | 1.32 | 0.75 | 1.77× |

Sample max drawdowns: MSTR **−84%**, BTC **−77%**. Re-run:

```bash
python3 -m venv .venv && .venv/bin/pip install yfinance pandas
.venv/bin/python scripts/mstr_btc_beta.py
```

## Bitcoin risk ranking (severity × plausibility, judgment)

See taxonomy note for scoring detail. Short version for long-term holders:

| Priority | Cluster | Why |
|----------|---------|-----|
| Highest day-to-day | Market drawdowns + leverage cascades | Already observed −50% to −80% paths |
| Highest irreversible | Custody / key loss | No undo |
| High structural | MSTR junior claim, dilution, mNAV | Extra layer on BTC |
| Medium | Regulation, ETF plumbing, miner geo concentration | Reprices; rarely “ends” BTC alone |
| Fat-tail / low near-term | Consensus bugs, CRQC signature breaks | Rare, severe; quantum **not** today |

## Quantum Q&A (plain words)

**Why worry at all?**  
Shor’s algorithm can turn a **visible public key** into a private key on a big enough fault-tolerant quantum computer, letting an attacker forge a spend.

**Is mining broken by Grover?**  
Not in any practical sense discussed in 2026 literature: quadratic speedup + enormous error-correction cost + difficulty adjustment.

**Which coins are scariest?**  
Pay-to-public-key and reused addresses; many early coins; Taproot outputs expose a key at rest. Fresh one-time hash addresses are safer until spent.

**What is the industry doing?**  
NIST standardized post-quantum signatures (2024). Bitcoin has draft BIPs (e.g. BIP-360 output types, BIP-361 migration/sunset ideas). Activation is a **governance** project measured in years.

**Timeline vibe (uncertain):** research ensembles put a non-trivial but minority chance of CRQC by ~2035 and better-than-even by ~2050 — with huge error bars. Prepare by tracking migration; don’t confuse press-release qubit counts with cryptanalysis.

## Monitoring

Use [`notes/05-monitoring-checklist.md`](notes/05-monitoring-checklist.md): BTC leverage & ETF flows, Strategy 8-Ks (BTC count, USD reserve, ATM), mNAV, preferred stress, BIP/quantum milestones, custody hygiene.

Hedges people discuss (puts, short BTC futures, rotating MSTR→spot BTC) are listed **descriptively only**.

## Disclaimer

This repository is for research education. It is **not** investment, legal, tax, or accounting advice. Cryptocurrency and MSTR are extremely volatile and can go to zero. Verify every number against primary SEC filings and peer-reviewed or preprint sources before acting.
