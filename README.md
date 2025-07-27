# 🧠 Proposal: Reincarnator  
**A Modular Swarm Agent for Detecting Smart Contract Reincarnations on Solana**  
*Built with the Eremos Agent Framework*

---

## Overview

**Reincarnator** is a behavioral detection agent designed to track **recycled smart contracts**, **reactivated high-risk wallets**, and **coordinated scam relaunches** on the Solana blockchain. 

This agent leverages **compound pattern detection** — combining contract fingerprinting, wallet dormancy analysis, airdrop funneling, and metadata mutation recognition — to surface high-confidence early signals of on-chain threat recurrence.

> 🔍 **Key Idea:** The most dangerous smart contracts aren’t always new — they’re often old code in new wrappers, deployed by wallets that disappeared and reemerged.

---

## Motivation

Solana’s environment makes it uniquely vulnerable to **scam reincarnation**:

- ⚡ **Low deploy cost** enables endless iteration by bad actors
- 🫥 **Pseudonymous wallets** make historical linking hard
- 🚀 **Retail FOMO** drives high inflow into unaudited tokens
- ⏳ **Rugs recycle** — often by dormant wallets or copycat deploys

Yet no public tool today *proactively* detects when previously malicious or dormant actors redeploy slightly modified versions of known scams.

**Reincarnator** fills this gap.

---

## Objectives

- ✅ Detect recycled smart contracts with ≥95% similarity to known malicious or suspicious code
- ✅ Surface deployer wallets that have been dormant for ≥90 days or tied to past scams
- ✅ Flag airdrop claimers funneling to the same centralized wallet or CEX deposit address
- ✅ Catch duplicate token deploys that differ only by minor metadata (e.g., symbol, supply)
- ✅ Emit real-time alerts for dashboards, firewalls, or public transparency feeds

---

## Detection Architecture

### 🧠 **Behavioral Patterns Tracked**

| Behavior | Description |
|----------|-------------|
| Code Cloning | Detect near-duplicate smart contracts using fingerprinting |
| Wallet Reawakening | Flag re-deployments from long-dormant or risk-associated wallets |
| Metadata Mutants | Identify redeploys of the same logic with only cosmetic metadata changes |
| Airdrop Funnels | Monitor mass airdrop claim wallets funneling to a common wallet/CEX |
| Compound Triggers | Only emit alerts when multiple suspicious traits overlap |

---

## Technical Design

### Modular Integration with **Eremos Agent Framework**

| Function | Module |
|---------|--------|
| Code Fingerprinting | `CodeSimilarityModule` (AST/Wasm diffing) |
| Dormant Wallet Profiling | `WalletActivityModule` |
| Risk Attribution | `WalletProfiler`, `FundingSourceModule` |
| Airdrop Funnel Tracking | `AirdropFlowAnalyzer` |
| Metadata Clone Detection | `TokenDeployNormalizer` |
| Alert Engine | `SwarmAgent` |
| Output Formatting | `SignalReporter`, `SeverityScorer` |

---

### Sample Alert Output

```json
{
  "signal": "reincarnation_detected",
  "wallet_status": "dormant",
  "wallet_last_active": "2024-09-02",
  "code_similarity": 0.972,
  "metadata_variance": true,
  "airdrop_funnel_detected": true,
  "previous_contract": "RugToken v1",
  "current_contract": "RugToken Reloaded",
  "severity_score": 9.2,
  "tags": ["reincarnation", "wallet_reawakening", "metadata_clone"]
}
