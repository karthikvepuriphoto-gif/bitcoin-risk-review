# How Bitcoin “encryption” works today

People say “Bitcoin encryption.” More precisely: Bitcoin uses **hashing** (SHA-256, RIPEMD-160) and **digital signatures** (ECDSA / Schnorr on secp256k1). Coins are not encrypted blobs; they are **locked to a public key or script** and spent by proving you hold the matching private key.

---

## Plain English

1. You create a huge random **private key** (like a secret password number).
2. From it, math on an elliptic curve produces a **public key** (safe to share in principle).
3. An **address** is usually a short fingerprint (hash) of that public key or of a script.
4. To spend, you publish a **signature** that only the private key could make, over the transaction details.
5. Miners / nodes check the signature and that you haven’t double-spent; they do **not** need your private key.
6. **Mining** is a separate race: repeatedly hash block headers with SHA-256 until the hash is below a difficulty target.

**Quantum worry (preview):** a future quantum computer running Shor’s algorithm could derive the private key **from the public key**. So the question becomes: *is your public key already visible on-chain?*

---

## Precise terms

### SHA-256 (and mining)
- **SHA-256:** cryptographic hash; 256-bit output; preimage resistance assumed classically.
- Bitcoin mining: double-SHA-256 on the block header; first to find nonce/extra-nonce such that `H < target` wins the block reward + fees.
- Difficulty adjusts ~every 2016 blocks (~2 weeks) to keep ~10-minute blocks.
- Transaction IDs, Merkle trees, and many commitments also use SHA-256.

### ECDSA on secp256k1 (legacy / still widely used)
- Curve: **secp256k1** — \(y^2 = x^3 + 7\) over a 256-bit prime field.
- Private key \(d\): integer in \(1..n-1\).
- Public key \(P = d \cdot G\) (elliptic-curve scalar multiplication of generator \(G\)).
- Hard problem: **ECDLP** — recover \(d\) from \(P\).
- Sign: hash message to \(z\), pick nonce \(k\), compute \(R = kG\), \(s = k^{-1}(z + r d) \mod n\), signature \((r,s)\).
- **Critical:** reusing nonce \(k\) across messages leaks \(d\) (famous wallet failures).

### Schnorr (BIP-340) / Taproot (BIPs 341/342)
- Activated Nov 2021 (block 709,632).
- Schnorr: signature \((R, s)\) with \(sG = R + eP\), \(e = H(R \| P \| m)\) (tagged hashes).
- Benefits: smaller fixed 64-byte sigs, proof-friendly security, **linearity** (MuSig aggregation), batch verify.
- Taproot output: tweaked public key; **key-path spend** looks like a single Schnorr sig; **script-path** reveals a Merkle branch.

### Address types (simplified)

| Type | Locking object | Pubkey on-chain before spend? |
|------|----------------|-------------------------------|
| **P2PK** (pay-to-pubkey) | raw pubkey | **Yes always** (early coins, incl. many Satoshi-era) |
| **P2PKH** | HASH160(pubkey) | No until first spend |
| **P2WPKH** (SegWit v0) | HASH160(pubkey) in witness program | No until first spend |
| **P2SH / P2WSH** | hash of script | Keys revealed when script path used |
| **P2TR** (Taproot) | 32-byte x-only pubkey (tweaked) | **Yes at rest** for key-path design (long-exposure quantum concern) |

### What is hashed vs what is signed
- **Hashed:** block headers (PoW), txids (transaction serialization), scripts/addresses (HASH160), Taproot tweaks, Merkle proofs.
- **Signed:** the sighash of the spending transaction (which inputs/outputs/amounts/scripts are covered depends on SIGHASH flags). The signature proves authorization; it does not encrypt the transaction (Bitcoin txs are public).

### Why addresses hide the public key (until they don’t)
- P2PKH/P2WPKH store `HASH160(pubkey)`. Preimage resistance means you cannot get the pubkey (hence cannot run ECDLP) from the address alone.
- **On first spend**, the pubkey is revealed in the input/witness → forever known for that key.
- **Address reuse** after that leave balances **exposed at rest**.
- **P2PK** and **Taproot key-path outputs** expose key material earlier by design.

---

## Mental model for security assumptions
- **Integrity of ownership:** ECDLP hard + good nonce hygiene + secure key storage.
- **Integrity of history / scarcity:** SHA-256 PoW + economic majority hashrate + social consensus on rules (21M cap enforced by node software).
- **Privacy:** weak by default (public ledger); address hygiene helps a little; not a cryptography failure.
