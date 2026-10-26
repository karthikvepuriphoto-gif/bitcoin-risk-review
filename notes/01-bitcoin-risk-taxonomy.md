# Bitcoin risk taxonomy (long-term holder lens)

**As of:** 2026-10-25 (America/Chicago).  
**Purpose:** Concrete risks ranked roughly by **severity × plausibility** for a multi-year holder.  
**Not financial advice.** Citations are primary or well-known public sources; label uncertainty where estimates disagree.

Severity × plausibility scores are **researcher judgment** (1–5 each → product). They are for prioritization, not probability forecasts.

| Rank | Risk cluster | Sev | Plaus | Score | One-line |
|------|--------------|-----|-------|-------|----------|
| 1 | Market / macro drawdowns & path-dependency | 5 | 5 | 25 | Multi-year −50% to −80% drawdowns have already happened |
| 2 | Custody & operational key loss | 5 | 4 | 20 | Permanent loss of coins; no recovery court |
| 3 | Regulatory / policy shock (esp. US, major economies) | 4 | 3 | 12 | Ban unlikely in US 2026 path, but tax/banking/ETF rules can reprice |
| 4 | Leverage & market-structure cascades | 4 | 4 | 16 | Futures, basis, liquidations amplify moves |
| 5 | Mining / consensus concentration | 4 | 2 | 8 | Pool/geo concentration real; sustained 51% attack costly |
| 6 | Protocol / consensus bugs | 5 | 1–2 | 5–10 | Inflation bugs exist historically; rare, high impact |
| 7 | Cryptography / quantum (signatures) | 5 | 1–2 near-term; rising later | 5–10 | No CRQC today; timeline uncertain (see quantum note) |
| 8 | Competitor L1s / stablecoin monetary competition | 3 | 3 | 9 | BTC can lose mindshare without “breaking” |
| 9 | Energy / ESG / political narrative | 2 | 3 | 6 | Narrative risk; physical energy use is real |
| 10 | Black swans (war, internet partition, major exchange collapse) | 4 | 2 | 8 | Fat tails; hard to price |

---

## 1. Protocol / technology

