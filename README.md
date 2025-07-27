# 🧠 Reincarnator – An Eremos Swarm Agent

**Detecting Recycled Smart Contracts and Reactivated Wallets on Solana**

Solana moves fast — and so do the scammers. Old smart contracts return in new wrappers. Dormant wallets reawaken to deploy the same grifts. **Reincarnator** is a compound-detection agent built with the Eremos framework to surface these *reincarnations* by linking reused contract logic, reactivated wallets, CEX funneling, and metadata mutations.

---

## 🚨 What It Detects

| Pattern | Behavior |
|--------|----------|
| 🧬 Code Cloning | Smart contracts with near-identical logic to historical ones (≥ 95% similarity) |
| 💤 Dormant Wallet Deploys | Contracts deployed by wallets inactive for ≥ 90 days |
| 🧟‍♂️ Wallet Reincarnations | Wallets tied to previous scams now deploying again |
| 🪄 Metadata Mutations | Token deploys with identical logic but minor tweaks in `name`, `symbol`, or supply |
| 🏦 Airdrop CEX Funnels | Multiple airdrop recipients funneling to the same CEX address |

---

## 🧠 Core Detection Logic

1. **Monitor Deployments**
   - Subscribes to all new program and SPL token deploys
   - Extracts bytecode or token metadata/state layout

2. **Fingerprint the Contract**
   - Normalizes contract constants (e.g., name, fees, supply)
   - Generates fingerprint (AST hash, Wasm structure, etc.)
   - Compares against historical fingerprints (≥ 95% match triggers step 3)

3. **Analyze Wallet Behavior**
   - Flags wallets inactive ≥ 90 days
   - Checks prior scam associations and funding sources (CEX, mixers, bridges)

4. **Track Airdrop Funnels**
   - Detects airdrop claim wallets funneling to the same destination (CEX or single wallet)

5. **Check Metadata Mutations**
   - Flags token deploys with matching logic but altered metadata fields

6. **Emit High-Severity Alert**
   - Alert is triggered only when multiple suspicious traits overlap

---

## 🏗 Eremos Integration

| Function | Eremos Module |
|---------|----------------|
| Code Fingerprinting | `CodeSimilarityModule` (AST/Wasm diff) |
| Wallet Activity | `WalletActivityModule` |
| Risk Attribution | `WalletProfiler`, `FundingSourceModule` |
| Airdrop Funnels | `AirdropFlowAnalyzer` |
| Metadata Diffing | `TokenDeployNormalizer` |
| Alert Triggering | `SwarmAgent` core logic |
| Output & Scoring | `SignalReporter`, `SeverityScorer` |

---

## 📦 Output Formats

The agent emits alerts in structured JSON format, ready for:

- Analyst dashboards
- Discord alerting systems
- Token explorer warning badges
- API integrations with firewalls and risk engines

```json
{
  "signal": "reincarnation_detected",
  "fingerprint_match": 0.97,
  "wallet_status": "dormant",
  "wallet_risk_score": 88,
  "code_hash": "0xabc123...",
  "original_contract": "TokenXYZ_v1",
  "current_contract": "TokenXYZ_v2",
  "metadata_variance": true,
  "airdrop_funneling": true,
  "severity": "high"
}
