# Quantum computing vs Bitcoin

## Direct answer (today)

### Have quantum computers ever had a chance to break Bitcoin encryption *today*?
**No.**

**Why:** Breaking secp256k1 signatures with Shor’s algorithm needs a **cryptographically relevant quantum computer (CRQC)** — on the order of **~1,200–2,330 logical qubits** and historically **hundreds of thousands to hundreds of millions of physical qubits** with full fault tolerance. As of mid/late 2026, leading devices are about **~1,000–1,200 physical qubits** with demonstrated logical qubits only in the **tens to ~100**, and **no CRQC exists**. Google/EF/Stanford whitepaper (arXiv:2603.28846, 2026) states cryptographically relevant machines do not exist today. Gap remains roughly **hundreds of times** even under aggressive resource estimates.

Hype often confuses **noisy intermediate-scale** demos with **fault-tolerant cryptanalysis**.

---

## Two algorithms people mix up

| Algorithm | Target in Bitcoin | Practical threat |
|-----------|-------------------|------------------|
| **Shor** | ECDSA & Schnorr (ECDLP on secp256k1) | **Real** once CRQC exists — forge spends if pubkey known |
| **Grover** | SHA-256 / PoW / hash preimages | **Weak** — only quadratic speedup; FT overhead huge; difficulty adjusts |

PoW is **not** the main quantum story. Gershteyn & Alber “Quantum Horizon” (arXiv:2606.14484, June 2026) calibrate that even optimistic quantum miners stay far behind ASIC networks; Grover parallelizes poorly (\(\sqrt{K}\)).

---

## Resource estimates (selected)

| Year | Source | Rough requirement for ECC-256 / secp256k1 |
|------|--------|-------------------------------------------|
| 2017 | Roetteler et al. | ~2,330 logical qubits (P-256 class) |
| 2022 | Webber et al. | ~13M physical (1 day) to ~317M (1 hour), ~2,871 logical |
| 2026 | Babbush et al. (Google Quantum AI et al.) | ≤1,200–1,450 logical; &lt;500k physical; minutes on optimistic superconducting assumptions |
| 2026 | Cain et al. (neutral atoms) | Aggressive: tens of thousands physical under different assumptions |

**Uncertainty:** estimates keep falling with **better algorithms**, not because a CRQC was built. Conservative vs aggressive figures still span orders of magnitude.

### Timeline forecasts (not predictions)
Quantum Horizon Monte Carlo blend (surveys + physics): roughly **~1-in-6 chance of CRQC by 2035**, ~30% by 2040, ~60% by 2050; wide 80% band ~2032–2060. Expert surveys (GRI/Mosca) vs bottom-up physics **disagree by ~a decade**. Treat as **scenario planning**, not a date.

---

## Which coins / UTXOs are most exposed?

A coin is quantum-exposed when its **public key is on-chain**.

1. **P2PK / some multisig** — pubkey always visible (early Satoshi-era payouts).
2. **Reused P2PKH/P2WPKH** — pubkey revealed on first spend; leftovers exposed.
3. **Taproot (P2TR) key-path** — output is a public key; long-exposure risk.
4. **Fresh never-spent hash addresses** — protected **until** spend; then a short mempool race if a *fast* CRQC exists (“mempool sniping”).

**Scale (2025–26 chain analyses summarized in Quantum Horizon):**
- ~**6M BTC** (~30% supply) quantum-exposed in some sense.
- ~**2.3M BTC** (~12%) **irreducible** (dormant/lost; cannot migrate).
- ~**3.7M** migratable if owners act.
- ~65–70% in fresh hash-based outputs: safer at rest.

Theft of dormant Satoshi-era coins would be a **confidence shock** even if “only” a fraction of supply.

---

## Why people worry
1. **Harvest now, decrypt later:** collect exposed pubkeys today; crack later.
2. **Resource estimates dropped sharply** in 2025–26 (algorithmic).
3. **Migration is political:** Bitcoin changes slowly; freezing legacy spends is contentious.
4. **Media** conflates lab qubits with CRQC and mining with signature breaks.

---

## Migration paths (Bitcoin)
- **NIST PQC (Aug 2024):** ML-DSA (FIPS 204), SLH-DSA (FIPS 205), ML-KEM (FIPS 203); Falcon still in pipeline historically.
- **BIP-360** (draft/evolving): quantum-safer output type — Taproot-like **without** ECC key-path (P2MR / P2TSH naming has evolved). Does **not** by itself choose the final PQ signature scheme. See [bip360.org](https://bip360.org/).
- **BIP-361** (draft): staged sunset / friction for legacy ECDSA/Schnorr after PQ outputs exist — politically hard (dormant coin ethics).
- Soft-fork preference in culture; emergency hard-fork sketches exist in wider ecosystem literature.
- Binding constraint per Quantum Horizon: **governance speed**, not absence of PQ algorithms.

**Holder hygiene that helps even before PQ activates:**
- Never reuse addresses.
- Prefer modern wallets that avoid exposing keys until spend (understand Taproot tradeoffs).
- Plan to migrate when PQ output types are widely supported.

---

## Hype vs real
| Claim | Verdict |
|-------|---------|
| “Quantum already breaks BTC” | **False** (2026) |
| “Quantum will kill mining next year” | **Misleading** — Grover ≠ practical 51% |
| “All BTC equally exposed” | **False** — depends on script & reuse |
| “No need to think until 2050” | **Complacent** — migration takes years; start watching BIPs/NIST |
| “Must sell MSTR because of quantum this quarter” | **Not supported** by current capability — but long-term governance risk is real |

---

## For MSTR / Strategy specifically
Strategy’s coins are a **corporate custody + policy** problem as much as a crypto problem. Quantum risk to *their* UTXOs depends on how keys are stored and which address types they use (not fully public in detail). Separately, a market-wide quantum scare could crush BTC price → crush MSTR via β and mNAV — **even without** a successful attack.