### Consensus splits & software bugs
- **CVE-2018-17144** (Bitcoin Core disclosure 2018-09-20): consensus inflation bug in 0.15–0.16.2 allowing a miner to create coins via duplicate inputs; also crash DoS in 0.14.x. Never exploited on mainnet; fixed before disclosure. Source: [bitcoincore.org notice](https://bitcoincore.org/en/2018/09/20/notice/).
- Historical hard-fork politics (BTC/BCH 2017) show social consensus can split the brand and liquidity even when code is “fine.”
- **Implication for holders:** keep client diversity awareness; large consensus changes (soft forks) are governance events.

### 51% attacks
- A majority of hashrate can reorder recent blocks, censor, or double-spend *their own* deposits elsewhere; cannot steal arbitrary UTXOs without keys.
- **Cost:** rises with hashrate; Schwab institutional note (2026) argues capex, energy, hardware supply, and competition make sustained attack expensive relative to extractable value under many assumptions. Source: [Schwab](https://www.schwab.com/learn/story/valuing-crypto-through-lens-51-attack).
- **Concentration (geo):** HashrateIndex Q3 2026 — US ~36.7%, Russia ~17.2%, China ~12.2%; top 3 ≈ 66%. Source: [HashrateIndex Q3 2026](https://hashrateindex.com/blog/global-hashrate-heatmap-update-q3-2026/).
- **Pools ≠ one attacker:** Top pools often exceed 50% *combined*, but miners can leave pools; coordination and reputation costs are high. Still a structural concern.

### Mining concentration / ASIC supply
- ASIC manufacturing historically concentrated (e.g., Bitmain and peers). Energy competition with AI/HPC (2025–26 mining reviews) can raise miner costs and increase selling pressure after halvings.

---

## 2. Cryptography
See `04-quantum-threat.md` and `03-bitcoin-cryptography.md`.
- **Today:** classical ECDSA/Schnorr on secp256k1 remains unbroken in practice.
- **Quantum:** Shor threatens signatures once a fault-tolerant CRQC exists; Grover is a weak threat to SHA-256/PoW.
- **Exposure today:** reused addresses, P2PK, and Taproot key-path expose public keys at rest.

---

## 3. Custody
| Model | Main risk | Notes |
|-------|-----------|-------|
| Self-custody (seed/hardware) | Loss, theft, inheritance failure | No counterparty; user is the bank |
| Exchange / custodian | Insolvency, hack, freeze, jurisdiction | Mt. Gox, FTX-type failures are precedents |
| ETF custody concentration | Operational/reg concentration | Spot ETF BTC custody still heavily Coinbase-linked in industry reporting (~80%+ range cited 2026); Fidelity and others diversify some funds |

SEC proposed broader crypto custody pathways for advisers/funds (Federal Register 2026-10-06) — regulatory *evolution*, not a ban signal.

---

## 4. Regulatory (US / global)
- **US (as of late 2026):** Spot BTC ETFs exist; OCC/SEC activity has been toward regulated custody rather than prohibition. Policy can still change with elections, tax treatment, bank capital rules, or sanctions.
- **ETF flows:** Large daily creations/redemptions can amplify short-term price; also deepen liquidity and institutional ownership.
- **Global bans:** China mining ban (2021) did not kill BTC; underground hashrate returned (HashrateIndex estimates). Full global ban is low plausibility; fragmented hostility is medium.
- **Stablecoin / banking rules** can affect on-ramps without touching the protocol.

---

## 5. Market structure
- High leverage on perpetual futures; forced liquidations cascade.
- Miner selling after reward halvings; treasury companies (incl. Strategy) can be buyers or, under stress, sellers.
- Basis/cash-and-carry and options markets transmit risk across venues.
- Liquidity thins in crashes; slippage for large holders is real.

---

## 6. Macroeconomic
- BTC often behaves as a high-beta risk asset in liquidity-driven regimes (correlation with tech/NASDAQ varies by year).
- Real rates, USD strength, and risk-off episodes have historically coincided with large drawdowns (e.g., 2022).
- “Digital gold” narrative competes with “levered tech beta” narrative — which one dominates is regime-dependent (**uncertainty**).

---

## 7. Energy / ESG narrative
- PoW energy use is large and visible; political attacks recur.
- Counter-narratives (stranded energy, grid balancing) exist; impact on price is narrative/regulatory more than physical for holders outside mining.

---

## 8. Competitors
- Other L1s compete for developer/mindshare; they have not replaced BTC’s monetary niche yet.
- Dollar stablecoins compete as *medium of exchange*; BTC’s thesis is more store-of-value / scarce asset.
- Path-dependency: network effects, liquidity, and brand are BTC’s moat — and also why a confidence shock (quantum theft of Satoshi-era coins, major ban) could be nonlinear.

---

## 9. Black swans
- Major war affecting chip/energy supply chains.
- Prolonged internet partition (hard for global UTXO set sync).
- Simultaneous failure of top custodians/exchanges.
- Successful theft of a large visible UTXO set (quantum or classical key compromise) → confidence shock even if “only” 10–12% of supply.

---

## 10. Adoption / path-dependency
- ETF and corporate treasury adoption can reverse.
- Cultural/political identity of BTC affects policy.
- Ossification vs upgrade capacity (relevant for post-quantum migration — governance is the binding constraint per 2026 research).

---

## Practical takeaway for a long-term holder
The **highest expected pain** historically has been **price path + leverage + custody mistakes**, not protocol failure. Protocol and quantum risks are **fat-tailed** (rare but severe). Treat custody as non-negotiable hygiene; treat quantum as a **multi-year migration watch**, not a 2026 trading panic.
