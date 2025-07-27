class ReincarnatorAgent(SwarmAgent):
    def __init__(self):
        self.code_similarity = CodeSimilarityModule()
        self.wallet_tracker = WalletActivityModule()
        self.wallet_profiler = WalletProfiler()
        self.signal_reporter = SignalReporter()

    def on_new_contract_deploy(self, deploy_event):
        contract_address = deploy_event.contract_address
        deployer_wallet = deploy_event.deployer

        # 1. Code Fingerprint
        fingerprint = self.code_similarity.fingerprint(contract_address)
        match_score, matched_contract = self.code_similarity.compare(fingerprint)

        if match_score < 0.95:
            return  # Not similar enough

        # 2. Dormancy & Risk Check
        dormancy_days = self.wallet_tracker.get_dormancy_days(deployer_wallet)
        risk_score = self.wallet_profiler.score_wallet(deployer_wallet)

        is_dormant = dormancy_days >= 90
        is_risky = risk_score >= 0.7  # normalized score 0-1

        # 3. Compound Trigger
        if is_dormant or is_risky:
            severity = self._compute_severity(match_score, dormancy_days, risk_score)

            self.signal_reporter.send(
                alert_type="Reincarnated Contract",
                contract_address=contract_address,
                matched_contract=matched_contract,
                match_score=match_score,
                deployer_wallet=deployer_wallet,
                dormancy_days=dormancy_days,
                risk_score=risk_score,
                severity=severity
            )

    def _compute_severity(self, match_score, dormancy_days, risk_score):
        if match_score > 0.98 and (dormancy_days > 120 or risk_score > 0.85):
            return "HIGH"
        elif match_score > 0.95 and (dormancy_days > 90 or risk_score > 0.6):
            return "MEDIUM"
        else:
            return "LOW"
