# 🧠 Reincarnator  
**Detecting Recycled Smart Contracts & Reactivated Wallets on Solana**  
*A Swarm Agent Proposal for the Eremos Framework*

---

## Overview

**Reincarnator** is a modular swarm agent that detects **recycled malicious contract behavior** on the Solana blockchain. It tracks **contract clones**, **wallet reactivations**, **airdrop funneling**, and **metadata-only redeploys** — all common techniques used in scam iterations and rugpull relaunches.

> Solana moves fast. Scammers move faster. Reincarnator spots familiar traps wearing new disguises.

---

## Motivation

Scams on Solana often follow a cycle:
- Copy existing malicious contracts (e.g., honeypots, rug factories)
- Deploy with a fresh name and symbol
- Use wallets that were dormant or had prior scam involvement
- Funnel airdrops into one centralized wallet or CEX

Most on-chain tools catch symptoms **after the exploit**. Reincarnator is built for **early detection** — based on recurring behavioral patterns, not just static heuristics.

---

## Agent Objectives

- ✅ Detect smart contracts ≥95% similar to previously flagged or known malicious contracts
- ✅ Identify contracts deployed by wallets that have been dormant ≥90 days
- ✅ Flag wallets tied to previous scams or funded through mixers/CEXs
- ✅ Catch copy-pasted tokens with only superficial metadata edits
- ✅ Track airdrop patterns where claimers converge to one wallet or CEX address
- ✅ Emit actionable, real-time alerts for dashboards and risk engines

---

## Detection Architecture

### 🧠 Behavioral Patterns Tracked

| Pattern | Description |
|--------|-------------|
| **Code Cloning** | Detects smart contracts with ≥95% bytecode or AST similarity |
| **Dormant Wallet Deploys** | Deploys from wallets inactive ≥90 days |
| **Wallet Reincarnation** | Reactivation of wallets previously tied to scams |
| **Metadata Mutants** | Same contract logic, altered token name/symbol/supply |
| **Airdrop Funnels** | Claim wallets funneling funds into one destination within a short time frame |

---

## 🔧 Detection Logic (Programmatic Flow)

### 1. **Monitor Deployments**

```ts
onNewDeploy(programAddress: Pubkey) {
  const bytecode = getProgramBytecode(programAddress);
  const metadata = parseSPLTokenMetadata(programAddress);
  ...
}


