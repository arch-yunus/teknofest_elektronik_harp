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

    def process_detection(self, freqs, magnitudes, raw_signal=None, params=None):
        """
        Analyzes detected signal using standard, LPI methods, and parameter matching.
        Activates the optimal countermeasure strategy.
        """
        # 1. Broad Spectrum Classification
        features = self.classifier.extract_features(freqs, magnitudes)
        label = self.classifier.predict(features)
        
        # 2. Specialized LPI Check
        lpi_result = {"final_verdict": "CLEAR"}
        if raw_signal is not None:
            lpi_result = self.lpi_detector.detect_all(raw_signal)
        
        # 3. Parameter-based Identification
        threat_name = "Unknown"
        if params:
            threat_name, threat_data = ThreatLibrary.identify_emitter(params)
            strategy = threat_data["countermeasure"]
            label = threat_data["label"]
        else:
            # Fallback to classifier if no params provided
            if lpi_result["final_verdict"] == "DETECTED":
                strategy = "SmartJamming_LPI"
                label = "LPI_Radar"
                threat_name = "LPI Threat"
            else:
                strategy = ThreatLibrary.get_countermeasure(label)
                threat_name = label

        self.active_strategy = strategy
        print(f"[Autonomy] Detection: {threat_name} (Label: {label}) -> Strategy: {strategy}")
        
        return strategy

    def get_system_status(self):
        return {
            "last_strategy": self.active_strategy,
            "status": "Operational"
        }
