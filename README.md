# 🧠 Reincarnator  
**A Swarm Agent to Detect Recycled Smart Contracts & Reactivated Wallets on Solana**  
*Built with the Eremos Agent Framework*

---

## 🧭 Overview

**Reincarnator** is a modular swarm agent designed to detect recurring on-chain threats on Solana — specifically, malicious or suspicious smart contracts being **recycled** under new wrappers and **deployed by dormant or risky wallets**.

Powered by Eremos, Reincarnator uses **compound behavioral detection** across:

- Contract bytecode similarity
- Wallet dormancy and historical risk
- Airdrop funneling into CEX wallets
- Token metadata mutations

> **Core Insight:** The most dangerous contracts on Solana aren’t always new — they’re often *old code in new wrappers*, deployed by reactivated wallets.

---

## ⚡ Motivation

Scammers iterate. They clone code, tweak names, and relaunch with new wallets — often catching retail off-guard again and again.

Solana’s characteristics make this easier:

- Near-zero deploy cost
- High wallet churn (Sybil behavior)
- Pseudonymous deployers
- Rapid retail momentum

There is currently no unified tool that proactively detects when **known bad code** is repackaged and **reintroduced** by previously inactive or tainted wallets.

**Reincarnator closes this gap.**

---

## 🎯 Detection Goals

Reincarnator emits high-confidence signals when:

- ✅ A contract is a **clone** (≥ 95% code similarity) of a flagged or previously suspicious one
- ✅ The deployer wallet is **dormant (≥ 90 days inactive)** or flagged for past scams
- ✅ The token is a **metadata-only fork** (same logic, tweaked name/symbol)
- ✅ Airdropped tokens **funnel rapidly** to a single CEX wallet or endpoint
- ✅ Multiple suspicious signals **co-occur**, boosting severity

---

## 🧬 Behavioral Patterns Tracked

| Pattern | Description |
|--------|-------------|
| **Code Cloning** | Identifies smart contracts with high bytecode similarity |
| **Dormant Wallet Reactivation** | Flags deployments by wallets inactive for ≥ 90 days |
| **Wallet Risk Scoring** | Profiles deployer based on scam history or suspicious funding |
| **Metadata Mutants** | Token redeploys with altered name/symbol but same logic |
| **Airdrop Funnels** | Tracks mass airdrop claims converging into a single wallet/CEX |

---

## 🏗️ Agent Architecture (Eremos Modules)

| Function | Eremos Module |
|---------|----------------|
| Deployment Monitoring | `DeployMonitor` |
| Code Fingerprinting | `CodeSimilarityModule` (AST/Wasm diff) |
| Wallet Behavior Analysis | `WalletActivityModule`, `WalletProfiler` |
| Metadata Normalization | `TokenDeployNormalizer` |
| Airdrop Flow Tracking | `AirdropFlowAnalyzer` |
| Compound Scoring Logic | `SwarmScorer` |
| Output & Alerting | `SignalEmitter`, `SeverityScorer` |

---

## 🔧 Detection Logic (Code-Like Flow)

```ts
onNewDeploy(programAddress: Pubkey) {
  const bytecode = getProgramBytecode(programAddress);
  const fingerprint = generateFingerprint(normalizeBytecode(bytecode));

  const match = compareFingerprints(fingerprint, knownMaliciousDB);
  if (match.similarity > 0.95) {
    const deployer = getDeployerWallet(programAddress);
    const walletRisk = getWalletProfile(deployer);

    const metadata = getTokenMetadata(programAddress);
    const metadataMatch = compareMetadata(metadata, match.metadata);

    const airdropRecipients = getInitialTokenDistributions(programAddress);
    const funnelTarget = detectFunneling(airdropRecipients);

    const conditions = [
      match.similarity > 0.95,
      walletRisk.dormant || walletRisk.riskScore > 8,
      metadataMatch.delta < 15,
      funnelTarget !== null
    ];

    const score = conditions.filter(Boolean).length;

    if (score >= 2) {
      emitSignal({
        type: "reincarnation_detected",
        deployer,
        fingerprint_similarity: match.similarity,
        metadata_variance: metadataMatch.delta < 15,
        funnel_target: funnelTarget,
        wallet_status: walletRisk.status,
        severity: score >= 3 ? "high" : "medium"
      });
    }
  }
}
