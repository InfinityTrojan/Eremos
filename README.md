# Eremos

Solana moves fast. Too fast.

Scams evolve. Wallets vanish, then return. Contract code gets cloned with slight tweaks. Retail walks into the same trap, again and again.

“Reincarnator” – Detecting Code Clones by Dormant or Suspicious Wallets on Solana Powered by Eremos Agent Framework

# Core Insight:
The most dangerous smart contracts on Solana aren’t always new — they’re often old code in new wrappers, deployed by wallets that vanished for months and then suddenly return.

This swarm agent tracks and records a compound behavior:
🧬 When near-duplicate contracts are deployed by wallets that have been long dormant or previously tied to high-risk activity.

#🧠 Agent Name: Reincarnator

#Goal:
Detect recycled contract logic paired with wallet reactivations, surfacing early warnings for:

Rugpull relaunches

Sybil reactivations

High-risk devs returning with "fresh" tokens

#Detection Logic:

1. Monitor Contract Deployments
Subscribe to all new program or SPL token deploys

Extract contract bytecode or state layout

2. Fingerprint the Code
Normalize constants (token name, supply, fees)

Generate a code fingerprint (hash or AST structure)

Compare against historical contracts

✅ If similarity > 95% → proceed to wallet analysis

3. Analyze Deployer Wallet
Pull wallet's historical activity

If wallet has been inactive ≥ 90 days, flag as dormant

If wallet was involved in prior scams/rugs, increase severity score

Track wallet funding source (e.g., CEX, mixer, bridge)

4. Combine Both Signals
If a dormant or flagged wallet deploys a clone contract, emit a high-severity alert.

This is a “reincarnation” of a previous on-chain pattern, and a powerful early signal of coordinated or repeat malicious behavior.

# How It Fits in Eremos Architecture:

| Concept                 | Corresponding Eremos Modules                                            |
| ----------------------- | ----------------------------------------------------------------------- |
| Code Similarity         | `CodeSimilarityModule` (could leverage decompiler or Wasm diff tooling) |
| Dormant Wallet Tracking | `WalletActivityModule`                                                  |
| Wallet Risk Analysis    | `WalletProfiler`, `FundingSourceModule`                                 |
| Signal Trigger          | `SwarmAgent` logic with compound scoring                                |
| Output Formatting       | `SignalReporter`, `SeverityScorer`                                      |

#Summary of Concepts Used

| Concept             | Role in Agent                                       |
| ------------------- | --------------------------------------------------- |
| Code Fingerprinting | Identifies recycled or malicious logic              |
| Dormancy Profiling  | Highlights ghost wallets coming back online         |
| Wallet Risk Scoring | Connects wallets to previous high-risk behavior     |
| Compound Triggering | Alerts only when multiple suspicious traits overlap |


# Summary
Agent Name: Reincarnator
Tracks: Contract clones deployed by dormant or suspicious wallets
Detects: Recycled scams, rugpull relaunches, ghost wallet activity
Why Solana: Cheap deploy cost + pseudonymity enables pattern abuse
Built For: Real-time alerts, analyst dashboards, trust signals in token UX



                   +----------------------+
                   |  Swarm Agent:        |
                   |   Reincarnator       |
                   +----------+-----------+
                              |
              +---------------+----------------+
              |                                |
+-----------------------------+   +----------------------------+
| CodeSimilarityModule        |   | WalletActivityModule       |
|-----------------------------|   |----------------------------|
| - Extract contract bytecode |   | - Track tx timestamps      |
| - Normalize constants       |   | - Compute dormancy period  |
| - Generate code fingerprint |   | - Detect reactivation      |
| - Check for 95%+ similarity |   +------------+---------------+
+-----------------------------+                |
                                               |
                           +-------------------v--------------------+
                           | WalletProfiler & RiskScorer Module     |
                           |----------------------------------------|
                           | - Check if wallet has prior rug links |
                           | - Analyze funding patterns (CEX, etc) |
                           | - Score wallet risk level             |
                           +-------------------+--------------------+
                                               |
                                    +----------v-----------+
                                    | Swarm Decision Logic |
                                    |----------------------|
                                    | If (clone + dormant) |
                                    | OR (clone + risky)   |
                                    | => Trigger Alert     |
                                    +----------+-----------+
                                               |
                                    +----------v-----------+
                                    |  SignalReporter      |
                                    |----------------------|
                                    | - Alert type         |
                                    | - Severity level     |
                                    | - Contract diff link |
                                    | - Deployer metadata  |
                                    +----------------------+





        #noobstar
