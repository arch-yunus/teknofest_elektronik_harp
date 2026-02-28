from .threat_library import ThreatLibrary

class AutonomyManager:
    """
    Autonomous Decision Support System (ADSS).
    Decides the best action based on classified signals.
    """
    def __init__(self, classifier, lpi_detector, jammers_map):
        self.classifier = classifier
        self.lpi_detector = lpi_detector
        self.jammers = jammers_map
        self.active_strategy = None

    def process_detection(self, freqs, magnitudes, raw_signal=None):
        """
        Analyzes detected signal using standard and LPI methods.
        Activates the optimal countermeasure strategy.
        """
        # 1. Broad Spectrum Classification
        features = self.classifier.extract_features(freqs, magnitudes)
        label = self.classifier.predict(features)
        
        # 2. Specialized LPI Check
        lpi_result = {"final_verdict": "CLEAR"}
        if raw_signal is not None:
            lpi_result = self.lpi_detector.detect_all(raw_signal)
        
        # 3. Decision Logic (Advanced Fusion)
        if lpi_result["final_verdict"] == "DETECTED":
            strategy = "SmartJamming_LPI" # Target LPI specific vulnerabilities
            label = "LPI_Radar"
        else:
            strategy = ThreatLibrary.get_countermeasure(label)
        
        self.active_strategy = strategy
        print(f"[Autonomy] Detection: {label} ({lpi_result.get('confidence', 'Standard')}) -> Strategy: {strategy}")
        
        return strategy

    def get_system_status(self):
        return {
            "last_strategy": self.active_strategy,
            "status": "Operational"
        }
